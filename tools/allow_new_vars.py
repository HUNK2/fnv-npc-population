"""Let a script gain variables at the end of its list, keeping every existing index.

fnv-mcp's builder refuses any change to a cached script's variable layout ("Existing semantic
variable indices changed"), even new variables added after the old ones. Adding at the end is safe
for saves: a save stores script variables by index, so old indices keep their values and new
ones start at zero. This tool checks that the source's declarations keep the cached ones as an
unchanged prefix (same names, same order, same kinds), then drops that script's cache entry so the
next in-game compile is accepted. Anything else (renamed, removed, reordered or retyped variables)
is refused. A user-defined function (a script with a "begin Function" block) keeps no variables in
a save, so any change to its list is accepted.

    python tools/allow_new_vars.py <spec.json> <ScriptEditorID>

Then run tools/rebuild.sh with the game running on the last build.
"""
import json
import os
import re
import sys
from pathlib import Path

BRIDGE = Path(os.environ.get('FNV_MCP_BRIDGE', Path(__file__).resolve().parents[2] / 'fnv-mcp-code' / 'bridge'))
KINDS = {'short': 1, 'long': 1, 'int': 1, 'float': 0, 'ref': 0, 'reference': 0, 'string_var': 2, 'array_var': 3}
DECL = re.compile(r'\s*(short|long|int|float|ref|reference|string_var|array_var)\s+([A-Za-z_][A-Za-z0-9_]*)\s*', re.I)


def declared(text):
    """Variables in declaration order as (name, kind); the compiler numbers them 1..n in this order."""
    out = []
    for line in text.splitlines():
        m = DECL.fullmatch(line.split(';', 1)[0])
        if m:
            out.append((m[2].casefold(), KINDS[m[1].lower()]))
    return out


def is_function(text):
    """A user-defined function: its variables live only while it runs, never in a save."""
    return re.search(r'^\s*begin\s+function\b', text, re.I | re.M) is not None


def cached_layout(entry):
    """(index, name, kind) from the cached SLSD/SCVR subrecords, sorted by index."""
    out, pending = [], None
    for tag, raw in entry['compiled']:
        data = bytes.fromhex(raw)
        if tag == 'SLSD':
            pending = (int.from_bytes(data[:4], 'little'), data[16])
        elif tag == 'SCVR' and pending:
            out.append((pending[0], data.rstrip(b'\0').decode('cp1252').casefold(), pending[1]))
            pending = None
    return sorted(out)


def check(old_layout, new_decls):
    """Return a refusal reason, or None when new_decls keeps old_layout as a prefix."""
    old = [(name, kind) for _, name, kind in old_layout]
    if [i for i, _, _ in old_layout] != list(range(1, len(old) + 1)):
        return 'cached indices are not 1..n'
    if new_decls[:len(old)] != old:
        return 'existing variables changed (renamed, removed, reordered or retyped)'
    return None


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    spec_path, edid = Path(argv[0]).resolve(), argv[1]
    spec = json.loads(spec_path.read_text(encoding='utf-8'))
    source = (spec_path.parent / spec['records'][edid]['source']).read_text(encoding='cp1252')
    cache_file = BRIDGE / 'state' / 'scripts' / (spec['project_id'] + '.json')
    cache = json.loads(cache_file.read_text())
    if edid not in cache:
        print('%s has no cache entry; nothing to do.' % edid)
        return 0
    old, new = cached_layout(cache[edid]), declared(source)
    reason = None if is_function(source) else check(old, new)
    if reason:
        print('Refused: %s.\n old: %s\n new: %s' % (reason, [n for _, n, _ in old], [n for n, _ in new]))
        return 1
    added = [n for n, _ in new[len(old):]]
    del cache[edid]
    cache_file.write_text(json.dumps(cache, indent=1))
    print('OK: %s keeps its %d variables; adds %s. Cache entry dropped.' % (edid, len(old), added or 'nothing'))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

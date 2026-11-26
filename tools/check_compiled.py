"""Fail when a built plugin has a script with no compiled data (SCHR data size 0).

fnv_spec build writes a script's source without its compiled data when its compile cache misses
(for example after the spec's forms change); the game then has no variables for it. Run with
fnv-mcp's Python (rebuild.sh does it after every build):

    <fnv-mcp>/bridge/.venv/Scripts/python.exe tools/check_compiled.py <plugin.esp>
"""
import struct
import sys
from pathlib import Path

BRIDGE = Path(__file__).resolve().parent.parent.parent / 'fnv-mcp-code' / 'bridge'
sys.path.insert(0, str(BRIDGE))
from fnv_mcp.esp import codec  # noqa: E402


def uncompiled(path):
    bad = []
    for rec, _ in codec.iter_records(Path(path).read_bytes(), types=('SCPT',)):
        subs = {s.tag: s.data for s in rec.subrecords}
        name = subs.get('EDID', b'?').rstrip(b'\0').decode('cp1252')
        schr = subs.get('SCHR')
        # SCHR: unused, reference count, compiled size, variable count, type, flags
        size = struct.unpack('<I', schr[8:12])[0] if schr and len(schr) >= 12 else 0
        if size == 0 or not subs.get('SCDA'):
            bad.append(name)
    return bad


def main(argv):
    bad = uncompiled(argv[1])
    if bad:
        print('UNCOMPILED scripts in %s: %s (run rebuild.sh with compile, the game on the last build)'
              % (Path(argv[1]).name, ', '.join(bad)))
        return 1
    print('all scripts compiled')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

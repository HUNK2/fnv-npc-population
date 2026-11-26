"""Call one fnv-mcp tool in-process, with one of this mod's specs as the project spec.

The registered fnv-mcp server is bound to its own project spec; this runs the same tool code with
our spec, without touching the server's project file. Run it with fnv-mcp's own Python:

    <fnv-mcp>/bridge/.venv/Scripts/python.exe tools/fnvmcp_call.py <spec.json> <tool> '<json args>'

Example: ... tools/fnvmcp_call.py mod/proofs/proofs.spec.json fnv_spec '{"action": "build"}'

Never run it while the MCP server's own live tools are talking to the game (one companion pipe).
"""
import asyncio
import json
import os
import sys
from pathlib import Path

# fnv-mcp's bridge folder: FNV_MCP_BRIDGE, else a fnv-mcp-code checkout next to this repo.
BRIDGE = Path(os.environ.get('FNV_MCP_BRIDGE', Path(__file__).resolve().parents[2] / 'fnv-mcp-code' / 'bridge'))
# The fnv-mcp project file whose install, profile and game settings are used (only spec and plugin change).
PROJECT_FILE = Path(os.environ.get('FNV_MCP_PROJECT', BRIDGE / 'projects' / 'hellowasteland.windows.json'))
START = Path.cwd()
sys.path.insert(0, str(BRIDGE))
os.chdir(BRIDGE)

from mcp import Client                      # noqa: E402  (fnv-mcp's venv)
from fnv_mcp.config import Project          # noqa: E402
from fnv_mcp.server import make_server      # noqa: E402


async def call(spec_path, tool, args):
    project = Project.load(str(PROJECT_FILE))
    spec = json.loads(Path(spec_path).read_text(encoding='utf-8'))
    project = project.model_copy(update={'spec': Path(spec_path).resolve(), 'plugin': spec['plugin']})
    async with Client(make_server(project)) as client:
        for attempt in range(6):        # the MCP server releases the companion pipe after 20 s idle
            result = await client.call_tool(tool, args)
            out = result.structured_content or {'text': [c.text for c in result.content if hasattr(c, 'text')]}
            if (out.get('error') or {}).get('code') != 'COMPANION_UNREACHABLE':
                return out
            await asyncio.sleep(8)
        return out


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    spec_path = (START / argv[0]).resolve()
    args = json.loads(argv[2]) if len(argv) > 2 else {}
    out = asyncio.run(call(spec_path, argv[1], args))
    print(json.dumps(out, indent=1)[:20000])
    return 0 if out.get('ok', True) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

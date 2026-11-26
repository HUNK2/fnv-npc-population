#!/bin/sh
# After tools/rebuild.sh: quit the game, install the built plugin, launch again at a start cell.
# Usage: tools/cycle.sh mod/proofs/proofs.spec.json [coc:Cell]   (needs the game's last build loaded before)
set -e
cd "$(dirname "$0")/.."
BRIDGE="${FNV_MCP_BRIDGE:-$(pwd)/../fnv-mcp-code/bridge}"
PY="${FNV_MCP_PY:-$BRIDGE/.venv/Scripts/python.exe}"
SPEC="$1"; START="${2:-}"
PLUGIN=$(python -c "import json,sys; print(json.load(open(sys.argv[1]))['plugin'])" "$SPEC")
summ() { python -c "import json,sys; d=json.load(sys.stdin); print('ok' if d.get('ok') else 'FAILED', json.dumps(d.get('error') or {k: d.get('data', {}).get(k) for k in ('wasRunning', 'installed', 'phase', 'cellName', 'pid')})[:600])"; }
"$PY" tools/fnvmcp_call.py "$SPEC" fnv_game '{"action":"quit"}' | summ
"$PY" tools/fnvmcp_call.py "$SPEC" fnv_install "{\"plugin_path\": \"$(cygpath -m "$BRIDGE")/build/$PLUGIN\"}" | summ
# MO2 refused to launch ("Cannot launch program") straight after a quit; give it a moment.
if [ -n "$START" ]; then sleep 8; "$PY" tools/fnvmcp_call.py "$SPEC" fnv_game "{\"action\":\"launch\",\"start\":\"$START\"}" | summ; fi

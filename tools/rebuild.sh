#!/bin/sh
# Compile a spec's scripts in the running game (its last build must be loaded), then build the plugin.
# Usage: tools/rebuild.sh mod/proofs/proofs.spec.json [compile|build]   (default: both)
# Then, with the game closed: fnv_install the built plugin and launch again.
set -e
cd "$(dirname "$0")/.."
BRIDGE="${FNV_MCP_BRIDGE:-$(pwd)/../fnv-mcp-code/bridge}"
PY="${FNV_MCP_PY:-$BRIDGE/.venv/Scripts/python.exe}"
SPEC="$1"; WHAT="${2:-both}"
summ() { python -c "import json,sys; d=json.load(sys.stdin); print('ok' if d.get('ok') else 'FAILED', json.dumps(d.get('error') or {k: d.get('data', {}).get(k) for k in ('scripts', 'path', 'written', 'recordCounts')})[:3000])"; }
if [ "$WHAT" != build ]; then "$PY" tools/fnvmcp_call.py "$SPEC" fnv_scripts_compile '{}' | summ; fi
if [ "$WHAT" != compile ]; then
  "$PY" tools/fnvmcp_call.py "$SPEC" fnv_spec '{"action":"build"}' | summ
  # a compile-cache miss writes a script without its compiled data: stop before it is installed
  PLUGIN=$(python -c "import json,sys; p=json.load(open(sys.argv[1]))['plugin']; print(p['name'] if isinstance(p, dict) else p)" "$SPEC" 2>/dev/null || true)
  if [ -n "$PLUGIN" ]; then "$PY" tools/check_compiled.py "$BRIDGE/build/$PLUGIN"; fi
fi
# The core is the company's master: the builder writes .esp only, so set the master flag after it.
case "$SPEC" in *mod/core/*) python tools/set_esm_flag.py "$BRIDGE/build/LivedInMojave.esp" ;; esac

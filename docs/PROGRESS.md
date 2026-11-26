# Progress

Updated at every task end. Workflow: `docs/plans/2026-11-26-build-workflow.md`.
The user asked (2026-11-27) for the whole plan to run without stopping at gates G4 to G7; those
calls are mine and are marked "my call" here and in the plans.

## Now

- Milestone: **M0 Proofs** (`docs/plans/2026-11-27-m0-proofs.md`), results in `docs/m0-results.md`
- Next: 0.6 (terminal from an item), 0.7, 0.10 to 0.13, then the crowd test 0.14

## Done

- 0.1 Ledger reference model (8 tests pass).
- 0.2 Tooling: `tools/fnvmcp_call.py` and `tools/rebuild.sh` build `mod/proofs` with fnv-mcp.
- 0.3 Dependencies load (xNVSE, JIP LN, JohnnyGuitar 5.28).
- 0.4 Live terminal labels, 0.5 clicked row (flag 4, route C), 0.8 limits (30 rows; text capped
  at 200 characters), 0.9 day tick.

## My calls (to review)

- Plugins are built in-process with fnv-mcp's tools (`tools/fnvmcp_call.py`), not by editing the
  MCP server's project file, because the server did not pick up the change.
- Clicked rows are found by polling row flag 4 (route C), not by row result scripts or JIP's
  click event: it needs no tool change and no event handler.
- Terminal text is cut to 200 characters before it is set (JohnnyGuitar has no length check).

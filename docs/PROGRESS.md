# Progress

Updated at every task end. Workflow: `docs/plans/2026-11-26-build-workflow.md`.
The user asked (2026-11-27) for the whole plan to run without stopping at gates G4 to G7; those
calls are mine and are marked "my call" here and in the plans.

## Now

- Milestone: **M1 One road** (plan: `docs/plans/2026-11-27-m1-one-road.md`)
- Done: 1.1 company model (21 tests), 1.2 two plugins (`LivedInMojave.esp` with the master flag,
  `MojaveCaravanCompany.esp`; in game `CCVersion` = 101 read from the core's `LIMVersion`).
- Next: 1.3 the day tick and the ledger in game, checked day by day against the model.

## Done

- **M0 Proofs** (2026-11-27), results in `docs/m0-results.md`:
  - 0.1 Ledger reference model (8 tests pass).
  - 0.2 Tooling: `tools/fnvmcp_call.py`, `tools/rebuild.sh`, `tools/cycle.sh`, and
    `tools/allow_new_vars.py` (3 tests) build and install with fnv-mcp.
  - 0.3 Dependencies load (xNVSE, JIP LN, JohnnyGuitar 5.28).
  - 0.4 Live terminal labels, 0.5 clicked row (flag 4, route C), 0.7 labels set on open,
    0.8 limits (30 rows; text capped at 200 characters), 0.9 day tick.
  - 0.6 terminal opened from a script: yes; from a Pip-Boy item: not proven (desk fallback, ALCH
    retry in M1).
  - 0.10 letters only from GameMode, out of combat; 0.11 moving people leaves no save growth;
    0.12 busy shield by source plugin; 0.13 old saves; 0.14 crowd: 30 extra settlers, still 60 fps.

## My calls (to review)

- The core plugin is `LivedInMojave.esp` with the master flag set after each build
  (`tools/set_esm_flag.py`): fnv-mcp's builder writes .esp files only.
- One terminal form with a 14-row pool shows every screen (M1 plan, "My calls").

- Plugins are built in-process with fnv-mcp's tools (`tools/fnvmcp_call.py`), not by editing the
  MCP server's project file, because the server did not pick up the change.
- Clicked rows are found by polling row flag 4 (route C), not by row result scripts or JIP's
  click event: it needs no tool change and no event handler.
- Terminal text is cut to 200 characters before it is set (JohnnyGuitar has no length check).
- G4: towns are **plugin-first** (no engine plugin). The crowd test hit no engine limit; the only
  near-player cap (20 actors) only stops face animation.
- The ledger opens at desks (runner's desk, relay desks); the Pip-Boy item is a bonus if the ALCH
  retry works.

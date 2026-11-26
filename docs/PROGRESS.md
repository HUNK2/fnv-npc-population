# Progress

Updated at every task end. Workflow: `docs/plans/2026-11-26-build-workflow.md`.
The user asked (2026-11-27) for the whole plan to run without stopping at gates G4 to G7; those
calls are mine and are marked "my call" here and in the plans.

## Now

- Milestone: **M1 One road** (plan: `docs/plans/2026-11-27-m1-one-road.md`)
- Done: 1.1 company model (21 tests), 1.2 two plugins (`LivedInMojave.esp` with the master flag,
  `MojaveCaravanCompany.esp`; in game `CCVersion` = 101 read from the core's `LIMVersion`).
  1.3 the day tick in game (`CCCoreScript`, `CCPriceFn`): `tools/ingame_run.py 14` matches the model
  on all 14 days (cash, sales, costs, events, losses), no script errors.
  1.4 the office terminal (`CCOfficeTerm`, `CCTermScript`, `CCTermDraw`, `CCPlanFn`; model
  `tools/terminal_model.py`, 14 tests): `tools/ingame_terminal.py` reads every row back after 22
  clicks over all six screens (front, prices, ledger, orders, routes, settings) and matches the
  model each time; the orders queued on the terminal run at the next tick as modelled; no script
  errors. Screenshots: `docs/evidence/m1/m1_terminal_screen0..5.png`.
  1.5 founding: Hollis Webb (Alice's agent) and the company terminal wait in a holding cell and are
  moved to a corner booth of the Prospector Saloon by `CCFounding`; topic "You lend money to
  traders?" with the plain, Jason Tagg (Alice dead) and Powder Ganger landlord pitches, the terms,
  and signing (500 of the player's caps); the wagon yard (cart, two pack brahmin) behind Chet's store
  and a chalkboard on his porch are enabled at founding. `tools/ingame_founding.py`: 13 checks pass
  (day 0 cash 2,500, loan 3,000, owner funds 0), no script errors. Pictures:
  `docs/evidence/m1/m1_founding_*.png`.
  1.6 the post (`tools/post_model.py`, 18 tests; company and terminal models updated, 62 model
  tests pass): the morning report (two pages of at most 200 characters), memos (at most 3 a day,
  a default applied at the deadline: road memo and prepay memo) and field letters (a message box,
  GameMode only, out of combat, at most one a company day; a while-you-were-away letter after 3
  days without a terminal visit). `tools/ingame_post.py`: 33 checks pass over 10 days (numbers,
  letters, the Post and Memos screens read back, answers applied at the next tick), no script
  errors. Pictures: `docs/evidence/m1/m1_post_*.png`, `m1_memos_*.png`, `m1_field_letter.png`.
  Not checked by eye: a real click on a Post row typing its text (read back by command instead).
- Next: 1.7 debt ladder, strikes, cures, busy shield, forecast banner.

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
- Hollis and his terminal are references in the mod's own holding cell, moved into the saloon once
  with JIP `MoveToCell` (FNV has no `PositionCell`): no vanilla interior cell is edited. The wagon
  yard and chalkboard are new persistent references in the Goodsprings exterior cells, initially
  disabled.
- Hollis is essential and uses `DefaultSandboxCurrentLocation256` (he sits in the booths near his
  table); his look and inventory come from the vanilla Crimson Caravan trader, without its factions.
- Signing needs 500 caps in the player's pocket (the doc's owner funds); with less, Hollis refuses.
  The landlord pitch only changes the words in M1; its heat and sealed-crate jobs come with M3.
- Company terminals are placed by script at run time (`PlaceAtMe`), not as references in vanilla
  cells: fnv-mcp cannot add references to vanilla interior cells yet.
- A terminal row shows at most 39 characters on screen (seen live; the rest is cut), so every
  label is written to fit 39.
- Company scripts read the core quest with `GetVariable`/`GetArrayVariable`/`SetVariable`, not
  `CCCore.var`: in-game compile cannot resolve `Quest.variable`.
- The plan is a function (`CCPlanFn`) used both by the daily plan and by the terminal's accept row.
- Open: the terminal types about one character a frame (about 10 s for a 12-row page). Left for
  later; the vanilla display-rate setting looks frame-limited.
- Terminal text is cut to 200 characters before it is set (JohnnyGuitar has no length check).
- G4: towns are **plugin-first** (no engine plugin). The crowd test hit no engine limit; the only
  near-player cap (20 actors) only stops face animation.
- The ledger opens at desks (runner's desk, relay desks); the Pip-Boy item is a bonus if the ALCH
  retry works.
- Bandits now rob the strongbox (the day's Primm takings) on the return leg, not the crates: a
  robbery takes 30%, a wreck all of it, capped at 3 days' burn; no event on day 1 (it could not be
  forecast). The road memo answers: send, hire a gun for 25 (cover 75), keep the wagon home
  (default). Over 56 days home is the best plain answer (a tired market recovers overnight), so a
  player who ignores memos barely meets bandits. Revisit in the 1.10 balance run.
- The prepay memo shows after paid bills when the loan is above 0 and cash - 300 still covers 14
  days of burn; default keep the cash.
- Opening any company terminal counts as a visit: it clears the waiting letter.
- Field letters are `MessageBoxEx` boxes from a GameMode quest script (`CCLetterScript`); a road
  letter's buttons answer the road memo.
- The ALCH ledger retry (Pip-Boy item) is not done in 1.6; the desks stay the way in.

## Open items for the final report

- fnv-mcp: when an in-game compile fails, the tool retries with editor IDs swapped for hex form
  IDs and reports the retry's error, which hides the real one (`call CCPlanFn` becomes
  `call 14000804`: "Expected user function").
- fnv-mcp `fnv_ui_do button` cannot pick a terminal row by its label (all rows share one tile name).
- Terminal typing speed, vanilla interior references, `Quest.var` in compile, console echo lines.
- The weekly statement (doc) is not built yet.

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
  1.7 the debt ladder (`tools/test_ladder.py`, 25 tests; 89 model tests pass): a missed bill is a
  deferred notice until it is served (a terminal visit or the notice letter shown); grace 3 days,
  final notice 5, seizure 7, receivership 7 more; a strike on each missed bill, 3 within 56 days is
  a takeover; cures: owner rescue from the player's pocket, sell the wagon (60%), walk away (two
  clicks); probation 14 days; a forecast warning on the front page and a letter when runway < 5;
  the busy shield stops the clocks and letters while the player is in a DLC's lands before its main
  quest is done. `tools/ingame_ladder.py`: 18 days, every day's numbers, letter text and ladder
  state match the model; Notice, Routes and closed screens read back; rescue, wagon sale from a
  letter and receivership; no script errors. Pictures: `docs/evidence/m1/m1_notice_letter.png`,
  `m1_notice_screen.png`, `m1_closed_terminal.png`.
  1.8 contracts, standing orders and hiring (`tools/test_hiring.py`, 25 tests; 114 model tests
  pass): paper staff (the founding driver and guard have names; cover = 15 for the driver + 30 a
  guard + a fifth of skill over 50), 3 to 6 seeded candidates every week, reference checks, hire
  and fire, dishonest staff skim; Primm's water contract offered as a memo (accept, counter,
  decline), delivered on the Goodsprings leg, a miss costs 10% and trust; three standing order
  slots that change the bookkeeper's plan. New terminal screens: Staff, Hire, Candidate,
  Contracts, Standing orders, Slot. `tools/ingame_hiring.py`: 18 days and every screen after every
  select match the model, no script errors. Pictures: `docs/evidence/m1/m1_staff_screen.png`,
  `m1_candidate_screen.png`, `m1_standing_slot.png`, `m1_contracts_screen.png`.
  1.9 tier 2 (`tools/test_tier2.py`, 16 tests; 130 model tests pass): trust from deliveries (+1 a
  leg that sells into a town) and Ghost Town Gunfight (+10 once); the tier gate (earned worth 1,500,
  no strike in 56 days, Goodsprings trust 50, Ghost Town done); the tier letter; the Build screen
  from the front page's CHAINS row (purifier, apothecary, well rig, forager hut, owner money first);
  the office (a shack by the Prospector Saloon with a scripted door into a new interior: desk and
  company terminal, map board, safe) and a Primm stall appear on the tier day. `tools/ingame_tier2.py`:
  every day's numbers, letter, trust, tier and cash match the model; tier 2 on day 13 with Primm's
  contract; the world refs enabled; building the well rig and purifier on the terminal; three days
  of workshop output in the warehouse; in through the office door, its terminal, and out again; no
  script errors. Pictures: `docs/evidence/m1/m1_build_screen.png`, `m1_office_inside.png`,
  `m1_office_exit.png`, `m1_office_outside.png`. `tools/balance_run.py` (100 model days for a
  passive, careful and good player) is ready for 1.10.
  1.10 milestone check (141 model tests pass; `tools/test_review.py` 11 of them): the review fixes
  (below) in the models and the game; the Memos screen moved to `CCMemoFn` (`CCTermDraw` was at the
  in-game compile limit; now 13.1 KB); a Primm branch terminal on the Vikki and Vance cashier
  counter. In-game checks on fresh games, all with 0 script errors: `ingame_run.py 28` matches the model on all 28 days; founding 14 checks (with the Primm terminal), post 33, ladder 70, hiring 133, terminal 23 (screens and clicks), tier 2 72 (with the tier 1 checklist) pass. FPS (`fnv_profile frame`, 5 s, vsync 60): Prospector Saloon 59.2 fps / 16.06 ms with the company, 60.0 / 16.02 with its refs disabled; Primm (Vikki and Vance) 60.0 / 16.12 with the branch terminal, 60.0 / 16.14 without; quest scripts 0.1 ms a frame. Old save `fnvmcp_test_rotf_release_car`: Hollis and both terminals placed, the quests run, founding and day 1 work (cash 3,195, the daily plan on), 0 script errors (the save was not overwritten).
  `tools/balance_run.py` (100 model days): passive nets 258 to 673 a week after week 1 (target
  about 250), careful and good players reach tier 2 on day 10 and repay the loan in week 6
  (targets 5 and 8), no ended companies. What to try: `docs/m1-what-to-try.md`.
- **M1 One road is done.** Then the towns design (`docs/towns-design.md`, reviewed) and T1
  Goodsprings (`docs/plans/2026-11-27-t1-goodsprings.md`, proofs in `docs/t1-results.md`).
- **T1 and M2** (commits 35c36ec, bf6302f): Goodsprings residents on schedules; four towns, three
  roads, site goods, staff and managers; the M2 checks pass in game. What to try:
  `docs/t1-what-to-try.md`, `docs/m2-what-to-try.md`. The world branch terminals and the tier 3
  stash, still open after M2, are done with M4 (below). T1.6 fights, rechecked with M4: the alarm
  never sent anyone home, for two reasons, both fixed. The engine never picked the flee package
  (eligible and first on the list, the sandbox still running after `EvaluatePackage`), so the alarm
  package is now a travel package (must reach, always run, ignore combat). And the plain
  `iAlarm && GameDaysPassed - fQuiet >= (1 / 24)` cleared the alarm the moment the fight stopped (now
  `eval` with parentheses: it holds for a game hour). `tools/ingame_town.py fight` then passes (the
  alarm in 1 s, every non-defender home within 60 s and alive), on the second fight in a game. The
  first fight in a fresh game failed 4 of 8: residents still walking to their morning places were
  home only after 60 s. Defenders killed are counted, as the design says: 1 or 2 of the 4 died to
  three geckos in each of the last three runs.
- **M3 The rival and the law** (plan `docs/plans/2026-11-28-m3-rival-law.md`): the Crimson Caravan
  as a rival (anger, price wars, poaching, NCR bids), heat, the licence and the duty, outlaw marks
  (`CCLawFn`, `CCLawScript`, `CCLawTextFn`; models `tools/law_model.py`, `tools/company_model.py`).
  `tools/ingame_m3.py` (game vs model every day) found three game bugs, all fixed: a plain
  `set x to arr[i]` aborts a script silently at run time (it killed every tier 2+ contract offer;
  now `let`); a plain `if` on an array element did the same in the weekly people pass (the 0x35F
  error, now `if eval`); and the bill estimate used the wages from before the day's staff changes
  (now recomputed; the model now writes its report at the tick, as the game does). The last run had
  0 script errors and 3 estimate mismatches, the ones fixed after it; `tools/ingame_m4.py` covers
  them again. What to try: `docs/m3-what-to-try.md`.
- **M4 The late game and the ending** (plan `docs/plans/2026-11-28-m4-ending.md`): done. Tier 4
  (the NCR quartermaster, forward tickets, lending to outfits) and tier 5 (favour in New Vegas, the
  three laws, share blocks, the race for Primm against the Crimson Caravan), then RETIRE and the
  three "20 years on" pages (`CCLateFn`, `CCLateUtilFn`, `CCLateTextFn`, `CCLateScript`,
  `CCEndingFn`, `CCEndLineFn` from `tools/gen_ending.py`; models `tools/late_model.py`,
  `tools/ending_model.py`; 273 model tests pass). `tools/ingame_m4.py 50` (game against the model
  every day for 50 days, tier 5 on day 36, a law passed and a share block bought, then retire) found
  four game bugs, all fixed: a `;` inside a string literal (it starts a comment), the bill estimate
  without the M3/M4 bills (now one shared act, `CCLawFn 13`), the forward memo's good read from the
  wrong digits, and a closed company's Post that never drew (the closed-page test read the screen
  before it was loaded). The last two runs passed all 326 checks with 0 script errors (tier 5 on day
  36; the closed Post and its three "20 years on" pages read back after RETIRE). A review pass then fixed: a closed company's "20 years on"
  pages could be pushed out of the Post by a same-day away, road or robbed letter (now written last,
  game and model, with a model test); result text cleared on all 16 rows; and the side taken at the
  Dam is now read for the ending's text, from the vanilla battle state (`vHDBattleController.iBattleState`;
  the battle quests themselves run from the game's start, so they can't be used). Checked in game:
  0 with no battle, House (2) with the state set to 3. Also in this step, from M2: branch terminals at Sloan and the Mojave Outpost,
  relay desks at the 188 and Novac, and the tier 3 strongroom chests (one stash, the office safe,
  from any branch). What to try: `docs/m4-what-to-try.md`, `docs/m2-what-to-try.md` section 6.

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

- (M2 2.6) Branch terminals stand at Sloan on Chomps Lewis's checkpoint table and in the Mojave Outpost
  barracks bar; relay desks on the 188's bar and the Novac motel's front desk; all placed once by
  `CCFoundingScript`, old saves too. The tier 3 remote stash is a footlocker beside each branch
  terminal that opens the Goodsprings office safe (now a real container, the vanilla empty safe).
- (M2) Any company terminal buys the tier 2 perk's crates, relay desks included (the model has no
  terminal location).
- (M3 review) The bill estimate (front page, page 2, the short-on-bills letter) now counts the duty on
  the declared share, the licence by tier, the cover premium and the quartermaster's bill, in the model
  and the game (`CCLawFn` act 13).
- (M4) The ending's laws line reads "N of the three laws" (no plural to get wrong).
- (M4) The ending names the side taken at the Dam from the vanilla battle state (1 NCR, 2 Caesar,
  3 House, 4 Yes Man); the last side seen is kept after the battle.

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
- 1.7: a notice is served only at a terminal visit or when its letter is shown; until then it is
  deferred and its clock does not run. Paying a deferred notice still counts the strike.
- 1.7: a second miss on probation skips Grace (straight to a final notice). A third strike within
  56 days is a takeover (7 days) that owner money cannot cure; curing it drops the oldest strike.
- 1.7: owner rescue comes from the player's caps, at most 2 weeks of running costs plus principal,
  once every 28 days, never in a takeover; it is booked as owner money and never counts for a tier.
- 1.7: selling the wagon gives 60% of its value (assets less buildings) and pays the arrears at
  once; a new wagon (700) can be bought on Routes when nothing is owed. Walk away needs two clicks.
- 1.7: the forecast warning shows when runway < 5 days and the company is ok or on probation;
  one forecast letter a bill cycle.
- 1.7: the busy shield is the player's cell coming from a DLC whose main quest is not done (quests
  looked up with `GetFormFromMod`); it stops the clocks, holds field letters and caps a day's event
  losses at the previous day's margin. A test switch `CCCore.iShieldTest` forces it.
- 1.7: letter order when several wait: closed, notice, forecast, away, road, loss.
- 1.8: candidates are drivers (1 in 4) or guards; hands still come with raw sites (tier 2). One
  wagon needs one driver, so a second driver cannot be hired; without a driver the wagon stays in
  the yard and a contract delivery is missed.
- 1.8: a contract offer is a memo only (no field letter); unanswered it is declined. Offers go
  only to a company with no open notice, a wagon and a driver.
- 1.8: FIRE needs two selects, like WALK AWAY. BACK on a screen reached from another screen goes
  back there (Candidate > Hire > Staff, Slot > Standing orders > Orders).
- 1.8: standing order values: keep 1 to 8 crates (step 1), prices 5 to 995 (step 5); changing a
  price order's good resets it to that good's anchor price; an emptied slot starts again at Primm
  and water. Contract crates ignore standing orders.
- 1.8: the bandit odds now use the crew's cover (r = cover / 60, clean chance r^2 / (1 + r^2)).
- 1.8: `CCCoreScript` must stay under about 16 KB compiled: the in-game compile failed at about
  18 KB ("loop at N jumps to 0"). The contract and the morning report moved to `CCContractFn`
  and `CCReportFn` (core now 12.7 KB). `CCTermDraw` is 15.8 KB, so new screens go in `CCTermDraw2`.
- 1.8 fix: the game's seeded roll lost whole units: `day * 7919 + seed * 104729` is about 1.3e8 and
  the script engine rounds it (single-float precision; the console gives 28 where the model gives
  25). Every game roll is now `((day % 100) * 19 + (seed % 100) * 29 + key * 31) % 100`, the same
  value as the model's formula. The bandit rolls had matched so far by luck.
- 1.9: the calls are in the M1 plan ("My calls for 1.9"): delivery and Ghost Town trust, the tier
  letter (kind 7), the Build screen (screen 15), the office as a vanilla shack with scripted doors,
  the Primm stall, no office rent.
- 1.9: the office terminal mesh faces 90 degrees off its rotation (set to 270 to face the room);
  the desk is turned 180. The exit marker stands west of the door, facing south-west, clear of a
  vanilla boulder (the third-person camera sat inside it).
- 1.9 fix: `fnv_spec build` wrote `CCCoreScript` without its compiled data after the spec's cells
  changed (a compile-cache miss), so the game had no `CCCore` variables. `tools/rebuild.sh` now runs
  `tools/check_compiled.py` after every build and stops on any uncompiled script.

- 1.10 review answers: (1) the daily plan now starts on at founding: the company works while you
  are away (design). (2) No float for the first week: the stress test showed a company with 0 to
  800 cash dies either way; rescue loans and the contract advance come in M2; the forecast warns
  5 days ahead. (3) A second miss on probation skips Grace, as the design says. (4) An unanswered
  road memo on a Primm delivery day sends the wagon (keeping it home would miss the delivery); the
  memo and the road letter give the odds of a clean run. (5) At tier 1 the CHAINS row opens a
  checklist of what tier 2 needs. (6) No bandits for 2 days after a new tier. (7) At most 10 people
  on the books (the Staff screen's rows). (8) Paying the loan down by hand is M2; M1 has the prepay
  memo. (9) Underdog contracts and easing after a loss are M2. (10) Correction: terminal text is
  not always cut to 200 characters: report page 1 can reach 214, under the engine's 259.
  (11) The sheriff flag is read once at founding; workshop hands are M2.
- 1.10: the Primm branch terminal is the company terminal form placed by `CCFounding` with
  `MoveToCell VikkiAndVance 1010 4027 7370`, facing the floor (heading 0).
- 1.10 fix (checks): a reputation box (`SetStage VMS16b 100`) and Sunny Smiles' greeting
  (DialogMenu) stop quest scripts; `tools/live.py to_game_mode` now closes both.

## Open items for the final report

- fnv-mcp: when an in-game compile fails, the tool retries with editor IDs swapped for hex form
  IDs and reports the retry's error, which hides the real one (`call CCPlanFn` becomes
  `call 14000804`: "Expected user function").
- fnv-mcp `fnv_ui_do button` cannot pick a terminal row by its label (all rows share one tile name).
- Terminal typing speed, vanilla interior references, `Quest.var` in compile, console echo lines.
- The weekly statement (doc) is not built yet.
- Not in M1: the successor chapter, rescue loans, the contract advance and the Hail Mary; the
  "after the loan is repaid" strike rules.
- 1.7 checked in game but only by the model: the takeover path and the walk-away second click.
  The busy shield's DLC detection is not checked in real DLC cells (M0 0.12 proved the source
  plugin test; the game used the test switch).
- fnv-mcp: after a `coc` launch the companion closes every message box for 90 s (the arrival
  closer), the mod's field letters too, and `fnv_status` does not list that task. The checks now
  wait until 105 s after launch (`tools/live.py`).
- fnv-mcp: the spec builder writes no door teleports (XTEL); the office doors are scripted.
  `fnv_spec build` can write a script uncompiled on a cache miss without saying so.
- Not in M1: office rent; skill-gated workshop hires (Survival 50 for the purifier).
- The checks move the game window to the monitor named in `tools/local.json` (not in git).
- Unverified: VMS16 (Ghost Town Gunfight) completion for a player who sided with the Powder Gangers;
  the DLC quest IDs used by the busy shield; `nVPrimmDeputyConv`.
- fnv-mcp (uncommitted in fnv-mcp-code): `fnv_spec build` now lets records name the plugin's own
  placed references by editor id (an AI package's location).
- (M3 review, low) The cover premium counts running roads in the game and running wagons in the model;
  they differ only if two wagons could share a road, which `buy_road` does not allow.
- A plain `set x to arr[i]` or a plain `if` on an array element aborts a script silently at run time,
  and a `;` inside a string literal starts a comment: both found by the in-game checks, worth a
  linter rule in fnv-mcp (`fnv_script_lint`).
- Not checked by eye: the "opens at tier 3" notice of a strongroom chest below tier 3 (a corner
  message); the Outpost and Sloan chests' spots (placed by coordinates; the Primm one was checked by
  ray, and every terminal by photo).
- (M4) Not checked in the game: a real Battle of Hoover Dam (the side read was checked by setting the
  battle state by console), and a closed company's ending pages on a day with an away, road or robbed
  letter (the order is fixed in the game and the model,
  and a model test covers it; the 50-day check retires with the player at the terminal).
- (T1.6) Defenders die too easily: 1 or 2 of the 4 (Amos, Marisol) were killed by three leveled geckos
  in each recent fight check. Worth more health or better arms for the defenders, or a check against
  raiders, as the design table has it. Also open: the first fight in a fresh game misses the 60 s
  target for residents still walking to their morning places.

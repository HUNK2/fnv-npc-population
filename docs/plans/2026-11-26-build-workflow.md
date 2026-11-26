# Build workflow: lived-in towns core + Mojave Caravan Company

How the mod gets built, from today to a release. The design itself is in the Claude Doc
"Mojave Caravan Company: full business design" (https://claude.ai/artifact/C2FeS7JVVZXkTiDsAuQKLr),
critic-approved and with all 15 decisions answered on 2026-11-26. This file is about the *how*:
the order, the loop each piece goes through, how things are proven, and where I stop and ask you.

## 1. What "done" means

- Two plugins, as you decided: a **lived-in towns core** (a master file) and the **company add-on**
  that needs it. Each milestone ends playable and could go to Nexus as a beta.
- Every milestone meets the "Done when" line from the design doc's Build order, proven in the
  running game, not assumed.
- Nothing in vanilla is edited: new records, new interiors, one new door per town, vanilla quests
  read and never written.

## 2. The order

```
M0 Proofs ──> M1 One road ──> Towns design ──> T1 Goodsprings ──> M2 Chains ──> M3 Rival & law ──> M4 Ending
 (live tests)  (company)       (talk + doc)     (lived-in core)    and people
```

- **M0 first**: it answers every "needs a live test" row in the design, plus the crowd test that
  settles the towns core question still open from before (plugin-first vs engine-plugin-first).
- **M1 next**: it is fully designed and the shortest path to something you can play. From M1 on the
  mod is already two files: the core starts as a thin master (shared factions, globals, the roles
  kit) and the company plugin lists it as its master, so your core/add-on split holds from day one.
- **Towns design, then T1**: the lived-in towns part has brainstorm notes but no design doc yet. It
  gets the same treatment the business got (design doc, review, your decisions) with the M0
  crowd-test numbers in hand, then Goodsprings is built as the first lived-in town.
- **M2 to M4** follow the design doc's Build order. Hiring real residents (M2) is where the two
  halves meet.

## 3. The loop every milestone follows

1. **Plan.** I write the milestone's plan in `docs/plans/` from the design doc: files, records,
   scripts, and the test that proves each task. Small tasks, each with its own test.
2. **Your OK.** You read the plan (or tell me to go ahead without reading it).
3. **Build, task by task** (section 4).
4. **Milestone check.** I run the design doc's "Done when" line in the game: an automated
   two-game-week run for M1, the 100-day balance run against the Numbers targets, an FPS
   comparison with vanilla in every town the milestone touches, and adding the plugins to an old
   test save.
5. **Review.** One fresh reviewer reads the whole milestone against the design and the plan
   (Sonnet by default; Opus only if you ask). I fix what it finds, or explain why not.
6. **Your playtest.** The design's "a tester plays two weeks" means a human: you. I give you a
   short "what to try" list and a test save. Your notes become fixes before the next milestone.
7. **Doc upkeep.** If the build proved part of the design wrong, I change the design doc and say
   what changed and why in the closing message, never silently.
8. **Beta (optional).** I package a zip (`release/`), you upload it to Nexus.

## 4. How one task is built

Each task in a plan goes through the same steps:

1. **Write the test first.** Ledger maths: a Python unit test against the reference model
   (section 5). Game behaviour: an `fnv_test` scenario with exact pass marks.
2. **See it fail** (the record or script does not exist yet).
3. **Build.** Records through `fnv_spec` (the fnv-mcp builder); scripts compiled with
   `fnv_scripts_compile`; our own C (only if a test proves script cannot do it) through
   `fnv_plugin_build` as a small xNVSE plugin.
4. **Install** into the Dev profile with `fnv_install` and **run the test live**.
5. **Look.** `fnv_photo` for anything visible, `fnv_script_errors` and `fnv_warnings` after
   every run, so a passing test with a hidden script error does not count as a pass.
6. **Keep the evidence**: screenshots, logs and numbers go into `docs/evidence/<milestone>/`.
7. **Record progress** in `docs/PROGRESS.md` (section 9) and commit (if you agree to git, G3).

A task is done only when its test passes in the game. If it fails twice for the same reason, I
stop guessing and debug it properly (read the engine code with `fnv_func`, trace the script),
and write down what I learn.

## 5. How things are tested (three layers)

| Layer | What it checks | Tool | When |
| --- | --- | --- | --- |
| Reference model | the ledger maths: prices, routes, wages, interest, strikes, tiers | `tools/ledger_model.py` (Python, unit tests); it must reproduce the doc's worked first week (day margins +746, +288, +94, +94, -117, +124, +91; net 722; day-7 net worth 923) | every task that touches money |
| In-game scenarios | behaviour in the real game: terminals, the day tick, saves, crews, raids | `fnv_test` scenarios in the Dev profile, on `fnv_test_save` saves; the in-game ledger is checked against the reference model's numbers for the same seed | every task |
| Runs and playtests | balance, feel, speed | the 100-day debug run (scripted player) against the Numbers targets; `fnv_profile` FPS against vanilla; your playtest | each milestone end |

The reference model and the in-game CCLedger must agree. When they differ, the model is the
spec for the maths, so the script gets fixed, unless the doc was wrong, and then both change.

## 6. Where files live

```
C:\DecompModGithub\fnv-npc-population\
  design\               the visualiser source (caravan-company.html)
  research\             engine catalogue, business research, swarm reports, critic rounds
  docs\plans\           this workflow and one plan per milestone
  docs\evidence\        screenshots, logs, numbers from live tests, per milestone
  docs\PROGRESS.md      where the build is now (section 9)
  mod\core\             the lived-in towns core: spec, scripts
  mod\company\          the company add-on: spec, scripts, terminal texts
  tools\                ledger_model.py and its tests, packaging, small helpers
  release\              readme, changelog, licence, packaged zips
```

Built plugins install only into the Dev profile, `C:\Modding\FNV-Dev` (Mod Organizer, profile `Dev`).

## 7. Who does the work, and the usage budget

- **I build it myself, in this session** (the "native" way). That costs far less than a fresh
  agent per task, which matters on your plan. The plans carry the design, so nothing is lost.
- **Helpers only when they pay off**, one at a time, never a swarm: Haiku or Sonnet for reading a
  large reference (JohnnyGuitar or JIP source, the decomp) and returning only the answer.
- **One review per milestone** (section 3, step 5). Opus only when you ask.
- **Usage checks**: I check usage at the start of each milestone and before any helper. If the
  limit is close, I stop at a task boundary with `PROGRESS.md` up to date, so nothing is lost.

## 8. Rules that hold the whole way

- Your real saves and your real game folder are never loaded, overwritten or deleted. Live tests
  use the Dev profile and test saves only.
- The unpacked game image (`%USERPROFILE%\.fnvdecomp\FalloutNV.exe`) never goes into a repo or a
  download; the API key is never printed. No decompiled code ships: any C we ship is our own.
- No vanilla record or reference is edited (the design's own rule).
- Before a live session: a display-on helper is started (a sleeping monitor hangs the game at
  startup), and on the first live day I check with you which monitor the game should use (my
  note about monitor 2 is from 19 November and may be out of date).
- Downloads, commits, pushes and Nexus uploads happen only as agreed with you (section 10).
- Every decision you make goes into memory as we go; every call I make is marked "my call" in the
  plan, so you can overrule it.

## 9. Keeping progress across resets

`docs/PROGRESS.md` always says: the current milestone and task, the last test that passed (with
its evidence path), what is half-done, and the next step. It is updated at every task end. Memory
gets the decisions and milestone results. A context reset, a usage limit or a reboot therefore
costs a re-read, not lost work.

## 10. Where I stop and ask you

| Gate | When | What I need from you |
| --- | --- | --- |
| G1 | now | OK this workflow (or change it) |
| G2 | start of M0 | JohnnyGuitar NVSE is not in the Dev profile. Either you install it there, or you OK me downloading the release from its official GitHub page (I'll give the file name and size first) |
| G3 | start of M0 | the project folder is not a git repo. May I `git init` it and commit after each task (local only)? Pushing to a private GitHub repo only when you say |
| G4 | end of M0 | the M0 results, plus the towns core question (plugin-first or engine-plugin-first) with the crowd-test numbers |
| G5 | each milestone plan | OK the plan |
| G6 | each milestone end | your playtest notes; whether to ship a beta |
| G7 | towns design | the lived-in towns decisions, the same way as the business ones |

Between gates I keep going without asking, and make the small calls myself, each marked in the
plan as my call.

## 11. M0 in outline (its full plan comes next, after G1)

| # | Task | Passes when |
| --- | --- | --- |
| 0.1 | Project set-up: the layout above; `tools/ledger_model.py` from the overnight economy sim, with unit tests | the model reproduces the doc's worked first week |
| 0.2 | Tool check: can `fnv_spec` write every record type the mod needs (quest with script, terminal with menu items and conditions, NPC, interior cell, a door placed in an exterior cell, form list, global, message, note, activator)? | each type builds and loads; any gap becomes an fnv-mcp fix first |
| 0.3 | Dependencies in the Dev profile: xNVSE, JIP LN NVSE (present), JohnnyGuitar NVSE (G2) | the game starts with all three loaded |
| 0.4 | A proofs plugin: one test interior with a company terminal, a test quest, three test NPCs, a road marker | it loads with no warnings |
| 0.5 | Terminal text round trip: set a label, open, change it while open, redraw; scroll position; gone after a reload | labels change live; scroll kept; rewrite-on-load confirmed needed |
| 0.6 | Open a terminal by script, from the console and from a Pip-Boy item | both open the right terminal |
| 0.7 | Menu event timing: does the open event run before the first draw? | new labels show on the first frame, or a fallback is chosen |
| 0.8 | Limits: 30 buttons and 259-character texts on one screen | scrolling and skipping work; typing time measured |
| 0.9 | Day tick: wait 5 days, exactly 5 steps; wait 20 days, 14 steps plus 1 summary; reload and wait again, same results (seeded rolls) | exact counts and same results |
| 0.10 | Field letter: a message box with buttons; waits during combat, dialogue and menus | it never appears at the wrong moment |
| 0.11 | Road crews: move a 3-person hired crew to a road marker and back; spawn and remove brahmin | no leftovers; save size steady over 10 cycles |
| 0.12 | Busy shield: the player's cell can be traced to a DLC plugin, also in DLC interiors | correct in every DLC land, false in Mojave interiors |
| 0.13 | Old save: add both plugins to a test save made without them | the company starts cleanly; deeds already done count |
| 0.14 | Crowd test (towns): 30 extra townspeople in Goodsprings | FPS against vanilla Goodsprings measured; which engine actor limits are hit (50-slot near-player cache, 20 complex-scene actors, 20 in combat) |

M0 ends with `docs/m0-results.md`, the design doc's "What is proven and what needs a live test"
table updated, and gate G4.

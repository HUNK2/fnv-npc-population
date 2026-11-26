# T1 Goodsprings: plan

**Goal:** Goodsprings gets 14 residents with homes, a day, a field, reactions and a fast alarm, in
the core plugin `LivedInMojave.esm`, with no vanilla record changed.

**Design:** `docs/towns-design.md` (reviewed 2026-11-27, Sonnet, 16 points folded in).
**Model:** `tools/town_model.py` (the spec the game follows), tests `tools/test_town_model.py`.
**Gates:** the user asked (2026-11-27) for the whole plan to run without stopping; plan approval
and the towns decisions (G5, G7) are my calls, marked here.

## Global constraints

- Plugin-first (G4): no engine plugin. xNVSE, JIP LN and JohnnyGuitar are already required.
- No vanilla record edited: residents and interior markers live in the core's holding cell
  `LIMHoldingCell` and are moved into town once (`MoveToCell`, as Hollis in M1); exterior statics
  and markers are the core's own references in the Goodsprings exterior cells.
- Nothing runs before Doc Mitchell's intro quest (VCG01) is done.
- FPS within 2 frames of vanilla Goodsprings at 7, 12 and 0 hours.
- Public MIT repo: no decompiled code, no personal paths.

## Records (my calls)

- **Packages** are built from vanilla templates, patched (layouts read from FalloutNV.esm):
  `PKDT` = flags u32, type u8, pad, behaviour flags u16, type data u16, pad (types: 1 follow,
  4 sleep, 6 travel, 10 flee-not-combat, 12 sandbox, 15 dialogue); `PLDT` = location type i32
  (0 near reference, 1 in cell, 3 near editor location), target FormID, radius i32; `PSDT` =
  month s8 (-1), day of week s8 (-1), date u8 (0), hour s8, duration i32 hours; `PTDT` = target
  type i32, target FormID, count i32, float.
  Templates: `GSSettlerCFSandboxPackage6x6` (sandbox), `GSSettlerAAMSleepPackage22x8` (sleep),
  `EasyPeteChairPackage8x4` (travel to a reference), `DefaultFollowLinkedClose` (follow),
  `EasyPeteHideInSaloonPackage` (flee not combat, conditioned).
- **Homes:** sleep and eat packages use "in cell" `GSHouseInterior01` to `04` (no marker needed
  inside a vanilla interior); the mod adds beds/bedrolls as its own references moved in once.
- **Package order per resident** (first match wins): alarm run-home (condition
  `GetQuestVariable LIMGoodsprings iAlarm == 1`), the gangers' departure (condition `iGone`),
  then the day blocks of `town_model.place()` by hour, then a home sandbox fallback.
- **Quests:** `LIMGoodsprings` (10 s): first run moves the cast, reads VMS16 / VMS16b / fame and
  infamy, sets `iGone`, `iExtraHand`, travellers enabled by hour; `LIMGSAlarm` (1 s, only while the
  player is in a Goodsprings cell).

## Tasks

| # | Task | Passes when |
| --- | --- | --- |
| T1.0 | Proofs (`docs/t1-results.md`) | off-screen schedule, text-only conversation, child race: each answered live; faction and doors answered (done) |
| T1.1 | Town model | DONE: `tools/test_town_model.py` 18 tests |
| T1.2 | Core plugin: factions, holding cell, 15 NPC bases, the two quests | builds, loads, `tools/ingame_town.py setup` reads the quest's day state = the model for VMS16 done / not done |
| T1.3 | Places: field statics (collisionless crop rows, fence, trough, scarecrow), field gate, porch chairs, beds | `fnv_place check` clean; photos `docs/evidence/t1/t1_*.png` |
| T1.4 | The day | `tools/ingame_town.py day`: at 6 hours, in town and after being away, each resident within 500 units of the model's place |
| T1.5 | Group walk | the Pruitts never more than 600 units apart on the walk; Amos disabled: Lena and Cal still arrive |
| T1.6 | Fights | three raiders at noon: alarm within 2 s, non-defenders home within 60 s, none of them killed |
| T1.7 | Reactions + vanilla quests | each reaction row from the real quest outcome; VCG01, VMS16 (both ends) and VMS16b (gangers) complete |
| T1.8 | Chat and lines | one pair holds a conversation on a porch at 19; every resident has 2 or 3 personal greetings |
| T1.9 | Milestone check | FPS at 7, 12, 0 vs vanilla with the town walking; old save (also one saved in Goodsprings); review; `docs/t1-what-to-try.md`; push |

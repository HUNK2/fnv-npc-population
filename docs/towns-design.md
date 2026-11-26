# Lived-in Mojave: towns design

The towns half of the mod (the core plugin, `LivedInMojave.esm`). The business half is
`docs/design.md`. This doc turns the 2026-11-26 brainstorm decisions into a buildable design.
Decisions the user made are marked **Decided**; everything else is my call (the user asked for the
whole plan to run without stopping at gates, 2026-11-27) and is marked **My call**, to be reviewed.

## Read me first

- **What it is.** Towns that look worked-in: more people who belong there (farmers, families,
  hands, a night watch), each with a day of their own, who react to what the player did to their
  town. Goodsprings first (T1), then the other towns the company reaches.
- **What it is not.** No random spawner, no crowd. No change to any vanilla named or story NPC. No
  engine plugin.
- **The bar.** A player who walks through Goodsprings at 7 in the morning, noon and midnight sees
  three different towns, can name why each person is where they are, and the frame rate is within
  a few frames of vanilla.

## Goals, non-goals, anti-goals

| | |
| --- | --- |
| Goals | believable residents (a fixed cast with names, homes and jobs); a daily rhythm; places to be (fields, homes, porches); reactions to the player's choices in that town; neighbours talking; cheap enough to add to every town later |
| Non-goals | smarter combat AI (dropped by the user 2026-11-26); whole-story reactions (Decided: local only for now); a new engine-level scheduler |
| Anti-goals | a town that feels crowded; residents who die in droves when a fight starts; anything that breaks a vanilla quest; a save that grows every day |

## Decided (2026-11-26)

1. **Fixed resident cast** per town, not generated people. Works on existing saves by reading the
   current quest state.
2. **Role-based reactions.** A few defenders fight; the rest flee home or hide; word spreads through
   town reputation. Enemy factions are exempt so combat and story stay intact.
3. **Opt-in rules.** Only the mod's own tagged townsfolk get the new rules. Vanilla named and story
   NPCs are untouched.
4. **Persistent / non-persistent split.** Persistent references for anyone whose day crosses doors
   or cells (families, shopkeepers, the night watch); ordinary placed references for people whose day
   stays in one outdoor area (they exist only while loaded, which is cheaper).
5. **The four additions:** daily rhythm (busy mornings, quiet nights); places to be (fields,
   farmhouse, homes); the town reacts to player choices (the user's favourite: "reinforcement in the
   choices you make"); neighbours chatting.
6. **Local reactions only for now**: Goodsprings reads Ghost Town Gunfight (VMS16), Run Goodsprings
   Run (VMS16b) and Goodsprings reputation.
7. **Group walking**: families and farmhands walk to the fields together.
8. **Towns core + company add-on**, two plugins; the company hires real residents (M2).
9. **One new door per town exterior** at most.
10. **Public release**; FPS within a few frames of vanilla Goodsprings (M0 0.14 measured 30 extra
    people: 59.6 fps against 59.8, no engine limit hit; **plugin-first**, G4).

## What Goodsprings has today (FalloutNV.esm)

- Named: Doc Mitchell, Sunny Smiles, Trudy, Chet, Easy Pete, Ringo, Victor; four generic
  `GSSettler*` (AM, CF, AAM, CM) on `GoodspringsFleePackage` + gunfight packages + sandboxes.
- Interiors: Doc Mitchell's house, the Prospector Saloon, the general store, the gas station, the
  schoolhouse, Victor's shack, an abandoned shack, and **four "Goodsprings Home" interiors
  (`GSHouseInterior01` to `04`) with nobody living in them**. Those homes are where new families go:
  no new door is needed for them.
- No farm: the spring (`GoodspringsSource`) and the cemetery are the only named outdoor places.
- Vanilla's flee package only runs from VMS16 quest variables (the gunfight).

## The cast (T1 Goodsprings): 14 people

**My call.** 14 extra people (well under the 30 the crowd test cleared, leaving room for other mods,
older PCs and the company's yard). Three households, three hands, a night watch, two travellers.

| Who | Lives | Day | Role in a fight | Persistent |
| --- | --- | --- | --- | --- |
| The Pruitt family: Amos (father), Lena (mother), Cal (son, 15) | Home 01 | fields at the spring 6 to 12 and 14 to 18, lunch at home, porch in the evening | Amos defends; Lena and Cal flee home | yes |
| The Okafor family: Joseph (well-digger), Ada (mends clothes), Ruth (girl, 9) | Home 02 | Joseph at the well/spring and the store; Ada on her porch and the store; Ruth plays near the schoolhouse, home by dusk | all flee home | yes |
| Widow Harlan and her nephew Wes | Home 03 | she keeps the chickens and the garden behind the house; Wes hauls water to the saloon | Wes defends | yes |
| Three farmhands: Dutchy, Marisol, Old Abe | bunk in Home 04 | walk to the fields with the Pruitts, eat at the saloon at noon, drink there in the evening | Marisol defends; others flee to Home 04 | yes |
| The night watch: Hector Vane | the gas station's back room (by day he sleeps there) | patrols the main road 21 to 5 with a lantern | defends | yes |
| Two travellers (a prospector and a drifter) | none | sit at the saloon's tables in the evening, sleep on bedrolls in the saloon's back corner; away by day (the town quest disables them 7 to 18) | flee | yes (a non-persistent actor cannot leave its cell; review 6) |

Names, faces and kits are placeholders for the build. Cal (15) is an adult-race NPC with a young
face; Ruth is the only child and uses an existing child race (checked with `fnv_record` before the
build: race, skeleton and walk animations). Children are essential and never hostile. Every
resident sleeps in a bed or bedroll of their own that the mod places (Home 04 gets three
bedrolls; the gas station back room and the saloon corner get bedrolls). Each resident has two or
three personal greeting lines, not only the shared chat.

## The day

**My call.** Four blocks, written as AI packages on each resident (vanilla's way: a package list
with time windows, first match wins).

| Time | Town |
| --- | --- |
| 5 to 7 | the watch walks home; farmers wake, eat, gather at the Pruitt porch |
| 7 to 12 | fields (group walk), well, store, chores; children at the schoolhouse yard |
| 12 to 14 | lunch: families home, hands at the saloon |
| 14 to 18 | fields and chores again |
| 18 to 22 | porches, the saloon; neighbours talk |
| 22 to 5 | homes; the watch on the road; the saloon has the two travellers and Trudy |

Departures are staggered: each resident's package windows start 0 to 30 game minutes apart
(review 15), so the town never moves as one. No weather rule in T1: the Mojave seldom rains
(review 8).

## Places to be

- **The fields**: a small irrigated plot by the spring, new statics (fence posts, crop rows from
  the NCR sharecropper farms' meshes, a water trough), a scarecrow; idle markers for hoeing and
  kneeling. Placed in the Goodsprings exterior cells from the core plugin (a mod's own references
  in vanilla exterior cells are fine; M1 placed the wagon yard that way).
- **Porches**: chair and lean markers on the homes' porches.
- **Chicken coop and garden** behind Home 03 (chickens are not in FNV: the garden alone; my call).
- **The saloon**: no change to vanilla references; the hands use the existing chairs (sandbox).

## Group walking

**Decided**: families and farmhands walk to the fields together. **My call** on how (after review
point 7): the Pruitt family walks as a group: Amos runs a travel package to the field gate marker,
Lena and Cal a follow package on him in the same window, with a fallback travel package of their
own when Amos is dead, disabled or not in their cell (package conditions), so the family never
stalls. The engine places followers single-file (`GetFollowerOffset` 0x00643FF0 sorts them by
distance), which reads as a family on a path. The hands walk on their own travel packages to the
same gate, 5 to 15 game minutes apart, so the road to the fields has people on it rather than one
column. Side by side needs an engine change (non-goal: plugin-first). At the gate everyone
switches to their own field sandbox.

## Reactions to the player's choices (local)

**Decided**: local only, from the quest state and town reputation. **My call** on the table:

| What the player did | What Goodsprings does |
| --- | --- |
| Helped in Ghost Town Gunfight (VMS16 done for the town) | the fields are busier (a fourth hand joins at stage done); residents greet the player by name; the Pruitts' porch has a "welcome" idle |
| Sided with the Powder Gangers (Run Goodsprings Run) | the families leave after one in-game day: the mod's own residents are moved back to the holding cell (no vanilla door or home is touched), the fields go to seed; only the hand who sided with the gangers stays |
| Goodsprings fame high | barter discount at Chet's from the residents' word (a greeting line only in T1; the discount needs a vanilla change and is a non-goal) |
| Goodsprings infamy high | doors lock at night; children stay inside; the watch shadows the player |
| The company (if installed) reaches tier 2 | Wes and one hand become hireable from the company terminal (M2, "hiring real residents") |

All reactions read state once a day in a core quest (`LIMGoodsprings`), so an old save gets the
right town on its first day with the plugin.

## Fights: who defends, who flees

**Decided**: role-based. Built with factions and packages, plugin-first:

- Every resident is in the mod's `LIMTownsfolkFaction` and in vanilla `GoodspringsFaction`, the
  way the vanilla settlers are, so the vanilla faction relations (Powder Gangers hostile) apply
  without editing a vanilla faction (review 4). T1.0 first lists every condition and script in
  FalloutNV.esm that reads `GoodspringsFaction`, so no quest counts our people by mistake.
- **Defenders** (Amos, Wes, Marisol, Hector): Aggressive 0, Confidence Brave, Assistance Helps
  Allies. They fight the player only if Goodsprings is attacked.
- **Everyone else**: Confidence Cowardly (the engine's own flee in combat), and a run-home travel
  package with the run flag, conditioned on `LIMGoodsprings.iAlarm`, for those not yet in combat
  (review 3: combat AI overrides the package stack, so the package is for the alarm, not the
  fight).
- **The alarm is fast** (review 1): a second quest `LIMGSAlarm` runs every second only while the
  player is in Goodsprings's cells; it sets `iAlarm` when a resident or the player is in combat in
  town, and clears it after a game hour of quiet. During VMS16's fight stages the alarm is on from
  the stage itself, so residents are home before the gangers arrive.
- **Word spreads**: an OnHit/OnDeath script on the residents' bases adds Goodsprings infamy
  (vanilla `AddReputation`), so the reaction table above follows (review 8).
- **Nothing before the intro**: the whole town system waits until Doc Mitchell's intro quest is
  done, so the tutorial walk-out stays vanilla (review 13).
- Enemy factions (Powder Gangers, raiders) are untouched.

## Neighbours chatting

**My call**: vanilla conversation packages (`Dialogue` package type with a target) between pairs at
the evening porches and the saloon, with a small set of shared topics (about 40 lines, text only,
no voice; subtitles as the game's own conversations use). Lines depend on the day's state (the
fields, the gunfight, the company's wagon if installed). Text-only conversation is unproven
(review 9): one pair is proven first; the fallback is sandbox idles and short barks.

## Old saves

- Every resident and every interior marker starts in the mod's own holding cell and is moved into
  town once by the core quest (as Hollis is in M1); exterior statics (fields, porch markers) are the
  mod's own references; no vanilla reference is changed. T1.9 also tests a save taken after
  visiting Goodsprings (review 12).
- The quest reads VMS16 and VMS16b stages and the reputation values on the first run, so a save
  past Run Goodsprings Run starts with the families gone.

## Performance

- 14 people (15 with the gunfight hand), all persistent. Budget: FPS within 2 frames of vanilla Goodsprings at noon and at
  midnight, `fnv_profile frame`, the M0 0.14 method.
- Persistent people out of the loaded area run on low process: the engine moves them by schedule
  only. That is unproven in this project (review 2), so T1.0 proves it before anything is built.
  The town quest runs every 10 seconds; the alarm quest every second only while the player is in
  town. Field crops are collisionless and the markers stand on vanilla navmesh (`fnv_pathing`),
  and T1.9 measures FPS with the town walking, not standing (review 11).

## Build: T1 Goodsprings

| # | Task | Passes when |
| --- | --- | --- |
| T1.0 | Proofs: a persistent NPC on a home/field schedule moves while the player is away (leave, wait, return at 3 set hours: it is where the schedule says); a text-only conversation package plays; every vanilla use of `GoodspringsFaction` listed; Home 01 to 04 doors unlocked or not; the child race works | each answered with evidence in `docs/t1-results.md` |
| T1.1 | Town model: `tools/town_model.py` (who is where at each hour, the reaction table) with tests | the tests pin each block and each reaction |
| T1.2 | Core plugin: faction, quest `LIMGoodsprings` (hourly, reads quest state), the 14 NPC bases, the holding cell | builds and loads; the quest's day state matches the model for VMS16 done/not done |
| T1.3 | Homes and places: residents in Home 01 to 04, field statics and markers, porch markers | photos of each place; no floating or buried objects (`fnv_place check`) |
| T1.4 | The day: packages per resident | an in-game check at 6 times of day, with the player in town and after the player was away (another cell, then back): each resident within 500 units of where the model puts them |
| T1.5 | Group walk to the fields | the Pruitts never more than 600 units apart on the walk, sampled every 2 s; Amos disabled: Lena and Cal still reach the field |
| T1.6 | Fights: alarm and flee/defend | three raiders attack at noon: the alarm is on within 2 s, defenders fight, the rest are home within 60 s; residents killed counted (target: none of the non-defenders) |
| T1.7 | Reactions | each row of the reaction table from the real quest outcome (VMS16 played to both ends, VMS16b to the gangers' side), not only by console |
| T1.7b | Vanilla quests intact | Doc Mitchell's intro, Ghost Town Gunfight (both outcomes) and Run Goodsprings Run (gangers' side) complete with the mod, from a new game and from a save; residents home during the fight stages |
| T1.8 | Chat | two pairs hold a conversation at the porches in the evening |
| T1.9 | Milestone check | FPS vs vanilla at 7, 12 and 0; old save; review; what to try |

## Review (Sonnet, 2026-11-27)

Sixteen points; the six blockers (slow alarm, unproven off-screen schedules, flee package under
combat, faction relations, touching vanilla homes, non-persistent travellers) and the vanilla-quest
task are fixed above, each marked "review N". Notes taken: staggered departures, personal lines,
beds, navmesh, old saves after a visit, tighter pass tests.

## Risks

- Residents wandering into the gunfight scene and breaking VMS16: the quest's alarm sends them home
  for VMS16's fight stages.
- The flee package fighting the vanilla `GoodspringsFleePackage` logic: ours only applies to our
  faction.
- Children in a Powder Ganger fight: essential, cowardly, flee first.

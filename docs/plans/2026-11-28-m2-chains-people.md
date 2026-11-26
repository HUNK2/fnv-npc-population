# M2: Chains and people, implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: superpowers:executing-plans (native, chosen in the build
> workflow). Steps use checkbox (`- [ ]`) syntax.

**Goal:** the company grows from one road to three: Sloan and the Mojave Outpost join, a second and a
third wagon run their own roads, Primm salvage, the smokehouse and the stone yard make goods, towns
level up from what you deliver, staff have numbers, traits and loyalty, two managers take chores off
your hands, contracts come from every town, and tier 3 opens.

**Architecture:** the same as M1. `tools/company_model.py` is the spec for every number; the game's
`CCCoreScript` and its functions follow it to the cap, checked by in-game runs. M2 widens the ledger:
4 towns and 12 goods (cells `town * 12 + good`), a warehouse per town, up to 3 wagons (one route
each). An M1 save is upgraded once (`iVersion` 1 to 2) by copying its 2 x 6 cells into the new layout.

**Spec:** `docs/design.md`: The map (Sloan, Mojave Outpost, roads), Goods and production chains
(smokehouse, stone yard, Primm salvage, town levels), People (numbers, traits, loyalty, managers),
Money (contracts), Growth (tier 3 and the tier perks), Relay desks, Balance targets.

## Global constraints

The M1 plan's global constraints stand (Dev profile and test saves only; no vanilla record edited;
200-character terminal texts; route C clicks; `%q` strings; appended variables; half-up whole caps;
the integer roll; letters from GameMode out of combat; nothing personal in the repo). Plus:
- Scripts stay under about 14 KB compiled (the in-game compile limit found in 1.9): new screens and
  steps go in new `CC*Fn` functions.
- An M1 save keeps every number it had (cash, loan, stock, staff, contract) after the upgrade.

## My calls (M2)

- **Three roads, not four.** Goodsprings - Primm (wagon 1), Goodsprings - Sloan and Primm - Mojave
  Outpost: all half a day each way, one round trip a day. Sloan - Primm (a day each way) waits for a
  later milestone: it needs two-day trips. A second wagon costs 700 (wagon and brahmin pair) from
  tier 2; a third from tier 3. Each wagon needs a driver; each road has its own danger: Primm 60,
  Sloan 30 (geckos, deathclaws from the quarry), the Outpost pass 60 (raiders).
- **Market goods and site goods.** Seven goods have markets in the towns (purified water, healing
  powder, ammo, dirty water, herbs, building materials, smoked meat); five are made or found only by
  the company's sites and sold to its own workshops (brahmin, stone, sand, scrap; stimpaks and
  moonshine are tier 4, M3). Site goods sit in the warehouse of the site's town.
- **Workshops and sites in M2:** corral (Goodsprings, brahmin), smokehouse (Primm, 1 brahmin -> 4
  meat, needs a Survival 35 hand, tier 3), sand pit and scrap yard (Primm salvage, tier 2), quarry crew
  (Sloan, stone, once Quarry Junction's deathclaws are dead) and stone yard (Sloan, 2 stone + 1 sand
  -> 2 materials, tier 3). Sand travels Primm -> Sloan only by the wagons' own load (it is a site good:
  the plan loads it like a crate with no sale, for the stone yard). Workshop levels with throughput
  (design) wait for M3.
- **Town levels** (Camp, Hamlet, Village, Town): a town's basics (water, meat, healing powder) are
  met on a day when each stock is at least 2 days of its use; 7 met days in a row plus building
  materials delivered since the last level (40, 90, 160 crates) raise the level; each level adds a
  quarter to the town's daily use of every good. 14 days unmet drop a level. Goodsprings starts a
  Hamlet, Primm a Village, Sloan and the Outpost Camps.
- **Staff numbers:** Skill, Nerve, Honesty, Loyalty (0 to 100) and one trait of eight (Haggler,
  Cautious, Reckless, Drinker, NCR veteran, Family man, Ambitious, Steady), each with one upside and
  one cost in the model's table. Roles: driver, guard, trader (spread -1 point per 10 Skill over 50
  on the wagon's road), clerk (each clerk is a wagon slot beyond the first), workshop hand (Skill
  checks the recipe). Loyalty starts at 55 (Low offer -10, Generous +10), +5 a week paid on time, -10 a
  missed bill; under 35 a raise memo; under 20 they leave. Loyalty lists its reasons on the person's
  page. Injury and death on the road wait for M3 (road crews).
- **Real residents as hires:** from tier 2, Wes Harlan and Marisol (lived-in Goodsprings, the town
  model's `hireable`) are among the candidates while Goodsprings stands; they keep their routine.
- **Managers in M2:** the bookkeeper (tier 2; Strict, Normal, Lenient: finds a skimmer with 100, 50, 0
  percent chance a week; Strict costs each clerk 5 loyalty a week) and the route manager (tier 3;
  Safe, Balanced, Fast: answers road memos itself: Safe keeps the wagon home, Balanced hires a gun
  when the clean chance is under 60, Fast always sends). The purchasing manager and the workshop
  foreman wait for M3 (M2 workshops each have one recipe and the plan already buys inputs).
- **Contracts from every town:** each week one offer from the town on the company's roads with the
  biggest shortage of a good the company can carry; open contracts: 1 at tier 1, 2 at tier 2, 3 at
  tier 3; each is the M1 contract shape (crates every 3 days for 28 days at sell price + 9%).
- **Tier 3:** earned worth 18,000 (the design's 8,000 was set before M2's wagons and sites, which count in worth; `balance_run.py` puts a good player at tier 3 on day 29 to 33 over 20 seeds), trust Liked (50) in two towns, Primm has a sheriff
  (`nVPrimmDeputyConv` done, as M1 reads it). Tier perks: at tier 2 the company buys trade goods from
  the player at a branch (purified water, healing powder; 0.8 of the anchor, up to 10 crates a day; a
  crate is 10 bottles or 10 powders); at tier 3 every branch has a company chest that opens the
  office strongroom (one container: a remote stash).
- **Relay desks:** a company terminal at the 188 Trading Post and in Novac (no market).
- **Visit length:** "a tier 3 visit under 8 minutes" is checked as clicks: the daily routine at tier
  3 (read the report, answer the memos, check each wagon, one contract) takes at most 25 clicks.

## Review focus

1. An M1 save upgraded mid-week: same cash, stock, staff, contract; bills land on the same day.
2. Three wagons and one event director: at most one road event in 3 days across the company.
3. A town dropping a level while a contract runs there: the contract stays as signed.
4. Hiring a real resident and the Powder Gangers taking Goodsprings: the hire leaves with the town.
5. Sand loaded for the stone yard on a full wagon: never sold, never counted as a sale.

---

## Tasks

| # | Task | Passes when |
| --- | --- | --- |
| 2.1 | Model: 4 towns, 12 goods, 3 roads, wagons, site goods (`company_model.py`, tests) | the M1 tests still pass; new tests for Sloan and Outpost prices, three wagons, sand to the stone yard |
| 2.2 | Model: town levels, staff numbers and traits, loyalty, managers, contracts per town, tier 3, perks | tests per rule; `balance_run.py`: a good player reaches tier 3 by day 28 to 35 |
| 2.3 | Game: the ledger widened (12-good cells, per-town warehouses, wagons), the M1 save upgrade | `ingame_run.py` matches the model for 14 days on a fresh game and on an upgraded M1 save |
| 2.4 | Game: Sloan, the Outpost, two more roads and wagons, sites and workshops, town levels | an in-game run of 28 days matches the model |
| 2.5 | Game: staff numbers, traits, loyalty, real residents, managers, contracts per town | `ingame_hiring.py` extended: matches the model |
| 2.6 | Game: terminal screens (Wagons, Towns, Managers), branches at Sloan and the Outpost, relay desks at the 188 and Novac, tier 3 perks | `ingame_terminal.py` extended to the new screens; every terminal opens the company |
| 2.7 | Milestone check | all in-game checks pass; tier 3 visit in at most 25 clicks; FPS; Sonnet review; `docs/m2-what-to-try.md`; push |

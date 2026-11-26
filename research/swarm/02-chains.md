# 02 - Production chains and logistics (2026-11-26)

Tags: [D] documented by source, [O] opinion, [V] read from FalloutNV.esm with fnv_record (read-only), [?] not verified, [NEW] our own invention (not vanilla).
Web access note: the Anno 1800, Factorio, Satisfactory and Schedule I wikis (fandom, wiki.factorio, satisfactory.wiki.gg) refused or 404'd automated fetches. Anno and Schedule I facts below come from search summaries plus the pages named; treat exact numbers there as [?].

## 1. Key findings

### 1.1 How chain games stay readable (and when they turn tedious)

- **Transport Fever 2** [D] https://www.transportfever2.com/wiki/doku.php?id=gamemanual:towns : a town has three growth factors (Destinations, Supply, Quality). Each district demands ONE cargo by default (commercial: goods, tools or food; industrial: construction material, machines or fuel). Level 1 and 2 buildings always demand the primary type. Fulfilled demands add up to +100% growth per district, and each building's supply rating (share of its cargo needs currently met) raises its level-up chance. Industries level when enough cargo is delivered AND inputs keep up; a progress bar shows the next level and its end zones mark the thresholds for downgrade and upgrade (https://www.transportfever2.com/wiki/doku.php?id=gamemanual:industriescargos). The manual does not say what a level changes in output or look [?].
- **Anno 1800** [O/D mix, search summaries; fandom wiki blocked]: five Old World tiers (farmers, workers, artisans, engineers, investors). Only BASIC needs must be met to advance; luxury needs raise happiness and tax income but do not add population. Upgrading a house also costs building materials (forum/wiki: farmers 4 timber, workers 6 timber, artisans 8 timber plus bricks, steel beams, windows) [?]. A Game Developer essay says Anno originally lacked a way to see production shortfalls and added exact production/consumption rates months later, and calls such diagnosis tools essential to making the genre approachable [O] https://www.gamedeveloper.com/design/an-ode-to-optimization-videogames . Takeaways: split needs into "grows you" vs "pays you", and make a tier upgrade also consume a build cargo.
- **Foundation** [D] https://wiki.polymorph.games/foundation/Resources : newcomers and serfs need one rustic food type; higher tiers need refined food, tavern goods and meals; villagers "need a wider variety of resources to remain happy" as they are promoted, which pushes the player into more complex chains; the Resources panel expands as buildings unlock. Takeaway: variety of goods per tier, not volume, is what creates new chains.
- **Factory-builder analysis** [O] https://leafwing-studios.github.io/Emergence/high-level/genre-analysis.html : satisfying = watching contraptions run, a complete solution that is easy to reach with optimisation on top, readable failures with debugging visualisation. Churn drivers = tedious waiting, no clear goal, poor pacing, hard recovery when a big part is disabled, no penalty for overproduction and mindless expansion. Takeaways: always show the current goal, make failure recoverable and traceable, add a cost to overbuilding (spoilage, upkeep).
- **Game Developer "ode to optimization"** [O] (URL above): each chain is a problem the player owns; upgrades force you to rebuild lines for higher yield; small fixes feel big ("that one conveyor belt").
- **Factorio forum** [O, via search summary only]: players resent hand-calculating ratios; they ask for in-game throughput tools. Takeaway: the terminal must do the ratio math for the player.
- **Schedule I** [D/O, Wikipedia https://en.wikipedia.org/wiki/Schedule_I_(video_game) + search summaries]: base product plus cheap ingredients mixed into a more valuable variant; hired botanists, cooks, dealers, cleaners; police pressure with random searches. Pricing is hidden effect multipliers on a base price [O, sources disagree between additive and multiplicative]. Takeaway for us: one cheap additive that raises a finished good's value is a satisfying "recipe discovery" with almost no new goods.
- **Banished** [?]: not opened. I will not cite it.

### 1.2 How few goods give depth

Anno-style depth comes from tiers of need, not from the number of goods. Foundation and Anno both gate the next tier on ONE new good. For our 4-town first version, 14 to 16 goods is enough if (a) every end good has a two-input recipe and (b) every town wants a different 3 to 4 of them.

## 2. FNV facts [V] (read from FalloutNV.esm)

### 2.1 Real recipes with cheap raw inputs (RCPE)
| Recipe | Inputs | Output | Station / skill |
|---|---|---|---|
| Healing Powder | 1 Xander Root + 1 Broc Flower | 1 Healing Powder | Campfire, none |
| Stimpak | 1 Surgical Syringe + 1 Broc + 1 Xander | 1 Stimpak | Workbench, Science 70 |
| Brahmin Steak | 1 Brahmin Meat | 1 Brahmin Steak | Campfire, Survival 35 |
| Desert Salad | Brahmin Steak + Pinyon Nuts + Barrel Cactus Fruit | Desert Salad | Campfire, Survival 55 |
| Cactus Water | 2 Prickly Pear Fruit + 1 empty soda bottle | 1 Purified Water | Campfire, Survival 30 |
| Mass Purified Water | 5 Dirty Water + Surgical Tubing + 2 Glass Pitchers | 4 Purified Water (tubing and pitchers returned) | Campfire, Survival 50 |
| Trail Mix | Apple + Pear + Pinyon Nuts + Sugar Bombs | Trail Mix | Campfire, Survival 25 |
| Ruby's Casserole (Primm) | Flour + Jalapeno + Mole Rat Meat + Radscorpion Gland | Casserole | Campfire, Survival 30 |
| Antivenom | 2 Radscorpion Gland + 1 Night Stalker Blood | 2 Antivenom | Campfire, Survival 40 |
| Cass' Moonshine | Yeast + Fission Battery + 2 Mutfruit + Maize | 2 Moonshine | Campfire, Survival 75 |
| Scrap Metal to Lead | 1 Scrap Metal | 200 Lead | Reloading bench, Repair 10 |
| 10mm Round | 1 Large Pistol Primer + 1 10mm Case + 9 Pistol Powder + 17 Lead | 1 round | Reloading bench, Repair 25 |
| Tanned Gecko Hide | Gecko Hide + Horsenettle Berry + Turpentine | Tanned hide | Campfire, Survival 25 |

### 2.2 Vanilla values (ENIT/DATA value field)
Scrap Metal 1, Lead 0, Pistol Powder 0, 10mm round 2, Dirty Water 10, Purified Water 20, Broc Flower 3, Xander Root 0, Healing Powder 5, Maize 5, Brahmin Meat 5, Brahmin Steak 5, Desert Salad 5, Ruby's Casserole 5, Moonshine 20, Antivenom 25, Stimpak 75. (ENIT first dword read as value; Moonshine and Stimpak match known values. Treat the others as readable but check in the GECK if one matters.)
Consequences:
1. Vanilla values are almost useless as wholesale prices: Lead and powder are worth 0. One Scrap Metal (value 1) becomes 200 Lead = about 11 rounds of 10mm (17 lead each), worth 22 caps at base value, so an ammo chain must be priced by OUR table, not vanilla.
2. Cooking adds no vanilla value (steak = meat = 5). Value added is in effects. Our workshops must add a price multiplier of their own.
3. Stimpak is the only high-value, low-input good (75 vs about 3). That is the natural "prestige" product, gated by Science 70 and the syringe.

### 2.3 Vendors and place facts
- **Chet (Goodsprings, `GSChet`)**: his stock list `VendorAmmoChet` is use_all: .22 LR, 9mm, .357 Magnum, 20 Ga, Small Energy Cell, 5.56mm. He also carries a Stimpak and a revolver loot list. He sells ammo, so he BUYS nothing we make except as ammo supply; our ammo chain competes with him. His buying list [?].
- **Johnson Nash (Primm, `PrimmJohnsonNash`)**: class VendorMisc; dialogue "Do you have anything for sale?" exists; Ruby Nash's dialogue takes radscorpion glands (food for her casserole). Nash's stock list [?].
- **Vikki and Vance (Primm)**: NPCs found are dealers, cashier and floor manager; I did not find a shop, so this is a casino, not a trade partner [?].
- **Mojave Outpost**: only generic "Caravaneer" traveler NPCs found by name; Lt. Haverford and the outpost trader not found by that search, so I do not know their names or stock [?].
- **Sloan**: `QJChompsLewis` exists; Jas not looked up [?].
- **Crops in the south**: Broc Flower and Xander Root have placed plants and `VCG03*` reference records; their exact locations were not checked [?]. Maize, jalapeno, pinto beans, barrel cactus: items exist [V for maize, jalapeno via casserole]; where they grow in the south was not checked [?].
- NCR imports: powder and primers are loot-only items in vanilla (no vendor list read) [?].

## 3. What this means for our mod: concrete proposals

### 3.1 (a) Goods list v1: 16 goods, 8 raw, 8 made

Unit = one "crate" (cargo unit, 10 items). Prices are OUR wholesale table, caps per crate, tuned later. All recipes are per batch.

| # | Good | Kind | Source place (v1) | Recipe | Workshop | Skill | Buyers | Base price/crate |
|---|---|---|---|---|---|---|---|---|
| 1 | Dirty Water | raw | Goodsprings spring/trough [?] | gathered | Well rig (cheap) | none | Primm (purifier), Outpost | 60 |
| 2 | Herbs (broc + xander, always paired) | raw | foraging camp, Goodsprings hills [?] | gathered | Forager hut | Survival 15 | Goodsprings clinic needs | 50 |
| 3 | Maize | raw | farm plot, Primm/Goodsprings [?] | farmed | Field | none | Primm, Sloan | 40 |
| 4 | Brahmin | raw (live) | Goodsprings/Primm pens | herded | Corral | none | Primm smokehouse | 120 per head |
| 5 | Quarry Stone | raw | Sloan quarry [NEW cargo], needs Quarry Junction cleared | mined | Quarry | none | stone yard | 50 |
| 6 | Sand | raw | desert flats near Primm/Outpost [NEW cargo] | dug | Sand pit | none | stone yard | 20 |
| 7 | Scrap Metal | raw | junk piles, Outpost scavengers | salvaged | Scrap yard | Repair 10 | smelter | 30 |
| 8 | Gunpowder | raw/import | NCR import (Outpost, legal, taxed) or Powder Ganger contraband (see 3.5) | bought | none | none | reloader | 90 legal, 55 illicit |
| 9 | Purified Water | made | Primm purifier | 5 Dirty -> 4 Purified (vanilla ratio) | Purifier | Survival 50 | Goodsprings, Primm, Sloan, Outpost | 110 |
| 10 | Healing Powder | made | Goodsprings apothecary | 1 Herbs bundle -> 1 | Apothecary | none (vanilla) | Goodsprings, Primm | 90 |
| 11 | Stimpak | made | Primm clinic bench | Healing inputs + imported Syringe | Clinic bench | Science 70 | Outpost (NCR), Sloan, rich buyers | 450 |
| 12 | Smoked Meat | made | Primm smokehouse | 1 Brahmin -> 4 crates meat (invented yield) then cook | Smokehouse | Survival 35 | Sloan, Outpost, Goodsprings | 85 |
| 13 | Building Materials | made | Sloan stone yard | 2 Stone + 1 Sand -> 2 (clay = rock + sand) [NEW] | Stone yard | none | ALL towns (build cargo for growth) | 120 |
| 14 | Lead | made | Primm reloading bench | 1 Scrap -> 200 Lead (vanilla) | Reloading bench | Repair 10 | reloader | 30 |
| 15 | Ammo | made | Primm reloading bench | 1 Lead + 1 Powder + 1 Scrap (case) -> 3 Ammo (abstracted from 17 lead + 9 powder + case + primer) | Reloading bench | Repair 25 | Outpost, Sloan, Goodsprings, Primm | 200 |
| 16 | Moonshine | made, illicit | back-room still | 2 Maize + 1 Dirty-water-purified -> 1 batch (our recipe; real Cass' Moonshine needs Yeast, Fission Battery, Mutfruit: too exotic) [NEW] | Still | Survival 40 | Primm, Sloan, Outpost | 160 legal-licence / 110 black market |

Ratio design, kept to small integers so the terminal can show them plainly:
- Water: 5 : 4. Meat: 1 : 4. Materials: 2 stone : 1 sand : 2 out (so 1 stone + 0.5 sand per crate). Ammo: 1 : 1 : 1 : 3.
- Ammo is the deepest chain (scrap -> lead, + powder, + scrap case, reloading bench): 3 raw goods, 2 workshops stages, 1 imported/illicit input. This is the "TF2 steel mill" of the mod.
- Prosperity needs only 1 new cargo (Building Materials); the other 7 made goods are real FNV items, so players recognise them.

### 3.2 (b) Workshops: cost, levels, effects

Workshops are placed buildings in a town (HQ or a rented plot). One level = more daily crate capacity, never a different recipe.

| Level | Build/upgrade cost | Daily capacity (crates in) | Output yield | Look in world |
|---|---|---|---|---|
| L1 Lean-to | 300 caps + 20 Building Materials | 4 | base | open shack, one worker NPC placed (marker) |
| L2 Shop | 900 caps + 40 Building Materials | 8 | +10% | roof, sign, second worker, small cart outside |
| L3 Works | 2,200 caps + 80 Building Materials | 16 | +20% and "quality" tier (Stimpak: no shortage penalty, ammo: +condition) | brick wall, chimney, yard stock piles, lantern at night |

How a level is earned (TF2-style [D]): a workshop levels when its throughput over the last 7 game days stays above 80% of capacity AND its supply rating is above 80%. Level up is offered as a memo ("Primm purifier is ready for L2: 900 caps"), not automatic, so spending stays a choice. A level can drop if supply fails for 14 days (soft decay, and the building becomes weathered, never destroyed).
Staff: the worker's skill sets quality. A Science 70 hire is needed for the clinic bench; a 50 Survival hire for the purifier. A player with those skills can do it themselves (company-owned bench, player-run) but that earns no passive income.
Build constraint: the stone yard requires Building Materials itself (bootstrap: first 20 from a one-time contract or Goodsprings salvage).
Engine cost: workshops are enable/disable stages of placed statics (two or three NIFs per stage); output is numbers in script. Medium effort.

### 3.3 (c) Town needs: Anno tiers, shown in the world

Each town has a **Settlement level** (0 to 3), like Anno's population tier: Camp, Hamlet, Village, Town.
- Basic needs (must be >=80% met for 7 days to advance): water, food, medicine.
- Luxury needs (do not advance the town; they raise **the town's wallet**, which sets buying prices): ammo, moonshine, stimpaks.
- Level-up cost: Building Materials (like Anno's timber/bricks): e.g. 40, 90, 160 crates, delivered by you.

Example needs, v1 (units per week at current level; scaled to the town; all numbers [NEW] to tune):
| Town | Basic | Luxury | Notes |
|---|---|---|---|
| Goodsprings (L1 Hamlet) | Purified Water 6, Smoked Meat 4, Healing Powder 3 | Ammo 2 | small; Chet sells ammo already, so the player competes with him |
| Primm (L1 -> L2 Village) | Purified Water 8, Smoked Meat 6, Healing Powder 4 | Moonshine 4, Ammo 4 | Primm with no sheriff raises Ammo demand +50% |
| Sloan (L1) | Water 6, Meat 6, Healing Powder 4, Building Materials (quarry crews) | Moonshine 3 | Quarry Junction deathclaws cut Stone supply until cleared |
| Mojave Outpost (L2 army post) | Water 8, Meat 8, Stimpak 3 | Ammo 6 | NCR demand for Stimpak and legal-source ammo only |

How supply shows in the world (growth you can see, not a menu): crossing a threshold enables a hidden stage of placed references: L1->L2 adds fenced yard, a market stall, a new sign, one more resident (a marker NPC from the lived-in-towns pool), a lamp post that lights at night; L2->L3 adds a stable, a proper store front. Under-supply flips the opposite: empty shelf props, a "closed" sign, one resident leaves. This matches the rule from BUSINESS-RESEARCH.md ("show growth in the world, not only in a menu").
Demand grows only with the town's level and supply history (TF2: supply adds growth [D]); never above what the town can afford, so over-delivering sells at a discount (Factorio-style overproduction penalty from the genre analysis).

### 3.4 (d) What unlocks at which company tier (from the brief's five tiers)

| Tier | Chains unlocked | New thing |
|---|---|---|
| Peddler | Herbs -> Healing Powder; Dirty Water -> Purified Water (Mass recipe at your own campfire; no workshop yet) | carry goods by hand/pack brahmin |
| Outfit | Smoked Meat (Primm smokehouse); L1 workshops; Maize -> Moonshine (legal home-still licence only) | first hired trader |
| Caravan company | Building Materials (stone yard, needs Quarry Junction clear); L2 workshops; Lead and Ammo (legal powder import via Outpost) | town upgrades become the main growth lever |
| Trading house | Stimpak chain (Science 70 hire + syringe import); L3 workshops; contraband powder and unlicensed spirits | heat and raids become live |
| Mojave concern | multiple chains in more towns; future: NCR supply contract (bulk ammo and stimpaks) | state contracts, rival price war |
One new chain per tier, always one new input to find (not just more money), matching the "each tier unlocks one new thing" rule in the brief.

### 3.5 (e) Two contraband chains (cross the legal line)

1. **Powder chain (ammo)**: legal path buys Gunpowder from NCR import at the Outpost at 90 caps, taxed, steady supply. Illicit path buys stolen powder from the Powder Gangers at 55 caps: cheaper and more volume, but each stolen crate adds heat to the Ammo you sell AND to the company whose reloading bench made it (the bench becomes "tainted" until a clean batch is run). Differs from moonshine: the **input** is illegal; the **end good is ordinary**, so selling it is safe, but a raid that finds the powder stock seizes the stock and a workshop.
2. **Moonshine chain**: all inputs are legal (maize, water); the **end good** needs an NCR spirits licence (a tier 3 permit, paid weekly). Without it, you sell to the black market (110 caps vs 160 legal) with higher margin per crate, but every sale raises heat in that town and NCR patrols can burn a batch in transit. Differs: nothing in the supply chain is suspicious; the exposure is in distribution.
Both feed one **heat** meter per region (lose the NCR licence at the top: second lose condition in the brief). Both let the player choose legal-slower versus illicit-faster on the same recipe, which is the "decision, not a payout screen" the research asks for.

### 3.6 (f) Terminal bottleneck display (text mockup)

Terminals cannot take typed input, so this is menu-driven and refreshed with live numbers (`ComputersMenu::DisplayTerminal` hook idea, untested). Menu: `1) Chains  2) Towns  3) Memos  4) Ledger`.

```
== CARAVAN CO. / PRIMM PLANT ==            Day 14 Wk 2     Cash 1,240
AMMO CHAIN                                   Supply  Stock  Flow/day
 Scrap Metal   [########--]  80%   <-- OK      18      +5/-4
 Lead          [#######---]  70%               54      +6/-5
 Gunpowder     [##--------]  20%   <-- BOTTLENECK  6   +1/-5   (Outpost import low)
 Reload bench  L1  [#####-----]  50% of 4 crates/day
 Ammo out      2.0/day   town wants 4/day   shortfall 2
 FIX: more powder, or contraband powder (cheaper, +heat). 
--- Water chain ---------------------------------------------
 Dirty Water   [########--] 80%   Purifier L1 [#########-] 90% -> L2 ready
-------------------------------------------------------------
1) Hire trader for Gunpowder  2) Show Outpost price  3) Back
```
Rules: the lowest bar among a chain's inputs is the bottleneck and is labelled; the line "FIX:" lists at most two actions; a workshop shows a progress bar to the next level (TF2 style [D]); one screen per chain, max 12 lines (NVSE menu notes have a fixed text area; numbers are rebuilt from script, fixed width).

## 4. Bold ideas

1. **Recipe discovery as Schedule I mixing** [NEW]: a "master" (e.g. Ruby Nash for food, the Primm doctor for medicine) teaches one named variant when you bring her an ingredient the first time: "Ruby's Casserole needs a Radscorpion Gland". Variant = same chain, +30% price, new town need. Costs one extra line in the recipe table, not a new good.
2. **Bottleneck as quest hook**: when the bottleneck is a raw good at a dangerous place (Sloan stone needs the Quarry Junction deathclaws cleared, powder needs Powder Gangers), the terminal flags a **contract** to resolve in person. Player adventure feeds the company (brief point), no forced chore.
3. **Sell the surplus to the rival** [NEW]: any town can be oversupplied; selling the excess to the Crimson Caravan at a loss keeps a chain alive but gives Alice share. Makes the rival a tool as well as an enemy.
4. **Seasonal-style demand pulses** [NEW]: a weekly "Outpost payroll day" doubles Ammo and Smoked Meat demand once; the terminal shows it a day ahead, a decision about pre-stocking.

## 5. Pitfalls and design flaws

- Vanilla item values are nearly worthless (Lead 0, powder 0, scrap 1, Xander 0 [V]); do not derive prices from them. Use our own table.
- The 200-lead-per-scrap recipe [V] would make lead effectively infinite: our abstraction caps lead per scrap per day.
- Too many goods per town overwhelms the terminal; keep each town to 5 to 7 lines.
- A chain where one input comes from an illegal place makes the legal fallback non-negotiable (do not hide the safe option); a legal option must exist for every chain.
- Tier upgrades gated only by money invite grind; the brief's "money + trust + a deed" fixes that, and Building Materials is a third lever.
- Vendor stock lists (Chet, Nash, outpost) were not fully read: do not claim exact vanilla stock in the release notes until checked.
- Real Cass' Moonshine, Stimpak and Antivenom use loot-only parts (syringe, yeast, fission battery, glands): a chain depending on them needs a purchase path, else it is a hunt chore.
- Anno-like tiers can punish time away; use soft decay and a recovery path (feeding a town back to L-1 only after 14 days).

## 6. Questions only the user can answer

1. Should Building Materials be a new cargo (our pick) or only real FNV items? New cargo makes "growth you can see" possible.
2. Is one illicit chain enough for v1 (moonshine, simpler) or both (powder as well)?
3. Do player skills matter (Science 70 to run the clinic bench yourself) or only hired staff?
4. May towns lose a level if starved, or stay put and only stop growing?

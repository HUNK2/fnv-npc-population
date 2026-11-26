# Business research: lose conditions, progression, prior mods

Gathered 2026-11-26 for the merchant company part of the mod. Three quick web sweeps (one search per game, mostly
search-result snippets, few full page reads). Nexus mod pages refused automated fetches, so mod details come from
snippets only. [D] = documented by the source, [O] = player or reviewer opinion.

## 1. How business games let you lose

| Game | How you lose | What is kept | Notes |
|---|---|---|---|
| Recettear | Miss a weekly debt installment | Restart with levels kept | Payment schedule always on screen [D] |
| OpenTTD | Cash negative for 3 quarters in a row | Nothing; company can be sold to a competitor first | Staged: warnings, then offer to sell, then gone [D] |
| Railroad Tycoon, Capitalism Lab | Hostile takeover by a rival buying your stock | - | Players call invisible takeovers frustrating [O]; Capitalism Lab pauses near a rival's bankruptcy so you can buy it [D] |
| Offworld Trading Company | Lose majority control | - | Defence: buy back your own stock [D] |
| Bannerlord | No company death; caravans captured, workshops lost when towns change hands | Everything else | Per-asset loss [D] |
| Papers, Please | Debt -> family suffers -> arrest | Reload allowed | [D] |
| Frostpunk | Warning, then about 48 hours to recover before exile | - | [D] |
| Sunless Sea -> Sunless Skies | Death felt too punishing; moved to "Legacy" inheritance | Part of the old run | Developer's own change [D] |
| GTA Online | You lose stock, never the business | The business | [D] |

Lessons: fixed, visible deadlines; staged warnings; recoverable failure (lose the company, not the save); prefer
asset loss over game over; a takeover only with visible stakes and a defence; a bailout path (sell assets, a
contract advance, a loan); do not punish time spent away on quests.

## 2. How business games make growth feel real

- **GTA Online**: office, then warehouse, then bigger payouts; a warehouse NPC sources stock [D]. Complaints:
  tedious source missions and forced pickup trips; remote collection later paywalled, which angered players [O].
- **Red Dead Online Trader**: 20 ranks; bigger wagons at ranks 5 and 10 [D]. Complaint: grind, low pay per run [O].
- **Bannerlord**: caravans start slower than workshops but earn more later; ambushes make escorts matter [O].
  Split opinion: workshops are buy-and-forget, weak after the early game [O].
- **Sim Settlements 2 (Fallout 4)**: city plans grow from a few farms to a metropolis; supply lines between
  settlements [D]. Its own add-on authors call caravan routing simplistic [O].
- **Kenshi**: manual caravan trading called tedious; players asked for automated routes [O].
- **Recettear**: merchant level rises with good sales and unlocks features [D].
- **Moonlighter**: shop upgrades bought with money only; reviewers stopped caring once upgrades were bought [O].
- **Stardew Valley**: Community Center rooms unlock in sequence; each repairs part of the town [D].
- **Two Point Hospital**: one star unlocks the next level; more stars give extras [D]; called repetitive [O].
- **Big Ambitions**: more businesses, then staff, then HQ, then warehouses; the growing numbers are the hook [O];
  managers need infrastructure; mid-to-late game repetitive, players want more automation [O].
- **Patrician, Port Royale**: automated convoys exist; setup fiddly and needs babysitting [O]; some enjoy setup [O].
- **Offworld Trading Company**: the market is the weapon; price watching drives victory [D/O].
- **Idle-game design writing**: old income sources go stale and remove decisions; rotate what matters [O];
  spoilage and risk keep idle play engaging [D]; a payout on return is a retention hook [D].

Lessons: show growth in the world, not only in a menu; gate each step on varied goals (money, trust, a deed),
each step unlocking one new thing to do; every automation step costs something and does one job; keep passive
income exposed to events; make the regular report a decision point, not a payout screen; no chores such as
pickup trips.

Sources: sportskeeda.com (GTA Online businesses, passive income), gamesradar.com (GTA Online loop, VCS review),
pushsquare.com (GTA+ collection paywall), rdr2.org (Trader guide), gamingnexus.com, pcgamer.com (Trader, Bannerlord
caravans, Moonlighter, Two Point Hospital, Offworld reviews), nerdlodge.com (Bannerlord), steamcommunity.com
(Bannerlord, Kenshi, Patrician threads), nexusmods.com/fallout4/mods/71724 (SS2 city plan), tvtropes.org (SS2),
gamedeveloper.com (Recettear analysis), game-wisdom.com (Moonlighter), stardewvalleywiki.com/Bundles,
wikipedia (Two Point Hospital, VCS), primagames.com and noobfeed.com (Big Ambitions), gamewatcher.com (Port Royale 4),
gameanalytics.com, machinations.io, destructoid.com (idle design).

## 3. Existing Bethesda business mods

No New Vegas mod lets the player run a company with staff, routes, walking caravans, a ledger, a rival and a
government. What exists falls into four kinds:

- **Join as a guard**: a caravan guard job on Mojave Outpost - Sloan - Grizzly routes, paid per stop
  (nexusmods.com/newvegas/mods/58721, remaster 83590).
- **Ride as a passenger**: pay about 70 caps to ride a caravan to a known marker (69990).
- **Rob caravans**: needs a script added by hand to each extra pack animal (69863).
- **Invest passively**: New Vegas Trade Center share system (42653); Mojave Stock Exchange (prices move with quests
  and NPC deaths).
- Also: Working Crimson Caravan Traders (Yukichigai) makes the vanilla Crimson Caravan traders tradeable; a
  Mojave survival overhaul with a caravan fast-travel network and farms (81969, new game required).

Other games: Rovan's Market Stall (Skyrim SE: up to five stalls, a hub audits accounts), A Ballad of Wealth:
Coinmaster (Skyrim: invest with a partner), Sim Settlements 2 caravans (Fallout 4), Bombay Trading Company (Fallout 3,
not read).

Forum wishlists (none released) ask for: a player caravan company, hiring guards and brahmin, supplying outlying
towns, competing with the Crimson Caravan, dealing weapons, naming your own company.

Likely failure points (inferred, not verified complaints): pure passive income, fixed scripted routes, heavy
dependence on other mods, vanilla caravan NPCs needing per-actor patches, new game required.

## 4. Transport Fever 2 production chains

From the official manual page (transportfever2.com/wiki/doku.php?id=gamemanual:industriescargos, last changed
2024-01-16): 16 cargo types (6 raw, 4 intermediate, 6 end) and 16 industries.

- Raw: coal mine, iron ore mine, oil well, forest, quarry, farm.
- Steel mill: iron ore + coal -> steel. Oil refinery: crude oil -> oil. Saw mill: logs -> planks.
- Chemical plant: oil -> plastic. Fuel refinery: oil -> fuel. Food plant: grain -> food.
  Construction materials plant: stone -> construction material. Tools factory: planks -> tools.
- Goods factory: plastic + steel -> goods. Machines factory: planks + steel -> machines.
- Towns take end goods only: commercial districts want food, goods, tools; industrial districts want construction
  material, fuel, machines.
- Factories level up when enough cargo is transported to and from them and supply keeps up; the stock list shows
  which input is the bottleneck. Unused industries are abandoned after 10 years.
- The manual does not say how deliveries grow towns (a separate towns page, not read). Community posts say town
  demand grows with town size and your supply.

## 5. FNV's own recipes (read from FalloutNV.esm with fnv_record)

- Healing Powder: Broc Flower + Xander Root (campfire, no skill).
- Stimpak: Surgical Syringe + Broc Flower + Xander Root (workbench, Science 70).
- 10mm Round: 1 large pistol primer + 1 10mm case + 9 pistol powder + 17 lead (reloading bench, Repair 25).
- Breakdown Scrap Metal to Lead: 1 scrap metal -> 200 lead (Repair 10).
- Mass Purified Water: 5 dirty water + surgical tubing + 2 glass pitchers -> 4 purified water, tools returned
  (Survival 50).
- Caravan Lunch: InstaMash + Pork n' Beans + Cram + Lunchbox (Survival 30).
- Chem recipes exist (Rocket, Slasher, Turbo, Hydra, Party Time Mentats); inputs not read.

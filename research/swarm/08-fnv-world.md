# 08 - The Mojave itself: world grounding for the caravan company

Sources: fallout.wiki pages (fallout.fandom.com refuses fetches with HTTP 402, so I used the newer fallout.wiki, which has the same content), plus read-only `fnv_record` lookups on FalloutNV.esm. Tags: [D] = documented on the wiki or in the ESM, [I] = my inference, [?] = not verified.

## 1. Key findings

### 1.1 Trade in the Mojave

**Crimson Caravan Company** (https://fallout.wiki/wiki/Crimson_Caravan , https://fallout.wiki/wiki/Crimson_Caravan_Company)
- [D] Founded in the Hub 130+ years before 2281; family-run (Demetre Romara and daughter Keri); two of the six seats on the Hub merchant council; offices in most big NCR cities. Policy: take any job for a high fee.
- [D] The New Vegas branch sits in a walled compound east of Freeside, close to the Gun Runners. Staff: Alice McLafferty (manager), Don Hostetler, Janet, Blake (store), caravaneers, traders, guards, a brahmin pen. Three buildings are enterable (Main Office, Guard Barracks, Caravaneer Barracks).
- [D] Largest NCR supplier of military-grade weapons plus provisions. It subcontracts much of its delivery work to wandering merchants. That is the opening for us: the player's company is a subcontractor-turned-rival.
- [D] State in 2281: "in recovery". Deathclaws at Quarry Junction blocked trade south of New Vegas; three subcontracted caravans were destroyed (raiders suspected, ash piles at the scene suggested energy weapons, i.e. the Van Graffs).
- [D] Hates Legion, Great Khan and BoS dress; guards go hostile; killing them costs NCR standing. The company is NCR-aligned.
- [D] Caravans carry brahmin for big hauls; in dangerous country caravans split into small bands to limit losses; guards are light-armoured with mixed melee and guns.

**Alice McLafferty** (https://fallout.wiki/wiki/Alice_McLafferty) [D]
- Executive manager of Crimson Caravan's Hub HQ who took over the New Vegas branch after Henry Jamison (a Redding rancher family's pick, interested in gambling and vice) ran it badly. Ruthless: industrial espionage, buyouts. Lobbies NCR politics for tariffs that hurt rival houses. Deal with the Van Graffs to squeeze Cassidy Caravans and the Gun Runners.
- ESM: NPC editor ID `AliceMcLafferty`; carries 100 caps, $5 NCR, a Crimson Caravan safe key, a laser pistol. Killing her fails Pressing Matters.
- Her dialogue topic quests: `VDialogueCrimsonCaravan` (000F8B6A), `vDialogueCrimsonCaravanGeneric` (0013FB81).

**Cassidy Caravans and Heartache by the Number** (https://fallout.wiki/wiki/Cassidy_Caravans , https://fallout.wiki/wiki/Heartache_by_the_Number)
- [D] Small, aggressive company founded by Cass; NCR was a core customer; undercut larger outfits. In 2281 the Van Graffs destroyed the caravan (staged to look like a Brotherhood attack, energy weapons disintegrated everything) under the deal with Alice. Cass was stuck at Mojave Outpost waiting on clearance papers from Ranger Jackson. Alice bought the remains (You Can Depend on Me).
- [D] Heartache outcomes: Peaceful = evidence from the Crimson Caravan office safe (Lockpick 50, or steal Alice's key) and the Silver Rush safe goes to Ranger Jackson, who passes it to the NCR "to decide the fate of the two companies" (the wiki does not say what; no visible change). Alice stays alive. The Van Graffs become permanently hostile (patch 1.2+). Violent = kill Alice and Gloria Van Graff; no wiki text on what happens to the Crimson Caravan afterwards. Both can be done in sequence (peaceful first, then kill). Killing Alice fails Pressing Matters. Killing Gloria or Jean-Baptiste Cutting fails Birds of a Feather.
- [I] So in vanilla, the Crimson Caravan keeps existing whether or not Alice is alive. Our mod must handle Alice dead (a "successor" manager under a different name, or her desk run by Don Hostetler) and Alice alive.

**The Van Graffs and Silver Rush** (https://fallout.wiki/wiki/Silver_Rush) [D]
- Freeside shop across from the Atomic Wrangler; biggest energy-weapons retailer; took over the building in 2071 by force. Gloria runs strategy; Jean-Baptiste Cutting is the muscle. Thugs search visitors at the door. They took over the energy-weapons trade after the Gun Runners withdrew from it following repeated caravan ambushes.

**Gun Runners** (https://fallout.wiki/wiki/Gun_Runners_(Location)) [D]
- Fortified weapons compound just south of Freeside; Isaac is informal leader; a Vendortron kiosk sells outside (stock changes Wednesdays and Sundays). Army contracts can be up to 90% of sales around New Vegas and Hoover Dam. Caravans carry weapons in cases rigged to explode if opened by the wrong hands. Accepts neither caps in some variants (that is a mod page; ignore).
- Quest hook: Dealing with Contreras - McCarran wants more guns and ammo than they can supply. This is a supply gap our company could fill.

**Far Go Traders** (https://fallout.wiki/wiki/Far_Go_Traders) [D]
- One of three Hub trade houses (with the Crimson Caravan and the Water Merchants). Hub-based (Downtown), nominally led by Butch Harris with Rutger as aide, effectively under the crime lord Decker. In 2281 competes with the Crimson Caravan for an NCR Army armour contract. Trade pitch: "chems, tires, guns, bullets, food, brahmin, dirt, even scraps of metal." They lose caravans to scavenger teams and to disappearances.
- [I] Perfect "cousin" for us: a second major house that is not present in the Mojave, so a Far Go licence/partnership is a lore-safe source of Hub goods without contradicting anything.

**Happy Trails Caravan Company** (https://fallout.wiki/wiki/Happy_Trails_Caravan_Company) [D]
- Small, Sac-Town based, serves New Reno and the Salt Lake City road; struggling; led in Honest Hearts by Jed Masterson (with Stella, Ricky). CORRECTION to the brief: **Ted Gunderson is NOT Happy Trails.** ESM shows `VMS18TedGunderson` / `VMS18HeckGunderson` belong to the Gunderson family of brahmin barons (Heck is met at the Ultra-Luxe; he is a Californian brahmin baron). Do not use Ted Gunderson as a caravan boss. The Happy Trails Honest Hearts questline is DLC and optional; reference at most as a rumour.

**Mojave Express and Johnson Nash** (https://fallout.wiki/wiki/Mojave_Express , https://fallout.wiki/wiki/Johnson_Nash) [D]
- Mojave Express is a package-delivery company with offices in the Hub and Primm; the Primm office is run by Johnson Nash (editor ID `PrimmJohnsonNash`, merchant, caps listed 111-1259, sells ammo and weapons) and wife Ruby. The Courier was hired as "Courier 6" after a robot ordered six couriers (originally seven) with a coded message. Dropboxes in Goodsprings, Novac, Freeside, Strip and the Primm office.
- Nash says he has lived in Primm about eight years and that the town has gone to hell; the townsfolk fled to Vikki and Vance after the Powder Gangers took over. Mojave Express is not dead: the Hub office still hires couriers. Nothing on the wiki says the Primm office has gone out of business, but Nash plainly treats it as a sideline to his trading.
- Quest/dialogue records: `PrimmNashDialogue` (000A23D8), `nVPrimmDeputyConv` My Kind of Town (000DA115), `nVPrimmVanceGun` Vance's Gun (000E2891).
- [I] A Mojave Express revival is lore-safe: the company exists, the player has literally worked for it, and Nash is a trader first. It cannot be "the player's courier job continues" (the Courier's job is deliberately vague per Sawyer, per the Mojave Express page), but a Mojave Express franchise is plausible.

### 1.2 Money

- [D] Caps are backed by water by Hub merchants (Joshua Sawyer statement quoted on https://fallout.wiki/wiki/Caps). Crimson Caravan controls cap production: it wants to control the presses to prevent mass production and inflation, and it can replace worn caps. Pressing Matters (`VMS51`, 0014EF5F): disable the counterfeit press at the Sunset Sarsaparilla HQ. Alice states counterfeits exist but are small-scale because they are slow to make; she fears "devaluing our currency by mass producing new bottle caps." Reward 500 caps.
- [D] Caravan companies and the Strip accept caps, NCR dollars and Legion denarius as legal tender (Caps page). Rates: NCR dollar = half a cap (https://fallout.wiki/wiki/NCR_dollar); denarius = 4 caps, aureus = 100 caps (wiki, via search; Legion coin value is not affected by the Barter skill). NCR notes: $5, $20, $100, issued by the Republic Reserve Bank in Angel's Boneyard.
- [D] Sloan quarry workers are paid in NCR dollars, not caps. NCR pay in dollars; caps are what the caravans and Mojave traders want. Hence a natural exchange business.
- [D] NCR gets "not one cap in tax revenue" from the Strip's resorts although it holds Hoover Dam (NCR page). Settlers in NCR territory register as citizens and pay taxes; market tariffs for territories are set by the Senate (Happy Trails example). Landowners and brahmin barons bribe their way to influence over the NCR economy.
- [D] Legion: bans drugs and alcohol trade; patrols in the Mojave are openly hostile to prospectors and traveling merchants; merchants like Dale Barton prefer Legion land because there is no protection to hire and no taxes. Cass says caravan life would be easier if the Legion held the roads. Legion coins carry "Aeternit Imperi"/"Pax Per Bellum" (aureus) and "Magnum Chasma" (denarius).
- [?] The brief mentions NCR "taxes on caravans" and a "Brahmin baron" rival. I found no dedicated NCR caravan-tax rule in the wiki; tariffs and citizen taxes exist, so a tax notice is plausible [I]. Brahmin barons are real in NV lore but they are California landowners; one (Heck Gunderson) is in the Ultra-Luxe.

### 1.3 The southern towns and the state variables that matter

Quest and variable names below come from `fnv_record`. I read the stage scripts; these are what is safe to condition on.

**Goodsprings** (https://fallout.wiki/wiki/Goodsprings) [D]
- About 13 residents: Trudy (bar, leader), Doc Mitchell, Chet (general store), Victor (Securitron), Sunny Smiles, Easy Pete, plus four generic settlers (`GoodspringsSettler01Ref`..`04Ref`) and Ringo, a Crimson Caravan trader hiding at the gas station. Economy: bighorner farming, meat and hides bought by traders; I-15 trade has shrunk. Buildings: Doc's house, general store, gas station, schoolhouse, Prospector Saloon, Victor's shack, settler homes. Spring (Goodsprings Source) is the town's name and water.
- ESM: Chet `GSChet` (00104C78) carries `CapsChange100` x10, a revolver loot list, a Stimpak; AI package `GSChetStoreSandbox`. Trudy `TrudyRef`, Doc `DocMitchellREF`, Sunny `SunnyRef`, Easy Pete `EasyPeteRef`, Ringo `RingoRef`.
- **Ghost Town Gunfight** = `VMS16` (00104EAE). Stages: 5 start, 10 talk to Sunny, 50 return to Ringo, 60 get the helpers, 65 ready, 70 the fight (Goodsprings and Ringo's allies vs Powder Gangers; Victor set unconscious), **100 = completed** (all Powder Gangers dead; script sets `VMS16.QuestComplete`=1, +Goodsprings reputation, -Powder Ganger reputation; Victor wakes; Ringo gets an after-quest package), 110 = failed. Reward paid 250 caps (100 town, 150 Crimson Caravan) per wiki.
- **Run Goodsprings Run** = `VMS16b` (0015EC5B), the Powder Ganger path (the Courier kills Ringo, Joe Cobb attacks). Stage 70 sets `bPowderGangAttacking`, makes Trudy, Doc, Sunny and Pete flee/die, **stage 100 = completed** (town taken; sets cell ownership of the Saloon and houses to the player, +Powder Ganger rep, +5 negative Goodsprings rep), 110 = failed. The two quests are mutually exclusive.
- What this means for "safe / dead / has a sheriff": safe = `VMS16` stage 100 reached; dead or taken = `VMS16b` stage 100; neither = the vanilla default of an open threat (Joe Cobb's Powder Gangers hunting Ringo).
- Goodsprings has no mayor or sheriff; Trudy leads informally. Our HQ town must tolerate all three states.

**Primm** (https://fallout.wiki/wiki/Primm) [D]
- Listed population 40 on the wiki; most is rubble. Vikki and Vance Casino (cashier, dealer, floor manager; Johnson and Ruby Nash own it after the town recovers), Bison Steve Hotel (Powder Gangers, Beagle held captive, Lucky .357 in a safe), Primm Slim (robot), the Mojave Express office, McBain's old sheriff's office. NCR squad under Lt. Hayes at the overpass; NCR camp southwest to keep convicts from Mojave Outpost.
- **My Kind of Town** = `nVPrimmDeputyConv` (000DA115). Stages and variables:
  - 20 spoke to Nash about finding Beagle; 25 rescued Beagle; 26 agreed to find new sheriff (shows NCRCF and Outpost on map); 30/35 find a candidate/petition; 45 sheriff arrived.
  - **110 = NCR sheriff**: `PrimmState`=1, `NCRSheriffState`=1, `iTownState`=1, `VStoryEventPrimmSheriff`=1, `VStoryEventPrimm`=1, +300 XP (Sgt. McGee).
  - **120 = Meyers sheriff**: `PrimmState`=2, `MeyerSheriffState`=1, `VStoryEventPrimmSheriff`=2.
  - **130 = Primm Slim sheriff**: `PrimmState`=4, `PrimmSlimSheriffState`=1, `VStoryEventPrimmSheriff`=3.
  - 100 = all sheriff candidates are dead (failed).
- Globals: `VStoryEventPrimm` (0013D255), `VStoryEventPrimmSheriff` (0015A0D6) - handy single-value flags for "Primm is secure" and "who is the sheriff".
- Town after a sheriff: townsfolk return home (Nash couple move back into the Mojave Express building), gambling resumes after NCR deserters led by Layla are dealt with. No sheriff = townsfolk stay in the casino and trade is dead.

**Sloan and Quarry Junction** (https://fallout.wiki/wiki/Sloan , https://fallout.wiki/wiki/Quarry_Junction) [D]
- East of Goodsprings; NCR limestone camp for cement shipped by rail to Boulder City and the Colorado fortifications. Residents: Chomps Lewis (foreman, `QJChompsLewis` 000E5958), Jas Wilkins (merchant), quarry workers, Snuffles the mole rat, plus Melissa and Tyrone (chemical subplot). Mess hall, machine shop, mining office, barracks.
- Powder Gangers stole the camp's dynamite; deathclaws moved into the quarry; workers on forced leave, generator failing. Paid in NCR dollars.
- **Quest state** is held in the quest script, not stages: quest `vFreeformSloan` (001406A5), script variables `bDeathclawAlphaDead`, `bDeathclawMotherDead`, **`bDeathclawLeadersDead`** (= both dead; Claws Out is done when Chomps is told), `QJGeneratorRepaired`, `SnufflesHealed`. Level 15 required for Claws Out. After the quest the workers appear in Boulder City's Big Horn Saloon (they relocate in-world) - the wiki does not say Sloan visibly reopens, so a mod can legitimately own that visible change.
- [I] This fits the brief's "stone yard" chain perfectly: the quarry is dead until our company (or the player) clears it, and the mod can set a flag "quarry reopened".

**Mojave Outpost** (https://fallout.wiki/wiki/Mojave_Outpost) [D]
- NCR gateway on I-15 near the state line: HQ and Barracks, Ranger Jackson, Major Knight, Ranger Ghost (sniper), Sgt. Kilborn, a bar run by Lacey (also hosts Caravan games), a Traveling Merchant who walks between the outpost and the 164 junction. Its mission is to escort and protect caravans on I-15 south of Primm and Highway 95. Since the prison break, a permanent post at Primm leaves too few troops to patrol, so caravans are backed up and traders are reluctant to spend. Clearance papers are the choke point.
- Quests there: Can You Find it in Your Heart?, Cold, Cold Heart, Heartache by the Number, Keep Your Eyes on the Prize, My Kind of Town, You Can Depend on Me. This is the NCR tax/licence desk of our mod [I].

**Nipton** (https://fallout.wiki/wiki/Nipton) [D]
- A trading town under Mayor Steyn who sold out both the NCR and Powder Gangers to the Legion for 8,000 caps; destroyed by Vulpes Inculta (a "lottery"). Ruins and a few survivors afterwards. Booted and Cold, Cold Heart start here. Not a viable trade partner in vanilla; useful as a "closed road" and a cautionary tale in memos.

**NCR Correctional Facility and Powder Gangers** (https://fallout.wiki/wiki/NCR_Correctional_Facility) [D]
- Former women's prison; inmates under Samuel Cooke rioted; they hold the dynamite from Sloan and blast powder (Cooke's stockpile). Eddie leads the remainder; Carter runs a shop in Cell Block B; Meyers (ex-sheriff, not a Powder Ganger) sits in the Visitors Center. Quests: I Fought the Law `VMS02` (0008D0E3), Eddie's Emissary, My Kind of Town. Back in Your Own Backyard = `VNelson` (00129445) is a Legion/NCR-fight quest at Nelson; not about the south. "Booted" and "Pheeble Will" were not verified; I could not find a "Pheeble Will" quest in this version. [?]
- Source of "powder" in the brief's ammo chain: Powder Gangers (contraband) vs NCR imports - consistent.

**Novac** (https://fallout.wiki/wiki/Novac) [D]
- Population about 18; Jeannie May Crawford (motel), Dr. Ada Straus, Craig Boone and Manny Vargas (NCR veterans), Cliff Briscoe (weapons). Lives on salvage from the REPCONN site, now blocked by ghouls. Highway 95 traffic has grown since I-15 became risky. Reasonable "later" town.

**Jean Sky Diving** (https://fallout.wiki/wiki/Jean_Sky_Diving) [D]
- Powder Ganger ruin with explosive crates; part of I Fought the Law. No wiki mention of a "Yangtze memorial" on this page; that site (Yangtze Memorial) is a known ruin north-west but not verified here. [?]

### 1.4 Vendors in the south (what sells what)

| Town | Vendor | Sells | Caps (if known) |
|---|---|---|---|
| Goodsprings | Chet (General Store) | general goods, ammo, small guns; Barter 25 to open stock in Ghost Town Gunfight | `CapsChange100` x10 in inventory per ESM [D] |
| Goodsprings | Trudy (Saloon) | drinks, food, radios; safe with a skill book | [?] |
| Primm | Johnson Nash | ammo, weapons | 111-1259 [D] |
| Primm | Vikki and Vance cashier | chips, currency exchange, magazines | [?] |
| Primm | Bison Steve shop | general | [?] |
| Sloan | Jas Wilkins | food; can cook deathclaw omelet (variable `JasMadeOmelet`) | [?] |
| Mojave Outpost | Lacey; Traveling Merchant | bar goods; traveller stock | [?] |
| NCRCF | Carter | prison shop | [?] |
| Novac | Cliff Briscoe | weapons | [?] |

Caps for most vendors need an NPC/container record read (not done).

## 2. What this means for our mod

### 2.1 Founding story: three lore-safe hooks (pick one, or let the player choose)

1. **The Alice loan (Claude's pick, keeps teeth).** Alice's office offers a "preferred subcontractor" loan: she wants a reliable southern carrier because Quarry Junction killed her routes. She funds you, takes a share of profit, and holds a lien on your first warehouse. This directly extends You Can Depend on Me (`VMS05`). She will happily crush you if you outgrow her. Lore support: she subcontracts, buys rivals, lobbies for tariffs, and has already destroyed Cassidy Caravans.
2. **Mojave Express franchise (ownership story).** Nash runs the Primm office as a sideline, with a dropbox and a courier job record. He has a building (the Mojave Express building in Primm) and an NCR/Hub contract that he cannot service because the town is gutted. The player, a real Mojave Express courier, buys or licenses the right to run packages as "Mojave Express (Southern Division)". Pros: strongest fit with who the player is. Cons: Nash's business is not described as dead, so frame it as a franchise, not as inheritance.
3. **Cassidy's ghost.** If the player completed Heartache peacefully, or if Cass sold to Alice but is alive and companion-less, offer "Cassidy Caravans" as a brand name to revive with Cass's blessing (she would need to be in the mood: Hand of Vengeance/Calm Heart perk is already set). Strong emotional hook, but do not require Cass as an NPC (companion state is complicated); use only her name and an optional letter if she is alive and not in the party.

### 2.2 Conditioning on vanilla state (concrete)

| Condition | Meaning | How to read it |
|---|---|---|
| Goodsprings safe | Ghost Town Gunfight done | quest `VMS16` stage 100 reached (`GetStageDone VMS16 100`) |
| Goodsprings lost | Powder Ganger takeover | `GetStageDone VMS16b 100` |
| Primm has a sheriff | My Kind of Town done | `VStoryEventPrimm` == 1; who: `VStoryEventPrimmSheriff` 1=NCR, 2=Meyers, 3=Primm Slim |
| Primm no sheriff | casino shut, town dead | `VStoryEventPrimm` == 0 and `nVPrimmDeputyConv` stage < 110 |
| Quarry cleared | Sloan can reopen | `vFreeformSloan.bDeathclawLeadersDead` == 1 |
| Alice alive | competitor intact | check `AliceMcLafferty` is not dead (GetDead) |
| Cass sold to Alice | Cassidy Caravans bought | `VMS05` stage progress (objectives 5-7 at `VCassCompanion` stages 5-9 are the You Can Depend on Me tail) |
| Heartache done | outcomes | `VCassCompanion` stage 100 = completed, 110 = failed |

- [I] A single "world state" byte per town derived from these, read once per game day, is enough for the whole company economy.

### 2.3 What residents a lived-in town adds

Per town, given what is there (all [I]):
- Goodsprings: water haulers, a bighorner herder, a second shopkeeper, a night watch, children, kids at the schoolhouse, Crimson Caravan drovers waiting for a convoy. It lacks traffic and people.
- Primm: a sheriff's deputy, a casino pit boss, a smokehouse butcher, ex-Powder Gangers given amnesty, NCR quartermaster staff, laundry/restaurant staff; reopened by sheriff state.
- Sloan: quarry crew, a cook (Jas), engineer for the generator, a timekeeper; many of these are currently in Boulder City.
- Mojave Outpost: clerks for clearance papers, a customs sergeant, Ranger escorts, a farrier.

### 2.4 Named NPCs as roles

| NPC | Where | Possible role |
|---|---|---|
| Ringo | Goodsprings gas station | first hire / first caravan boss (Crimson trader; lost his caravan; set to lead the company's New Canaan run) |
| Trudy | Goodsprings | town broker, first customer, rumour source |
| Chet | Goodsprings | supplier, rival (raises prices) |
| Sunny Smiles | Goodsprings | guard captain candidate (hunter, Ghost Town Gunfight ally) |
| Easy Pete | Goodsprings | explosives hire (dynamite, quarry blasting) |
| Chomps Lewis | Sloan | quarry customer, contract giver |
| Jas Wilkins | Sloan | cook, canteen vendor |
| Johnson Nash | Primm | partner or rival; Mojave Express liaison |
| Lacey | Mojave Outpost | bar/rumour source |
| Ranger Jackson | Mojave Outpost | NCR liaison; tip-off or ally; he holds Cass's clearance |
| Cass | Mojave Outpost (before companion) | optional founder voice |
| Alice McLafferty | Crimson Caravan compound | lender and rival |
| Henry Jamison | Atomic Wrangler | ex-branch manager; could be a rival's disgraced hire |
| Gloria Van Graff | Silver Rush | dirty-money rival |
| Meyers / McGee / Primm Slim | Primm | sheriff for the town's policy |
| Eddie | NCRCF | Powder Ganger contraband seller |

## 3. Bold ideas (grounded in the lore)

1. **"Clearance papers" are the real gate.** The Outpost jams caravans because NCR has too few soldiers. The company starts with no papers; getting an Outpost licence is tier 1, an escort contract tier 2 (Ranger escorts are exactly what the Outpost promises), a "preferred carrier" mark tier 3. This uses the exact bottleneck vanilla describes and gives the NCR heat mechanic a home. Terminal: a clearance queue with 3-day wait that you can bribe down (dodgy path). Cost: one number per route.
2. **Exchange desk as a profit line.** Pay caravans in dollars, Legion coin, caps: the three currencies and their rates are fixed by lore (dollar = 1/2 cap, denarius = 4, aureus = 100). The company can run an exchange spread at Primm or Mojave Outpost: buy dollars from Sloan workers (paid in NCR dollars) at 0.45 caps, sell to the NCR sutler at 0.5. Tiny but flavourful profit; also a laundering risk (Pressing Matters shows counterfeiting is the thing Alice fears). Do NOT print caps in-mod (lore: Crimson Caravan controls the presses).
3. **A "quarry reopened" visible change.** Sloan only reopens if the deathclaws die; the mod can then put the workers back on the road and have your trucks haul limestone. That makes the player's adventure visible in the business and the town (the brief's building-materials chain).
4. **Alice dead?** Make the loan terms a branch: if Alice is dead after Heartache's violent path, a Crimson Caravan "regional office" writes the same loan (the company outlives her). This keeps our failure ladder valid either way.
5. **Cassidy's Ghost event.** After the company hits a tier, a one-time memo: "A woman who says her name is Rose of Sharon has been asking about your wagons." Only if Cass is alive and not in the party. Sentimental payoff.
6. **The Van Graffs as the dodgy path's counterpart.** The Van Graffs ambush caravans (Gun Runners withdrew from energy weapons for that reason). A raid on your convoys by "energy-weapon disintegrations" is canonical; the NCR can raid your office for suspected Van Graff contraband. Do not blame the Brotherhood unless the story calls for it (Alice staged that).

## 4. Pitfalls and lore constraints (things we must not contradict)

- Crimson Caravan is NCR-aligned and hostile to Legion/Khan/BoS dress; our company must not be Legion-friendly on the main path. A Legion deal needs an explicit "dodgy" label.
- Caps are water-backed and Crimson Caravan controls the presses: no player-printed caps, no mass cap rewards beyond lore.
- NCR dollar = half a cap; denarius 4; aureus 100. Do not invent other rates.
- Alice may be dead; Gloria may be dead; Cass may or may not be a companion. Never assume any of them is alive without a check.
- Ted Gunderson is not a caravan boss (see 1.1). Happy Trails is a Sac-Town company led by Jed Masterson, mentioned in vanilla, seen in Honest Hearts.
- Sloan workers are paid in NCR dollars and, once the quarry is cleared, the vanilla game moves them to Boulder City; do not invent a Sloan cap economy.
- Primm's Johnson Nash is a Mojave Express branch manager and a trader; Courier 6 was a "one-off job" in lore. Do not rewrite the Courier's origin (Sawyer's explicit intent).
- Goodsprings quests are mutually exclusive: if the player ran Run Goodsprings Run, the town is Powder Ganger-held and its residents may be dead. HQ must have a fallback location.
- Nipton is gone; do not place a living Nipton trade post. Novac and Mojave Outpost can host a later route.
- The NCR collects no cap tax from the Strip: a tax notice in our terminals should target Mojave companies/residents (citizen registration), not the Strip.
- Quest scripts are shared: do not call `SetStage` on vanilla quests. Read only.
- Wiki claims that I could not verify: Nash vendor caps beyond 111-1259; Chet's merchant chest value; the NCR "fate of the two companies" outcome after Heartache; "Pheeble Will"; "Yangtze memorial".

## 5. Writing voice, with six sample terminal pieces

How the game writes business [D, from the wiki text of Alice, Ringo, Cass, Crimson Caravan guards, Gun Runner Isaac]: flat, practical, slightly bored; money is stated as a number; threats come with a price tag; understatement for disasters ("the numbers are small"); contracts are casual about death. Frontier economics: caps = trust; "everything has a price, the surprise is who sets it"; no heroics in the memo; the humour is dry and slightly cruel. Memos use second person; managers sign off with a name and a surname that sounds like a tool or an animal.

**1. Morning report line**
> DAY 14. Water: 38 gal, spring is holding. Wagon 2 is at Primm and the Vance table still owes you 120 caps. Yesterday, a cow ate your first-aid kit. No customers complained. You are down 42 caps on the week and up one wagon.

**2. NCR tax notice (Mojave Outpost)**
> NCR MOJAVE OUTPOST - CLEARANCE OFFICE
> Notice of Assessment: Southern Haulage
> The Republic notes your caravan activity on I-15 between Goodsprings and this Outpost. Under the Citizen Registration Act, companies of more than three wagons owe the Republic 7% of declared freight, payable in caps or NCR dollars. Dollars preferred.
> Payment may be deferred once. Sergeant Kilborn reminds you that deferral is not forgiveness.
> -- Clearance Clerk, for Ranger Jackson

**3. An offer from Alice**
> To: [Proprietor]
> I have read your last quarter and I like it. I would not say that to a rival. Which means you are not yet one.
> Quarry Junction has cost me three caravans and a good deal of patience. I need a carrier who can reach Sloan and Primm without losing the shipment, and I will pay for that, in advance, at a rate I can still explain to my family. You will carry my freight at a discount and my name on your wagons.
> Come by the compound before noon. Bring a pen. I do not use verbal agreements.
> -- A. McLafferty, Crimson Caravan Company

**4. A manager's note**
> From: Ringo, Wagon Boss
> Chief. Wagon 2 is fine. The driver is fine. The brahmin are fine. The 40 crates of Sloan stone are mostly fine. Two crates are now a different shape. Nobody is angry but the stone.
> I need three more guards or a bigger wagon. Both would be better. Ask me again on Monday and I will say the same thing.

**5. A raid warning**
> OVERHEARD AT THE PRIMM CHECKPOINT
> An NCR clerk asked a trader what was in "that unmarked wagon." The trader said "stone." The clerk said "stone doesn't hum."
> Someone in Mojave Outpost is counting your wagons. Whoever it is does not work for Alice. We have heard her people fine rates, not raids. This is the other kind of people. Move the cargo or the licence, preferably both.

**6. A rumour**
> A drifter at Goodsprings says the Powder Gangers have a new buyer for powder. Not the NCR, not the Crimson Caravan. Someone with clean boots and a lot of energy-weapon cases. Trudy would not say who, only that the buyer pays in aurei, not caps. Make of that what you will.

## 6. Questions only the user can answer

1. Founding story: Alice loan, Mojave Express franchise, or let the player pick one of both on the first terminal?
2. Do we treat Alice dead as "company continues under a regional office" or drop the loan option entirely?
3. Do you want Cass in the story at all (a letter, a name on a wagon), or keep her out because of companion state?
4. Is a Legion-friendly dodgy path in scope, or NCR-only for the first version (Legion currency still accepted by lore)?
5. Should the mod move vanilla NPCs (Ringo, Chet) into company roles, or only use new tagged NPCs and treat vanilla people as customers? (The brief says vanilla named NPCs are untouched; Ringo as the first hire would contradict that unless he is just a contact.)

# Mojave Caravan Company: full business design

Nov 26, 2026 · @AfricanWarlord

## Read me first

**What this is.** The full design for the Mojave Caravan Company: an FNV mod in which the Courier borrows 3,000 caps from Alice McLafferty's agent, founds a trading company in Goodsprings, and runs it entirely from terminals while playing Fallout. Nine Sonnet agents researched it overnight (their reports are in `research\swarm`), I wrote it up here, and an Opus critic briefed as an expert game designer reviewed it in rounds.

**The critic's verdict: approved** in round 3 of 3, with no blocking issues left. Round 1 found 3 and round 2 found 2; every fix is listed in the Critic log.

### The design on one page

- **The loop.** A 5-minute visit: front page (Cash, Bills, Runway, Heat), the post, at most 3 memos that all have safe defaults, the bookkeeper's plan in one press, then back to adventuring. The company works while you are away and writes to you.
- **Money.** Each town's stock sets its prices (half to one and a half times the anchor). New routes pay; tired routes do not; contracts pay the wages. Two cash pots: only money the company earned pays bills or counts toward a tier.
- **Goods.** 17 goods in five chains (water, medicine, food, building, ammo) plus moonshine. Tier 1 trades the towns' own small surpluses; your workshops take over from tier 2 and level up with throughput.
- **Growth.** Five tiers, Peddler to Mojave concern. Each brings a new kind of decision, is gated on earned worth, trust and a deed from a vanilla quest (with a slower way round), and gives a perk that changes how you play Fallout.
- **People.** Named hires with Skill, Nerve, Honesty, Loyalty and traits; managers take over whole areas.
- **The road.** Danger with a cause you can go and remove, trouble forecast a day ahead, and real fights when you are near.
- **The rival.** The Crimson Caravan with an aggression ladder, a named captain and a memory, ending in a merger or a three-block takeover.
- **The law.** The NCR licenses, taxes, bids and inspects. The dodgy side is a slope with heat, warrants and raids.
- **Losing.** Strikes, not the size of the debt; at least 7 days of warnings; DLC time is protected; a lost company becomes a successor chapter.
- **The late game.** Forward contracts, patrons with strings, lending to small outfits as Alice did, laws, and a "20 years on" epilogue.
- **Building it.** Five milestones. M0 proves the engine risks in the real game first; M1 is one playable road.

### New since the visualiser

The starter trade, the two cash pots and strikes, the busy shield for DLC time, the bookkeeper's plan, tier perks, lending as Alice, relay desks for the north, and patrons who give abilities. The visualiser (https://claude.ai/artifact/XiPe2UdjwvPXT23HSCEvPd) predates all of these; this doc wins where they differ.

### Your decisions

You answered all 15 on 26 November 2026 (listed under Risks and open questions). Every pick stands except riding the wagon (15), which you turned down, so it is out of the design. The five that change the most are now settled: a successor chapter after losing, with gone for good as the Ironman setting (1); a lived-in towns core with the company as an add-on (3); JohnnyGuitar NVSE as a hard requirement (5); only powder and moonshine as contraband at launch (8); and owner money in its own pot (13).

**How to read it:** this page, then The loops, Money, Growth and Losing for the core. The rest is reference for building.

## The fantasy and the pillars

You are the Courier who borrowed money from the wrong woman and turned one cart into the company that feeds the south of the Mojave.

The player starts with a cart, a pack brahmin and a loan from Alice McLafferty of the Crimson Caravan. Alice funds small outfits because most of them fail, and when they fail she takes their routes. That is what happened to Cass's family company. Thirty game days later your wagons run Goodsprings to Primm, your stone is in Sloan's new houses, and Alice is no longer smiling.

**Five pillars** (every system below serves at least one):

1. **A career, not a spreadsheet.** Each tier changes what you *do*, not only how big the numbers are: peddler (you trade), boss (you hire), industrialist (you build chains and grow towns), magnate (you set policy and fight the rival), power broker (you shape the rules and the Mojave's future).
2. **A company with a memory, run by post.** You read your company's mail. Letters reach you while you quest, each with one bet in it. Crews have names, a bookkeeper writes each week's page in a Mojave voice, and Alice remembers what you did to her.
3. **Growth you can see.** Every step shows in the world: a sign, a wagon, a chimney that smokes, a town that gets a new house built from your stone.
4. **The road is real.** Danger has a colour you can read and a cause you can go and fix with a gun. Your adventures move prices.
5. **Fair failure.** Every deadline is on the front page. Warnings come before penalties, there is always a way back, and you lose the company, never the save.

**The new gameplay** (what no tycoon game we found combines): letters with standing orders instead of a dashboard; named crews who can die and be sung about; forward contracts you must fill by a date; a rival with a face and a memory; quests that act like the GTA V stock missions (buy, act, sell); and a lost company that becomes a successor chapter instead of a game over.

## Goals, non-goals and constraints

The company must make the player feel it growing, must be able to fail, and must stay fun when the player spends most of the game questing elsewhere.

**Goals**

- A real lose condition that is fair: visible deadlines, staged warnings, a way back.
- Growth the player can see in the world, not only in a menu: wagons, signs, staff, buildings, busier towns.
- Decisions worth making every game day, without babysitting.
- Production chains that make routes and staff skills matter.
- A rival and a government that push back, so profit never becomes automatic.

**Non-goals for the first version**

- The whole Mojave. The first version covers Goodsprings, Primm, Sloan and Mojave Outpost.
- Item-by-item barter. Money is ledger maths once a game day.
- Changing vanilla quests or named NPCs.

**Anti-goals** (it fails even if it works)

- A spreadsheet with a Fallout skin.
- Chores: forced pickup trips, daily clicking to keep income alive.
- Punishing the player for being away on the main quest.
- A pile of caps with nothing left to spend it on.
- A dodgy path that is simply better than the legal one.

**Hard constraints**

| Constraint | What it means for the design |
| --- | --- |
| Fallout: New Vegas 1.4.0.525, xNVSE + JohnnyGuitar NVSE | Script-driven; no other big mods required |
| Run entirely from a terminal (user's decision) | Menu choices only, no typed input; numbers shown in body text |
| Public release on Nexus | Works on existing saves and common load orders |
| Vanilla quests intact | Heartache by the Number and the Crimson Caravan quests still work |
| AI is only simulated near the player (about 20 complex actors) | The company is mostly numbers; caravans walk for real only when the player is close |
| Placed NPCs, no runtime spawner (user's decision for towns) | New staff and residents are placed in the plugin and enabled when hired |

## The loops at every time scale

The company runs on five clocks. Each clock asks for one kind of decision, and none of them needs the player to stand at a terminal for long. The rule behind all of them: **the company works while you adventure, and tells you about it by post.**

| Clock | Length | What happens | What you decide |
| --- | --- | --- | --- |
| A visit | about 5 real minutes at a terminal | read the front page and the post, answer memos, queue orders | where tomorrow's wagons go; yes or no on each memo |
| A day | ticks at 06:00 game time | prices move, wagons arrive, workshops make goods, wages are paid, the morning report is written | nothing is forced: every memo has a default |
| A week | bills on day 7 | loan payment, wage bill, duty; the weekly statement; NCR bids open; staff review | pay down the loan or keep cash; bid or not; raise a wage or let someone go |
| A season | 28 days | licence renewal, an NCR decree, one calendar event each week | which chain to grow, which town to back, clean or dodgy for the next month |
| The run | about 10 to 15 weeks of play | tiers, deeds, the rival's arc, the endgame | what kind of company you become |

### A visit

One visit, in order:

1. **Front page:** Cash, Bills, Runway, Heat, and one line about the rival.
2. **Post:** the morning report and any letters.
3. **Memos:** at most 3.
4. **Orders:** routes for tomorrow, buy and sell orders, workshop settings, standing orders.
5. Leave.

Orders do not act at once. They queue and apply at the next tick, so the terminal never needs a real-time simulation and the player cannot move a price by pressing a button ten times (see the no-flip rule under Money).

**The bookkeeper's plan.** Every morning the bookkeeper drafts tomorrow's orders from the Tape: which wagon goes where, with what. One press accepts it, and the player changes only what they want to. Before managers arrive at tier 3, this is what keeps a visit short.

A visit should fit in 5 real minutes at tier 1 and stay under 10 at tier 5, because managers (see People) take over the routine as the company grows. If a visit at tier 4 takes longer than one at tier 2, that is a design bug.

### A day: the morning report

At 06:00 the day ticks. If the player slept or travelled past several mornings, the missed days run one after another (see How it is built in FNV). The bookkeeper then writes the morning report: a short letter, then a table.

> Boss. Wagon 2 reached Primm before noon with eight crates of purified water. Sold six at 236 a crate, better than I hoped, and held two back because the price was sliding. Ruth's crew says there are fresh tracks on the road past the Powder Ganger camp. Could be nothing. The Caravan put a second wagon on Primm this week. Cash is 1,912, the loan payment is in four days, and we can cover it.

Under the letter: yesterday's money in one line (sales, costs, net), the cash and runway, and **tomorrow's forecast**, one line naming the likeliest trouble ("Bandit sign on the Primm road: medium"). The forecast is how the event director (see The road) keeps surprises fair: a big loss is always forecast at least one day ahead.

### Memos

At most 3 memos a day. Each has a question, two or three answers, a **default** that happens if the player ignores it, and a **deadline** (the next tick, at most 3 days).

> **Memo: Primm wants a water supply contract.** The general store will take 4 crates every 3 days at 210 for the next 28 days. Accept / Counter at 225 (they may walk) / Decline. *Default if unanswered by tomorrow: Decline.*

Defaults are always the cautious answer, never the ruinous one. Ignoring the post costs the player chances, not the company. The one thing a default can never settle is a lender's served notice (see Losing and coming back).

### A week

On day 7:

- **Bills:** the loan instalment (at least 300 principal plus 4% interest on the balance), the wage bill (wages are quoted per day and paid weekly), brahmin feed, duty.
- **The weekly statement:** the week's profit and loss, the best and worst route, a 4-week sparkline of earned worth, and one paragraph of the bookkeeper's opinion.
- **NCR bids** open for 2 days (see The NCR, the law and the dodgy side).
- **Staff review:** anyone with low Loyalty says so (see People).

### A season of 28 days

One calendar event each week gives the month a shape the player can plan around:

| Week | Event | Effect |
| --- | --- | --- |
| 1 | NCR payday at the Mojave Outpost | Outpost demand for moonshine, smoked meat and stimpaks ×1.3 for 3 days |
| 2 | Dust week | travel times +50%; bandit chance −30% (they shelter too) |
| 3 | Goodsprings harvest | herbs and maize supply ×1.5, so their prices fall |
| 4 | Licence renewal and the NCR decree | pay the licence; the next decree (a new duty, a ban, a subsidy) is posted for the next 28 days |

### Away from the desk

The player will spend most of the game away from the HQ. Four rules make that work:

- **Standing orders.** Simple rules the company follows without the player: "keep Primm stocked with 8 crates of water", "sell ammo above 220", "never pay more than 70 for herbs". 3 slots at tier 1, 3 more each tier.
- **Letters.** At most 1 letter a day reaches the player in the field, as a message box with answer buttons ("a runner found you"), and only when a decision is needed, never during combat, dialogue or a menu. The postbag holds 5 unread items; past that, the oldest routine items take their defaults and are filed.
- **The while-you-were-away letter.** After 3 or more days away, one letter sums up: what happened, the money, at most 3 decisions the absence caused, and one hook (a rumour, a buyer, a threat).
- **Away mode.** The player can tell the bookkeeper "I'll be gone a week". It takes effect only once 2 game days have passed since they last left an office, costs profit ×0.85, blocks new contracts, and ends when they open a company terminal. While it runs, managers use cautious presets and the event director halves its threat budget (see The road).

And the **served-notice rule** from Losing and coming back holds everywhere: nothing can be seized from the player until a notice has reached them and its grace days have passed.

## The map: towns, roads and sites

Four towns at launch, all in the south-west corner that the early main quest runs through, so a new character can meet the company on their first day out of Doc Mitchell's house.

| Town | Role | Supplies | Wants most | Company sites | Gate to grow here |
| --- | --- | --- | --- | --- | --- |
| Goodsprings | Home and HQ | dirty water, herbs, maize, brahmin; a small surplus of purified water and healing powder | purified water, smoked meat, healing powder | HQ office; well rig, forager hut, fields, corral; purifier and apothecary (tier 2); clinic (tier 4) | Goodsprings safe (Ghost Town Gunfight) for tier 2 |
| Primm | Market town on the I-15 | salvaged ammo, salvaged brick and timber, brahmin, sand, scrap | purified water, smoked meat, healing powder, moonshine; ammo use +50% while it has no sheriff | branch office; sand pit, scrap yard; smokehouse (tier 3); reloading bench and still (tier 4) | a sheriff (My Kind of Town) for tier 3 |
| Sloan | Quarry town | stone, once Quarry Junction is cleared | water, meat, healing powder, moonshine; building materials for the quarry crews | quarry crew and stone yard (tier 3) | the Quarry Junction deathclaws dead |
| Mojave Outpost | NCR border post | legal powder, syringes, scrap; NCR contracts | water, meat, stimpaks; ammo from a legal source only | depot (a bonded store); the NCR desk for the licence, duty and bids | none; contracts need NCR standing |

### Roads

Travel is counted in ticks, so the terminal can say plainly when a wagon will be back.

| Road | Wagon time | Danger at the start | Notes |
| --- | --- | --- | --- |
| Goodsprings – Primm | half a day each way: a round trip in one day | medium: Powder Gangers | the first route, the one the tutorial week runs on |
| Goodsprings – Sloan | half a day each way | low: geckos; deathclaws stray from Quarry Junction | quiet until the stone trade starts |
| Primm – Mojave Outpost | half a day each way | medium: raiders on the pass | where the NCR money is |
| Sloan – Primm | one day each way | medium: Powder Gangers along the I-15 | the long road that skips Goodsprings |

Road danger changes with the world: clearing the Powder Gangers, the NCR patrols the player pays for, and the rival's moves all shift it (see The road).

### Where the company stands in each town

- **Goodsprings HQ:** from tier 2, a small office near the Prospector Saloon (at tier 1 the company runs from a terminal at the agent's table inside the saloon) with a door to a new interior: the main terminal, the bookkeeper's desk, a map board that fills in as routes open, and a strongroom for the till. If Goodsprings falls to the Powder Gangers, the office stays but pays them (the Powder Ganger landlord variant under Growth).
- **Branch offices:** a terminal and a clerk in each town once a route runs there. Every branch terminal opens the same company, so the player never has to walk home to run it.
- **Workshops** sit where their input is, so the map explains the chains: water and herbs at Goodsprings, meat and ammo at Primm, stone at Sloan, imports through the Outpost depot.

**Relay desks** (from M2): a company terminal with no market at the 188 Trading Post and at Novac, so the company stays within reach when the main quest takes the player north. The tier 4 deed, an NCR contract delivered in person, can be done at Camp McCarran.

### Later towns (after launch)

| Place | When | What it adds |
| --- | --- | --- |
| Novac | tier 3 and up | a Highway 95 route north; demand for water and meat |
| Freeside | tier 4 | the Crimson Caravan's home ground; the Kings; a contact for the dodgy side |
| The Strip gate | tier 5 | Mr. House's representative as a possible patron |
| NCR Correctional Facility | any tier, if the player deals with the Powder Gangers | a contact for contraband powder; no trading post |
| Nipton | while the Legion holds it | a closed road, shown on the map board as a warning |

The earlier visualiser has an interactive version of this map: https://claude.ai/artifact/XiPe2UdjwvPXT23HSCEvPd (it predates this doc, so where they differ, this doc wins).

## Goods and production chains

Seventeen goods make five chains: nine come from the ground or from imports, eight are made in your workshops. Seven of the eight made goods are real FNV items; the new one is building materials (stone plus sand, the user's "clay = rock + sand").

Vanilla values are useless as wholesale prices (lead and powder are worth 0, one scrap metal makes 200 lead), so the mod keeps its own price table per crate. Every ratio is a small whole number so the terminal can show it plainly.

| Good | Kind | Comes from / made from | Workshop, skill | Bought by | Anchor per crate |
| --- | --- | --- | --- | --- | --- |
| Dirty water | raw | Goodsprings spring | Well rig | Purifier | 100 |
| Herbs (broc + xander) | raw | Goodsprings hills and new fields | Forager hut, Survival 15 | Apothecary, clinic | 60 |
| Brahmin | raw | Goodsprings and Primm pens | Corral | Smokehouse | 120 a head |
| Maize | raw | New fields at Goodsprings | Field | Still | 40 |
| Stone | raw | Sloan quarry, once the deathclaws are dead | Quarry crew | Stone yard | 50 |
| Sand | raw | Flats south of Primm | Sand pit | Stone yard | 20 |
| Scrap metal | raw | Salvage at Primm and the Outpost | Scrap yard, Repair 10 | Reloading bench | 30 |
| Powder | import or contraband | NCR import at the Outpost, or the Powder Gangers | — | Reloading bench | 90 legal, 55 contraband |
| Syringes | import | NCR sutler at the Outpost | — | Clinic | 150 |
| Purified water | made | 5 dirty → 4 (vanilla ratio) | Purifier, Survival 50 | Every town | 200 |
| Healing powder | made | 1 herbs → 1 (vanilla recipe) | Apothecary | Goodsprings, Primm, Sloan | 100 |
| Stimpaks | made | 1 herbs + 1 syringes → 2 | Clinic bench, Science 70 | Mojave Outpost, Sloan | 375 |
| Smoked meat | made | 1 brahmin → 4 | Smokehouse (Primm), Survival 35 | Sloan, Outpost, Goodsprings | 100 |
| Building materials | made | 2 stone + 1 sand → 2 | Stone yard (Sloan) | Every town: the growth cargo | 150 |
| Lead | made | 2 scrap → 1 | Reloading bench, Repair 10 | Reloading bench | 40 |
| Ammo (100 rounds) | made | 1 lead + 1 powder + 1 scrap for cases → 2 | Reloading bench, Repair 25 | Outpost, Primm, Sloan | 200 |
| Moonshine | made | 2 maize + 1 purified water → 2 | Still, Survival 40 | Primm, Sloan, Outpost | 160 licensed |

**The five chains**: water (spring → purifier), medicine (herbs → healing powder → stimpaks with a skilled hire and imported syringes), food (brahmin → smokehouse), building (stone + sand → materials that grow towns), ammo (scrap → lead, + powder + cases → rounds: the deepest chain, our Transport Fever steel mill). Moonshine is the sixth, small and shady.

### Starter trade: what the towns make themselves

Before the company builds anything, each town already makes a little of something and uses a little of everything. Tier 1 is trading those small surpluses. From tier 2 your own workshops beat the towns on volume and cost, and that is the first upgrade you feel.

Each cell is **daily use / normal stock → resting mid price** in crates and caps (the price formula is under Money; stock drifts back toward normal each night). A normal stock above three days of use means a surplus town, so the price is low; below it, the price is high. Each town level adds a quarter to the town's use.

| Good (anchor) | Goodsprings | Primm | Sloan | Mojave Outpost |
| --- | --- | --- | --- | --- |
| Purified water (200) | 4 / 34 → 152 (the settlers' pump and filters) | 10 / 14 → 236 | 6 / 6 → 250 | 8 / 12 → 233 |
| Healing powder (100) | 2 / 18 → 75 (made by the settlers) | 4 / 4 → 125 | 3 / 3 → 125 | 2 / 6 → 100 |
| Ammo (200) | 4 / 4 → 250 | 2 / 20 → 146 (salvage); 3 / 20 → 162 while Primm has no sheriff | 2 / 2 → 250 | 4 / 4 → 250, legal source only |
| Dirty water (100) | 1 / 30 → 59 | 2 / 2 → 125 | 2 / 2 → 125 | — |
| Herbs (60) | 1 / 15 → 40 | 1 / 1 → 75 | — | — |
| Building materials (150) | 1 / 0 → 225 | 1 / 10 → 110 (salvaged brick and timber) | 2 / 0 → 225 | — |
| Smoked meat (100) | 4 / 4 → 125 | 6 / 12 → 110 | 4 / 2 → 136 | 6 / 6 → 125 |
| Stimpaks (375) | 1 / 1 → 469 | 1 / 1 → 469 | 1 / 1 → 469 | 2 / 1 → 509 |
| Moonshine (160) | — | 3 / 1 → 224 | 2 / 1 → 217 | 2 / 0 → 240 |

The first roads therefore pay both ways: Goodsprings water, healing powder, dirty water and herbs out to Primm and Sloan; Primm's salvaged ammo back to Goodsprings and on to the Outpost. Meat, stimpaks and moonshine have buyers but no source until your own workshops make them: that is the prize of tiers 2 to 4. Workshop inputs are not shown: powder and syringes are bought at the Outpost depot at their anchor price (up to 3 and 1 crates a day); maize, brahmin, scrap, sand and stone come from your own raw sites (see Core numbers, under Numbers) or are bought where they are made, at their anchor price. These are first values for tuning (see Numbers).

**Workshops level with throughput**, Transport Fever style. When a workshop has run above 80% of capacity with 80% of its inputs supplied for 7 days, a memo offers the upgrade; it never happens by itself, so spending stays your choice. Starved for 14 days, it drops a level and looks weathered, never destroyed.

| Level | Cost | Crates in a day | Output | What you see |
| --- | --- | --- | --- | --- |
| 1 Lean-to | 300 caps | 4 | base | Open shack, one hand at work |
| 2 Shop | 1,200 caps | 8 | +10% | Roof, painted sign, second hand, a cart outside |
| 3 Works | 2,200 caps + 60 building materials | 16 | +20%, and stimpaks and ammo sell 10% higher | Stone wall, smoking chimney, stock piles, a lamp at night |

Staff skill matters: the clinic needs a Science 70 hire, the purifier a Survival 50 one. You can run a bench yourself if you have the skill, but that earns nothing while you are away.

**Towns grow like Anno settlements.** Each town has a level (Camp, Hamlet, Village, Town). Basic needs (water, food, medicine) met at 80% for 7 days, plus a delivery of building materials (40, 90, 160 crates), raise the town a level. Luxury needs (ammo, moonshine, stimpaks) do not grow the town; they fatten its wallet, so it pays more. Each level raises the town's daily use of every good by a quarter (a bigger market for you), adds residents from the lived-in towns pool, and enables a set of placed objects: a fenced yard, a market stall, a lamp post, then a stable and a proper store front. A town starved of basics for 14 days slips back one level.

**Chains unlock one per tier**, and each needs one new input you have to go and find:

| Tier | New chain | What you have to find |
| --- | --- | --- |
| 1 Peddler | None: trade the towns' own surpluses (Starter trade, above) | A route that pays |
| 2 Outfit | Purifier and apothecary (water and healing powder) | A first hire with Survival 50 |
| 3 Caravan company | Smokehouse in Primm; stone yard in Sloan when Quarry Junction is clear | Primm needs a sheriff; Sloan needs the deathclaws dead |
| 4 Trading house | Reloading bench (ammo) and clinic (stimpaks); the still | Powder (NCR import or contraband), syringes, a Science 70 hire |
| 5 Mojave concern | NCR army contracts for bulk ammo and stimpaks | Standing with the NCR, or a patron |

**Two chains cross the line.** Powder Ganger powder makes the *input* illegal: cheaper and plentiful, but a raid that finds it seizes the stock and the bench, and the ammo it made is clean once sold. Unlicensed moonshine makes the *sale* illegal: nothing in the supply chain is suspicious, but every black-market sale raises heat in that town. Every chain always keeps a legal way to run.

## Money: the ledger, prices and the P&L

Every town holds one stock number per good. Price comes from that stock and is capped between half and one and a half times the anchor price. Selling the same good to the same town every day is punished, and a new route or a contract is the way out.

**The crate** is the only cargo unit (10 bottles of water, 100 rounds, 20 cuts of meat). A starting wagon with two brahmin carries 8 crates. Anchor prices follow vanilla item values so the world stays consistent: a crate of purified water is 200 caps because a bottle is worth 20.

**Price per town and good**, recomputed for every crate bought or sold (so a big dump visibly drives the price down):

```latex
r = \frac{\text{stock}}{3 \times \text{daily use}} \qquad m = 0.5 + \frac{1}{1 + r} \qquad \text{mid} = P_0 \times m \times \text{news}
```

An empty shelf pays 1.5 times the anchor, three days of cover pays the anchor, and a glut falls toward half. The buy and sell prices sit a spread either side of the mid; the spread starts at 10% and shrinks with town trust and the trader's Barter, down to 2%. **News** is an event factor (Powder Gangers raid Primm: ammo ×1.4 for a week; Quarry Junction cleared: materials at Sloan ×0.85) that fades a quarter of the way back each day and is rumoured a day or two ahead.

**Markets recover unevenly.** Each night a short stock refills 25% of the way to normal (half-life about 2.4 days), but a glut drains only 12% (about 5.4 days). The money agent's simulation of one wagon on Goodsprings–Primm: +746 caps on day 1, +288 on day 2, then about +90 a day. That **thin-market trap** is deliberate: it is what pushes you to open a new route, add a good or sign a contract.

**Contracts are the steady half.** A supply contract ("Primm saloon: 4 crates of water a week at 215 for 4 weeks") pays about 9% over a normal spot price, does not move the town's spot stock, and costs 10% of its value plus trust for each missed delivery. Contract volume per town and good is capped at half the town's daily use, and it counts toward market share. Town supply contracts are open from tier 1 (one at a time until tier 2); NCR bids open at tier 4. Before that, once the player holds Mojave Outpost clearance at tier 3, the NCR desk offers one trial contract (water for the garrison), and delivering it in person is the tier 4 deed. The NCR Treasury rescue loan's contracts are assigned, not bid for. Rule of thumb on the help page: *contracts pay the wages, spot trade pays the growth.*

**The P&L** (the weekly statement, every line always visible):

| Group | Lines |
| --- | --- |
| Revenue | Spot sales, contract deliveries, workshop output, NCR supply contracts, contraband (dodgy side), storage rent (tier 4) |
| Cost of goods | Cargo bought, workshop inputs, spoilage (perishables lose 6% a day on the road) |
| Running costs | Wages, brahmin feed (3 caps a day each), wagon wear, rent and upkeep, tolls, NCR duty and licence, insurance, bribes and fines |
| Losses (own lines, never buried) | Road events, NCR raids, rival sabotage and price-war write-downs |
| Finance | Loan interest, late fees; principal shown in cash flow |
| Bottom lines | Operating profit, net profit, **net worth** (cash + stock + wagons and buildings at book − debt) |

Earned worth (net worth minus the caps the owner put in) is the main growth number and the one the tier gates use; market share against the Crimson Caravan is the second.

**Founding money**: Alice lends **3,000 caps at 4% a week** on the balance, with at least 300 of principal due each week; paying early costs nothing. You put in 500 of your own (owner funds). Her agent at the Prospector Saloon in Goodsprings signs it with you as a letter of credit; Alice herself sends for you later, once you are worth watching. Setup (wagon 400, two brahmin 300, a driver and a guard, the licence 150) costs about 1,000, leaving 2,500 to trade with and a net worth of about 200. A competent player clears the loan in about 5 game weeks; a cautious one in 8.

**Two cash pots: operating cash and owner funds.** Only **operating cash**, the money the company earned plus its loans and contract advances, pays bills, stock and wages; the front page's CASH and Runway count only it, and owner funds are shown on the Ledger screen. **Owner funds** hold the founding 500, every top-up, and the margin on anything the company sells to you (that sale is booked at cost and the rest goes to owner funds). Owner funds can buy wagons, buildings and upgrades, never stock, wages or bills; selling an owner-funded asset puts the money back into owner funds. You may top up whenever you like, before or after the loan: it speeds up growth, but it cannot keep a bill from being missed. The only way owner money touches a bill is the **owner rescue** after a miss (see Losing and coming back), and the strike still stands. Tier gates, records and sparklines use **earned worth**: net worth minus all the owner money put in. Dividends come out of owner funds first.

**Money sinks**, built in from day one so cash never piles up uselessly: buildings and their upkeep, wages that rise with tenure, a progressive NCR duty (2% of sales, 3.5% above 5,000 a week, 5% above 20,000), town building projects, price wars, insurance and training, and a **till limit**: more than 5,000 caps sitting in one depot is a raid target unless you pay guards or move it.

**No flipping exploit.** The company sells to the player at 1.1 times the anchor, at most 2 crates a day for the player's own use (booked at cost, the margin going to owner funds), and buys from the player at 0.8, at most 10 crates a day. Vanilla vendors pay at most about 0.9 of value (read from the barter settings), so buying cheap from your own company and selling to Chet never pays. A crate traded with the player is a fixed vanilla bundle shown on the Tape (for example 10 bottles of purified water, 5 stimpaks, or 100 rounds of a calibre the company loads: 9mm and 10mm at launch); other calibres, and goods the company does not trade, are refused.

## Growth: five tiers, five jobs

Each tier gives you a new kind of decision, not a bigger copy of the last one, and each is gated on money, trust and a deed done in the world, the way Assassin's Creed Brotherhood makes you burn the tower before you can rebuild the street.

| Tier | You become | The new decision | Gate: money + trust + deed | What changes in the world |
| --- | --- | --- | --- | --- |
| 1 Peddler | A trader | What to carry and where (the price board) | Sign Alice's letter of credit with her agent at the Prospector Saloon | A hand cart and brahmin behind Chet's store, a chalkboard of today's goods, and a terminal at the agent's table in the Prospector Saloon |
| 2 Outfit | A boss | Who to hire, which contracts to sign | Earned worth 1,500, loan payments on time, Goodsprings trust Liked, **Goodsprings safe** (Ghost Town Gunfight done) | A rented office with a sign and a terminal, a manager at the desk, company banners on the brahmin, a stall in Primm |
| 3 Caravan company | An industrialist | What to build, which town to grow | Earned worth 8,000, trust Liked in two towns, **Primm has a sheriff** (My Kind of Town) | The smokehouse chimney smokes, stone piles grow in Sloan, guards in company coats on the road, Goodsprings houses get extensions built from your stone |
| 4 Trading house | A magnate | Policy for managers, NCR bids, clean or dodgy | Earned worth 25,000, loan repaid, Mojave Outpost clearance, **an NCR contract delivered in person** | A warehouse with wagons waiting, an NCR clerk visiting, Alice's agent watching your yard |
| 5 Mojave concern | A power broker | Laws, patrons, and what to do about Alice | Earned worth 80,000, majority share in 3 of 4 towns, **beat Alice or win a patron** | Your flag over Mojave Outpost and Primm, a proper company building, staff walking in shifts |

**Each tier also changes how you play Fallout**, because caps alone mean little to a Courier who already has plenty. As an Outfit, your traders buy loot that is a trade good at the company's crate price (up to 500 caps a day; weapons and armour are not bought) in towns where you hold 20%. As a Caravan company, any branch takes your loot and the wagons bring it home: a remote stash. As a Trading house, vendors in towns you lead give you 10% off. As a Mojave concern, crew reports mark raider camps and ambushes on your map, and a company guard can travel with you as a light companion.

Earned-worth targets are first guesses for tuning. The aim: tier 2 by day 14, tier 3 by week 4, tier 4 by week 7, tier 5 around week 11 (very roughly 5, 20, 35 and 55 real hours, since game time also passes in sleep and fast travel).

**If you sided with the Powder Gangers** (Run Goodsprings Run), Goodsprings is still your HQ, but the gang are your landlords: sealed-crate runs for the gang from day one, heat starts at 20, and the tier 2 deed becomes "keep the gang paid for 7 days".

**Market share** is the second growth number: for each town, the share of its weekly use that you supplied, against the Crimson Caravan and local sellers. It is computed only from deliveries you can see, never from a hidden rating.

**How growth is made felt** (none of these cost much to build):

- **Records**: the report marks a new best day, best week, biggest crate margin or longest streak without a missed payment.
- **Trend lines**: a 14-day text sparkline beside earned worth, share and each route.
- **A tier-up letter** from your bookkeeper, a dated line in the company history ("Day 23: the Sloan stone yard opened"), and the world change within one game day.
- **The deed ledger**: one page listing which of your adventures unlocked what ("Quarry Junction cleared: stone yard").
- **Beating Alice somewhere**: "You now sell more water in Primm than the Crimson Caravan" is its own headline.
- **The office map board**: a physical board in the HQ where pins and string appear for each route you run.
- **Towns talk**: residents mention the company by name once your share there passes 20%, and again at 40%.

## People: staff and managers

Staff are a name, four numbers, one or two traits and a history; managers each take one chore off your hands and each can go wrong in one way that names your own policy.

**Who you hire comes from the towns.** Every hire is one of the mod's own placed residents (the lived-in towns part), so they already have a house, a bed and a routine; the job adds a walk to work. Vanilla named NPCs (Trudy, Chet, Sunny Smiles, Johnson Nash, Chomps Lewis) are never hired. They give references, sign supply deals and send you their nephews. Their records and scripts are never edited.

**Roles**

| Role | Does | Skill shown |
| --- | --- | --- |
| Trader | Sells at each stop; sets the margin | Barter |
| Caravan master | Leads one caravan; fight, run or talk | Survival |
| Guard | Adds to a caravan's defence | Guns |
| Brahmin handler | More cargo, less spoilage | Survival |
| Clerk | Runs the office; each clerk adds one route slot | Speech |
| Workshop hand | Runs a bench; some recipes need a skill (stimpaks need Science 70) | Science, Repair or Survival |
| Medic | Halves injuries on the road | Medicine |

**Numbers per person** (0 to 100): **Skill** in the role, **Nerve** (danger, heroics, panic), **Honesty** (skimming; shown only as a band after a reference check), **Loyalty** (quitting, poaching). Plus up to two traits from a list of about 24, each with one upside and one cost: Haggler, Cautious, Reckless, Drinker, NCR veteran, Ex-Legion, Family man, Ambitious, Grudge against a faction.

**Loyalty always lists its reasons**, RimWorld style, on the person's page: +10 paid on time, +15 you saved them in person, −15 a colleague died on the same run, −12 Crimson Caravan offered more. Under 35 they ask for a raise or leave; under 20 they may sell route information to Alice. New hires start at 55, plus or minus the wage offer.

**Wages**: paid per day: driver 10, guard 12, trader 20, workshop hand 14, manager 40, a Science 70 chemist 60; within a role, +1 cap a day per 10 Skill above 50. Tenure rungs (Rookie, Hand, Veteran, Master at 4, 12 and 30 runs) add 25% wage and raise the skill cap. Master is the last rung, so there is no wage spiral.

**Injury and death** are rolled on the road (defence against danger). A death can only happen when the route page showed the danger above the crew's defence before the run, so every loss traces back to a choice you saw. The dead get a line on the wall in the office and a family the town remembers.

**Managers automate one chore each** (menus only, no typing):

| Manager (tier) | Takes over | Policy presets | Goes wrong when |
| --- | --- | --- | --- |
| Route manager (3) | Sends and re-routes caravans | Safe / Balanced / Fast / Opportunist | Opportunist chases a price spike into Powder Ganger land |
| Purchasing manager (3) | Buys workshop inputs | Stock up cheap / Just in time / Starve the rival of one good | Overbuys goods that spoil; a supplier bribes a dishonest one |
| Workshop foreman (3) | Recipe order, bench staffing | Highest margin / Fill shortages / Medicine first | Chases margin and a town goes dry |
| Bookkeeper (2) | Weekly books, catches skimming, writes the week's page | Strict / Normal / Lenient | Lenient misses theft; Strict annoys a clerk into leaving |
| Fixer (4, dodgy side) | Pays inspectors, hides contraband, warns of raids | Quiet / Standard / Loud | A fixer with loyalty under 40 sells you out |

Each manager also has an **autonomy** setting: Ask me (a memo per decision), Within budget (acts up to a cap), Full (acts and reports; Trading house tier only). Every manager mistake in the report names the policy that allowed it, so the blame lands on a choice you made.

**Hiring** (Staff > Hire): 3 to 6 candidates a week, each with a role fit, an asking wage and one rumour line ("lost a cousin to the Powder Gangers"). Before you offer you can buy a reference check (5 to 20 caps, 1 day: Honesty band and a quote from a named townsperson), a test run at half wage (true Skill and Nerve), or, for managers, an interview in person at a place the terminal marks (reveals the hidden trait, +10 Loyalty). Offers are Low, Fair or Generous.

**Staff stories** come as memos with two or three choices: a raise demand, Alice poaching your best trader (always one day's warning), embezzlement found by a strict bookkeeper, a guard who held the road alone (gains the trait Steady, and the town talks), a sick mother and an advance, a mutiny after two deaths on one route, the family of a dead guard asking for owed wages.

**Limits for version 1**: about 60 staff in fixed slots, hiring more than a fifth of a small town drains it (fewer guards, less stock, lower trust).

## The road: caravans, danger and events

Every route has a danger colour you can read, a chance of a clean run you can see before you send a wagon, and a cause you can go and remove yourself.

**A caravan is a crew with a name.** "Dusty" is a wagon, two brahmin, a driver, a guard and a history line ("14 deliveries, one ambush held"). A crew that survives three fights earns a nickname and a trait; one that dies goes on the wall in the office. A famous crew is sung about in the saloon of the town it saved, which adds a little trust there, and makes Alice want to poach it.

**Route danger** comes from the world first: Powder Gangers loose near Primm, no sheriff in Primm, deathclaws at Quarry Junction, a gang on the Sloan road. The colour (green, yellow, orange, red) is printed on the route page with its cause. Then a **cover** number (guards, scouts, an armoured wagon) gives the chance of a clean run:

```latex
P_{\text{clean}} = \frac{r^2}{1 + r^2}, \qquad r = \frac{\text{cover}}{\text{danger}}, \qquad 5\% \le P \le 95\%
```

The director decides which roads get an event; this chance only resolves an event it has placed, and most trips meet none. Even cover gives 50%, 1.5 times gives 69%, double gives 80%. A failed run is usually costly but survivable (lose 30% of the cargo, a guard hurt, a day late); about one failure in three loses the wagon (within the loss limit below) and can hurt, or rarely kill, a named crew member. The route page says it in words: "Cover 45 against danger 60. One veteran more makes this road 69%."

**Stance per route**: Cautious (danger ×0.7, profit ×0.85, a day slower), Standard, or Hustle (danger ×1.5, profit +30%, more spoilage).

**Clearing the road yourself** drops a route one colour for 10 game days and gives the crews on it +15 loyalty. Some causes go away for good when the vanilla quest is done: the deathclaws, the Powder Gangers, the empty sheriff's office.

**Paper or real.** When you are away, the trip resolves at the morning tick on paper. When you are within reach of the route while a trip is out, the crew appears on the road for real: the hires' own characters, moved from their homes, plus spawned brahmin and spare guards. A rolled ambush becomes a real fight whose result is written back to the ledger. Named crew cannot die in a real fight (they go down and get up hurt), so being there is never worse than the paper result. A **radio call** gives you 6 game hours (12 real minutes) to come and help; ignore it and the paper roll stands. The paper result is set to about what an average player would get, so being there is a bonus, never a requirement.

**The event director** (RimWorld's storyteller, simplified):

- **Threat** grows with net worth on a soft cap and with how visible you are (towns where you hold over 40%). The first 10 days of the company are gentler, and the director eases off for a week after a serious loss.
- **How often**: one event every 3 days as a Peddler, rising to one a day as a Mojave concern. Mix: 45% bad, 30% good, 25% dilemmas; every quiet day beyond 4 shifts the mix 3 points toward good.
- **Pacing**: a stress meter stops crises coming back to back; after any crisis come two calm days; no bad event on bill day or the day before.
- **Tomorrow's forecast** sits at the top of the report, Into the Breach style: "Jackal band near the Primm road, about 60 strong. Your cover there: 45." You can reroute, reinforce, change stance or go yourself.

**The deck** has 24 events to start, each with a paper and a real version. Samples:

| Event | Kind | Choices |
| --- | --- | --- |
| Powder Ganger toll on the Primm road | bad | Pay 15% of the cargo, fight, or bribe with five boxes of lead |
| Cazadors at night on the Sloan road | bad (crisis) | Camp till dawn, press on, or burn flares (20 caps, halves the danger) |
| Axle break | bad (nuisance) | A Repair 25 hand fixes it, leave the wagon, or ride for help |
| Stranded rival wagon | good | Salvage the cargo, rescue them (they owe you), or report it to the NCR |
| Price spike after a Powder Ganger raid closes a market | good | Sell now at +40%, or hold for more and risk a fall |
| Wounded NCR trooper hitches a ride | dilemma | Carry him (two days slower, NCR standing, a Ranger contact), or refuse |
| Unmarked crates on an abandoned wagon | dilemma | Keep them (300 caps, heat +8), return them, or report them |
| A drifter offers to guard for half wage for 14 days | dilemma | Hire him, hire him and do his favour, or refuse; a callback follows a week later |

**Insurance** (an optional line per route, priced from what it is expected to pay out on that route, so it loses a little on average and pays off against the losses it was bought for):

| Cover | Price | Pays | The catch |
| --- | --- | --- | --- |
| Crimson Cover, from Alice | 1.15 × its expected payout on that route | 60% of losses within 2 days | She gets your manifests, so her price wars hit your routes more precisely |
| NCR war-risk | free | 80% | Only for NCR contract cargo, no contraband, NCR standing 40+ |
| Reserve fund | 10% of weekly profit set aside | up to the fund | Empty when you need it most |
| Omerta assurance | 1.3 × its expected payout on that route | 100%, contraband included | A collector visits after every claim |

**Loss limits**: no event takes more than 25% of gross assets (and at tier 1 no more than 3 days of runway); a wreck can be salvaged for 50 to 80% of its cargo within 2 game days; a wainwright rebuilds a wagon in 2 days at 60% of its cost.

## The Crimson Caravan: a rival with a face and a memory

The Crimson Caravan plays by the same ledger rules you do, makes at most one move a day, and gets angrier the more of its market you take. Alice tells you what she remembers.

**Grounded in the game's own notes.** FalloutNV.esm already shows the Crimson Caravan supplying the NCR, binding its caravaneers with work contracts, lobbying for a tariff on the Gun Runners, and planning to "overwhelm" a rival town with cheap NCR goods. Those are exactly the moves it makes here.

**What it watches** each game day: your share per town, your margin on each route (only once a route makes 120 caps a day or holds 25% of a town, so a small outfit stays under her radar), your wages against hers, your NCR contracts, your heat, and your cash.

**Aggression** runs 0 to 100 and starts at 20, because she lent you the money. It rises with your share over hers, with every bid you win and every sabotage of yours she catches; it falls when you pay her tribute or become her partner.

| Aggression | Moves she uses |
| --- | --- |
| Under 30 | Price signals and counter-bids on contracts |
| 30 to 60 | Price wars, poaching your staff, buying out your suppliers |
| 60 to 80 | Sabotage, tip-offs to the NCR |
| Over 80 | All of it, plus a buyout offer the moment your cash is short |

**Her own supply.** The Caravan starts with 30% of the daily use of water, meat and ammo in Primm and the Mojave Outpost, and 10% in Goodsprings and Sloan, delivered into the same town stock you trade against. A price war cuts her price by 10% and adds 10 points of share for 14 days; a buyout or an exclusive deal moves 15 points of one good in one town; a route she loses to you halves her share there. **Leading her** in a town means your weekly share is above hers in at least three of that town's goods.

**Cassidy Caravans, reborn.** If Heartache by the Number ends against Alice, Cass can lend her family name: the company may trade as Cassidy Caravans, with a letter and a new sign, and no vanilla record edited.

| Move | Trigger | Effect | How you see it |
| --- | --- | --- | --- |
| Price war | Your share in a town over 25% and rising for 3 days | Your top two goods there sold 15% cheaper for 5 days | Memo; "Lowest prices in the Mojave" posters on her stall |
| Poach | Your wages 10% under hers | Takes one low-loyalty hire a week at +20% wage | A day's warning; later you see them in her coat |
| Supplier buyout | One of your suppliers sells only to you | Pays them 130%; your input cost rises 25% | The supplier wears her patch |
| Undercut bid | One of your contracts renews within 7 days | Bids 8% lower | Both bids on the memo |
| Tip-off | Your heat 60+, her aggression 40+ | Heat +15, once in 10 days | Rangers arrive with "an anonymous letter" |
| Sabotage | Aggression 60+ | A warehouse fire (−20% stock) or a stampede; leaves evidence | Smoke, dead brahmin, Van Graff men seen near the road |
| Buyout offer | Your cash under 14 days of wages | 2.5 times last month's profit for the company | A letter; always at least 7 days to answer |
| Ignore | Your share in a town under 5% | Nothing | Nothing: small and quiet is a valid strategy |

**How you fight back**: match her price (it pays if your chain makes the good cheaper than her imports), sign exclusive supply deals (+20% for 30 days, blocks a buyout), poach her unhappy caravaneers, run contracts in person so she cannot underbid, or have your fixer hit her wagons (40% success; failure costs heat and aggression). Three pieces of her sabotage evidence, taken to Ranger Jackson, cost her a 500-cap NCR fine and her next NCR bid, without touching any vanilla quest.

**Alice remembers.** A small set of grudge flags (you robbed a Crimson wagon, poached her staff, won a price war, paid your loan early, exposed her in Heartache by the Number) changes her numbers and is quoted back in her letters: "I note you still owe me for Mara, Courier." Every fifth grudge promotes a named Crimson captain who leads her guards on your roads, learns your habits after three fights, and can be killed for good as a field boss.

**Steal her ledger.** Her office terminal and safe (the same ones Heartache by the Number uses) can hold a copy of her plans: read it and for one week you see her aggression and next move.

**One rival item per report**, at most. Standing orders can answer the routine moves ("match price cuts up to 15%").

**Lore safety.** Alice may be dead, Cass may have sold, Heartache may have gone any way. The mod only reads those states. If Alice is dead, Jason Tagg (the Modoc branch manager named in her notes) takes the New Vegas desk and the same rules apply. Her offers come through the mod's own quest and dialogue topic, never by editing her vanilla records.

**The end of the rivalry** (tier 5): a **merger**, where Alice offers partnership once you lead her in three towns (aggression goes to 0, she takes 25% of profit, and the Gun Runners and Van Graffs step in as the new rival); or a **takeover**, where you buy blocks of Crimson shares by out-trading her route by route and win her board's votes with contracts and favours. Win, and she works for you or leaves; lose the vote, and she comes for your debt.

## The NCR, the law and the dodgy side

The NCR is the government you pay, bid against and sometimes cheat. Its best contracts only go to clean companies, so smuggling pays more per crate but closes the richest door.

**The NCR's tools** (its desk is the clearance office at Mojave Outpost, where vanilla already has caravans backed up waiting for papers):

| Tool | How it works |
| --- | --- |
| Clearance licence | Needed to trade between NCR settlements. 150 caps per 28 days at tier 1, rising to 3,000 at tier 5. Unpaid: a warning, then wagons held at the Outpost after 8 days (held, not seized) |
| Duty | 2% of sales, rising to 3.5% and 5% for big companies. Declaring less adds heat |
| Tolls | 20 caps a wagon through the Outpost; free once you are a preferred carrier (tier 4) |
| Supply contracts | 1 to 3 posted each week ("1,200 rounds of 5.56 for the Outpost in 10 days"). Lowest bid wins among bidders with 60%+ on-time deliveries. Pays 1.3 times market and NCR standing, but pays 10 days late, so it strains cash |
| Inspections | Once in 30 days, or once in 10 if heat is 20+. They check the licence and the books. First fault is a warning, then a fine of 5% of the week's revenue |
| Patrols | 60 caps a week puts a Ranger on one route: danger −20% there |
| Decrees | Every 28 days, with the licence renewal, the morning report prints a new rule, Papers Please style: "Ammunition shipments over 500 rounds need a permit (25 caps)" |

**NCR standing** is the company's own 0 to 100 number, earned by contracts and taxes paid on time. Vanilla NCR reputation only nudges it (Idolized: licence −20%, half the inspections; Vilified: no new contracts, double inspections), so a quest swing never wipes out the company's history. Ranger Jackson can never be bribed.

**When the player commits to a side** (the main-quest point where the other factions turn hostile, read from vanilla quest stages), one regime switch changes the rulebook for the rest of the run. It happens then, not after the battle, because vanilla FNV ends at the Dam. NCR keeps these rules and makes tolls cheap; the Legion replaces tax with a 12% tribute and bans NCR goods; Mr. House adds a Strip licence and Securitron checks; an independent Vegas has no tax, more danger and a stronger Crimson Caravan. The mod works the same if the player never commits.

**The dodgy side is a slope, not a switch.** You choose how far down to go:

1. Under-declare sales (saves duty, heat +2 a week per 10% hidden)
2. Run sealed crates for a Powder Ganger or Omerta contact: 50 caps a trip, at most one run every 3 days, heat +5, and at any heat a 10% chance that a patrol searches the wagon (a 100-cap fine and heat +10); open from tier 1
3. Buy Powder Ganger powder (only while they exist)
4. Sell moonshine without a spirits licence
5. Move chems for an Omerta contact in Primm (after launch, if approved)
6. Fence stolen NCR gear (the most profitable, and NCR troopers notice; after launch, if approved)

No slaves, ever; Legion goods stay material.

**The dodgy menu has to be found.** Its terminal options stay hidden until you meet a contact in person (Eddie's runner at the NCR prison, or the Omerta man in Primm). After that, one new page appears on the terminal.

**Heat** (0 to 100, always on the front page next to Runway):

| Heat | What happens |
| --- | --- |
| 0 to 19 Quiet | Nothing |
| 20 to 39 Noticed | Inspections every 10 days; the clerk gets curious |
| 40 to 59 Watched | Road searches: each trip with contraband has a 10% chance of losing it; Alice knows |
| 60 to 79 Hot | NCR contracts frozen; tip-offs; a raid becomes possible |
| 80 to 99 Imminent | A warrant is served and the raid follows the warrant rule (below), unless bribed or cleared; licence suspended |
| 100 | A warrant at once, and no bribe |

Net heat gain is capped at +3 a day. Heat falls 2 a day by itself, 4 a day after 7 clean days, faster with a fixer, a fine paid or a donation to the NCR war effort.

**The raid.** Every raid needs a warrant, served like a debt notice (at a terminal or by a runner, never while the busy shield is up). The raid then happens at the next company office the player enters, or on paper 7 days after the warrant if they stay away. On paper: guard strength against raid strength, and the result is win (but the company is marked outlaw), bribed, or seized (contraband, a warehouse for 14 days, 20% of cash). For real at an office, and the first raid is always real if the player reaches an office within the warrant's 7 days (your decision): Rangers walk up and you choose to fight (infamy, more heat), bribe (Speech 60 or twice the fine), surrender (lose the contraband, keep the company) or run. Whatever its result, a raid sets heat to 50, and no new warrant can be served for 7 days after it. A second raid within 28 days at heat 80+ revokes the licence: the second way to lose.

**Tools of the trade**: a **hidden warehouse** (400 caps, 30 a week, holds 40% of your contraband, 15% chance a raid finds it, and a found one means automatic seizure), a **fixer** (cuts fines by a quarter, warns of raids 70% of the time, launders 20% of dirty margin at a 10% loss; a fixer with loyalty under 40 sells you out), and the **customs manifest**: declare honestly, mislabel the crates, or split the load. One load in five is checked.

**Why it is tempting but not better**:

|  | Clean | Dodgy |
| --- | --- | --- |
| Margin | Base | +25% (sealed crates) to +120% (stolen gear) on dodgy lines |
| Fixed costs | Duty and licence | Fixer 80 a week, hidden warehouse 30 a week, bribes |
| Swings | Small | A raid costs 20% of cash, stock and a warehouse |
| NCR contracts | Open, the best margins at standing 60+ | Frozen at heat 60 |
| The rival | Competes on price | Gets a weapon: tip-offs |

The aim, to check in tuning: about +35% profit at heat 30 to 40, break-even by heat 70 once fines and frozen contracts count. Heat 50 is the knee where a careful smuggler sits.

## Losing and coming back

You can lose the company two ways, debt or the law. Both take at least 7 game days of visible warnings, and both end in a successor chapter, not a game over. What ends a company in debt is **strikes**, not the size of the arrears, so a full pocket can buy time but not immunity.

**Always on the front page:** Cash, Bills due (date and amount), **Runway** (days until cash runs out at the current burn) and **Heat**. Nothing that can end the company is ever off that page.

**The debt ladder**

| Stage | Trigger | What happens | Time to act |
| --- | --- | --- | --- |
| Forecast | Runway under 5 days | Banner and one Pip-Boy note: "short by about 180 caps on bill day" | up to 5 days before |
| Missed | Bill day, cash below bills | Pays wages first, then tax, rent, loan; 10% late fee on the rest; a notice is served | day 0 |
| Grace | day 0 to 3 | Normal play, every sale counts | 3 days |
| Final notice | day 3 | Cure 60% of arrears within 2 days, or lose an asset | 2 days |
| Seizure | day 5 | Creditor takes your most valuable asset (not HQ) at 60% of its value | 2 days |
| Receivership | day 7 | The company ends; your office becomes a Crimson Caravan branch | — |

Alice holds the first loan, so her receivership is literal. After the loan is paid, unpaid tax and rent go to an NCR receiver who auctions your assets, and Alice buys them. Either way her sign ends up over your door, as it did with Cass's company.

**Strikes.** A missed bill day becomes a strike when its notice is served, whoever pays it later. Bills deferred during one absence are served together as **one notice and one strike**, and each strike's 56 days count from the day it was served. A third strike within 56 days opens a **7-day takeover notice**. It replaces the normal debt ladder for that miss, and it can be cured only from operating cash (a rescue loan counts) or by selling assets (or by walking away), never with owner money: "I lent to a company, Courier, not to your pocket." Curing it clears the oldest strike. After the loan is repaid, strikes still count: at two late wage days the crew of the worst-paid route walks off, and at three late duty payments the NCR receiver serves the same 7-day notice.

**The served-notice rule and the busy shield** keep time away safe. Bills that fall due while you are away pay themselves from company cash. A bill that cannot be paid is *deferred* (a 10% late fee, no clock) until its notice reaches you: at any company terminal, or from a runner who finds you in the Mojave when you are not in combat, dialogue or a menu. Nothing is served automatically. While you are in a DLC's own lands (judged by where your current cell comes from, so Mojave interiors such as your office do not count), and only until that DLC's main quest is done (afterwards a DLC home such as the Sink is ordinary time away: new bills defer, but served notices keep running and paper losses are not capped), every debt and law clock stops and paper losses are capped at one day's profit. Every cure below is on the runner's message box as well as the terminal, so a notice can always be answered where it reached you. A player deep in the main quest or a DLC never comes back to a dead company.

**Cures at Final notice** (one menu, each with its price on screen):

1. **Sell assets** to a named buyer: wagons and cargo at 60%, workshops at 50%, stock at 70%.
2. **Contract advance**: a town or the NCR pays half a booked contract now; deliver in 6 days or pay back 1.5 times.
3. **Rescue loan** from one of three lenders (below).
4. **Owner rescue**: up to 2 weeks of bills from your own pocket, once a season. It cures the notice but not the strike, and it stays owner money, never counting toward a tier.
5. **Hail Mary contract**: one job at 150% pay and 1.5 times the danger. Succeed before the clock ends and the notice is cured.
6. **Walk away**: wind the company up yourself, on better terms than receivership.

| Rescue lender | Up to | Price | Strings |
| --- | --- | --- | --- |
| NCR Treasury, Mojave Outpost | 3 weeks of bills | 6% a week, 4 weeks | Two NCR contracts a week at set rates; heat must stay under 20; a monthly auditor |
| Alice McLafferty | 4 weeks of bills | 8% a week, 4 weeks | Takeover clause: one missed payment and she takes the office |
| The Omertas, through a Primm contact | 5 weeks of bills | 25% a week, 2 weeks | A silent partner takes 20% of profit; you carry their sealed crates (heat +5 a trip) |

Clearing the arrears puts you on **probation** for 14 days: a second miss skips Grace.

**The law ladder** (the dodgy side, see the NCR section): heat 60 makes a raid possible, and a raid costs stock, a fine and a warehouse, not the company. The company ends only on **revocation**: a second raid within 28 days while heat is 80 or more. That takes at least 7 days, because net heat gain is capped at +3 a day and every raid needs a warrant served like a debt notice.

**Anti death spiral rules**

- No single event takes more than 25% of gross assets (cash, stock, wagons and buildings), and at tier 1 no more than 3 days of runway.
- After a serious loss, towns post underdog contracts at +15% for 3 days, and the director goes easier for a week.
- No bad events on bill day, the day before it, or the 2 days after you reach a new tier.
- A lost wagon leaves a wreck you can salvage for 50 to 80% of the cargo within 2 game days.
- Every bad event ends with a "what went wrong" line naming the cheap fix: "guards below cover for this road; add one veteran."

**After losing: the successor chapter** (your decision: start over smaller; gone for good is the Ironman setting)

| You keep | You lose |
| --- | --- |
| The company's story, and half of each town's trust (Goodsprings keeps all of it) | Every building, wagon, contract and all market share |
| Every recipe and chain you unlocked, and every route you found | Your tier: you are a Peddler again |
| One loyal manager (the others can be rehired at 120% wage) | The HQ, which is now a Crimson Caravan branch; buying it back costs twice its price, paid from the successor's own earnings |
| Your own caps, and 5% of the company's peak earned worth as seed money (cap 1,500 caps) | 25% of the unpaid arrears, due over 4 weeks (waived if you walked away before seizure) |

The successor is founded by your loyal manager and run from the terminal in that manager's house until it can afford an office. The old office wall keeps the names of the dead, and winning back the Goodsprings office from Alice becomes the successor's first goal. An **Ironman** setting (named so it is not confused with FNV's own Hardcore mode) makes the loss permanent for players who want that.

## Your adventuring feeds the business

The quests you would do anyway are the company's biggest levers: they open towns, kill route threats and move prices. Like Lester's missions in GTA V, a player who reads the market can buy before a deed and sell after it.

**Vanilla quests the company reads** (read-only checks; the mod never sets a vanilla stage):

| Quest or state (how it is read) | What it does to the company |
| --- | --- |
| Ghost Town Gunfight done (`VMS16` stage 100) | Goodsprings is safe: the tier 2 deed, Goodsprings trust up a step, office rent halved |
| Run Goodsprings Run done (`VMS16b` stage 100) | The Powder Ganger landlord start: cheap powder, heat 20 |
| My Kind of Town (`VStoryEventPrimm` = 1) | Primm reopens: the tier 3 deed, the smokehouse site, Primm demand up by half. The sheriff matters: NCR (`VStoryEventPrimmSheriff` 1) means cheap patrols and more inspections; Meyers (2) lower duty and a blind eye; Primm Slim (3) steady and dull |
| Claws Out: Quarry Junction leaders dead (`vFreeformSloan.bDeathclawLeadersDead`) | The stone yard opens, the Sloan road drops two danger colours, building materials get cheaper for a few days |
| Powder Gangers at the NCR prison (I Fought the Law, `VMS02`) | Wiped out: Primm roads safer, contraband powder gone. Allied: cheap powder and a smuggling contact |
| Heartache by the Number (`VCassCompanion` 100 or 110) | Exposed Alice: her aggression starts 15 higher. Alice dead: Jason Tagg takes her desk |
| You Can Depend on Me (`VMS05`) | You bought Cass's company for Alice: she starts friendlier and trusts your paper |
| Vanilla NCR reputation | Nudges NCR standing by up to 10 either way |

**News you can trade.** When a quest outcome changes a market, the change arrives with a delay and fades (the news factor in the money section). Kill the Powder Gangers on the Primm road and ammo in Primm stays expensive for a few days while the road is still feared: a player who stocked ammo first sells high.

**Things you can do in person** (always optional, always a bonus over the paper result):

- **Clear a road**: one danger colour down for 10 game days, and +15 loyalty for the crews on it.
- **Ride along**: when a crew appears on your road you can take the first shot in an ambush; the crew remembers.
- **Close a deal face to face**: your Barter or Speech, not the trader's, sets the spread, and the town's trust rises.
- **Interview key hires**: reveals their hidden trait and adds loyalty.
- **Bluff an inspection or a raid**: Speech checks read from your own skills.
- **Carry sealed dispatches** for the Mojave Express. Johnson Nash still runs the Primm office as a sideline, so he offers the Courier what you were hired for: a sealed parcel to a named person by a deadline (Goodsprings to Mojave Outpost in 12 game hours). High pay, no ledger maths, and later relay riders can run the line slower without you. Kept slightly less profitable than trade, so it stays a treat and not the best play.

**The company feeds the adventure back**: rumours built from the ledger and quest state ("the geckos are back near the spring"), supplies from your own warehouse at 1.1 times the anchor (within the 2-crate daily limit under Money), an escort for your own trips, and a bed and a locker in every branch office.

## The terminal: screens and layout

The whole company is run from FNV terminals. Three engine facts shape every screen (details under How it is built in FNV):

1. **The body text of a terminal cannot change** while the game runs. It holds only a title and a hint.
2. **Button labels and result text can change**, up to 259 characters each, and JohnnyGuitar NVSE can redraw the open terminal. So the live numbers live in the button labels.
3. **Buttons added at run time cannot run a script.** Every action is a pre-made button in the plugin, from a pool of numbered slots that are shown, hidden and relabelled by script.

So a screen is a list of one-line rows. Each row is a button. Selecting a row either opens the next screen or does one thing.

### Layout rules

- **One row, one fact,** about 55 characters so it fits on one line. Numbers right-aligned in fixed columns.
- **Detail pages are result text:** at most 259 characters a page, so a long letter is split into pages A, B, C (the morning report in The loops at every time scale is two pages).
- **No typed numbers.** Quantities use step buttons (+1, +4, half, all) and presets. A typed text box exists in JIP NVSE and is used for naming the company and the wagons only, and naming is optional (your decision).
- **Orders queue.** A row like "Send wagon 2 to Primm with 8 water" adds to the pending list; the 06:00 tick applies it. The pending list can be cancelled row by row.
- **ASCII only:** bars `[####------]` and 8-day sparklines built from `_.-=*#`, because the terminal font has no symbols.
- **Short texts on purpose:** the terminal types text out slowly, so a page that takes more than about 3 seconds to type is too long.

### The front page

```
MOJAVE CARAVAN CO.  -  Goodsprings office     (static title)
> CASH 1,912   BILLS in 4d: 420   RUNWAY 9d   HEAT 12
> PLAN     bookkeeper's plan for tomorrow: ACCEPT
> POST     morning report, 2 letters (1 new)
> MEMOS    2 waiting, 1 due tomorrow
> ROUTES   2 wagons out, 1 home       [.-==*#**]
> PRICES   best: water GS>Primm +84 a crate
> CHAINS   purifier 92%  apothecary STARVED (herbs)
> TOWNS    Primm: 22 materials to Village
> STAFF    9 on the books, 1 unhappy (Ruth)
> CONTRACTS  2 running, NCR bid closes tomorrow
> RIVAL    Caravan cut Primm water by 5%
> ORDERS   3 pending (apply at 06:00)
> SETTINGS / AWAY MODE
```

Each row opens its screen. The front page never shows more than 13 rows, so it is readable at a glance.

### The screens

| Screen | What it shows | What you can do |
| --- | --- | --- |
| Post | morning report pages, letters, the weekly statement | read; open the memo a letter refers to |
| Memos | at most 3, each with its default and deadline | pick an answer |
| Routes and crews | each wagon: crew, cargo, where, back when, danger colour | assign route and cargo, set the stance dial, recall |
| Prices ("the Tape") | per good: price in each town, the trend, crates left before a glut | queue buy and sell orders |
| Chains | each workshop: level, throughput bar, the bottleneck input | set what it makes, accept an upgrade memo |
| Towns | level, needs met, materials to the next level, market share | sign a supply contract |
| Staff | each person: role, four numbers, traits, wage, mood | hire, fire, promote to manager, set a manager's autonomy |
| Contracts and NCR | running contracts, NCR bids, licence, duty, standing | bid, renew, pay early |
| Ledger | week P&L in short rows, loan, runway, the 8-week sparkline | pay down the loan, take a rescue loan when offered |
| Rival | aggression band, last three moves, the captain's name | counter-moves (see The Crimson Caravan) |
| Standing orders | the rules the company follows while you are away | add, edit, remove |
| The back room | hidden until the player has a contact in person | dodgy deals (see The NCR, the law and the dodgy side) |
| Settings | away mode, difficulty, typing speed, Ironman | toggle |

No screen has more than 14 slots; long lists page with "Next" and "Back" rows.

### A letter on screen

Letters use the game's flat, dry business voice: money as a number, trouble with a price tag, no heroics.

> **From: Ruth Coyle, wagon boss.** Wagon 2 is fine. The driver is fine. The brahmin are fine. Eight crates of Sloan stone are mostly fine; two are now a different shape. I need two more guards or a bigger wagon. Ask me again Monday and I will say the same thing.

That is 257 characters with the sender line: one page.

### Where the player can open it

- **The HQ terminal** in Goodsprings and **a branch terminal** in each town with a route. Every terminal opens the same company (the script reads which terminal was opened).
- **The company ledger**, an inventory item that opens the nearest office terminal from the Pip-Boy. This depends on a live test; if it fails, the runner's desk and the relay desks (see The map) keep the company within reach.
- **In the field,** the runner's message box is a small desk: the front-page numbers, memos, the cures for a served notice and "accept the bookkeeper's plan", shown when a runner finds the player (at most one a day; see The loops at every time scale).

## The late game: bets, patrons, laws and the ending

Tycoon games usually die in the late game: money piles up and stops meaning anything. Here, from tier 3 on, the score changes from caps to **commitments**: bets you must deliver, patrons you must please, and laws you must win. Money still matters, but it is no longer the only thing that does.

### Forward contracts (from tier 3)

A buyer offers to pay today's price for goods delivered later: "Mojave Outpost garrison: 20 crates of purified water at 205, delivered by day 24." Accept, and the row sits on the front page with its day count until it is filled.

- You can borrow half the ticket's value against it at once (the contract advance from Losing and coming back).
- Miss the date and you pay 25% of the value and lose trust with that buyer.
- If the bookkeeper sees you will miss it, Alice offers to buy the ticket at 70% and deliver it herself: you are out of the hole, and she is in your town.
- Never more than 3 open at once, and never a hidden deadline.

This is the bet the player feels: the spring dries, a wagon is late, and the last crate lands on the last day.

### Patrons with strings (from tier 4)

A patron gives a large sum and asks for something every week. The "strings" sit as one line on the front page.

| Patron | When | What you get | The strings | Break a string |
| --- | --- | --- | --- | --- |
| NCR quartermaster, Mojave Outpost | tier 4, NCR standing 60+ | preferred-carrier status (no tolls, first look at army bids, war-risk cover on all clean cargo) and 10,000 caps at 2% a week | heat under 20; no Legion trade; army contracts on time | status withdrawn, the loan due in 14 days, standing −30 |
| The Omertas, by letter | tier 4, after a back-room contact | a fence on the Strip that takes contraband at full price, and 8,000 caps with no interest | carry one sealed crate a week, unopened, through Primm | the next time you are on the road, their men are waiting (a real fight) |
| Mr. House's representative | tier 5, once the player has met House in the main quest | Securitron escorts on the roads into Vegas (danger two steps lower) and 20,000 caps for 20% of profit | he reads the ledger; he may veto one route a season | he sells his share to Alice |

One patron at a time is the normal case. A second from a rival faction is allowed, and then a vanilla quest can force the choice. The mod only reads vanilla reputation; it never changes it.

### Lending: you become Alice (tier 4)

Small independent outfits from the lived-in towns pool start asking the company for start-up loans. You set the terms, and the same debt ladder runs in reverse with you as the creditor: their notices, their strikes, their letters. When one fails you take its route and its wagon, the way Alice took Cass's company; or you forgive the debt and gain a loyal supplier and town trust. It is a late-game use for surplus cash, a moral choice with a price on it, and Alice notices you are playing her game (a grudge flag).

**Rules:** each outfit is one ledger line with a weekly profit roll against its instalment, and harsher terms make a miss more likely. What you recover when it fails is capped at the principal still owed, and seizing an outfit is a grudge with that town. Built in M4.

### Laws and lobbying (tier 5)

NCR contracts delivered on time and deeds done in person earn **favour**. Once a season the player can spend favour to pass or repeal one law. Alice earns and spends favour too, and at high aggression she lobbies against you. Each law is one sentence and a ledger modifier:

| Law | Effect |
| --- | --- |
| Licensed carriers only | licence fees double; small independents leave the roads (less competition, for Alice too) |
| Water ration act | purified water at the Outpost is fixed at 220 a crate |
| Road patrol levy | duty +1%; every route one danger step safer |
| Stimpak standard | only stimpaks from a level 3 clinic may be sold to the NCR |
| Outpost dry law | moonshine is illegal at the Mojave Outpost (black-market margin up, heat up) |
| Escort act | NCR war-risk cover is free for every company |
| Cap press audit | the Crimson Caravan's cap presses are inspected: Alice's cash −10% a week for a season |
| Open roads act | tolls abolished; patrols cut, so danger rises one step |

When the player commits to a side before the Dam, the regime switch (under The NCR, the law and the dodgy side) can sweep the laws away: under the Legion the NCR patron leaves and the laws lapse; under Mr. House his patron offer becomes free; in an independent Vegas there are no laws at all.

### Ending the rivalry

The deed that opens tier 5 is either beating Alice (a merger or a takeover, under The Crimson Caravan) or winning a patron (above). A player who reached tier 5 through a patron can still end the rivalry there, and most will: it is the last big story of the company.

**A takeover is three share blocks**, each bought with a deed and a price: lead Alice in Primm for 14 days and pay 5,000; win an NCR contract she bid on and pay 10,000; poach her best captain and pay 15,000. Hold all three and her board votes her out. **After a merger**, the Gun Runners and the Van Graffs become the rival, using the same move table as Alice and starting at aggression 30.

### Pressure that grows with you

So a big company is not a safe company:

- The licence rises to 3,000 per season and duty steps up at 5,000 and 20,000 caps of weekly sales.
- Each town can only absorb so much of a good before it gluts, so growth must come from new chains and towns, not more wagons on the same road.
- The rival targets whoever leads a town, and at tier 5 that is always you.
- Staff expect raises as tenure grows, and managers make mistakes when they are overloaded (see People).

### The ending: "20 years on"

The company never has to stop. When the game gives its point-of-no-return warning before the Dam, or when the player chooses "retire" at tier 5, the bookkeeper writes a closing page from the ledger: the towns fed and how big they grew, the crews lost (the roll call), how Alice ended, clean or dodgy, the patron, and the laws. Three pages of result text:

> Twenty years on, Goodsprings is a town with two streets and a water tower painted with your mark. Primm still argues about the sheriff. The Caravan sells blankets in Freeside now. Alice sends a card every year. It is not friendly.

The page is built from tags (about 150 short lines, so two endings rarely read the same), and it is the last thing the company says.

## Numbers: a worked first week and balance targets

### The first week, simulated

The money agent ran the price rules from Money as a script: one wagon (8 crates a leg), one round trip a day between Goodsprings and Primm, the player picking the best crates each morning.

**Day 0.** Loan 3,000 plus the player's own 500 = 3,500 cash. Setup costs 1,000 (wagon 400, two brahmin 300, hiring a guard 80 and a driver 70, the licence 150). Cash 2,500, debt 3,000, net worth 200.

| Day | Out to Primm | Back to Goodsprings | Day margin | Cash |
| --- | --- | --- | --- | --- |
| 1 | 8 crates, +380 | 7 crates, +366 | **+746** | 3,247 |
| 2 | 8 crates, +238 | 2 crates, +50 | +288 | 3,535 |
| 3 | 3 crates, +71 | 1 crate, +23 | +94 | 3,629 |
| 4 | 3 crates, +69 | 1 crate, +25 | +94 | 3,723 |
| 5 | 2 crates, +48 | bandits take the crate: −165 | −117 | 3,606 |
| 6 | 3 crates, +69 | 2 crates, +55 | +124 | 3,730 |
| 7 | 3 crates, +66 | 1 crate, +25 | +91 | 3,822 |

**The week's statement**

| Line | Caps |
| --- | --- |
| Sales | 8,178 |
| Cost of goods | −6,857 |
| Gross margin (after the bandit loss) | 1,321 |
| Wages: driver 10 + guard 12 a day | −154 |
| Feed: 2 brahmin × 3 a day | −42 |
| Depot rent | −70 |
| NCR duty, 2% of sales | −164 |
| Wagon wear (not cash) | −49 |
| **Operating profit** | **842** |
| Loan interest, 4% of 3,000 | −120 |
| **Net profit** | **722** |
| Principal paid (cash only) | −300 |

End of week: cash about 2,972, debt 2,700, **net worth 923**. The morning report on day 8: "Net worth record. Margin per crate fell from 61 to 24 since Monday."

**What it teaches.** Day 1 is a windfall; by day 3 the route is tired because both towns are full of what you sold them. That is the thin-market trap, by design: the memo says "add a route". A good player's week 2: a second wagon (500), the Mojave Outpost road (toll 20), the first Primm water contract, then the purifier the day tier 2 arrives. That gives net worth about 2,000 by day 14, which is earned worth about 1,500: tier 2 and the loan cleared around week 5. One tired route alone nets about 250 a week: positive, but too little to live on. That is the push to grow.

The simulation's cargo matches the starter trade (under Goods and production chains): Goodsprings' own purified water and healing powder out to Primm, Primm's salvaged ammo back. Its prices come from the economy report's launch table, which the starter table extends to all four towns. A new game starts with no sheriff in Primm (salvaged ammo at 162, not 146), which puts day 1 nearer +580 than +746, still inside the target. Milestone 1 re-runs it on the final table, the no-sheriff case first, before the loan size, the interest rate and the tier 2 gate are fixed.

### Balance targets

These are the numbers tuning must hit, checked by a scripted run of the ledger functions before any live test.

| Measure | Target |
| --- | --- |
| Day-1 profit on a fresh route | +500 to +800: new routes pay |
| One tired route, net | about +250 a week: positive but not enough |
| Loan repaid | week 5 for a good player, week 8 for a careful one |
| Tier times | tier 2 by day 14, tier 3 by week 4, tier 4 by week 7, tier 5 around week 11 |
| Worst single event at tier 1 | never more than 3 days of runway (the director's loss limit) |
| Contract share of income at tier 3 | 30 to 50%: contracts pay the wages |
| Dodgy against clean | +35% profit at heat 30 to 40; break-even by heat 70 |
| Losing | losing comes from overreaching (wagons and workshops bought on thin cash, then a bad week; or the dodgy side); a passive player stalls at tier 2 rather than going broke; any loss gives 7 or more days of warnings |
| Real raids | at most one in 28 days |
| Visit length | 5 minutes at tier 1, under 10 at tier 5 |

### Core numbers at a glance

| Number | Scale | Goes up with | Goes down with | Starts at |
| --- | --- | --- | --- | --- |
| Town trust (one per town) | 0 to 100: Wary under 25, Accepted 25, Liked 50, Trusted 75 | each on-time delivery +1, a contract completed +3, a deed done there +10, a famous crew | a missed delivery −3, a raid in town −10, gouging in a shortage −2 a day | 20 (Goodsprings 35) |
| NCR standing | 0 to 100 | an NCR contract +4, duty and licence paid on time +1 a week | heat over 40 −1 a day, Legion trade, a raid −15 | 30 |
| Favour (tier 5) | points | each NCR contract on time +1, each deed +2 | a law costs 3 to 6 | 0 |
| Heat | 0 to 100 | dodgy actions, net +3 a day at most | 2 a day, 4 after 7 clean days, a fixer, fines | 0 (20 with the Powder Ganger landlord) |
| Market share | % per town and good | your deliveries (spot and contracts) as a share of the town's weekly use | the rival's and the town's own supply | 0 |
| Earned worth | caps | profit | losses; dividends beyond paid-in capital | −300 (net worth 200 less the 500 you put in) |
| Strikes | 0 to 3 | a missed bill day, once served | each falls off after 56 days | 0 |
| Workshop capacity | output crates a day | level 1: 4, level 2: 8, level 3: 16 | starvation drops a level | — |
| Raw sites (well rig, forager hut, field, corral, sand pit, scrap yard, quarry crew) | 200 caps and one hand each | 4 crates a day, levelling like workshops | starvation of hands or tools | — |

Building materials are sold to towns like any other good. A town's growth project buys materials at the anchor price (150), at most 4 crates a day, so delivering them pays steadily and grows the town but cannot be farmed at shortage prices.

## How it is built in FNV

The whole company is a simulation on paper (quest variables and arrays) with a terminal front end and a few placed objects. Almost nothing needs real NPCs walking the Mojave, which is what makes it buildable and stable.

**Needs:** xNVSE, JIP LN NVSE (menu events, message boxes) and JohnnyGuitar NVSE (changing and redrawing terminal text). Without JohnnyGuitar the terminal would show no live numbers, so it is a hard requirement (your decision).

### Scripts

| Part | Job | Runs |
| --- | --- | --- |
| CCCore (quest) | the day tick: compares GameDaysPassed with the last day run, runs the missed days one by one, weekly bills on day 7, tier checks; holds the critical numbers | every 15 seconds |
| CCLedger (functions) | the maths only: prices, demand, route profit, wages, interest, event rolls; no side effects, so it can be tested from the console | called by CCCore |
| CCTerm (quest) | the terminal bridge: reads the button the player picked, queues or applies the order, rewrites the labels, redraws | while a company terminal is open |
| CCWorld (quest) | near-player work: spawning and removing road crews, switching tier objects on | every 3 seconds, only when needed |
| CCEvents (functions) | on every load: re-register the handlers, rewrite the terminal texts, re-apply tier objects | on load |

### Saving the company

- **Critical numbers in quest variables** (saved in the normal save): cash, loan, week, last day, heat, tier, licence, strikes. About 20 values.
- **Detail in xNVSE arrays** (saved in the cosave): towns, routes, staff, a 60-day ledger history, the memo queue. If the cosave is lost, the company is rebuilt from the critical numbers with default detail, and the bookkeeper says so in a letter.
- **Terminal text is not saved by the game**, so it is rewritten after every load.

### The day tick

Every 15 seconds CCCore checks the day. Rules: the day only moves forward (a guard against the known GameDaysPassed glitches); a long absence runs at most 14 missed days at once and folds anything older into one summary step, so a month in the Divide does not freeze the game for seconds; the order queue is applied first, then the day runs.

**Rolls are seeded.** Every random roll uses a stored company seed plus the day plus the route or event id, so reloading a save and waiting again gives the same result unless the orders changed. **The busy shield** is a check before each day step: is the player's current cell or worldspace one of the DLC lands (a form list of the DLC worldspaces and interior cells, or the source plugin of the player's cell)? It does not use GetInWorldspace, which is false in every interior. It covers a DLC's lands only until that DLC's main quest is done. While the shield is up, the debt and law clocks do not advance, no runner serves a notice, and paper losses are capped at one day's profit. Company terminals, which only exist in the Mojave, can always serve.

### Terminals

- About 14 terminal forms: the front page and one per screen. Each has a pool of up to 14 pre-made buttons (the front page uses 13); each button's script stores which slot was picked; its condition shows or hides it; its label is rewritten by script.
- JIP's menu-open event for the Computers menu (1057) runs when any company terminal opens; JIP's GetMenuTargetRef says which one, so every branch terminal shares the same forms.
- Field letters use a JIP/xNVSE message box with buttons (to confirm in a live test). They wait while the player is in combat, dialogue or a menu.

### The world

- **New interiors** for the HQ and branch offices; one new door in each town's exterior (your decision). No vanilla record or reference is edited.
- **Growth you can see:** for each town and tier, one marker that switches on its signs, crates, stalls and lamps.
- **Road crews:** the hires are persistent characters, disabled at home while their wagon is out on paper. When the player comes near the route, the real crew is moved to the road with MoveTo, and only brahmin and spare guards are spawned and removed later. Named crew are protected from death during a real fight. The company never relies on NPCs travelling while unloaded, because that is unproven.
- **Raids:** real NCR officers at the office if the player is in the cell; otherwise on paper. The first raid is real whenever the player reaches an office within the warrant's 7 days (see The NCR, the law and the dodgy side).
- **Vanilla quests and people are read, never written:** quest stages are checked with GetStageDone; no SetStage on a vanilla quest; vanilla reputation is never changed. Alice's offer comes from her agent (a new character at the Prospector Saloon) as a letter of credit, and Alice herself speaks through a new dialogue topic on a mod quest, so her own dialogue is untouched; if she is dead, Jason Tagg's office makes it.

### What is proven and what needs a live test

| Feature | How | Status |
| --- | --- | --- |
| Live button labels and result text | JohnnyGuitar SetTerminalMenuItemText | proven live (M0 test 0.4) |
| Redraw while open | JohnnyGuitar RefreshTerminalMenu | proven live (M0 test 0.4) |
| Body text with numbers | impossible by script | proven impossible; designed around |
| Actions from the terminal | pre-made buttons with scripts and conditions | vanilla feature |
| Know which button was clicked | the engine sets flag 4 on the clicked row; the script polls and clears it | proven live (M0 test 0.5) |
| Know which terminal is open | JIP GetMenuTargetRef 1057 | in the source |
| Open a terminal from an item | a script activates the terminal (Activate player 1) | from a script: proven; from a Pip-Boy item: not proven, so the ledger opens at desks (M0 test 0.6) |
| Day tick with catch-up | GameDaysPassed compare | proven live (M0 test 0.9) |
| Arrays survive saving | xNVSE cosave | documented; mirrored for safety |
| Tier objects | enable-parent markers | vanilla feature |
| Road crews near the player | MoveTo for the hired crew, PlaceAtMe for brahmin, plus an AI package | proven: no save growth over 20 cycles (M0 test 0.11) |
| NPCs travelling while unloaded | vanilla travel packages | not verified: not used |

### The first live tests, in order

1. **Terminal text round trip:** set a label, open the terminal, change it while open and redraw; check the scroll position, and that the edit is gone after a reload (it should be, which is why CCEvents rewrites it).
2. **Open a terminal by script** from a console and from an item used in the Pip-Boy.
3. **Menu event timing:** does the open event run before the first draw, so the new labels show at once?
4. **Limits:** 30 buttons and 259-character texts on one screen: scrolling, typing time, skipping.
5. **Road crews:** move a 3-person hired crew to a road marker and back, spawn and remove brahmin, and check for leftovers and save growth.

In the same session: a tick test (wait 5 days: exactly 5 day steps), a field-letter message box test, and adding the mod to an old save. The fnv-mcp tools (fnv\_test, fnv\_spec) can drive all of these in the real game.

## Build order

Five milestones. Each one is playable on its own and could go to Nexus as a beta, so the mod is never months from a release.

| Milestone | What it adds | Tiers | Done when |
| --- | --- | --- | --- |
| M0 Proofs | the five live tests, the tick test, the field-letter test, the old-save test | none | every "needs a live test" row under How it is built in FNV has an answer |
| M1 One road | Goodsprings HQ, Primm branch, one wagon, Alice's loan (and the Tagg fallback), the starter trade, the price board and the bookkeeper's plan, morning report, memos, weekly bills, the debt ladder with strikes and the busy shield, seeded bandit events only, 3 standing orders, the purifier and apothecary, basic hiring, one contract type | 1 and 2 | a tester plays two game weeks, can read every number, and survives or loses for reasons they can name |
| M2 Chains and people | smokehouse, stone yard, Primm salvage; town levels; staff numbers and traits; managers; more contract types; tier perks; Sloan and the Mojave Outpost; relay desks at the 188 and Novac | 2 and 3 | tier 3 in about 4 game weeks; a tier 3 visit under 8 minutes |
| M3 Rival and law | the Crimson Caravan's AI, NCR licence, duty and bids, heat, raids, the back room, insurance, forward contracts and road crews | 3 and 4 | both a clean and a dodgy company reach tier 4; never more than one raid in 28 days |
| M4 The ending | patrons, laws, ending the rivalry (three share blocks), the regimes at the faction commitment, lending, the successor chapter, the epilogue, the bookkeeper's phrase library (about 150 lines) | 4 and 5 | a full run ends on a "20 years on" page |
| Later | Novac, Freeside, the Strip gate; more of the lived-in towns pool |  |  |

**How tuning is done.** The ledger maths lives in CCLedger functions with no side effects, so a debug command can run them for 100 simulated days with a scripted player and write the results to a file. fnv-mcp drives that run in the real game; the balance targets under Numbers are the pass marks. No balance number in this doc is final until that run agrees.

## Risks and open questions

### Risks

| Risk | Why it matters | What the design does |
| --- | --- | --- |
| The terminal feels slow | text types out slowly; 259 characters a text | one-line rows, short pages, a typing-speed setting; limits tested first in M0 |
| It turns into a spreadsheet chore | the classic tycoon failure | letters and defaults instead of a dashboard; managers take over routine; visit-length targets; any screen nobody uses is cut |
| Thin markets feel punishing | day 3 of a route is dull | contracts, new routes and the memo that says so; tuned against the targets |
| The player ignores the company for weeks | they are playing Fallout | cautious defaults, away mode, the while-you-were-away letter; nothing is seized without a served notice |
| The late game snowballs | money stops mattering | commitments (bets, patrons, laws) and pressure that grows with you |
| One bad week spirals into a loss | unfair failure | the anti-spiral rules, rescue lenders and the successor chapter |
| A vanilla quest gate is never done | the player skipped or failed it | every deed has a slower way round (below) |
| The cosave is lost | the detail is gone | critical numbers mirrored in quest variables; rebuild with a letter |
| Mod conflicts in Goodsprings and Primm | many mods edit these towns | new interiors, one door per town, switchable markers, no edits to vanilla records |
| Alice dies, or is killed mid-run | she is the rival's face | the Tagg fallback at the start; later, her named captain takes over the Caravan's ledger |
| Scope is too big for one modder | the feature list is long | milestones that ship alone; M1 is small on purpose |
| Script load | a 15-second tick and arrays | the ledger runs once a game day; profile with fnv-mcp before each release |
| Save-scumming the tick | FNV autosaves on wait and sleep, so a lost wagon can be rerolled | seeded rolls: a reload gives the same result unless the orders changed |
| A full wallet makes losing optional | FNV players carry 10,000+ caps by midgame | owner funds never pay bills or count toward a tier; one owner rescue a season; a third strike opens a 7-day takeover notice that only operating cash can cure |
| A DLC runs the debt clock out | Dead Money cannot be left for many game days | the busy shield freezes every clock in a DLC's lands until that DLC's main quest is done |

**Every deed has a slower way round** (my rule, to stop a vanilla quest locking a tier):

- Goodsprings safe: or the Powder Ganger landlord variant (under Growth).
- Primm has a sheriff: or pay for the company's own Primm guard post (1,500 caps and 14 days of Primm deliveries at 80%).
- Quarry Junction cleared (for stone): or hire a hunting party (2,500 caps, a risky event that can kill crew).
- An NCR contract in person, beating Alice or a patron: already open to every player.

A deed already done before the mod was installed counts at once; the deed ledger fills in on the first day.

### Your decisions

You answered all 15 on 26 November 2026. Every pick below stands except 15: you turned down riding the wagon, so it is out of the design.

| # | Question | Answer |
| --- | --- | --- |
| 1 | After losing: a successor chapter, or the company is gone for good? | successor chapter; "gone" as the Ironman setting |
| 2 | Goods: FNV items plus the new building materials, or FNV items only? | FNV items plus building materials |
| 3 | One mod, or a lived-in towns core with the company as an add-on? | towns core plus company add-on (each useful alone) |
| 4 | Road crews spawned near the player only, for the moments you meet a wagon? | yes |
| 5 | JohnnyGuitar NVSE as a hard requirement? | yes: without it there are no live numbers |
| 6 | Is the first raid always played for real? | yes |
| 7 | Can named crew die for good? | yes, rarely, with injuries far more common, and a roll call |
| 8 | Contraband: Powder Ganger powder and unlicensed moonshine only, or chems and stolen NCR gear too? | powder and moonshine at launch |
| 9 | Founding story: Alice's loan, a Mojave Express franchise from Johnson Nash, or let the player pick? | Alice's loan; the franchise as a later option |
| 10 | A typed text box for naming the company and the wagons? | yes, optional |
| 11 | One new door in each town's exterior cell? | yes |
| 12 | Legion and House regimes at launch, or NCR rules only? | NCR rules at launch; the regimes in M4, switched when the player commits to a side (vanilla ends at the Dam) |
| 13 | Owner money in its own pot: it buys wagons and buildings, never pays bills (except one owner rescue a season after a miss) and never counts toward a tier? | yes: otherwise a full FNV wallet makes losing optional |
| 14 | Tier perks that change how you play Fallout (company prices for your loot, a remote stash, discounts, map markers, a company guard)? | yes |
| 15 | Ride the wagon: travel with your own wagon like fast travel, dropped into the road's event if one was placed? | no: turned down, out of the design |

## Critic log

An Opus agent, briefed as an expert game designer, reviewed the whole doc against the brief and the research. Its approval was the bar for calling the doc done. Full reviews: `research\swarm\CRITIC-ROUND-N.md`.

### Round 1: rejected (3 blocking issues, 16 others)

| Blocking issue | What changed |
| --- | --- |
| Tier 1 had nothing to trade: every good a town wanted came from a tier 2+ workshop, and the week-1 numbers rested on trade that no longer existed | The starter trade table (each town makes and uses a little of everything); the week-1 simulation now matches it; M1 includes the purifier, apothecary, hiring and one contract type |
| The player's own caps were a bottomless bailout and could buy tiers, so losing was optional | Paid-in capital and earned worth; one owner rescue a season while a loan runs; three strikes end the company whoever pays |
| A DLC (Dead Money) could run the whole debt ladder out while the player could not act | The busy shield freezes every clock outside the Mojave and during DLC main quests; nothing is served automatically; every cure is on the runner's message box |

The 16 others, all taken: road risk made one system (the director places events, one loss cap of 25% of gross assets, insurance priced from each route's expected loss); seeded rolls against save-scumming; away mode now has a cost; the bookkeeper's plan as a one-press default for daily orders; relay desks at the 188 and Novac plus the runner's desk for the northern game; Alice's agent at the Prospector Saloon; the regime switch moved to the faction commitment and the epilogue to the point-of-no-return warning, because vanilla ends at the Dam; level 2 workshops for caps only and salvaged materials at Primm; a tier 1 dodgy job and the bigger contraband held for after launch; raids need a served warrant and happen at the next office; heat gain capped; contract volume capped; a core numbers table; a consistency pass (decrees every 28 days, wages quoted per day and paid weekly, supply contracts vs standing orders, Ironman, tier 2 by day 14); hired crews are persistent characters moved to the road; crates are fixed vanilla bundles; the takeover's three share blocks, the merger's new rival, the successor's house terminal, and patrons that give abilities as well as cash.

Both of the critic's bold ideas were adopted: **ride the wagon** and **tier perks** that change how you play Fallout (under Growth). You later turned down riding the wagon (decision 15), so it is out of the design.

### Round 2

Rejected, 2 blocking issues, 12 others. The starter trade was confirmed sound (all 34 resting prices re-derived from the formula).

| Blocking issue | What changed |
| --- | --- |
| The wallet still bought immunity and tiers: buying your own goods the day before a bill paid it, and that margin counted as earned worth; after the loan, top-ups prevented every strike | Two cash pots: only operating cash pays bills, stock and wages; owner funds (top-ups and the margin on sales to you) buy only wagons and buildings; sales to the player capped at 2 crates a day |
| Bills deferred during a DLC were served together as three strikes and an instant takeover | One absence is one notice and one strike; a strike's 56 days count from the serve; a third strike opens a 7-day takeover notice that owner money cannot cure |

The 12 others, all taken: the busy shield judges DLC lands by where the player's cell comes from (GetInWorldspace is false in every interior); the sealed-crate job is 50 caps, once every 3 days; growth projects pay the anchor price, capped per day; a raid sets heat to 50 and blocks a new warrant for 7 days; insurance priced from expected payout; one number for Primm's lawless ammo, and the week-1 caveat updated; the tier 1 terminal is at the agent's table in the Prospector Saloon; town supply contracts open at tier 1, NCR bids at tier 4; the loot perk covers trade goods only; 14 button slots per screen; away mode counts from leaving an office; riding the wagon joins the 06:00 departure.

The critic's bold idea was adopted: **lending, you become Alice** (under The late game).

### Round 3

**Approved.** No blocking issues. The critic checked every way owner money could reach a bill and found none open, and found the strike and raid timings fair (at least about 10 days between the two raids that revoke a licence).

Its 7 non-blocking points were all taken before hand-over: the busy shield covers a DLC's lands only until that DLC's main quest is done (so the Sink cannot shield a company forever); a trial NCR contract at tier 3 so the tier 4 deed is reachable; operating cash includes loans and advances, and the takeover notice replaces the ladder for that miss; the heat table and the first-raid rule follow the warrant rule; the sealed-crate job carries a search risk; lending has rules and sits in M4; and the Crimson Caravan's own share per town is given. Its last bold idea, **Cassidy Caravans, reborn**, was adopted too (under The Crimson Caravan).

## Sources

**The research behind this doc** (nine agent reports, each with its own source list and evidence tags), in `research/swarm/`: 01 economy, 02 chains, 03 risk and failure, 04 rival and law, 05 people, 06 RPG business lessons, 07 FNV tech, 08 FNV world and lore, 09 wildcard ideas, and the shared brief BRIEF.md. The earlier NPC catalogue is in the folder above it.

**Game data:** FalloutNV.esm records (quests, NPCs, factions, terminals, notes) read through the fnv-mcp tools, and the decompiled engine for the terminal and description code.

**Engine extensions (source code read):**

- JohnnyGuitar NVSE, terminal functions: https://github.com/carxt/JohnnyGuitarNVSE
- JIP LN NVSE (menu events, text input, file writing): https://github.com/jazzisparis/JIP-LN-NVSE
- xNVSE (arrays, events, menu IDs): https://github.com/xNVSE/NVSE

**Lore** (fallout.wiki): Alice McLafferty, Crimson Caravan Company, Cassidy Caravans, Mojave Express, Johnson Nash, Goodsprings, Primm, Sloan, Quarry Junction, Mojave Outpost, NCR Correctional Facility, Nipton, Novac, NCR dollar, Caps, Heartache by the Number. Example: https://fallout.wiki/wiki/Crimson\_Caravan\_Company

**Design references:**

- Production chains and town growth: Transport Fever 2 manual (https://www.transportfever2.com/wiki/doku.php?id=gamemanual:industriescargos), Foundation resources, Railroad Tycoon, Offworld Trading Company.
- Markets and trading: Dope Wars, Recettear, Schedule I.
- Failure and coming back: Darkest Dungeon, Rogue Legacy, Hades, FTL, Sunless Sea, This War of Mine, Frostpunk.
- Pacing and events: RimWorld (raid points, mood), Left 4 Dead's director, Into the Breach (telegraphed threats), XCOM.
- Business inside an RPG: Assassin's Creed Brotherhood, Dragon Age Inquisition's war table, Metal Gear Solid Peace Walker, Yakuza 0, Mafia III, Mount and Blade II caravans, Shadow of Mordor's nemesis system.
- Idle and away play: Clicker Heroes offline progression, idle game design notes.

The full URL lists are in each report's last section.

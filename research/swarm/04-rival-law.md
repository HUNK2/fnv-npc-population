# 04 - The Rival, the Government, the Dodgy Side

Angle: Crimson Caravan as an AI rival with memory; the NCR as a government; smuggling, heat and raids.
Tags: [D] documented by a source I opened, [O] opinion, [K] my own knowledge, not opened this session (treat as unverified),
[G] read from FalloutNV.esm with fnv_record (read-only).

Source honesty: fandom.com and several wikis refused automated fetches (HTTP 402/404). I opened Wikipedia pages
(Offworld, Mafia III, Dope Wars, Papers Please, Yakuza 0), the GameBanshee quest guide, and read the game's own notes.
The Nemesis, Schedule I and Capitalism Lab/OpenTTD AI points come from search snippets or memory and are flagged.

## 1. Key findings

### 1.1 What the game says about the Crimson Caravan [G]
Records in FalloutNV.esm give real lore that we can quote and build on:
- `CrimsonCaravanNote04` "War Effort": McCarran asked for more frequent supply runs to the NCR's outlying outposts; Alice
  negotiated "additional terms in our favor" but may "lower our hiring standards"; caravaneers are held by **work contracts**
  ("were it not for the work contracts, some would have run off"). So the CC is already the NCR's military supplier and
  its labour is bound, a poaching target.
- `CrimsonCaravanNote03` "Gun Runner Tariff" (from Jason Tagg, Modoc branch manager): Alice pushed a tariff on Gun Runner
  weapons that "didn't make it past the Senate"; Gun Runners "have too much pull in California". The CC uses **lobbying**
  as a weapon and sometimes loses.
- `CrimsonCaravanNote01` "New Canaan Branch Proposal": Mormon taxes put CC "at a severe disadvantage to their own caravans";
  plan: "overwhelm them with a flood of cheap NCR goods", favours from "contacts back in California". **This is the exact
  price-war pattern we want**: dump cheap goods into a town to starve the local seller.
- `GunRunnerNote02` "Crimson Caravan Reparations": Gun Runners plan to "pull some strings at McCarran" to bar CC staff from buying
  ammo. Government access (McCarran/NCR purchasing) is contested between companies.
- `CrimsonCaravanNote02` "Re: Henry Jamison": CC "encourages" a branch manager to resign; irritation at a frontier branch.
- Also in the esm: Blake (`CrimsonCaravanBlake`), generic Caravaneers and Crimson Caravan Guards (several variants), a
  Brahmin (`CrimsonCaravanBrahmin`), a leveled caravaneer list, a safe + key. Alice's own record name not shown in the
  first 40 search results (search was capped); look it up by name before building.

### 1.2 Heartache by the Number (do not break it) [D]
Source: https://www.gamebanshee.com/falloutnewvegas/walkthrough/heartachebythenumber.php
- Cass starts it at Mojave Outpost; Alice's quest "You Can Depend on Me" is to buy Cass's company for CC (persuade with Barter
  50/75 costing 750 caps or 12 Whiskey, or free Speech 50/75).
- Evidence is in two safes (Silver Rush back room, CC main office). Handing it to Ranger Jackson: nobody is arrested, Van Graffs
  turn hostile, **"the Crimson Caravan takes no notice, so McLafferty's quests remain available."**
- Option 2: kill Gloria Van Graff and Alice McLafferty (sneak attack works).
Implications: vanilla treats CC as untouchable and Alice as a quest-giver with scripted state. Our mod must (a) never alter
those quest variables, (b) put our own "Alice" behaviour behind a separate set of globals, (c) handle **Alice dead** and
**Cass sold / not sold** states as inputs. If Alice is dead, CC is run by a successor (our invention: "Jason Tagg moves from Modoc
to take the New Vegas desk" - Tagg is a real name in a note, nice continuity).

### 1.3 Other games [mixed]
- **Offworld Trading Company** [D, Wikipedia: https://en.wikipedia.org/wiki/Offworld_Trading_Company]: black market buys raise their own price,
  which warns opponents, who often answer with a goon squad that protects one structure from most sabotage and can steal the
  sabotage. Hostile takeover by majority stock; "you're warned when a rival has enough money to buy you out, but the rival isn't
  alerted" -> tense cash races. Lesson: visible escalating price on dirty tricks + a warning before takeover.
- **Mafia III** [D, https://en.wikipedia.org/wiki/Mafia_III]: you overrun a location, assign one of your lieutenants to run the area;
  allies "slowly come to respect his skill"; neglected ones abandon you and you must eliminate them. Lesson: a fixer/lieutenant
  with loyalty that needs feeding.
- **Dope Wars / Drug Wars** [D, https://en.wikipedia.org/wiki/Dope_Wars]: 30 days, 100 coat spaces, $2,000 start, loan shark with fast
  repayment or you lose, random events (muggings, price spikes, finds), Officer Hardass chooses between arrest / run / fight /
  keep dealing, each choice risks injury. Lesson: **police encounters as a short gamble with 3 options**; our raid should offer
  the same trio (fight, bribe, surrender).
- **Papers, Please** [D, https://en.wikipedia.org/wiki/Papers,_Please]: citations reduce that day's pay; bribes add income but risk
  discovery and imprisonment; **rules change every day and get harder as relations with neighbours worsen**; debt ends the game.
  Lesson: the NCR rulebook as a changing list shown in the morning report, penalties as pay deductions first, then prison.
- **Nemesis system** [snippet only, https://gamesradar.com/shadow-mordor-nemesis-system-amazing-how-works - page body did not
  load; summary from search results]: captains are promoted by killing the player or each other; they gain levels and abilities
  when the system "takes a turn"; they can learn to counter the player's style after several encounters; state updates when you
  die or leave. [K] Also: they taunt you with what happened last time, and have fears and strengths you learn through intel.
  Lesson: memory must be **spoken back** to the player; a rival who remembers but never says so feels like a stat.
- **Schedule I** [O, search snippets only; fan guides conflict]: heat builds with visibility and behaviour; a bribe option exists at
  low heat (1-2 stars, one officer); curfew increases patrols; getting caught takes illegal items and fines you rather than ending
  the game. Lesson: caught = lose the goods + pay a fine, not game over (matches our "asset not company" rule). Numbers unverified.
- **Yakuza 0** [D partly, https://en.wikipedia.org/wiki/Yakuza_0]: the side businesses are praised ("addictive", "best part") and
  teach the player by missions that speed up the business. I could not open a source on the Five Billionaires rival mechanics, so
  I only use [K]: each property rival has a face, a boss fight and a taunting dialogue; beating the rival is a milestone.
- **Capitalism Lab, OpenTTD AI companies, Railroad Tycoon, Big Ambitions**: not opened this session. [K] The relevant pattern in all:
  AI rivals follow the same economy rules as the player (they pay wages, hit cash limits) so they can be out-played; they open
  a new route where you profit. The research file BUSINESS-RESEARCH.md section 1 already covers their lose conditions.
- **Empire of Sin, Payday heat, GTA wanted level, Watch Dogs**: not opened; used only as [K] patterns (staged star thresholds;
  heat decays when you lie low; informants).

### 1.4 NCR money and law in FNV
- [snippet, https://fallout.fandom.com/wiki/NCR_dollar via search] NCR dollar is about 40% of a water-backed cap by 2281, ~10% of a
  Legion denarius; caps, NCR dollars and Legion money are all accepted by caravan companies and on the Strip. Use this exchange
  rate for the tax and licence **paid in NCR dollars** (0.4 cap each) vs caps. Water backing: [K], not confirmed here.
- [K] NCR present at Mojave Outpost (Rangers, Jackson), Primm (NCR troopers at Primm Slim/Bison Steve area after the sheriff
  question), NCR Correctional Facility (Powder Gangers), McCarran, Camp Golf etc. Powder Gangers produce explosives powder.
  Omertas run the Gomorrah; Kings are Freeside's protectors; Van Graffs run Silver Rush, a weapons maker/seller allied with CC.
  These are all well-known vanilla facts; verify exact placements in the CK record when building.

## 2. Proposals

### 2A. Crimson Caravan as an AI rival ("Alice's Ledger")

**Principle**: the CC is not an abstract score. It is **Alice McLafferty plus four named managers** playing the same
rules as the player on the same ledger, each town having a CC "share". It plays one move per game day and each move is
chosen from a small table, so it is predictable enough to counter and different enough to surprise.

**What it watches (once per game day, at midnight tick)**
1. Market share per town: ours vs CC (percent of the town's weekly demand served).
2. Our margin on each route: price sold minus cost, from the public ledger (CC sees a route's margin only above a
   **visibility** threshold: route profit >= 120 caps/day or town share >= 25%).
3. Our headcount in each town and our wages vs CC wages.
4. Our contracts with NCR and our NCR standing (CC covets those).
5. Our heat (see 2C). If heat >= 40, CC knows something.
6. Our cash trend (if cash < 2 weeks of wages, **buyout window** opens).

**Its response table** (each day roll once; Aggression A = 0..100, see below)
| Trigger | Move | Effect (numbers) | Visible as |
|---|---|---|---|
| Our share in a town >= 25% and rising 3 days | **Price war** | CC sells our top 2 goods in that town at -15% for 5 days (cost to CC: 3 x town demand x 0.15 x price from its own fund). Our margin there drops by the same, our share loses ~1.5 points per day. | Morning report memo; CC stall sign changes to "Crimson Caravan - Lowest Prices in the Mojave" posters; extra CC caravaneer idles at the town square. |
| Our wages < CC wages by 10%+ | **Poach** | Takes one staff (lowest-loyalty first, rank-1 or 2 only) per week, offering +20% wage. If staff has loyalty >= 70 they refuse and a note says so. | Staff NPC replaced; CC guard stands with them in a town; message "Mara took a Crimson Caravan contract". |
| Our supplier has one customer (us) | **Buy out supplier** | CC pays supplier 130% for exclusivity. Our input cost for that good rises 25% unless we sign an exclusive contract (below). | Supplier NPC wears CC patch; shop prices change. |
| A contract (NCR, town) we hold has renewal in 7 days | **Undercut bid** | Bids 8% lower on NCR contract. | Memo with the two bids. |
| Heat >= 60 | **Tip off the NCR** (see 2B) | Adds +15 heat, once per 10 days. Needs CC to have evidence (our contraband trade volume) and Alice's grudge >= 40. | Rangers show up with "an anonymous letter". |
| A = high and relationship = enemy | **Sabotage** | Brahmin stampede, cargo spoilage in a warehouse (-20% stock) or burned wagon. Costs CC 150 caps. Every attempt leaves **evidence points**; 3 evidence = a note we can use in the NCR (below). | Fire at a warehouse; dead brahmin; Van Graff men seen near the route. |
| Our cash < 14 days of wages and we owe the CC loan | **Buyout offer** | Offers 2.5x last month's profit. Refusing costs nothing; accepting ends the company with the bonus: keep 50% of cash and become **a CC branch manager** (a way out of a lost game, see 4). | Alice's letter; a terminal message. |
| Our share in a town < 5% | **Ignore** | Saves the CC a move. | None. Note the player can use this: be small and unprofitable and it leaves you alone. |
| Stalemate | **Open a branch** | Builds CC stall in a town we do not serve. | CC wagon arrives. |

**Aggression A**: starts at 20 (Alice is friendly; she gave you the loan). Each day: +1 per 10% of town share we hold over
CC; +5 when we beat a CC bid; +10 when we are caught sabotaging; -10 when we pay a protective tribute to CC; -20 when Alice is a
partner. A < 30: only price signals and bids; 30-60: poaching and supplier buyout; 60-80: sabotage; > 80: war (full). Max once a
move per town per 2 days, to keep the report to 1-3 items.

**How the player fights back**
- **Undercut**: match -15% for 5 days costs us about (town daily demand x price x 0.15 x 5). Works if our cost is lower via production chains.
  Fun: the first time you win a price war with a workshop chain (e.g. Primm smokehouse) is a memorable moment.
- **Exclusive contracts**: offer a supplier 120% price for 30 days exclusive (cost +20%); blocks CC buyout for 30 days.
- **Sabotage of their own**: terminal option "Hire Eddie's boys" cost 120 caps, 40% chance of success, success: CC loses a wagon (800 caps value);
  failure: +20 heat on us and +15 Aggression. Needs the fixer manager (2C).
- **Take contracts in person**: finishing the NCR bid contract by hand (escort run, clearing the road) gives a +12 Standing bonus
  and denies the CC bid. This is the "adventurer feeds the company" rule.
- **Poach back**: CC staff with loyalty <= 40 can be hired for +15%, with a conversation (Speech 40, or Barter).
- **Expose**: evidence points from sabotage (3 points) can be delivered to Ranger Jackson (vanilla NPC at Mojave Outpost):
  CC pays a 500-cap NCR fine and loses its next NCR bid (once per 30 days). It does not harm the quest state.
- **Alice partner** (late deed): at tier 4 (Trading house) with market share >= 40% in three towns, and Cass's quest not in the
  "Alice dead" state, Alice offers a **Merger**: A resets to 0, we share routes, the CC takes 25% of profits, no more rivalry; the rival role is
  taken by the Gun Runners / Van Graffs (a plausible replacement, with a "Silver Rush" consortium). Fun: a way to retire the main
  antagonist, with a consequence.

**Nemesis-like memory ("Alice remembers")**
A ledger of **grudge flags**, each a bit + a counter, spoken back in dialogue and terminal notes:
`robbed_cc_caravan`, `killed_cc_guard`, `exposed_cc` (Heartache option 1), `killed_alice` (inherited from vanilla), `poached_staff`,
`won_price_war_n`, `sold_to_cc`, `refused_buyout_n`, `paid_loan_early`, `defaulted_late_n`.
Rules:
- Each flag changes Alice's/Tagg's letters (templates with the flag's name: "I note you still owe me for Mara, Courier").
- Flags change numbers: `exposed_cc` adds +15 to starting A and removes the "loan" friendliness; `paid_loan_early` gives -15.
- Every 5 grudges promote **a CC captain** (Nemesis style): a named caravaneer (Blake? an invented "Dutch Riker") who leads CC guards and shows up on
  the road to harass our caravans; he learns: after 3 fights vs our player he carries counter gear (higher DT). He can be killed in the
  field to clear a route (a named boss), which gives a visible victory and a loot item.
- Letters in the morning report: one line of voice, e.g. "Alice McLafferty: Our offer for your Primm stall stands. Do think about it."

**Shown in the world**: CC wagons in towns, CC stall banners (a swapped sign model in the Primm/Outpost stand), new CC guards on
roads (existing NPC records, so no new assets), posters. In the report: a "Rival" line with CC share per town (for 3 towns).
**Build difficulty**: low (numbers only: ledger and table) to medium (captain on the road: a few placed/spawned actors tied to the company's activity).

### 2B. The NCR as government ("the Rangers and the Rulebook")

**Instruments** (in the terminal, a menu "NCR Office" at Mojave Outpost or Primm; the NCR has a Licence Clerk)
1. **Trade licence**: you cannot run caravans between NCR-controlled settlements without one.
   - Peddler tier: free. Outfit: 100 NCR$ (250 caps) per season (28 game days). Caravan company: 400 NCR$. Trading house: 1,000 NCR$. Mojave concern:
     2,500 NCR$ (price scales by number of routes: +30 NCR$ per active route).
   - Missing a payment: warning at day 1, caravans in NCR land stopped at day 8 (they are "held at the outpost", an asset hold, not seizure).
2. **Tax**: 8% of declared revenue paid weekly (NCR dollars; tariff on imports 5% on goods tagged "foreign": Legion-made, Van Graff?). Declaring less is
   **under-declaring** and adds heat (+2 per 10% hidden per week).
3. **Tolls**: road tolls at Mojave Outpost and a Primm check point; 5 caps per wagon unless you hold a licence of tier 2+ (free).
4. **Supply contracts with bids**: each week the NCR posts 1-3 contracts (e.g. "300 rounds 5.56, Outpost, 10 days, 14 caps/round"). Your bid (a number)
   competes with the CC and the Gun Runners. Winner: lowest price among bidders whose reliability >= 60. Reliability = deliveries on time / 10 last.
   Reward: +5 NCR standing, 1.3x market price, 10-day payment delay (cash flow risk!).
5. **Inspections**: random, 1 per 10 days at HQ if heat >= 20, otherwise 1 per 30. Checks (a) licence valid, (b) ledger match
   (declared vs actual stock, you are asked with 2 menu options), (c) guards licensed. Penalties: fine 5% of weekly revenue per violation (one violation = warning first time).
6. **Patrols**: each NCR-patrolled route (Goodsprings-Primm-Outpost) has danger -30% for a fee? No: **NCR patrols are free but only on roads
   where NCR standing >= Liked and a patrol point exists**. Our company can add a patrol subscription: 60 caps/week = danger -20% on one route (they send a Ranger
   to ride along). NCR standing +. [Mechanic: a danger number used by the paper-resolution roll.]
7. **Bribery**: a Clerk can waive a fine for 2x its amount (barter or Speech 50; failure: +15 heat). A **Ranger tip**: for 150 caps get an advance warning of a raid by 1 day (if heat < 60).
   Risk: repeated bribes are logged, each bribe +5 heat when the Clerk is "Loyal to the Republic" (Ranger Jackson cannot be bribed ever; vanilla NPC).

**Plugging reputation in**
- Vanilla NCR reputation (Fame/Infamy; Liked/Idolized...) gives a modifier: Idolized: licence -20%, bids +5% bonus, inspection chance 0.5x;
  Vilified: licence +100% and **no new NCR contracts**, inspections 2x. Infamous (Fame gained but infamy high): treat as Wild card: tolls charged.
- A NCR Standing on the company is its own number (0-100) from contracts and taxes paid on time, and **separate** from vanilla reputation (so the
  company's behaviour is not wiped by a quest). Vanilla rep only modifies it by +/-10.
- A "Rule of the day" in the report, Papers Please style: e.g. "New decree: ammunition above 5.56 needs a permit" or "Water tax raised 2 points."
  Changes 1 per 14 days; it forces small changes in the plan (a decision, not a chore).

**Faction endings (Hoover Dam)** [K for outcomes]
- **NCR wins**: standard rules persist; licences lose their price; new "Rangers' Road" subsidy; tolls drop; **CC grows (+10 A)** because it supplies the
  Army; the Gun Runners get a trade advantage.
- **Legion wins** (Caesar): NCR rules vanish; the Legion rules at the Outpost: **tribute 12%** of revenue and **no NCR goods**; new licence is the "Frumentarii permit"; Ranger
  inspections disappear but Legion "censors" check contraband (slavery, chems forbidden = a different heat). Caps become the standard currency and NCR$ is worthless (price 0.1).
- **House wins**: the Strip rules: **Securitron checks** + a Strip tariff, taxes 5%, no heat from NCR, but House's "licence" to sell in New Vegas cost 500 caps/week.
- **Independent** (Mr House or no one): road gangs are cheaper to bribe, no tax, higher danger (+20%), CC grows strong (A +20), because no one polices it.
- Doing nothing / before ending: the rules above (NCR in Mojave).
Implementation: one global "regime" variable, 4 tables of constants; low-medium difficulty. The endings only
matter if the player finishes the main quest; the mod must work if the endgame is never reached.

### 2C. The dodgy side (smuggling, heat, raids)

**Contraband list** (each as a new "Goods" tag with price multiplier and heat per unit; some also exist as vanilla items)
| Contraband | Source | Margin | Heat per 100 units/week | Notes |
|---|---|---|---|---|
| Powder Ganger powder (pistol powder / blasting) | Powder Gangers, Goodsprings area/Quarry; they sell cheap if the player has not wiped them out | +60% | +8 | needed for ammo chain (cheaper than NCR import). If NCR killed the Powder Gangers, the supply dries. |
| Chems (Jet, Psycho, Med-X, Buffout) from Fiends/Kings/Omertas | Fixer contact | +90% | +15 | Kings forbid in Freeside; Omertas are partners. |
| Stolen NCR gear (ammo, armour, stimpaks from Outpost depot) | Raiders/Powder Gangers | +120% | +20 | CC and NCR will both notice. |
| Legion-made goods (Legion denarii, slaves are NO; weapons (machetes), leathers) | Fort/Nipton border | +70% | +10 | Needs Legion standing > 0; adds Legion rep. Not slaves: the mod does not do slavery trade. |
| Brotherhood tech (energy cells, bits) | Hidden Valley leftover/ BoS bunker | +100% | +12 | dependent on BoS state; rare. |
| Unlicensed water (untaxed) | Goodsprings spring | +25% | +4 | the "gentle" first step into the dark. |
Why the gentle one: a **gradient** of dodginess: tax dodging (under-declare), unlicensed water, powder, chems, stolen gear. The player chooses where to stop.

**Heat model** (0-100 per company, one number; plus a per-town sub-heat for the town where it happened, 0-100 each)
- Raises: contraband units sold (table above, scaled by units/100 weekly), under-declared revenue (+2 per 10% hidden/week), caught smuggling guard
  skirmish (+15), killing an NCR trooper (+40 vanilla Infamy also adds +20), a CC tip-off (+15), a bribe logged (+5), a witness (a townsperson who
  sees the transfer; +3 per).
- Lowers: decay **-2 per game day** (so ~14 per week; lying low for ~20 days clears 40); stop dealing for 7 days: decay doubles to -4; pay a "fine" (NCR clerk): -10 per 100
  caps; hire a **fixer** (below): -3 per day extra; clean line of 20 days: -10 bonus; donating to NCR (supplies for the front): -5.
- Thresholds:
  - 0-19 Quiet: nothing.
  - 20-39 Noticed: inspections 1 per 10 days; Clerk gets curious (memo).
  - 40-59 Watched: patrol cars (Rangers "visit" the warehouse; some wagons searched on the road; **10% chance each caravan trip of a search** with loss of contraband, no fine); CC knows.
  - 60-79 Hot: a tip-off may come (see below), warrant letter ("we are examining your books"); NCR contracts frozen.
  - 80-99 Raid imminent: a raid on the 2nd to 5th day (random) unless bribe/fixer; licence suspended.
  - 100: raid happens NOW at the next morning tick. Optionally *all* warehouses with contraband. Licence revoked if you are convicted.
- Caught at the road: contraband seized, ~(contraband value) fine; heat stays.

**Tip-offs**: a Ranger friend or an NCR clerk (bribed) warns you at heat >= 60: "Raid in 2 days." Gives a menu "Move stock / clear the warehouse / prepare defences / bribe".
Also from CC (a rival Nemesis angle: CC's tip can be exposed by evidence). Tip-offs can be false (10% each), costing a day's trade.

**The raid** (the set piece)
- **On paper** (player away; 90% of cases): the NCR arrives at HQ; resolved at the morning tick. Roll: our guard strength (sum of guard levels) vs raid strength
  (heat/2 + 10 per Ranger). Outcomes: Win (the Rangers withdraw but you gain +20 Infamy and the company becomes "Outlaw") / Bribed (pay 3x fine) /
  Seized (lose contraband stock + 1 warehouse for 14 days, fined 20% of cash) / Licence revoked (the second lose condition: the company is shut down by
  law). The report says "NCR raid at HQ. Guards 4 vs Rangers 6 ... you lost 340 caps of stock, fine 600".
- **Played for real** (player at HQ at the morning tick, about 25% of cases and always for the first raid): Rangers (existing vanilla NCR Ranger/Trooper
  actors, placed or spawned by script near HQ) walk to HQ, a Ranger captain speaks to the Manager/the player in a scripted line. Choices (a terminal or dialogue
  line, one-time): **Fight** (guards fight with you; killing NCR gives +40 heat, kills Rangers = Infamy, wins the "fight" outcome); **Bribe** (Speech 60, or caps = 2x
  fine; 70% success; failure = surrender with -10 Standing); **Surrender** (lose contraband + fined, keep the company); **Run** (no HQ: licence revoked). 
  [Companion: the guards help only if their loyalty >= 50.]
- **Hidden warehouse**: a small building (cost 400 caps + 30 caps/week) disguised as a cellar; holds up to 40% of contraband stock; raid roll
  chance of discovery: 15% base, +10% per inspection passed with it on, -10% with a fixer. Danger: a hidden warehouse that is found makes the raid
  "Seized" automatically.
- **Fixer manager**: a manager role (the "Fixer", hire at tier 3) with skills: Bribe (reduces fine by 25%), Tip (guarantees a warning if heat >= 60 with 70%),
  Launder (convert 20% of contraband margin into clean income, losing 10%). Wage 80 caps/week. Loyalty issue: a fixer with loyalty < 40 **sells you out** (heat +30). Mafia III-like: neglect makes
  them leave.

**Why the dodgy path is tempting but not strictly better** (numbers)
| Axis | Clean | Dodgy |
|---|---|---|
| Margin | base | +60% to +120% on contraband lines |
| Cost | Tax 8% + licence | tax avoided (up to -8%) but fixer wage 80/week, hidden warehouse 30/week, bribes ~200/month |
| Variance | low | big: a raid costs 20% of cash + stock + 14 days of a warehouse, lose-the-company risk at heat 100 |
| NCR contracts | open (the best contracts need Standing >= 60) | frozen at heat >= 60: the best margins are in clean NCR contracts |
| Rival | CC fights in market | CC gets the **tip-off weapon**: your dirty trade is CC's best arm |
| Reputation | NCR + Strip | Fiends/Kings/Omertas liked, NCR down, vanilla Infamy moves |
| Quest side effects | none | blocks some NCR quest lines (do not alter vanilla flags: only the company's own) |
Expected value: contraband adds maybe +35% profit at heat 30-40, the same profit at heat 70 equals break-even because of fines + frozen contracts.
**Rule**: a heat of 50 is the knee in the curve; the player can sit there if they pay the fixer.

**Partners (shady)**: the Omertas (Gomorrah): moves chems; Kings (Freeside): sells to them for a share, forbids hard drugs in Freeside;
Powder Gangers: source of powder if alive; Van Graffs: a "supply" for unregistered weapons but they are the CC's friend. Every partner has a
**price and a leash**: e.g. Omertas take 15% and ask for a favour once a month ("run this package past the Outpost").

### 2D. Ten+ concrete rival and law events
1. **Price war in Primm.** Our smokehouse hits 28% share. Next morning memo: "Crimson Caravan is selling brahmin jerky at 9 caps (we sell 11)." Options: match -15% (cost ~210 caps over 5 days), hold (lose ~1.5 share/day), or "Take it to Alice" (barter an agreement: -10 A, costs 200 caps).
2. **Poached manager.** Our Outpost trader Mara (loyalty 45) is offered +20%. Options: counter +25% (cost 30 caps/week), let go, or talk to her (Speech 50 = +15 loyalty). If lost, the CC route gets better and a "Mara" CC guard is seen in Primm.
3. **Supplier buyout.** Brahmin farmer at Goodsprings sells to us only. CC offers 130%. Menu: sign exclusive for 30 days at 120%, or find another source (Primm farm, 3 days).
4. **Sabotage at night.** Warehouse fire (-20% stock) with a Van Graff-branded match on the ground; evidence +1. Options: pay repairs, investigate (mission: find the arsonist at the Silver Rush; the player can do it in person).
5. **Buyout letter.** At low cash: Alice's offer; 2.5x monthly profit. The text voice: "Business is a hard game, dear. The offer won't be there next season." Refuse/accept/ask for time (+7 days, costs a loan interest).
6. **NCR bid.** 1,200 rounds of 5.56 for the Outpost. Bids: CC 13.2, Gun Runners 14.0, ours slider 11-17 caps. Lowest bid with reliability >= 60 wins. Win: 10-day payment delay.
7. **Surprise inspection.** At heat 28: NCR clerk asks to count the stock at HQ. Menu: "Show the books" / "Show the books (hide 40 caps of powder)" (roll 60% to pass; failure +15 heat and fine) / "Pay him" (Speech 40).
8. **Tip-off letter.** "Someone told the Rangers about the powder." (CC tip). If we kept evidence about CC sabotage, the player can answer with an anonymous return counter-tip (-A?).
9. **Raid, for real.** The player is at HQ when five Rangers come. Fight, bribe (Speech 60), surrender; each with a result table and a companion line (Cass: "Girl, you got a bag of caps? Pay the man.").
10. **Raid on paper.** At 4 guards vs 6 Rangers: seized stock, 600 fine. Report in one line, three follow-up options (fund legal defence 300 caps: halves the fine next time; hire more guards; bribe).
11. **Powder Ganger deal.** A Ganger runner offers 400 powder at 60% price if we carry two packages. Heat +8/100; sourcing dies if the NCR clears the Correctional Facility.
12. **Road search.** An NCR checkpoint opens at Primm: each wagon with contraband has a 10% chance; the Ranger says "Open the crates, please."
13. **Ranger tip.** At heat 62 an NCR corporal at Primm sends word: "Rangers are coming Thursday." Option: clear the HQ stock to the hidden warehouse (cost 40 caps), bribe (150), or ignore.
14. **Captain Dutch Riker.** After 5 grudge flags, a CC captain with six guards ambushes our wagon at Goodsprings Road. The player in range can fight; a defeat on paper loses 20% of the cargo and gives him a rank.
15. **Merger offer.** After beating the CC in three towns Alice invites us to the Tops(?) / her office: "Rather than bleed each other dry, shall we be partners?" (Q: gives player 75% of profit, CC 25%, the new rival is Gun Runners.)
16. **Decree.** "From next week, ammunition shipments over 500 rounds need a permit (50 NCR$)." Forces contracts to be split or permits bought.
17. **Hoover Dam outcome message.** On the day the Dam battle ends the morning report prints the new regime table.

## 3. Bold ideas
1. **Alice's Ledger as a real in-game item**: the player can steal or read the CC ledger (a note and a computer terminal at the CC office, like the safes in Heartache) and learn the AI's current Aggression A and next-day move for a week. Intelligence lets you counter. (Uses the existing safes' location; low difficulty.)
2. **Two-key terminal**: dirty actions are hidden menu items that appear only after meeting a contact (JohnnyGuitar can add menu items at runtime), so the "dodgy side" is physically discovered, not a tab you see on day one.
3. **Heat shown as a prop**: a stack of Ranger posters at HQ, a patrol of NCR troopers on the road, a "Wanted" ledger on the notice board. No HUD bar needed.
4. **The Auditor mini-game**: during an inspection the player picks 3 of 5 ledger lines to present, as in Papers, Please: a short terminal puzzle that rewards knowing your own books.
5. **Rival with a face**: letters from Alice, not tables; every rival move has one line of voice that mentions a previous flag (Nemesis memory spoken back).
6. **Company-flip**: if you lose to the buyout, you become the CC branch manager in the same towns (play a lighter second game as a manager, win back the company by beating your old numbers over 60 days). The "lose" is a sideways state.
7. **Laundering through the Strip**: cleaning dirty caps via a casino (Gomorrah/Tops) with a house cut and a chance of being fleeced. Feeds the Omerta partner.

## 4. Pitfalls
- **Do not break Heartache by the Number.** Never write to vanilla quest variables; read-only. If Alice is dead or Cass already sold, the mod needs working fallbacks.
- **Invisible takeovers anger players** (BUSINESS-RESEARCH): the buyout must warn at least 7 days before and can be refused; Offworld warns the victim [D].
- Too much AI rival **babysitting**: cap at one rival item per report, and let the player set standing orders ("match prices up to 15%").
- Heat that never decays punishes time away: decay must run while the player is away (it does, per game day). Cap the damage of a raid while the player is on a vanilla quest (use the last-seen-at-HQ day).
- Taxes + wages + rent + fees will drown the player: keep total fixed overhead <= ~35% of an average week's revenue at each tier.
- A dodgy path that is strictly best would erase the clean path; keep the knee at heat 50 and the contract freeze at 60.
- Real raids spawn Rangers: killing NCR actors may interact with vanilla NCR reputation and quests. Use existing records but avoid killing named vanilla NPCs; fall back to paper if scripts see a vanilla quest running at the Outpost.
- The NCR dollar rate (about 40% of a cap) is from a search snippet of a fan wiki; verify before hard-coding.
- Alice's numbers in the table are our own design, not read from the game; test for balance with a simulation script first.
- Slavery trade: do not add it; Legion contraband stays material goods.
- Do not over-trust my [K] vanilla facts about placements (NCR at Primm, Outpost, Powder Gangers at the Correctional Facility); check with fnv_record before writing records.

## 5. Questions only the user can answer
1. Should the CC have **named, killable** managers (Alice, Tagg, a captain), or stay a faceless company that never dies? Killing Alice in vanilla already happens; do we respect that?
2. Is losing the company to the **CC buyout** allowed to turn the player into a CC branch manager (a sideways game), or just a loss?
3. Real raids: should the player always see the **first** raid for real (a tutorial), even if away (the mod would wait until they return)?
4. Is contraband allowed to include **chems** and **stolen NCR gear**, or should the dodgy side be limited to taxes and powder for a lighter rating on Nexus?
5. May the NCR dollar be a **second currency** in the company ledger (0.4 caps), or is everything in caps for simplicity?
6. May the company side with **Legion/House** rule sets after the Dam, or is the mod NCR-only by design?

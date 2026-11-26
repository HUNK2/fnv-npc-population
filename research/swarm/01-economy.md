# 01 - The money model (markets, ledger, P&L, legible numbers)

Agent angle: THE MONEY MODEL. Written 2026-11-26. [D] = documented by the source, [O] = player/reviewer opinion,
[calc] = I computed it (numbers from my own small simulation, formulas below, not from a game), [read] = read from
FalloutNV.esm with read-only fnv_record lookups.

Honest note on sourcing: fandom wikis, PC Gamer, the Paradox forum and Elite's wiki refused automated fetches
(HTTP 402 / truncated). Most pages below were opened, but several only gave qualitative text, and Capitalism Lab, EVE,
Port Royale and Sunless Sea economy details were NOT obtained. I do not cite them for numbers.

---

## 1. Key findings

### 1.1 FNV's own economy [read]

- Barter GMSTs (decoded from the float bytes): `fBarterBuyBase` = 1.55, `fBarterBuyMult` = -0.45,
  `fBarterSellBase` = 0.45, `fBarterSellMult` = 0.45. [inferred from the values, the exact skill expression is engine
  code] this gives buy price = value x (1.55 - 0.45 x Barter/100) and sell payout = value x (0.45 + 0.45 x Barter/100):
  Barter 0 -> pay 155%, get 45%; Barter 100 -> pay 110%, get 90%. So the vanilla player's best case is a 20-point
  spread (110% vs 90%). Our wholesale company must sit inside that band (see 2.9, exploit control).
- Base item values (ENIT/DATA value field): Purified Water 20, Stimpak 75, Healing Powder 5, 10mm Round 2,
  Brahmin Meat 5, Broc Flower 3, Xander Root reads 0 in its value field (looks like an oddity; we set our own, ~3).
- Consequence: vanilla values are tiny per unit (2 to 75 caps). A "crate" cargo unit is mandatory so a wagon load is
  worth four figures and the numbers stay readable.

### 1.2 Price models in other games

| Game | How price is set | Useful part for us | Source |
|---|---|---|---|
| Bannerlord | Per-category supply and demand per town; demand from consumption plus workshops; more stock = lower price. Each unit you buy raises the price (a horse 100 -> 106 -> 113, about 6% a step). Each town has a daily consumption budget per category scaled to prosperity (prosperity 5000: about 500 denars grain, 400 meat, 200 butter a day). Consumed goods raise town stats (food stores, productivity). Sellers short of cash accept lower prices. UI: trade rumours, profit tracking. [D] | Per-unit price impact, budgeted demand, goods that make towns grow | gamebanshee.com/k4cr3 (Bannerlord developer blog, opened) |
| Victoria 3 | Market price = base price moved by the balance of buy vs sell orders; "the more Buy Orders than Sell Orders the higher the price"; poorly connected states trade only part of the price (Market Access). Shortage slows building efficiency. No numbers published in the diary. [D] | Base price as anchor; shortage has a gameplay cost, not only a price | gamewatcher.com/victoria-3-dev-diary-9-national-markets-open-economic-model (opened) |
| Elite Dangerous | Supply and demand have a natural equilibrium that trading pushes away from; they drift back at a rate depending on the good; demand recovers roughly 2-3x slower than supply; pricier goods recover slower. Community estimate, may be out of date. [O] | Asymmetric recovery: gluts last longer than shortages | forums.frontier.co.uk (found via search, snippet only) |
| X4 | Prices are a percentage of a base price, driven by each station's own stock level; buying one unit at a time visibly raises the price, bulk buying avoids it; prices lag behind. [O] | Stock-driven price, lag | steamcommunity.com / forum.egosoft.com (search snippets only) |
| Offworld Trading Co. | Supply and demand "fluctuates constantly"; price formula not stated. Black-market actions raise their own price with each purchase, which warns rivals; you are warned when a rival can afford a buyout but they are not told you know. [D] | Rising price per purchase as a visible alarm; "can they afford me" tension | en.wikipedia.org/wiki/Offworld_Trading_Company (opened) |
| Anno 1800 | Upkeep per building; negative balance usually from overbuilding a chain; the balance line is a live rate that moves; supply vs demand shown on a statistics screen (0 balanced, negative shortage, positive overproduction); advice: keep a small surplus because a big surplus is just upkeep. [O] | Balance sheet that shows chain cost; "surplus is waste" | steamcommunity.com/app/916440 threads, forums.pcgamer.com (search snippets) |
| Drug Wars (1984) | 30 days, 6 areas, a day per trip; $2,000 cash vs $5,500 loan shark debt (the beej.us clone adds 10% daily interest); coat holds 100 units; random events (mugging, price spike, price crash, find) ; score = cash + stock - debt. Price ranges not published. [D] | The loan on screen, daily drama, one number to chase | en.wikipedia.org/wiki/Drug_Wars_(video_game), beej.us/tmp/drugwars.html (both opened) |
| Patrician III | Ranks from Shopkeeper up to Alderman gated on wealth and reputation (feasts, donations, defending). Goods unsupplied -> town markets decline. [D] No price model on the page. | Reputation as a second currency | en.wikipedia.org/wiki/Patrician_III (opened) |
| Sunless Sea | Death is permanent but successors inherit some possessions via a will. [D] | Loss that carries something over | en.wikipedia.org/wiki/Sunless_Sea (opened) |

Pattern across all of them: a **base price** anchor, a **stock-vs-target ratio** as the price driver, **your own
trades move the price**, recovery takes **time**, and growth-feel comes from **seeing the margin** before you commit
(Bannerlord rumours, X4 trade filter, Drug Wars price board).

---

## 2. What this means for our mod: the money model

### 2.1 Goods, crates, anchor prices

Cargo unit is the **crate**. Anchor price P0 per crate is derived from vanilla item values [read] so the world feels
consistent. Wagon (1 wagon + 2 brahmin) carries 8 crates at the start.

| Good | Crate | Vanilla unit value | P0 per crate (caps) |
|---|---|---|---|
| Purified water | 10 bottles | 20 | 200 |
| Healing powder | 20 doses | 5 | 100 |
| 10mm ammo | 100 rounds | 2 | 200 |
| Brahmin meat | 20 cuts | 5 | 100 |
| Stimpak (needs Science 70 hire) | 5 | 75 | 375 |
| Building materials (new cargo) | 1 pallet | none | 150 |
| Broc + Xander (workshop input) | 20 | 3 | 60 |

### 2.2 How a town's price for a good is set (formula)

Per town t and good g the game keeps ONE number: `stock` (crates held in the market).

```
cons   = crates the town uses per day            (grows with the town, see 2.8)
Tref   = 3 x cons                                 (three days of cover = "normal")
r      = stock / Tref
m      = 0.5 + 1 / (1 + r)                        (price multiplier, always between 0.5 and 1.5)
mid    = P0 x m x news                            (news = event multiplier, default 1.0)
spread = max(0.02, 0.10 - 0.02 x trust - 0.0004 x trader_Barter)   (trust 0..4; trader Barter 0..100)
ASK    = mid x (1 + spread)     what you pay when you buy from the town
BID    = mid x (1 - spread)     what you get when you sell to the town
```

Properties: r = 0 (empty shelf) -> m = 1.5; r = 1 -> m = 1.0; r = 2 -> 0.83; r = 4 -> 0.70; r large -> floor 0.5.
Bounded on both sides, so no town ever pays 0 caps or 10,000 caps. Smooth, one division, easy for NVSE script math.
Example (spread 0.06, trust 1, Barter 50), Goodsprings water: cons 4/day, Tref 12, stock 34 -> r = 2.83, m = 0.76,
mid 152, ASK = 161. Primm water: cons 10/day, Tref 30, stock 14 -> r = 0.47, m = 1.18, mid 236, BID = 222.
Gross spread 61 caps on a 161-cap crate, 38%. That is the first-day opportunity the report must make visible.

**Each crate moves the market:** price is recomputed per crate inside a batch (like Bannerlord's step per unit [D]).
Primm water: one crate shifts r by 1/30, so about -0.9% per crate; dumping 7 crates drops BID about 6%.
Goodsprings ASK rises about 1.5% per crate bought (smaller town, r step 1/12).

**News multiplier.** `news` is a per-(town,good) factor that events set and that decays 25% of the way back to 1.0
each day. Examples: Primm without a sheriff: ammo x1.40 for the days it holds; Quarry Junction cleared: building
materials x0.85 at Sloan (supply restored); Powder Gangers raiding a road: that road's ammo and meat x1.25 at both
ends. Telegraphed one to two days ahead through radio/rumours so a reading player can pre-load (see 3.2).

**Daily drift (the "natural" market).** Each (t,g) has a natural stock N. Every game day, before the player's morning
report:

```
if stock < N:  stock += (N - stock) x 0.25      shortages refill fast: half-life 2.4 days
if stock > N:  stock -= (stock - N) x 0.12      gluts drain slowly:    half-life 5.4 days
```

Launch table (stock at day 1 = N; cons/day, N in crates):

| Town | Water | Healing powder | 10mm ammo | Brahmin meat |
|---|---|---|---|---|
| Goodsprings | cons 4, N 34 | cons 2, N 18 | cons 4, N 4 | cons 4, N 4 |
| Primm | cons 10, N 14 | cons 4, N 4 | cons 2, N 20 | cons 6, N 12 |

(Goodsprings produces water and herbs, so a high N; it needs ammo and meat. Primm needs water and herbs, makes ammo.)
Numbers above are tuned with my own simulation [calc]; the scale factor K (town depth) is the main tuning knob.

### 2.3 Demand recovery and saturation when you keep selling

- Every crate you sell raises `stock`, lowers BID, and takes about 5 days to half-recover (12% drain). That is the
  Elite asymmetry [O] done on purpose: selling the same thing daily is punished, selling something new is rewarded.
- Pulling stock out of a producer town recovers faster (25%), so buying is easier to repeat than selling.
- [calc] Simulation result, one wagon, two towns, greedy player: day 1 margin +746, day 2 +288, day 3 +94, then
  about +90 a day (K=2). Steady-state week-2 gross margin only about 570 caps against about 270 fixed costs.
  With depth K=3 about 870. This is the "thin market trap": with two towns and four goods a lone wagon saturates in
  three days. That is the intended engine for expansion (new route = new windfall), but the launch numbers must keep
  steady-state net positive (K=2.5 or more).
- Market depth grows with delivered goods: each full week a town receives >= 80% of its building-material demand,
  `cons` for all goods in that town rises +4% (cap +60%). Your growth literally widens your markets.
- Spoilage: meat and any perishable lose 6% of stock a day in the wagon or depot (a cost line, and a reason for a
  smokehouse). Water, ammo, powder do not spoil.

### 2.4 Contracts: the stable half of income

Spot trading is the gamble; contracts are the predictable part (Patrician-style standing orders, Recettear-like
schedule on screen):

- A standing order: "Primm Saloon: 4 crates water/week at 215 flat, 4 weeks" (about mid +9% over spot at normal r).
  Missing one delivery: -10% of the order value as a penalty and trust -1 step.
- Bulk delivered to a contract does NOT move the town's spot stock (it is the town's own supply deal), so contracts
  are the escape valve from saturation and the reason a manager can run a route unattended.
- Rule of thumb for the player: contracts pay the wages, spot trading pays the growth.

### 2.5 The full P&L line list

Revenue (weekly statement):
1. Spot sales (sum of BID x crates)
2. Contract deliveries
3. Workshop output sold (water purifier, smokehouse, reloading bench, stone yard)
4. NCR government supply contracts (ammo and medicine to Mojave Outpost, paid +15%, require the licence)
5. Contraband sales (dodgy path; high margin, adds Heat)
6. Warehouse storage fees (tier 3+, other firms rent shelves)

Cost of goods:
7. Cargo purchases (ASK x crates)
8. Workshop inputs (broc, xander, scrap metal, primers, powder)
9. Spoilage and shrinkage (6%/day perishables; 1% of cargo value as breakage and theft)

Operating costs:
10. Wages (driver 10/day, guard 12/day, trader 20/day, workshop hand 14/day, manager 40/day, Science-70 chemist 60/day)
11. Animal upkeep and feed (3 caps/day per brahmin)
12. Vehicle wear (1% of wagon value a day, repair bill when player is away; non-cash depreciation on the statement)
13. Rent and building upkeep (depot 70/week, warehouse 25/day, workshop 18/day)
14. Tolls (NCR gate, Mojave Outpost 20/wagon/pass)
15. NCR trade duty: 2% of sales (turnover) and licence renewal (150 a month)
16. Insurance premium (optional, 2% of cargo value, halves road-loss penalty)
17. Bribes and fixers (dodgy path) and fines when caught

Losses (shown on their own line, never buried):
18. Road events resolved on paper (guards vs danger): cargo lost, wagon damage
19. Raids by the NCR on the office (confiscated stock plus fine)
20. Crimson Caravan sabotage and price war write-downs (stock sold below cost to hold share)

Financing (below operating profit):
21. Loan interest (Alice, 4% a week on the outstanding balance)
22. Late fees (see 2.7)
23. Principal repayment (cash flow only, not a P&L cost)

The statement ends with three lines the player learns to love: **Operating profit**, **Net profit**, **Net worth**
(cash + stock at book + wagons/buildings at book - debt). Net worth is the single "growth number" (Drug Wars score
logic [D]); market share is the secondary one.

### 2.6 Starting capital, loan, payback target

- Loan: **3,000 caps** from Alice McLafferty at **4% a week on the balance**, minimum **300 caps principal a week**
  plus interest. Early payoff is free: no penalty, and Alice sends a note (a hook for the rival relationship).
- Player puts in **500** of his own caps as equity (company cash is separate; later dividends move it back).
- Day-0 shopping: wagon 400, two brahmin 300, guard 80 + driver 70 (hire fees), NCR trading licence 150: **1,000**,
  leaving **2,500** working capital. Company net worth after setup: 500 - 300 expensed = **200**.
- Cash on hand at founding is 3,500 and net worth is 500: the player sees "debt 3,000" every morning (Drug Wars
  rule: the debt is always on screen [D]).
- Target payback: a competent player, expanding on a normal path, repays the loan in about **5 game weeks (about 28
  real hours at timescale 30)**; a cautious one 8 weeks; the failure ladder starts at 12 weeks of no progress, or
  one missed installment (see 2.7). Projected net profit by week, decent player (extrapolated from the week-1
  simulation, not simulated): W1 about 840, W2 about 600 (route saturates, a second route opens, second wagon bought),
  W3 about 900, W4 about 1,200, W5 about 1,500; cumulative about 5,000, enough to clear the 3,000 principal plus
  about 400 total interest and still fund wagon 2 and a third town. [calc/estimate]
- Tier 2 (Outfit) costs 2,500 to found plus net worth >= 4,000, loan cleared, one deed, so the loan payoff is a
  natural milestone, not an end.

### 2.7 Failure ladder expressed in caps

| Step | Trigger | What the ledger does |
|---|---|---|
| 1 Warning | Cash after the weekly bills < installment | Morning report banner, 3 game days grace, late fee 5% of installment |
| 2 Notice | Installment missed once | +1 week's interest as fee, trust with Alice -1, one wagon pledged |
| 3 Seizure | Missed twice | Pledged wagon or a warehouse seized (one asset, Alice's agents drive it away), repaid at 60% of book value off the debt |
| 4 Takeover | Debt > 1.5 x net worth or three missed | Office becomes a Crimson Caravan branch; the player keeps their own caps and a "Legacy" offer |

Bailout options at every step: sell a wagon at 70%, take a contract advance (20% of a 4-week order paid up front), an
emergency loan from Alice at 8%/week (use is itself a failure signal). After the loan, the same ladder runs on
wages, rent and tax, and the NCR shutdown rides on the Heat meter, not on money.

### 2.8 Money sinks (so cash is never a pointless pile)

1. **Tier fees plus deeds**: Outfit 2,500, Caravan company 12,000, Trading house 60,000, Mojave concern 250,000.
   A tier is one new thing to do, visible in the world (signs, wagons, staff, buildings).
2. **Buildings** (warehouse 3,000 + 25/day; stone yard 4,500; smokehouse 2,800; reloading bench 3,500; purifier 2,000)
   with real upkeep: Anno's lesson that a surplus without throughput is just upkeep [O].
3. **Staff**: wages grow with headcount and tenure (+2% a month raises on a 30-day cycle), managers 40/day.
4. **Progressive NCR levy**: duty 2% of sales up to 5,000/week, 3.5% above, 5% above 20,000/week.
5. **Town building**: Crimson Caravan is on the other side, but a town you supply with building materials unlocks
   concrete benefits (a new stall, a guard post, a well) bought with caps and materials. Stardew bundle logic [D]: a
   shopping list with a visible result.
6. **Price war**: spend 40-200 caps/day to undercut Crimson in one town for a week and take market share.
7. **Vault limit**: depot cash above 5,000 per depot (no bank) is exposed; raiders target it at 5% a week unless
   you pay guard wages or move caps out. Hoarding costs you.
8. **Dividends** to the player: caps leave the company; the player's own caps are for vanilla shopping.
   Company needs a cash reserve (shown as "weeks of wages in the till": the report warns below 2).
9. **Dodgy path**: bribes, fixers, fines, losing confiscated stock.
10. **Insurance, training** (raise a trader's Barter by +5 for 300 caps), **marketing** (+0.5 trust per month per town).

### 2.9 Exploit control (barter loop)

Company sells goods to the player at 1.10 x P0 and buys from the player at 0.80 x P0 (outside, no more than 10 crates
a day). Vanilla vendors pay at most 0.90 x value [read, inferred], so a player cannot buy cheap from the company and
flip to vendors, nor sell vendor loot to the company above what vendors would pay.

### 2.10 The morning report (what the player sees)

FNV terminals are menu-driven with body text; I assume about 40 characters wide and under 20 lines a screen
(measure it in game). Pages of three or four lines each. ASCII only: unverified that the FNV font draws
Unicode block characters, so sparklines use `_.-=*#`.

```
CARAVAN CO.   MON  DAY 8   (WEEK 2)
------------------------------------
CASH        3,972   +  612 vs Sun
NET WORTH   1,140   + 217  *RECORD*
DEBT        2,700   (Alice) due Fri
SHARE PR    18%  (+2)  vs Crimson 51%
NET WORTH 14d  _.-.--=-=*=**#
------------------------------------
1 BEST SPREADS TODAY
2 YESTERDAY'S RUNS
3 MEMOS (2)
4 STATEMENT (WEEK)
5 PRICES: WATER  AMMO  POWDER  MEAT
6 BACK
```

Price board, one good:

```
WATER             ASK    BID   TREND
Goodsprings        161    --    _.-==
Primm               --    222   =-.__
margin per crate    61 (+38%)
crates left to saturate: ~9
```

The "crates left to saturate" line (how many crates until BID falls 10%) is the number that makes the player feel clever:
it turns the formula into a quantity they can act on.

Statement page (week):

```
WEEK 1 STATEMENT
Spot sales        7,820
Contract              0
COGS             -6,360
GROSS MARGIN      1,460  (19%)
Wages              -154
Feed/wear/rent     -161
Duty 2%            -164
Loss (bandits)     -191
OPERATING PROFIT    790
Interest            -120
NET PROFIT          670
vs last week        n/a
```

Rules for the numbers (all reports):
- Always show **delta vs yesterday and vs same weekday last week** with sign; show the best number so far with
  `*RECORD*` when it is beaten (best day, best week, biggest crate margin, longest no-miss streak).
- One sparkline per big number (net worth, market share, per route margin); 14 values, scale to the series min/max.
  Draw a `v` or `^` on a day with an event.
- Round to 10s in headings, exact in statements. Report only 3 headline figures on the first screen.
- One "decision" (memo) at the bottom with a deadline: "Primm Saloon offers 4 crates/week at 215 for 4 weeks: ACCEPT /
  COUNTER 225 (60% chance) / PASS".
- Never show negative cash without the cause on the next line (loan installment, loss).

### 2.11 Worked example: first 7 game days (K=2, one wagon, Goodsprings and Primm)

Setup (day 0): cash 3,500 -> spend 1,000 (wagon 400, brahmin 300, guard 80, driver 70, licence 150) -> **cash 2,500**,
debt 3,000, net worth 200. The wagon makes one round trip a day (8 crates per leg). The player picks the best crates.
(Numbers are from a script simulation, [calc], rounded, price impact per crate as in 2.2.)

| Day | Morning prices (mid): Water GS/PR, Ammo GS/PR | GS -> PR (buy / sell, margin) | PR -> GS (buy / sell, margin) | Day margin | Cash |
|---|---|---|---|---|---|
| 1 | 152/236, 250/146 | 7 water + 1 powder: 1,237 / 1,617, +380 | 7 ammo: 1,132 / 1,499, +366 | **+746** | 3,247 |
| 2 | 159/220, 208/158 | 5 water + 3 powder: 1,104 / 1,342, +238 | 2 ammo: 338 / 387, +50 | +288 | 3,535 |
| 3 | 163/211, 204/158 | 2 water + 1 powder: 430 / 501, +71 | 1 ammo: 168 / 191, +23 | +94 | 3,629 |
| 4 | 162/210, 203/157 | 2 water + 1 powder: 428 / 497, +69 | 1 ammo: 166 / 191, +25 | +94 | 3,723 |
| 5 | 161/209, 203/155 | 2 water: 344 / 392, +48 | 1 ammo: bandits take the crate on the road, -191 sale | -117 | 3,606 |
| 6 | 161/208, 207/155 | 2 water + 1 powder: 425 / 494, +69 | 2 ammo: 331 / 386, +55 | +124 | 3,730 |
| 7 | 161/208, 203/156 | 2 water + 1 powder: 425 / 491, +66 | 1 ammo: 165 / 191, +25 | +91 | 3,822 |

Week-1 statement (cash basis, Sunday night):

| Line | Caps |
|---|---|
| Sales (spot) | 8,178 |
| Cost of goods | -6,857 |
| Gross margin (incl. bandit loss) | 1,321 |
| Wages (driver 10 + guard 12) x 7 | -154 |
| Feed 2 brahmin x 3 x 7 | -42 |
| Depot rent | -70 |
| NCR duty 2% of sales | -164 |
| Vehicle wear (non-cash, 1% x 700 x 7) | -49 |
| **Operating profit** | **842** |
| Loan interest 4% x 3,000 | -120 |
| **Net profit** | **722** |
| Principal installment (cash only) | -300 |

End of week: cash about 2,972, assets 651 (wagon+brahmin after wear), debt 2,700 -> **net worth 923** (+723 on day 0's
200). Signal for the report: "Net worth record. Margin per crate fell from 61 to 24 since Monday. Water at Primm -16%."
What the player does about it: Day 3 onward the water/ammo pair is dry: **the memo says "Add a route"**. A third town
(Sloan or Nipton later) restores a +700 day-1-style windfall; contracts (2.4) cover the steady drain.
Steady-state with this route alone: about 570 gross a week (K=2) against about 270 fixed (wages, feed, rent) plus duty:
net of about 250. That is the pressure to expand, and it must be tuned (K or contract values) so it stays positive.

Week 2 plan for a good player: buy wagon 2 (500), open Mojave Outpost (toll 20 per wagon), sign the Primm Saloon
contract, start the water purifier. Net worth about 2,000 by day 14, cleared loan around week 5.

---

## 3. Bold ideas

1. **The Tape** (hard: low). A terminal page "BEST SPREADS TODAY" that ranks every (route, good) by margin per crate,
   crates before saturation, days of travel, and risk, like a Drug Wars board. The player's skill is picking, not
   spreadsheet math. The staff (a hired trader) can only read the tape after you hire them; their Barter changes the
   spreads shown.
2. **Radio-news shocks** (low-medium). Radio New Vegas items and rumour barks telegraph `news` multipliers one to two
   days ahead. A player who listens (or reads the memo) pre-loads for the spike: Bannerlord's trade rumours [D] with
   a Mojave voice. Knowing the world pays; ties business to quests.
3. **Forward contracts** (low). Lock BID now for delivery in 3 days (a premium 4%); if the market moves against you
   it pays, if for you it costs. Drug-Wars-style risk with a hedge.
4. **Price war lever** (medium). Spend caps per day to cut Crimson's share in one town, shown as a share bar and
   a daily cost. Offworld's lesson [D]: let the rival's buyout threat be visible, with a defence.
5. **Alice's friendly scoreboard** (low). A monthly letter from Alice with both companies' net worth, share, and a
   one-line barb. Gives growth a rival-scaled meaning, no extra system.
6. **Two sets of books** (medium, dodgy path). Contraband revenue is hidden: the statement shows an "honest" and a
   "true" column; Heat reads the gap. Reading the gap is a new decision.
7. **Records wall** (low). A terminal page of bests (best day, best route, biggest crate margin, longest streak) that
   also becomes a plaque in the office model (cheap art).
8. **Crate density as a trade skill** (low). Hire a "packer" who raises wagon capacity by 1 crate per level (visible
   in cart model) since capacity is the strongest lever for a thin market.

---

## 4. Pitfalls and design flaws to avoid

1. **Thin-market trap.** [calc] 2 towns x 4 goods saturate in three days and income falls from +746 to about +90 a
   day. Launch with at least 3 towns and 8 goods per wagon decision, or the "expand" pressure becomes "starve".
2. **Day-1 windfall conditioning.** The player will remember the first day (+746) and quit when it ends. Soften with
   contracts, and show "steady state estimate" on the tape so the dip is expected.
3. **Duty too high.** 5% of sales ate 31% of gross margin in my first run; keep taxes 2% of turnover or tax profit.
4. **Rival and player share one market.** Crimson's supply into Primm should go through the same `stock`, otherwise
   "market share" is a cosmetic number and cannot be defended or lost.
5. **Floating-point drift.** NVSE scripts use floats: store `stock` as a fixed-point integer (tenths of crates) and
   round caps at the end of each crate; keep a ledger total that reconciles daily (a hidden audit).
6. **Opaque formula.** If the player cannot predict the price, they stop trading. Always show ASK, BID, spread,
   "crates before saturation", and the 3 reasons for a price (stock level, news, trust discount).
7. **Idle income stales** (BUSINESS-RESEARCH idle design [O]): contracts and Crimson moving in on profitable routes
   must erode old income; do not let a route earn forever unchanged.
8. **Barter exploit** (see 2.9): the company's player-facing prices must sit inside the vanilla 0.90/1.10 band.
9. **Inflation of caps.** Vanilla players have 10,000+ caps by midgame. Tier fees, upkeep and building costs above
   are scaled so that caps are never trivial; re-check against a late-game vanilla save's wealth.
10. **Terminal width and refresh.** Pages are static text; live numbers need the DisplayTerminal hook (untested per
    the brief). Plan a fallback: precomputed pages refreshed with JohnnyGuitar's menu-item edits at the morning
    update.
11. **Unicode sparklines may not render.** Stay ASCII until the font is checked.
12. **Missed-payment ladder vs time away.** A weekly bill falling due while the player is deep in a quest must
    auto-pay from company cash and only warn if cash is short; a short grace of three days is already in the ladder.

---

## 5. Questions only the user can answer

1. Pace: is "about 5 game weeks (28 real hours) to repay the loan" right, or should the first payoff come sooner
   (about 3 weeks) so the player sees tier 2 inside one play session?
2. Are the player's own caps and the company's caps allowed to merge freely (dividends both ways), or should company
   cash be locked away from the player until tier 3?
3. Is the 3,000 / 500 / 4% weekly loan acceptable, or do you want a harsher Drug Wars style (10% a day on a smaller
   sum) for tension?
4. Do you want a cap on how much the player can short-circuit the market by manually spamming a good (a
   per-day volume limit), or should self-inflicted saturation always be allowed?
5. Pre-existing question for the table: after losing the company, start over smaller (my pick) or gone for good? The
   money side needs: legacy = 20% of final net worth in caps.

Sources actually opened: gamebanshee.com/k4cr3, gamewatcher.com/victoria-3-dev-diary-9-national-markets-open-economic-model,
en.wikipedia.org (Drug Wars, Offworld Trading Company, Patrician III, Sunless Sea), beej.us/tmp/drugwars.html. Search
snippets only (weaker): forums.frontier.co.uk, steamcommunity.com and forum.egosoft.com (X4), forums.pcgamer.com and
steamcommunity.com (Anno 1800), pcgamer.com Bannerlord guide (truncated, nothing used from it).

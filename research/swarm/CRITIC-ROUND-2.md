Verdict: REJECT

# Critic round 2: Mojave Caravan Company design (revised DOC-EXPORT.md)

The whole revised doc has been re-read and every round 1 fix checked against the text. All 34 starter-trade resting prices were re-derived from the price formula.

**Where the round 1 blockers stand:**
- **Blocker 1 (nothing to trade at tier 1): closed.**
- **Blocker 2 (the player's wallet): only partly closed.** Money can still reach the company through a door the fix did not cover.
- **Blocker 3 (time away): closed in intent.** But the new strike rule, combined with deferred bills, reopens it as an instant loss.

Both remaining blockers need about a paragraph each to fix. Apart from those two, the doc is close to approval.

## 1. What works

- **The starter trade is sound.**
  - Every resting price in the table matches the formula, for example Goodsprings water 4/34 gives 152, Outpost moonshine 2/0 gives 240, and Primm ammo 3/20 gives 162.
  - The first road now pays both ways: water, healing powder, dirty water and herbs go out; salvaged ammo comes back.
  - Meat, stimpaks and moonshine are left as the prizes of tiers 2 to 4, which is the right shape.
  - Building materials from the Primm salvage yard also free town growth from the Quarry Junction gate.
- **Paid-in capital and earned worth are coherent.**
  - Earned worth starts at −300, and that is fine: climbing out of the hole is a good opening story.
  - Nothing divides by earned worth. The loss cap now uses gross assets, which stay positive.
  - Dividends come out of paid-in capital first, and the owner rescue is booked as paid-in capital, so the bookkeeping holds together.
- **Time away is now humane.**
  - Nothing is served automatically.
  - Bills that cannot be paid while the player is away are deferred.
  - Every cure is on the runner's message box.
  - Field letters wait while the player is in combat, dialogue or a menu.
- **The road risk is one system.**
  - The director places events, and P_clean only resolves an event it placed.
  - There is one loss cap, on gross assets.
  - Rolls are seeded, so reloading a save does not re-roll the day.
  - Named crew cannot die in a real fight.
- **The company now follows the player north.** Relay desks at the 188 and Novac, the tier 4 deed at Camp McCarran, Ride the wagon and the tier perks all do this.
- **M1 is now a real game.** It has a starter trade, a purifier, an apothecary, hiring and one contract type.

## 2. Blocking issues

### 2.1 The wallet still buys immunity and tiers, through sales to the owner and top-ups after the loan

**Sections:**
- Money, "No flipping exploit" ("the company sells to the player at 1.1 times the anchor").
- Adventuring, "supplies from your own warehouse at 1.1 times the anchor".
- Money, "Company cash and your caps are separate" (Alice's covenant, and "once the loan is repaid you may put caps in whenever you like").
- Losing, "Strikes" ("a full pocket can buy time but not immunity").

**Scenario A: dodging a strike while the loan runs.**
- The company is 600 caps short for tomorrow's bill.
- The player buys 3 crates of purified water from their own company at 220 each, putting 660 caps of their own money into company cash.
- The bill is paid, so there is no miss, no strike, and the covenant is never touched.
- The roughly 60 caps of margin per crate are also booked as earned worth.

The covenant limits *owner money* to 500 plus one rescue a season. A purchase is not owner money under the doc's rules, so it slips straight past.

**Scenario B: buying a tier.**
- At the clinic, a crate of stimpaks costs about 105 to make (herbs 60 plus syringes 150 make 2 crates). The owner pays 412 for it, so about 307 per crate lands in earned worth.
- At 10 crates a day, that is roughly 3,000 earned worth a day. A 20,000-cap wallet meets the tier 3 money gate in about three days, and most of the tier 4 one in about a week.
- The player also keeps 50 stimpaks a day.
- Even with water at tier 1, the purchases count as income.

**Scenario C: after the loan.**
- Once the loan is repaid (week 5 to 8), top-ups are allowed at any time.
- A player who tops up before every bill day never misses one, so no strike is ever recorded.
- The doc's own claim, "a full pocket can buy time but not immunity", is therefore false for the rest of the run.

**Fix: keep two cash pots.**
- **Operating cash** is what the company earned. Only operating cash pays bills, and Runway on the front page uses it.
- **Owner funds** are made of three things:
  - the founding 500;
  - every top-up;
  - the margin above cost on any sale to the owner. Book that sale at cost; the rest goes to owner funds.
- Owner funds can buy wagons, buildings and upgrades, never stock and never bills. Selling an owner-funded asset returns the money to owner funds.
- The only way owner funds pay a bill is the cure after a miss, and the strike stands.
- Cap sales to the owner at about 2 crates a day, for the player's own use.

Investment still speeds up earnings, which is fine. It just cannot pay the wages, rescue the company from a strike, or count toward a tier.

### 2.2 Deferred bills are served together, and three strikes at once means an instant takeover

**Sections:** Losing, "Strikes" ("three strikes within 56 days and the creditor takes over at once, wherever the stage clock stands"), and "The served-notice rule and the busy shield" ("a bill that cannot be paid is deferred ... until its notice reaches you").

**Scenario.**
- A tier 2 company that overreached is losing about 200 a week and has 300 in cash.
- The player enters Dead Money for about 15 real hours, which is about 19 game days.
- Two or three bill days pass. Each one is short, so each is deferred, as the doc says.
- The player walks out at the Outpost. A runner finds them and serves the notices, and the notices become three strikes.
- "The creditor takes over at once."
- The player saw no Forecast, no Grace period and no cure.

That breaks three things the doc promises:
- "A player deep in the main quest or a DLC never comes back to a dead company."
- "Both take at least 7 game days of visible warnings."
- Pillar 5, fair failure.

The same thing happens with two deferred strikes plus one older strike. The doc also never says whether a strike's 56 days count from the bill day or the day it is served.

**Fix:**
1. Bills deferred during one absence are served as **one notice and one strike**.
2. A strike's 56-day window counts from the day it is served.
3. A third strike opens a **7-day takeover notice**, not an instant takeover. It can be cured only from operating cash or by selling assets (or by walking away), so the strike rule still cannot be bought off with the player's own caps.

## 3. Non-blocking issues

1. **The busy-shield check is wrong as written (How it is built, The day tick; Losing).** **Fix:** decide whether the player is in DLC content by where their cell or worldspace comes from: a form list of DLC worldspaces and interior cells, or the source plugin of the player's cell. Count DLC main-quest stages only once the player has actually entered the DLC. Fix this before M1, because M1 includes the shield.
   - `GetInWorldspace WastelandNV` returns 0 in every interior cell. That includes the HQ and every branch office, which are all new interiors, plus saloons and the beds players sleep in.
   - Read literally, "nothing is served" while the shield is up means a notice can never be served at a company terminal.
   - The debt and law clocks freeze on any day the tick runs indoors, and most players sleep and wait indoors.
   - "A DLC main quest is running" is also too broad. The DLC start quests, triggered by radio signals, can sit active in the quest log for dozens of hours before the player goes.
   - If built as written, both ways to lose stall, and the dodgy side runs with no raids.
2. **The sealed-crate fee is out of scale at tier 1 (Dodgy slope, rung 2).** **Fix:** set the fee to about one cargo slot's clean margin (40 to 60), or limit runs to one per 3 days.
   - 150 caps a run, against a tired route that nets about 36 caps a day.
   - A run every second day adds about 525 caps a week while heat climbs about 1 point every 2 days, keeping it under 40.
   - Tier 1 becomes a smuggling game, and the dodgy path is simply better there, which is one of the doc's own anti-goals.
3. **Growth projects can become a money pump (Core numbers: "a town's growth project is a standing purchase at the spot price").** **Fix:** project deliveries go into stock and the price is recomputed per crate, or they are paid at a fixed price at the anchor, with a cap per day.
   - If project deliveries do not move stock, each level buys 40, 90 or 160 crates at the empty-shelf price (225).
   - Made at the stone yard for about 60 a crate, that is roughly 48,000 per town, and about 190,000 across four towns.
   - It would be the dominant late-game income.
4. **A raid does not reset heat (The raid; The law ladder).** The doc does not say what heat is after a raid. At heat 80+, a second warrant can follow the first raid within a day, so revocation can come about 2 days after raid 1, against "at least 7 days". **Fix:** a raid sets heat to 50, and no new warrant can be served within 7 days of a raid.
5. **Insurance is priced against the wrong number (Insurance).** Crimson Cover costs "1.15 times the route's expected loss" but pays only 60%, so the player loses about 55% of the expected loss on every policy. Omerta assurance loses about 30%. **Fix:** price each policy on its expected *payout* times 1.15.
6. **Primm ammo without a sheriff has three different numbers (Town table; Starter trade; News).** **Fix:** use one number, and let the M1 re-run use the no-sheriff case.
   - The three are: "+50%" (town table), daily use 3 giving +11% (starter trade), and ×1.4 (news).
   - The simulation used the sheriff price (146), but a new game starts without a sheriff (162).
   - That makes day 1 nearer +580 than +746. This is still inside the target range.
7. **Where is the tier 1 terminal? (Growth table).** Tier 2's world change is "a rented office with a sign and a terminal", yet M1 runs tier 1 from the HQ terminal. **Fix:** say where it is: a back-room terminal at Chet's store, or at the agent's table in the saloon.
8. **Week 2 of the simulation uses tier 2 unlocks before tier 2 (Numbers).** The purifier and the first contract appear in week 2, but tier 2 arrives on day 14. The memo example also offers a contract at tier 1. **Fix:** state in the tier table and in M1 whether one contract type is open at tier 1.
9. **The Outfit perk "buys your loot at company prices" is undefined for loot the company does not trade (Growth, tier perks).** Weapons and armour have no price, nowhere to go, and would drain company cash to the player. **Fix:** trade goods only, under the existing crate rules, or write the rest off at 50% of value.
10. **The front page has more rows than a terminal has buttons (The front page; Terminals).** The front page has 13 button rows, but each terminal form has a pool of 12 ("No screen has more than 12 action slots"). **Fix:** give the front page 13 slots, or fold SETTINGS into another row.
11. **The away mode trigger is ambiguous.** "2 or more game days from any office" could mean time or distance. **Fix:** "2 game days since the player last left an office".
12. **Ride the wagon is not tied to the 06:00 queue.** Can the player ride at 14:00? **Fix:** riding joins the next departure, or the wagon leaves at once and its schedule shifts.

## 4. Bold suggestion

**At tier 4, you become Alice.**
- **How it plays.**
  - Small independent outfits (mod NPC caravans in the lived-in towns pool) ask the company for start-up loans.
  - You set the terms. The same debt ladder code then runs in reverse, with you as the creditor.
  - When an outfit fails, you take its route and its wagon, the way Alice took Cass's.
  - Or you forgive the debt and gain a loyal supplier and town trust.
- **What it does.**
  - It closes the fantasy's loop ("you borrowed money from the wrong woman"), and it gives a moral choice with a ledger price.
  - Lending is a late-game use for surplus cash, so it doubles as a money sink.
  - Alice will notice you are playing her game, which makes a natural grudge flag.
- **Cost.** Low to medium: it reuses the ladder, the notices and the letters.

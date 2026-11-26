Verdict: REJECT

# Critic round 1: Mojave Caravan Company design (DOC-EXPORT.md)

Reviewer stance: systems designer, read the whole doc and the brief, checked specific claims against 01-economy.md, 02-chains.md, 03-risk.md and 04-rival-law.md. Three blocking issues, all fixable without changing the pillars. Most of the design is strong; the blockers sit in the first hour of play (nothing to trade), in the lose condition (the player's pocket voids it), and in time away (a DLC can kill the company).

## 1. What works

- **Letters, memos with cautious defaults, a capped postbag and orders that queue to the 06:00 tick.** This is the right answer to "terminal only" and "the player is away". The queue also kills the press-ten-times price exploit and keeps the scripting simple.
- **The price model is bounded, legible and makes expansion feel necessary.** Price is set per crate, between 0.5x and 1.5x the anchor. Shortages recover faster than gluts. That gives the player a readable reason to open a new route, which is better than an arbitrary decay.
- **Vanilla quests act as deeds, each with a slower way round.** Clearing Quarry Junction or getting Primm a sheriff moves the company, and no tier is locked behind a quest the player skipped. Danger has a colour and a cause the player can go and remove with a gun. This is how "your adventuring feeds the business" should work.
- **The architecture respects FNV's limits.** The company is a simulation on paper. Critical numbers live in quest variables, detail lives in the cosave, and the company is rebuilt if the cosave is lost. Buttons are pre-made pooled slots. M0 proves the risky engine pieces first, and every milestone can ship on its own.
- **The rival is grounded in the game's own notes and escalates in steps the player can see.** "Small and quiet is a valid strategy" is a real decision, and Alice's grudge flags give her a memory without editing her records.
- **Failure has staged, visible warnings, and the lost company becomes a successor chapter, not a game over.** The intent is right. The holes are in the details (see 3.2 and 3.3).

## 2. Blocking issues

### 2.1 Tier 1 has nothing to trade, so M1 has no game

**Sections:** Goods and production chains (goods table, "Bought by" column), The map (town table), Numbers (first week), Build order (M1).

**What the doc says.** Goodsprings supplies dirty water, herbs, maize and brahmin. Primm supplies brahmin, sand and scrap. Mojave Outpost supplies powder, syringes and scrap. The only buyer listed for every raw good is one of the player's own workshops (purifier, apothecary, smokehouse, still, stone yard, reloading bench). Every good a town *wants* is a made good from a tier 2+ workshop: purified water, smoked meat, healing powder, moonshine, ammo and stimpaks. Tier 1 is defined as "None: buy and sell only".

**Scenario.** A tester starts M1 (Goodsprings HQ, Primm branch, one wagon, tiers 1 and 2) and opens the Tape. No good is cheap in one town and wanted in the other, in either direction. The wagon has nothing to earn with while the 420-cap weekly loan bill runs. The M1 pass mark ("survives or loses for reasons they can name") cannot be met, because the reason is the design.

**Why the doc's note does not cover it.** The doc calls the week-1 simulation's cargo list "an early price list ... its shape is the point". It is more than cargo. In 01-economy section 2.11, Goodsprings *sells* purified water and healing powder and Primm *sells* ammo. The final tables moved all three into tier 2-4 workshops, which removes both legs of the only trade. 02-chains (line 125) had the peddler crafting at a campfire, and the doc dropped that too. The 3,000-cap loan, the 4% rate, the tier 2 timing and the "tired route nets about 250 a week" target were all calibrated on trade that no longer exists. On the Goodsprings-Primm road there is also no back-haul until the Primm smokehouse at tier 3.

**Second problem in the same place.** M1 claims tiers 1 and 2, but everything tier 2 unlocks is in M2: purifier and apothecary, staff numbers and hiring, and contracts. M1's tier 2 therefore unlocks nothing.

**Fix:**
- **(a) Write a starter trade matrix into the town table.**
  - Each town has a small natural surplus of one or two finished vanilla goods. For example:
    - Goodsprings: purified water from the spring and healing powder made by the settlers (01-economy's N 34 and 18).
    - Primm: salvaged ammo.
    - Outpost: NCR surplus goods at list price.
  - Each town also uses a little of some raws (Primm buys herbs and dirty water for its own use), so a back-haul exists.
  - At tier 2 your own purifier and apothecary then beat the town's small surplus on volume and margin. That is the felt upgrade.
- **(b) Publish the per-town `cons` and N table for every good.** That is 4 towns x 17 goods; 01-economy gives only 4 goods x 2 towns.
- **(c) Re-run the week-1 simulation on the final tables first.** Only then fix the loan size, the interest rate and the tier 2 gate.
- **(d) Fix M1's scope.** Either move the purifier, apothecary, basic hiring and one contract type into M1, or make M1 "tier 1 only".

### 2.2 The player's pocket is a bottomless bailout and maybe a tier skip, so losing is opt-in

**Sections:** Money ("Company cash and your caps are separate"), Losing and coming back (cure 4 "Your own caps"; the successor chapter), Growth (net-worth gates).

**What the doc says.** "Your own caps can rescue the company." Cure 4 is interest-free with no limit; its only cost is "no dividends until you are off probation". The doc never says whether the player can also put caps in at any other time; the founding has them put in 500. 01-economy pitfall 9 already warns that "Vanilla players have 10,000+ caps by midgame", and the casinos add more. 01-economy question 2 (can caps move freely both ways?) was never settled. The doc also dropped the research's tier fees, which were the money sink scaled against that wealth.

**Scenario 1.** In week 3 a wagon is lost and the player is 600 short on bill day. At Final notice they move 600 from a 7,000-cap pocket. Probation costs nothing, because they never needed dividends. This repeats after every bad week.
- On the clean path, debt is the only way to lose, and it never happens unless the player chooses it.
- The law loss is opt-in by definition, since it only follows from dodgy play.
- The user's first requirement was "a lose condition with real progression". As written there is none for a player with an ordinary FNV wallet.

**Scenario 2.** If caps can go in at will, a player comes back from the Strip with 20,000 caps, puts in 8,000, and meets the money gate for tier 3 the next morning. The number that is meant to make growth felt has been bought. The successor chapter has the same hole: "you keep your own caps" plus a buy-back of the office at twice its price means a rich player loses nothing.

**Fix:**
1. Book owner money as an owner loan (debt) or as paid-in capital. Base tier gates, records and the net-worth sparkline on **earned worth** (net worth minus paid-in capital).
2. Allow an owner rescue once per season, up to 2 weeks of bills. It cures the notice, but **the missed bill stays on record as a strike**.
3. Let strikes end the company, not arrears. Three missed bill days in 56 days means the creditor takes over, whoever paid. Alice can say it: "I lent to a company, Courier, not to your pocket." After the loan is repaid, staff count the strikes (late wages lead to walk-offs) and so does the NCR receiver.
4. State plainly whether the player can put caps in at will. The pocket stays a lifeline the player feels, not a permanent shield.

### 2.3 Time away is not safe: the 10-day auto-serve runs the whole debt ladder while the player is locked in a DLC

**Sections:** Away from the desk, Losing and coming back (the served-notice rule), How it is built (the day tick).

**What the doc says.** A stage clock starts when the player opens a terminal, when a runner finds them, or when 10 game days pass and a Pip-Boy note fires. From the serve to receivership is 7 days. The cures are a terminal menu.
- So the company can end 17 game days after a missed bill day without the player being able to act at all.
- At timescale 30, one real hour is 1.25 game days. Dead Money cannot be left until it ends, and it and the other DLCs take many real hours, which is 10 to 20 game days plus sleep. The doc itself mentions "a month in the Divide".

**Scenario.** On day 20 the company is slightly cash-negative: a tired route nets about +250 a week against a 420 loan bill. The player enters the Sierra Madre, and the day-21 bill is missed. On day 31 the Pip-Boy note fires inside the Villa, and on day 38 the company goes into receivership. The player walks out of Dead Money to a Crimson Caravan sign on their office. This breaks two promises the doc makes:
- "A player deep in the main quest can never come back to a dead company."
- The anti-goal "Punishing the player for being away".

**A related gap.** Field message boxes can fire during combat or dialogue. The research's "Busy shield" (03-risk line 124) froze the ladder clocks during main and DLC quests and capped paper losses there; it was dropped from the doc.

**Fix:**
1. No auto-serve, and frozen ladder clocks, while the player is outside the Mojave worldspace (a `GetInWorldspace WastelandNV` check) or in a DLC main quest. Field letters wait while the player is in combat, dialogue or a menu.
2. Bills that come due while the player is away auto-pay. A bill that cannot be paid becomes "deferred" (a late fee only) until the notice is served in person or by a runner.
3. Every cure must be reachable from the field message box: own caps, sell an asset, a rescue loan, walk away. A served notice must always be something the player can act on where it reached them.
4. Port the Busy shield from 03-risk into the doc.

## 3. Non-blocking issues

1. **Road risk is two systems with three different loss caps (The road; Loss limits; Balance targets; Insurance).**
   - **Two systems.** The doc never says whether P_clean is rolled on every run or only on events the director places. 03-risk meant the second. Read as "every run", even cover fails half of all runs and one in six loses the wagon, which breaks the director's pacing rules.
   - **Three caps that disagree:**
     - 30% of net worth: 60 caps on day 0, and undefined when net worth is negative, which a company carrying the loan often is.
     - "3 days of runway".
     - "One failure in three loses the wagon": a 400-cap wagon cannot be lost under the 30% cap until net worth is about 1,400.
   - **Insurance pays on average.** At 3% for 60% cover it wins whenever the clean chance is under about 90%. At 69% clean, the expected payout is about 10% of the cargo against a 3% premium.
   - **Fix:** "The director picks the event and the road; P_clean resolves it". Use one cap on gross assets, not net worth. Put 03-risk's cover and danger values into the doc. Price each route's insurance at about 1.15 times its own expected loss.
2. **Save-scumming the tick (The day tick).** Save at 05:59, wait, see the wagon lost, reload, wait again for a fresh roll. FNV's autosave on wait and sleep makes this effortless. **Fix:** seed every roll from a stored company seed plus the day plus the route or event ID, so a reload gives the same result unless the orders changed.
3. **Away mode is a free safety switch (Away from the desk).** Set "I'll be gone a week" at the HQ, wait 7 x 24 hours, and the threat is halved at no cost. **Fix:** away mode only takes effect once the player is 2 or more days and some distance from any office. Its cost is explicit (profit x0.85, no new contracts). Coming back early ends it.
4. **The daily orders have no default (A visit; The terminal).** Memos have defaults; orders do not. Each order means wagon, then road, then good, then quantity on nested screens, about 5 or 6 typed-out presses per wagon per day until managers arrive at tier 3. **Fix:** a "Bookkeeper's plan" row on Routes. The bookkeeper drafts tomorrow from the Tape; one press accepts it, and the player edits only what they want to change.
5. **The company leaves the player's path after tier 2 (The map; Adventuring; Where the player can open it).**
   - The main quest takes the player out of the south within about 5 to 10 real hours, so tiers 3 to 5 happen while they are in Vegas and the north. There is no office, road or deed up there except House's representative at tier 5.
   - If the Pip-Boy ledger test fails, "branch terminals are the design" turns the company into a commute.
   - **Fix:** make the field message-box desk a real fallback: front page, memos, cures and "accept plan". Add a thin northern presence at launch: a terminal at a Novac or 188 relay desk, and NCR deliveries to Camp McCarran as in-person deeds.
6. **Where is the loan signed? (Fantasy; Tier 1 gate; Lore safety).** Alice sits at the Crimson Caravan compound by Freeside, a long and dangerous walk for a level 2 Courier. The doc wants the company met on day one. **Fix:** a Crimson Caravan agent at the Prospector Saloon offers Alice's letter of credit, and Alice appears in person later.
7. **FNV ends at the Dam (After the Hoover Dam; Laws; The ending; decision 12).**
   - Vanilla has no play after the Battle of Hoover Dam, so the regime switch cannot run.
   - "When the main quest ends, the bookkeeper writes a closing page" cannot run either.
   - **Fix:** tie the regimes to the faction lock-in before the Dam, or cut them. Trigger "20 years on" from Retire or from the point-of-no-return warning.
8. **Building materials gate everything, and they depend on Quarry Junction (Workshop levels; Town growth; Tier 3 world change).**
   - Level 2 workshops (20 materials), town growth (40 to 160) and tier 3's "houses built from your stone" all need stone. Stone needs the Quarry Junction deathclaws dead (a high-level fight) or a 2,500-cap hunting party.
   - Most players will reach tier 3 with every workshop at level 1 and no town growth.
   - **Fix:** a low-grade materials source not gated on Quarry Junction (salvaged timber and brick at Primm), or caps-only level 2 workshops.
9. **The dodgy side barely exists before tier 4 at launch (the slope; decision 8).**
   - Before the reloading bench and the still, the only dodgy options are under-declaring and "unlicensed water". The water licence does not exist anywhere in the NCR tools.
   - The Powder Ganger landlord start's "cheap powder from day one" has no use until tier 4.
   - **Fix:** a tier 1-2 smuggling job (carry sealed Powder Ganger or Omerta crates for a flat fee plus heat). Define the water licence or drop that rung.
10. **Holes in the law ladder (Heat; The raid).**
    - "First raid always real, at HQ" can be dodged forever by using only branch terminals and the ledger, leaving heat at 100 with no raid.
    - "Heat cannot jump 60 to 80 in a week" is not enforced: a tip-off adds 15 and every black-market sale adds heat.
    - Paper raids "seize" while the player is away, which contradicts the served-notice rule.
    - **Fix:** the raid happens at the next office the player enters, or on paper 7 days after a served warrant. Cap net heat gain at +5 a day.
11. **Contracts are an uncapped second market (Money: contracts).** Contract deliveries do not move spot stock, and there is no volume limit, so a player stacks contracts on one town and spot-sells into it as well. **Fix:** contract volume per town and good is capped at 50% of `cons`, and it counts toward market share and the rival's view.
12. **Core variables are undefined (Growth gates; Towns; Chains).** **Fix:** one variables table (scale, sources, sinks, starting value). The missing ones:
    - Town trust: its scale, how it is earned, and what "Liked" means.
    - Favour: how much each contract earns.
    - The denominator for market share.
    - Raw sites: cost, output and staff.
    - Workshop capacity: input crates or output crates?
    - Building materials: sold to towns ("bought by every town") or donated (the "town building projects" sink)?
13. **Numbers and words that disagree.** **Fix:** one consistency pass; rename the automation rules "house rules" and the permadeath setting "Ironman".
    - Tier 2 "in week 1" versus the simulation's net worth of 923 on day 7 and "about 2,000 by day 14".
    - Decrees every 14 days (NCR tools) versus every 28 (the season table).
    - Wages "paid per day" versus the weekly wage bill.
    - "A careless player sees a Forecast warning by week 3" versus a tired route that burns about 150 caps a week from 2,900 in cash and never runs dry before the loan is paid.
    - Workshops for "imports at the Outpost", but no Outpost workshop exists.
    - "Standing order" means both the player's automation rules and a buyer's contract.
    - "Hardcore" collides with FNV's own Hardcore mode.
14. **Placed hires versus spawned crews (People; The road; The world).** Ruth Coyle has a bed in Primm, so a PlaceAtMe crew makes a second Ruth on the road, and the town shows her at home while she is "on a trip". **Fix:**
    - Hires are persistent references, disabled at home during a paper trip.
    - A real encounter moves the real references (MoveTo).
    - Named crew are essential during real fights, so being there is never worse than the paper result.
15. **Goods exchanged with the player are undefined (No flipping exploit).** "Buys from the player at 0.8, at most 10 crates a day" does not say which items make a crate. A player could sell 1,000 looted rounds of a cheap calibre as 10 ammo crates for 1,600 caps a day. **Fix:** map each crate good to one vanilla item and count, price ammo per calibre, and refuse calibres the company does not make.
16. **The endgame and the successor are underspecified (End of the rivalry; Patrons; Successor).**
    - The takeover ("share blocks", "board votes") has no rules.
    - The merger's new rival (Gun Runners and Van Graffs) has no moves.
    - The successor loses every building, so it has no terminal to run the company from.
    - Patrons give cash at the tier where cash matters least.
    - **Fix:**
      - The takeover is three share blocks, each a deed plus a price.
      - The new rival reuses the move table.
      - The successor runs from the loyal manager's house terminal.
      - Patrons grant abilities instead of cash: Securitron escorts, preferred-carrier status, a fence on the Strip.

## 4. Bold suggestions

1. **Ride the wagon.**
   - **How it plays.** A Routes row reads "Ride with wagon 2 to Primm". The screen fades, game time runs to the arrival, and the player steps off at the destination with the crew. If the director rolled an event on that road, the player is dropped mid-route into it, with the crew spawned around them.
   - **What it fixes.**
     - The real road becomes something the player chooses to see, not luck of being nearby.
     - The early southern game gets a reason to use your own wagons instead of fast travel.
     - Later, wagons to Novac and McCarran become the company's reach north.
   - **Cost.** It is FNV-native (fade to black, advance the time, MoveTo a marker) and reuses the road-crew spawn. Medium.
2. **The company makes you a different Courier.** FNV caps are abundant, so dividends mean little. Instead, each tier grants one power that changes how you play Fallout:
   - Outfit: your traders buy your loot at company prices in towns where you hold 20% share.
   - Caravan company: wagons haul your loot from any branch, a remote stash.
   - Trading house: discounts in towns you lead.
   - Mojave concern: crew reports put ambush and raider-camp markers on your map, or a company guard joins you as a light companion.

   This keeps the company relevant to the RPG during the hours the player spends in the north.

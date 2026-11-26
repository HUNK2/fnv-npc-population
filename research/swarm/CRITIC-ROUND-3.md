Verdict: APPROVE

# Critic round 3: Mojave Caravan Company design (final revision of DOC-EXPORT.md)

I re-read the whole revised doc and checked both round 2 fixes against every place that money and clocks touch.

- **Both round 2 blockers are closed.**
- **No new blocking flaw.**
- **Seven non-blocking items remain.** The first two should be fixed in the doc before M1, because they are one-line fixes to rules M1 builds: the busy shield, and the tier 4 deed. Everything else is clarity or tuning.

## 1. What works

- **The wallet hole is shut.** I looked for every route by which owner money could reach a bill and found none left open:
  - Only operating cash pays bills, stock and wages, and Runway counts only operating cash.
  - Owner funds buy fixed assets only, and selling an owner-funded asset returns the money to owner funds.
  - Sales to the player are capped at 2 crates a day and booked at cost, with the margin going to owner funds. The player's wallet can no longer pay the company's bills or add to earned worth.
  - The owner rescue is once a season, and the strike stands.
  - The takeover notice can never be cured with owner money.
  - Earned worth stays consistent through all of these, and dividends come out of owner funds first.
  - A full pocket now speeds up growth but cannot keep a failing company alive. That is exactly the user's "real lose condition".
- **Strikes are fair.**
  - One absence gives one notice and one strike.
  - The 56 days count from the day the notice is served.
  - A third strike opens a 7-day takeover notice rather than ending the company at once, so "at least 7 days of warnings" now holds on every path.
- **The law ladder's minimum now holds.** A raid sets heat to 50, and no new warrant can be served for 7 days. With heat gain capped at +3 a day, there are at least about 10 days between the two raids that revoke the licence.
- **The busy shield is buildable.** DLC lands are judged by the source of the player's cell, and company terminals can always serve notices.
- **Round 2's money pumps are shut.** Growth projects now pay the anchor price, 4 crates a day. Insurance is priced on expected payout.
- **The design as a whole is strong.**
  - The early game is playable: starter trade, the bookkeeper's plan, one contract type.
  - The company follows the player north: relay desks, Ride the wagon, tier perks.
  - Failure is legible.
  - The rival has a face and a memory.
  - The milestones each ship on their own.

## 2. Blocking issues

None.

## 3. Non-blocking issues

1. **Fix before M1: the busy shield can be lived in (The day tick; Losing: "the served-notice rule and the busy shield").**
   - **The problem.** The shield is up whenever the 06:00 tick finds the player in a DLC's lands. Old World Blues' Sink, Zion and the Divide can all be revisited after their DLC is finished, and the Sink is one of FNV's most popular player homes.
   - **What goes wrong.** A player who sleeps in the Sink is shielded at every tick:
     - Debt and law clocks never advance, so a warrant's 7-day paper raid never comes.
     - Paper losses are capped at one day's profit.
     - The company cannot fail, and the dodgy side runs with no risk. The player never knows why.
   - **Fix:**
     - The shield covers a DLC's lands only while that DLC cannot be left, which means until its main quest is done.
     - After that, being in those lands counts as ordinary time away. Runners cannot reach the player, so new bills defer, but clocks on notices already served keep running, and paper losses are not capped.
     - Update the stale Risks row as well ("freezes every clock outside the Mojave and in DLC main quests").
2. **Fix before M1: the tier 4 deed needs an NCR contract, but NCR bids only open at tier 4 (Money: contracts; Growth table; NCR tools).**
   - Read literally, tier 4 cannot be reached.
   - The "slower way round" list ("an NCR contract in person ... already open to every player") shows the intent.
   - **Fix:** once the player holds Mojave Outpost clearance at tier 3, the NCR desk offers one trial contract (for example, water for the garrison). Delivering it in person is the deed. The NCR Treasury rescue loan's "two NCR contracts a week" are assigned contracts, not bids; say so.
3. **What counts as operating cash (Money: two cash pots).** The doc defines operating cash as "the money the company earned", which literally excludes Alice's 3,000 loan, rescue loans and contract advances. Under that reading the company could not buy stock on day 1, and the loan cures would not work. **Fix:**
   - Loans and advances land in operating cash.
   - The front page's CASH is operating cash; owner funds are shown on the Ledger screen.
   - Say whether a rescue loan can cure the 7-day takeover notice, and that the notice replaces the normal debt ladder for that miss, so the two never run side by side.
4. **The heat table and the first-raid rule lag behind the warrant rule (Heat table; The raid; decision 6).** **Fix:** heat 80+ serves a warrant, and the raid then follows the warrant rule. The first raid is real if the player enters an office within the 7 days, and on paper otherwise.
   - "80 to 99: a raid within 2 to 5 days" and "100: raid at the next morning tick" contradict the rule that a raid comes at the next office the player enters, or on paper 7 days after the warrant.
   - "Always real the first time" contradicts the paper fallback.
5. **The sealed-crate job carries no risk (dodgy slope, rung 2).** **Fix:** a 10% search chance on every run at any heat (a fine plus heat +10), or a fee that shrinks when heat is under 20.
   - Each run adds heat +5, and runs are limited to one every 3 days.
   - Heat falls 2 a day, so it drains back to about zero before the next run.
   - The job pays about +117 a week (roughly +47% on a tired route) with no trade-off, so the first dodgy step is simply better than staying clean, which is one of the doc's own anti-goals.
6. **Lending has no milestone and no rules (Late game: "Lending: you become Alice").** It appears in no milestone, and it does not say how a borrowing outfit earns money or what you get back when it fails. Predatory terms would guarantee a seized wagon and route. **Fix:**
   - Put it in M4.
   - Give each outfit one ledger line: a weekly profit roll against its instalment, more likely to fail on harsher terms.
   - Cap what you recover at the principal still owed.
   - Seizing an outfit is a grudge flag with that town.
7. **The Crimson Caravan's own supply is never given (Rival; Ending the rivalry; Market share).** Three rules need her per-town share, and there are no numbers for it or for how her moves change it:
   - "lead her in three towns" (the merger);
   - "lead Alice in Primm for 14 days" (a takeover block);
   - the price-war trigger.

   **Fix:** give her starting share per town and good (for example 30% of daily use in Primm and the Outpost, 10% in Goodsprings and Sloan), feeding the same stock numbers, and show how each of her moves changes it.

## 4. Bold suggestion

**Cassidy Caravans, reborn.**
- **How it plays.**
  - If Heartache by the Number ends with Alice exposed, a new mod-quest topic lets Cass (as a companion, not a hire) offer to put her family name on your company.
  - Accept, and the sign over your door changes to "Cassidy Caravans". Alice's aggression gets a permanent +15, but Cass's old contacts open a supplier in Primm.
  - At "20 years on", the epilogue line is about Cass, not Alice.
- **Why it fits.** It respects every constraint: no vanilla record is edited, Cass is not hired, and the mod only reads quest stages. It turns the vanilla quest the design keeps walking around into the company's emotional peak.
- **Cost.** Low: one topic, one sign swap, a few letters.

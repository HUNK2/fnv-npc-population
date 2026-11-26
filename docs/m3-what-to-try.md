# M3 The rival and the law: what to try

M3 adds the Crimson Caravan as a rival and the NCR as the law. All of it starts at tier 3 (the
caravan company), so nothing changes below it. The numbers were checked by script against the model
in `tools/company_model.py` and `tools/law_model.py` (`tools/test_m3_law.py`, `tools/balance_run.py`,
and in the game `tools/ingame_m3.py`). These are the things worth seeing with your own eyes.

## Before you start

- The same plugins as M2. An M2 save gets the M3 ledger the first time it loads: heat 0,
  aggression 20, NCR standing 30, and if it is at tier 3 already, an inspection 30 days out.
- Tier 3 is still worth 18,000, two towns Liked (trust 50) and a sheriff in Primm.

## 1. The new rows

At tier 3 the front page's last row reads `TOWNS  N trusted, heat H, NCR S`. The Towns screen has
five more rows under the sell rows:

| Row | What it does |
| --- | --- |
| `RIVAL  anger A` | the Crimson Caravan's aggression; `war XX to day D` while a price war runs |
| `DECLARE  100% of sales` | select: 100, 90, 80%. Hiding sales lowers the NCR duty but makes heat |
| `SEALED  crates OFF` | select: a sealed crate on the Primm road, 50 off the books, at most every 3 days |
| `COVER  Crimson Cover OFF` | select: 40 a running wagon a week; pays back 60% of a road loss |
| `NCR  standing S, inspect day D` | the NCR's opinion of you, and the next inspection |

## 2. The rival

Sell more than a quarter of a town's weekly use and keep growing, and her aggression climbs 10 a
week. From 30 she moves once a week:

- a **price war** in your biggest town: 15% off everything you sell there for 5 days (20% if you
  bought Crimson Cover: she reads your manifests). Contract prices stay as signed.
- or a **poach**: Alice courts the least loyal person under 40. The report names them; raise their
  loyalty to 40 by the next morning (a raise, paid wages) or they leave.

Look for: the war line in the morning report and the `war` tag on the RIVAL row, and prices on the
Prices screen dropping in that town for the five days.

## 3. The NCR

- The licence is 400 a season at tier 3 (900 at tier 4), and the Outpost road pays a 20 cap toll
  each run.
- Every 30 days (10 when heat is 20 or more) the NCR inspects the books. Hidden sales or unpaid
  bills are a fault: the first is a warning, the next ones fine 5% of the last week's sales.
- On day 5 of each week, when the Outpost road runs and heat is under 60, a memo `NCR BID: OUTPOST
  AMMO` asks for 4 crates of ammo every 3 days for 14 days. Bid 1.3 times the market, or 1.2 to
  beat the Crimson Caravan once her aggression is 40. Each delivery is +2 NCR standing.

## 4. Heat, warrants and raids

Heat comes from hiding sales (2 a week per 10% hidden) and sealed runs (5 each; a patrol search
adds 10 and a 100 cap fine). It cools 1 a day, 2 after 7 clean days. At heat 80 a warrant is served:
a letter, and a memo `WARRANT SERVED  raid in 7d`.

- Pay a fixer 300 and the papers get lost: heat drops to 50.
- Or let them come: on the day, guard cover 60 or more holds them off, and you are outlaws (NCR
  standing 0, no more NCR bids). Under 60 they take a fifth of the cash. A second raid within 28 days
  revokes the licence and closes the company.

Look for: the warrant letter in the field, right after any debt notice in priority.

## 5. Tier 4: the trading house

Worth 40,000 earned, the loan repaid, no arrears, NCR standing 50, at least one NCR delivery, not
outlaws and no recent strike. The letter says the toll is gone and the licence is 900 a season.

## Known limits

- The rival is in the ledger only: there are no Crimson Caravan wagons on the roads.
- Raids happen on paper; nobody comes to the office.
- Forward contracts and meeting the rival in person are M4.

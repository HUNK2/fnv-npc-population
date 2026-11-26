# M4 The late game and the ending: what to try

M4 adds what a big company does with its money and its name: forward tickets from tier 3, the NCR
quartermaster, lending to small outfits and buying out the Crimson Caravan from tier 4, laws and
retiring at tier 5, and the "20 years on" letters when the company ends. Below tier 3 nothing changes.
The numbers were checked by script against the model in `tools/company_model.py`,
`tools/late_model.py` and `tools/ending_model.py` (`tools/test_m4_late.py`, `tools/balance_run.py`,
and in the game `tools/ingame_m4.py`). These are the things worth seeing with your own eyes.

## Before you start

- The same plugins as M3. An M3 save gets the M4 ledger (the CCLate quest) the first time it loads:
  no tickets, no loans, favour 0, no laws, no share blocks.
- Tier 4 is still worth 40,000 with the loan repaid, NCR standing 50 and an NCR delivery made.
  Tier 5 is earned worth 80,000 after the late debts, a bigger share than hers in three towns,
  all three share blocks or the quartermaster kept 28 days, no outlaw mark and no recent strike.
- A good company in the model reaches tier 4 near day 57 and tier 5 near day 80.

## 1. Forward tickets (tier 3)

On day 2 of a week a memo may ask for 12 crates of one good in one town within 10 days, at 10% over
the normal price. It is only offered when a running road's other end sells that good for less.

- `accept`, or `accept with an advance of N` (half the ticket's value now, earned back crate by crate).
- The Contracts screen lists each ticket as `FWD PR water 4/12 by 31`.
- The bookkeeper's plan loads ticket crates first. Crates carried into the town go to the ticket
  before the market (the market price there does not move).
- A missed ticket costs a quarter of what is left and 5 trust; an unearned advance becomes arrears.

## 2. The NCR quartermaster (tier 4)

With NCR standing 60 and no outlaw mark, a memo offers 10,000 caps at 2% a week, repaid 500 a week
on bill day. His string: heat under 20 and never outlaws. Break it and the rest is due at once
(arrears) and standing drops 30. Keep him 28 days and the ending says so.

## 3. Lending (tier 4)

Every 2 weeks an outfit (Harlan Freight, Primm Haulers, Sloan Stone Co., Outpost Supply) asks to
borrow 1,000 to 3,000 over 8 weeks. Lend at 2%, 4% or 8% a week: the higher the rate, the likelier
they miss a week (10, 20, 35 in 100). Two misses in a row and a memo asks: seize the wagon (half the
loan, at most what is owed, and the town's trust drops 10) or forgive it (trust +10). The report
line says what they paid.

## 4. Buying her out (tier 4)

The Towns screen gains `SHARES  N of 3`. Each block has a deed first:

| Block | Deed | Price |
| --- | --- | --- |
| 1 | lead her in Primm for two bill days in a row | 5,000 |
| 2 | beat her to an NCR bid with the low bid while her anger is 40 or more | 10,000 |
| 3 | hold two blocks | 15,000 |

When the deed is done the row reads `BUY a block for N`: select it. After the third block her
board votes her out: no more anger, price wars or poaching.

## 5. Laws (tier 5)

Each NCR delivery earns favour. The Towns screen's `LAWS  favour F: PASS <law>` row spends 5 favour
(once every 28 days) on the next law, in order:

- Free trade act: the NCR duty is halved.
- Carrier act: no more licence fee.
- Press audit: her anger drops 20.

## 6. Retiring and the ending

At tier 5 the Settings screen has `RETIRE  hand the company on`; select it twice. The company closes
and the Post keeps the last letters: three "20 years on" pages written from the company's history
(how it ended, the towns, the roads, the crew, Alice, the NCR, the patron, the loans, the close).
Any other ending (receivership, takeover, walking away, a revoked licence) writes them too. The
closed terminal's `POST  the last letters` row opens them.

Worth trying:

- Retire with three towns trusted, then again (another save) after a receivership: the pages differ.
- Let a poached person go to her: the ending names them.
- Take the quartermaster's deal and keep heat under 20 for 4 weeks, then retire.

## Known limits

- The side you took at Hoover Dam is not read yet, so the ending's side line never shows.
- A seed whose candidates never include a clerk never runs a second wagon (seed 77, an M2 limit).

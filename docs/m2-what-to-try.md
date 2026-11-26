# M2 Chains and people: what to try

M2 grows the company from one road to three. Everything below was checked by script in a fresh
game (`tools/ingame_m2.py`, `tools/ingame_run.py`, `tools/ingame_upgrade.py`) against the model in
`tools/company_model.py`; these are the things worth seeing with your own eyes.

## Before you start

- The same plugins as M1: `LivedInMojave.esm`, then `MojaveCaravanCompany.esp`.
- An M1 save upgrades itself the first time it loads: cash, loan, stock, staff and Primm's
  contract stay as they were. A letter is not shown for it.

## 1. Tier 2: the new rows

Reach tier 2 as in M1 (worth 1,500 earned, Goodsprings trust 50, Ghost Town Gunfight done, no
strike in 56 days). Then open the terminal.

Look for: a new last row on the front page, `TOWNS  N trusted, managers M of 2`. ROUTES now has a
row for the Sloan road (`SLOAN ROAD  BUY a wagon for 700`) and one for the Outpost road (opens at
tier 3). BUILD lists ten buildings: the M1 four, then the corral, sand pit and scrap yard (tier 2),
the smokehouse (tier 3) and the quarry and stone yard (tier 3 and the Quarry Junction deed).

## 2. A second wagon

1. ROUTES, then the Sloan road row: 700 caps from your own money first, then the company's cash.
2. STAFF, HIRE: a wagon needs a driver, and each wagon after the first needs a clerk. From tier 2
   the candidates have Nerve and a trait, and you choose a fair, low or generous offer (loyalty
   starts at 55, 45 or 65).

Look for: the wagon row reading `idle` until it has a driver and a clerk, then `runs`. The morning
report then says how many wagons ran ("Boss. 2 wagons ran: ...").

## 3. The Towns screen

- Each town's level (Camp, Hamlet, Village, Town) and trust. Keep a town's water, meat and healing
  powder at 2 days of use for 7 days and deliver building materials to grow it a level.
- BOOKKEEPER: hire for 40 a day; each select moves Strict, Normal, Lenient. Strict finds skimmers
  every week but costs each clerk loyalty.
- ROUTE MGR (tier 3): answers the road memos itself (Safe keeps the wagon home, Balanced hires a gun
  when the odds are bad, Fast always sends).
- SELL rows: sell the company 10 purified water for 160 or 10 healing powder for 80, up to 10 crates
  a day. The caps go into your pocket, the crate into the Goodsprings warehouse.

## 4. People

- Wes Harlan and Marisol, who live in Goodsprings, are among the candidates from tier 2. They keep
  their routine in town.
- Loyalty moves with pay, offers and the bookkeeper; under 35 a person asks for a raise (a memo),
  under 20 they leave. If the Powder Gangers take Goodsprings, the residents on the books leave with
  the town.

## 5. Tier 3

Worth 18,000 earned, trust 50 in two towns and a sheriff in Primm. Then the Outpost road, the
smokehouse and the route manager open.

## 6. Branches, relay desks and the strongroom

Every company terminal opens the same company, so you never have to walk back to Goodsprings.

| Where | What | Spot |
| --- | --- | --- |
| Primm | branch | the Vikki and Vance cashier counter |
| Sloan | branch | Chomps Lewis's checkpoint table |
| Mojave Outpost | branch | the end of the barracks bar |
| 188 Trading Post | relay desk | the bar on the overpass |
| Novac | relay desk | the Dino Dee-lite front desk |

From tier 3 the footlocker beside each branch terminal (Primm, Sloan, the Outpost), "Company
strongroom chest", opens the safe in the Goodsprings office: one stash you can reach from any
branch. Below tier 3 it says when it opens. Worth trying: put something in at Primm, then take it
out at the Outpost.

## Known gaps

See `docs/PROGRESS.md`, "Open items for the final report".

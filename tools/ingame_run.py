"""Run the company in the game for N days and compare each day with tools/company_model.py.

Founds the company in the running game (CCCore) with seed 1234 and the daily plan on, jumps the
clock one day at a time, reads the day history arrays and checks them against the model (no
sheriff: a fresh coc start has not done My Kind of Town). Needs a game started fresh with
MojaveCaravanCompany.esp loaded. A run already finished with the test seed is only read back.
Run with fnv-mcp's Python:

    <fnv-mcp>/bridge/.venv/Scripts/python.exe tools/ingame_run.py [days]
"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import company_model as cm                  # noqa: E402
import live                                 # noqa: E402

EVENTS = {'': 0, 'bandits_driven_off': 1, 'bandits_took_cargo': 2, 'bandits_wreck': 3}
FIELDS = ('aHistCash', 'aHistSales', 'aHistCosts', 'aHistEvent', 'aHistLoss')


def model_days(days):
    c = cm.Company(live.SEED, sheriff=False)
    c.found()
    c.auto = True
    rows = []
    for _ in range(days):
        r = c.tick()
        rows.append((r.cash, r.sales, r.costs, EVENTS[r.event], r.event_loss))
    return rows


async def read_days(s, days, first=0):
    game = []
    for i in range(first, days):
        row = []
        for f in FIELDS:
            row.append(int(await s.value('CCCore.%s[%d]' % (f, i))))
        game.append(tuple(row))
    return game


async def run(days):
    async with live.session() as s:
        await s.to_game_mode()
        done = await s.value('ar_Size CCCore.aHistCash')
        if await s.value('CCCore.iFounded') and await s.value('CCCore.iSeed') == live.SEED and done >= days:
            print('reading a finished run (%d days in the game)' % done)
        else:
            await s.found(auto=1)
            print('founded: cash %d owner %d loan %d' % (await s.value('CCCore.iCash'),
                                                        await s.value('CCCore.iOwner'),
                                                        await s.value('CCCore.iLoan')))
            for _ in range(days):
                await s.next_day()
        return await read_days(s, days), await s.script_errors()


def compare(game, model, first_day=1):
    bad = 0
    print('day  game (cash sales costs event loss)        model')
    for d, (g, m) in enumerate(zip(game, model), first_day):
        bad += g != m
        print('%3d  %-38s %s%s' % (d, g, m, '' if g == m else '   <-- differs'))
    return bad


def main(argv):
    days = int(argv[0]) if argv else 14
    game, errors = asyncio.run(run(days))
    bad = compare(game, model_days(days))
    print('script errors: %d' % len(errors))
    for e in errors[:10]:
        print('  ', e)
    print('MATCH' if not bad and not errors else 'DIFFERS on %d day(s)' % bad)
    return 0 if not bad and not errors else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

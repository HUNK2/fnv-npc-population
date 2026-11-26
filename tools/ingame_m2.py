"""Check the M2 company in the game against tools/company_model.py (M2 tasks 2.3 to 2.6).

Needs a fresh game with MojaveCaravanCompany.esp loaded and no company (for example started with
coc GSProspectorSaloonInterior). Founds the company with the test seed and the daily plan on, and
completes Ghost Town Gunfight (CompleteQuest VMS16) first, as a test shortcut for the deed.

  every day   numbers, the letter shown, trust in the four towns, the tier and cash match the model
  day 3       Primm's contract accepted on the Memos screen
  tier 2 day  the front page (TOWNS row), Routes: buy the Sloan road's wagon; Build: the corral, the
              well rig and the purifier; Towns: hire the bookkeeper, sell two crates of purified
              water; Staff: hire a driver and a clerk
              when the week's candidates have one
  then        every day to day 28, with the 48 warehouse cells compared
Run with fnv-mcp's Python:

    <fnv-mcp>/bridge/.venv/Scripts/python.exe tools/ingame_m2.py [last day]
"""
import asyncio
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import company_model as cm                  # noqa: E402
import ingame_run                           # noqa: E402
import live                                 # noqa: E402
import post_model as pm                     # noqa: E402
import terminal_model as tm                 # noqa: E402
from ingame_ladder import Checks, box, open_terminal, pocket, read_rows   # noqa: E402

GAME_GOODS = cm.ALL_GOODS            # the game's cells: town * 12 + the good's index here


async def game_state(s):
    out = []
    for e in ['CCCore.aTrust[%d]' % i for i in range(4)] + ['CCCore.iTier', 'CCCore.iCash']:
        out.append(int(await s.value(e)))
    return tuple(out)


def model_state(c):
    return tuple(int(c.trust[t]) for t in cm.TOWNS) + (c.tier, c.cash)


async def game_wh(s):
    return [int(await s.value('CCCore.aWh[%d]' % (ti * 12 + gi)))
            for ti in range(4) for gi in range(len(GAME_GOODS))]


def model_wh(c):
    return [c.wh[t][g] for t in cm.TOWNS for g in GAME_GOODS]


async def run(last_day):
    check = Checks()
    c = cm.Company(live.SEED)
    c.found()
    c.auto = True
    t = tm.Terminal()
    async with live.session() as s:
        await s.to_game_mode()
        await s.found(auto=1)
        await s.console('set CCCore.iShieldTest to 0')
        await s.console('CompleteQuest VMS16')
        c.ghost_town_done = True
        check('the M2 ledger is in place (iInit 5)', await s.value('CCCore.iInit') == 5)
        check('48 warehouse cells', await s.value('ar_Size CCCore.aWh') == 48)

        async def compare(what):
            c.pocket = await pocket(s)
            labels, results = await read_rows(s, 1), await read_rows(s, 2)
            want_l, want_r = tm.labels(c, t), tm.results(c, t)
            ok = labels == want_l and [(x or '').strip() for x in results] == [x.strip() for x in want_r]
            detail = ''
            if not ok:
                detail = '\n    '.join('%2d game  %r\n       model %r' % (i, g, w) for i, (g, w)
                                       in enumerate(zip(labels + ['-'] * 14, want_l + ['-'] * 14))
                                       if i < max(len(labels), len(want_l)))
            check(what, ok, detail)

        async def click(n, what=None):
            await s.console('SetTerminalMenuItemFlags CCOfficeTerm %d 4' % n)
            await s.wait_for('GetTerminalMenuItemFlags CCOfficeTerm %d' % n, want=False)
            await asyncio.sleep(0.4)
            c.pocket = await pocket(s)
            tm.click(c, t, n)
            if what:
                await compare(what)

        async def back(what=None):
            await click(len(tm.labels(c, t)) - 1, what)

        async def visit():
            await open_terminal(s)
            c.terminal_visit()
            t.screen, t.confirm = tm.FRONT, False

        async def close():
            await s.tool('fnv_ui_do', {'action': 'close_all'})
            await s.to_game_mode()

        async def day(d):
            c.pocket = await pocket(s)
            await s.next_day()
            r = c.tick()
            letter = c.field_letter()
            want = pm.letter_text(letter) if letter else None
            buttons = c.letter_buttons(letter) if letter else None
            got = await box(s, 12 if want else 3, 0)
            if letter:
                c.answer_letter(letter, 0, buttons)
            await asyncio.sleep(0.5)
            game = (await ingame_run.read_days(s, d, first=d - 1))[0]
            row = (r.cash, r.sales, r.costs, ingame_run.EVENTS[r.event], r.event_loss)
            check('day %d numbers' % d, game == row, 'game %s model %s' % (game, row))
            check('day %d letter: %s' % (d, letter.kind if letter else 'none'),
                  (got or '').strip() == (want or '').strip(), 'game %r\n    model %r' % (got, want))
            g, m = await game_state(s), model_state(c)
            check('day %d trust x4, tier, cash %s' % (d, m), g == m, 'game %s' % (g,))
            return r

        async def hire(role):
            """Hire the first candidate of this role on the Hire screen, at the fair offer."""
            pick = next((i for i, p in enumerate(c.candidates) if p.role == role), None)
            if pick is None:
                check('no %s among the candidates this week (model)' % role, True)
                return
            await click(pick, 'candidate page: a %s' % role)
            rows = tm.candidate_rows(c, t)
            row = next(i for i, r in enumerate(rows) if r[2] == 'hire' or (r[2] and r[2][0] == 'hire'
                                                                         and r[2][1] == 'fair'))
            await click(row, 'HIRE the %s (fair offer)' % role)

        async def staff_up(d):
            """Hire the driver and the clerk wagon 2 needs, if this week's candidates have them."""
            drivers = sum(1 for p in c.staff if p.role == 'driver')
            clerks = sum(1 for p in c.staff if p.role == 'clerk')
            need = [r for r, n in (('driver', 2 - drivers), ('clerk', 1 - clerks)) if n > 0]
            if not need or not any(p.role in need for p in c.candidates):
                return
            await visit()
            await click(7, 'day %d Staff' % d)
            await click(next(i for i, r in enumerate(tm.staff_rows(c, t)) if r[1] == 'hire'), 'Hire')
            for role in need:
                await hire(role)
            await back()
            await back()
            await close()

        tier_day = None
        for d in range(1, last_day + 1):
            r = await day(d)
            if d == 3:
                await visit()
                await click(3, 'day 3 Memos: the contract offer')
                row = next(i for i, (_, _, m, a) in enumerate(tm.memo_rows(c))
                           if m and m.kind == 'contract' and a == 0)
                await click(row, 'ACCEPT the contract')
                await back()
                await close()
            if r.tier_up and tier_day is None:
                tier_day = d
                await visit()
                await compare('front page at tier 2 (TOWNS row)')
                await click(4, 'Routes at tier 2: the Sloan road can be bought')
                await click(1, 'buy the Sloan road wagon')
                await back()
                await click(6, 'Build: ten buildings')
                for row in (5, 3, 1):
                    await click(row, 'build %s' % cm.BUILD_ROWS[row - 1])
                await back()
                await click(13, 'Towns: levels, trust and the managers')
                await click(4, 'hire the bookkeeper (Normal)')
                await s.console('player.AddItem WaterPurified 20 1')
                c.carried['water'] = int(await s.value('player.GetItemCount WaterPurified'))
                await click(6, 'sell the company a crate of purified water')
                await click(6, 'and another')
                check('the bottles left the pack', int(await s.value('player.GetItemCount WaterPurified'))
                      == c.carried['water'])
                await back()
                await close()
                await staff_up(d)
                check('wagons: game %d, model %d' % (await s.value('ar_Size CCCore.aWagonRoad'), len(c.wagons)),
                      await s.value('ar_Size CCCore.aWagonRoad') == len(c.wagons))
            elif tier_day and (d - 1) % 7 == 0:
                await staff_up(d)               # day 1 of a week: new candidates
            if tier_day:
                g, m = await game_wh(s), model_wh(c)
                check('day %d warehouses (48 cells)' % d, g == m, 'game %s\n    model %s' % (g, m))
        check('tier 2 by day 14 (day %s)' % tier_day, tier_day is not None and tier_day <= 14)
        runs = [int(await s.value('ar_Size CCCore.aHistCash'))]
        check('wagon 2 ran on some day (model: %s)' % (any(r.runs > 1 for r in c.history),),
              any(r.runs > 1 for r in c.history))
        errors = await s.script_errors()
    return check.bad, errors


def main(argv):
    last = int(argv[0]) if argv else 28
    bad, errors = asyncio.run(run(last))
    print('script errors: %d' % len(errors))
    for e in errors[:10]:
        print('  ', e)
    print('PASS' if not bad and not errors else 'FAIL (%d checks)' % bad)
    return 0 if not bad and not errors else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

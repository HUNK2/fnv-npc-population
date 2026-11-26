"""Check staff, hiring, the supply contract and standing orders in the game against the model (M1 task 1.8).

Needs a fresh game with MojaveCaravanCompany.esp loaded and no company (for example started with
coc GSProspectorSaloonInterior); it founds the company with the test seed and the daily plan on.

  day 1      the week's candidates match the model (names, roles, skill, honesty, wage, rumour);
             at the terminal: Staff, Hire, a candidate's screen, a reference check (10 caps), hiring
             him (a skimmer: honesty under 30), FIRE selected once and cancelled; Orders > Standing
             orders: slot 1 keep Primm stocked with 7 herbs, slot 2 pay at most 190 for water
  day 3      Primm's contract offer on the Memos screen; ACCEPT
  day 4      signed and the first delivery (4 crates of water on the Goodsprings leg)
  day 9/10   the road letter's "Keep it home": the day-10 delivery is missed
  day 14     the driver is fired (two selects)
  day 15     no driver: the wagon stays in the yard; a driver from the new candidates is hired
  days 16-18 deliveries again
Every day: the day's numbers, the letter shown, the contract (on, price, next day, delivered,
missed), Primm trust, cash and the staff match the model; every terminal screen's rows match after
every select. Screenshots go to docs/evidence/m1/. Run with fnv-mcp's Python:

    <fnv-mcp>/bridge/.venv/Scripts/python.exe tools/ingame_hiring.py
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
from ingame_ladder import Checks, box, open_terminal, pocket, read_rows, screenshot  # noqa: E402

DAYS = 18
ROLE = {'driver': 0, 'guard': 1}


async def text(s, expr):
    out = await s.console('printc "v=%%z" (%s)' % expr)
    got = [line[2:] for line in out if line.startswith('v=')]
    return got[-1] if got else None


async def game_staff(s):
    n = int(await s.value('ar_Size CCCore.aStaffName'))
    return [await text(s, 'CCCore.aStaffName[%d]' % i) for i in range(n)]


async def game_candidates(s):
    n = int(await s.value('ar_Size CCCore.aCandName'))
    out = []
    for i in range(n):
        row = [await text(s, 'CCCore.aCandName[%d]' % i)]
        for a in ('aCandRole', 'aCandSkill', 'aCandHon', 'aCandWage'):
            row.append(int(await s.value('CCCore.%s[%d]' % (a, i))))
        row.append(await text(s, 'CCCore.aCandRumour[%d]' % i))
        row.append(int(await s.value('CCCore.aCandChecked[%d]' % i)))
        out.append(tuple(row))
    return out


def model_candidates(c):
    return [(p.name, ROLE[p.role], p.skill, p.honesty, p.wage, p.rumour, int(p.checked)) for p in c.candidates]


async def game_contract(s):
    on = int(await s.value('CCCore.iConOn'))
    k = (on,)
    if on:
        k += tuple([int(await s.value('CCCore.%s' % v)) for v in ('iConPrice', 'iConNext', 'iConDone', 'iConMissed')])
    return k + (int(await s.value('CCCore.aTrust[1]')), int(await s.value('CCCore.iCash')))


def model_contract(c):
    k = c.contract
    out = (1, k.price, k.next_due, k.done, k.missed) if k else (0,)
    return out + (int(c.trust['PR']), c.cash)


async def run():
    check = Checks()
    c = cm.Company(live.SEED)
    c.found()
    c.auto = True
    t = tm.Terminal()
    async with live.session() as s:
        await s.to_game_mode()
        await s.found(auto=1)
        await s.console('set CCCore.iShieldTest to 0')

        async def compare(what):
            c.pocket = await pocket(s)
            labels, results = await read_rows(s, 1), await read_rows(s, 2)
            want_l, want_r = tm.labels(c, t), tm.results(c, t)
            ok = labels == want_l and [(x or '').strip() for x in results] == [x.strip() for x in want_r]
            detail = ''
            if not ok:
                detail = '\n    '.join('%2d game  %r | %r\n       model %r | %r' % (i, g, gr, w, wr) for i, (g, gr, w, wr)
                                       in enumerate(zip(labels + ['-'] * 14, results + ['-'] * 14,
                                                        want_l + ['-'] * 14, want_r + ['-'] * 14))
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
            g, m = await game_contract(s), model_contract(c)
            check('day %d contract %s, trust, cash' % (d, r.contract or r.signed or '-'), g == m,
                  'game  %s\n    model %s' % (g, m))
            g, m = await game_staff(s), [p.name for p in c.staff]
            check('day %d staff %s' % (d, m), g == m, 'game %s' % g)
            page = await text(s, 'CCCore.aPage[0]')
            want_p = pm.report_pages(c)[0]
            check('day %d report page 1' % d, page == want_p, 'game  %r\n    model %r' % (page, want_p))
            if d % 7 == 1:
                g, m = await game_candidates(s), model_candidates(c)
                check('day %d candidates %s' % (d, [x[0] for x in m]), g == m, 'game  %s\n    model %s' % (g, m))
            return r

        # day 1: hiring and standing orders
        await day(1)
        await visit()
        await compare('day 1 front page (staff, contracts)')
        await click(7, 'Staff screen')
        await click(len(c.staff) + 1, 'Hire screen')
        pick = next(i for i, p in enumerate(c.candidates) if p.honesty < cm.SKIM_HONESTY and c.can_hire(i))
        await click(pick, 'Candidate screen: %s' % c.candidates[pick].name)
        await screenshot(s, 'm1_candidate_screen')
        await click(2, 'reference check (10 caps)')
        check('reference check paid', int(await s.value('CCCore.iCash')) == c.cash)
        await click(1, 'hired: back on the Hire screen')
        await back('BACK to Staff: cover with the new guard')
        await screenshot(s, 'm1_staff_screen')
        await click(2, 'FIRE selected once: confirm')
        await click(0, 'another select cancels it')
        await back('BACK to the front page')
        await click(10, 'Orders')
        await click(4, 'Standing orders')
        await click(0, 'slot 1')
        await click(0, 'slot 1: keep stocked')
        for _ in range(4):
            await click(2)
        await compare('slot 1: herbs')
        await click(4, 'slot 1: LESS (7)')
        await screenshot(s, 'm1_standing_slot')
        await back('BACK to Standing orders')
        await click(1, 'slot 2')
        for _ in range(3):
            await click(0)
        await compare('slot 2: pay at most, water')
        await click(4)
        await click(4, 'slot 2: LESS twice (190)')
        await back('BACK to Standing orders: two set')
        await back('BACK to Orders: the plan follows the orders')
        await back('BACK to the front page: PLAN count')
        await close()

        for d in (2, 3):
            await day(d)
        await visit()
        await click(3, 'day 3 Memos: the contract offer')
        row = next(i for i, (_, _, m, a) in enumerate(tm.memo_rows(c)) if m and m.kind == 'contract' and a == 0)
        await click(row, 'ACCEPT the contract')
        await back()
        await click(8, 'Contracts screen: the offer is accepted, not signed yet')
        await back()
        await close()

        for d in range(4, 15):
            await day(d)
        check('a delivery was made and one missed', c.contract is not None and c.contract.done >= 1
              and c.contract.missed >= 1, str(c.contract))

        # day 14: the contracts screen, then fire the driver
        await visit()
        await click(8, 'day 14 Contracts screen')
        await screenshot(s, 'm1_contracts_screen')
        await back()
        await click(7, 'Staff screen')
        await click(1, 'FIRE the driver: confirm')
        await click(1, 'FIRE the driver: fired')
        await back('front page without a driver')
        await close()

        r = await day(15)
        check('day 15: no driver, the wagon stayed in the yard', not r.crew and not r.loads)
        driver = next((i for i, p in enumerate(c.candidates) if p.role == 'driver'), None)
        check('day 15: a driver among the candidates', driver is not None)
        if driver is not None:
            await visit()
            await click(7, 'Staff screen: no driver')
            await click(len(c.staff) + 1, 'Hire screen')
            await click(driver, 'Candidate screen: the driver')
            await click(1, 'hired the driver')
            await back('BACK to Staff: a driver again')
            await back()
            await close()
        for d in range(16, DAYS + 1):
            await day(d)
        errors = await s.script_errors()
    return check.bad, errors


def main():
    bad, errors = asyncio.run(run())
    print('script errors: %d' % len(errors))
    for e in errors[:10]:
        print('  ', e)
    print('PASS' if not bad and not errors else 'FAIL (%d checks)' % bad)
    return 0 if not bad and not errors else 1


if __name__ == '__main__':
    sys.exit(main())

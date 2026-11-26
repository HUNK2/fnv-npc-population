"""Check that an M1 save upgrades to M2 with every number it had (M2 plan 2.3, review focus 1).

Two steps, each in a fresh game session:

  m1     with the M1 plugin installed (MojaveCaravanCompany.esp from M1 1.10) and a fresh coc start:
         found the company with the test seed, run 5 days (checked against the model), accept Primm's
         contract on day 3, save the test save fnvmcp_test_cc_m1_upgrade and write the ledger to
         tools/.upgrade_m1.json.
  m2     with the M2 plugin installed: load that test save, check the ledger was widened (iInit 5,
         48 cells, the contract moved into the arrays) and still holds the saved numbers, then run 5
         more days against the model.

    <fnv-mcp>/bridge/.venv/Scripts/python.exe tools/ingame_upgrade.py m1|m2
"""
import asyncio
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import company_model as cm                  # noqa: E402
import ingame_run                           # noqa: E402
import live                                 # noqa: E402
import terminal_model as tm                 # noqa: E402
from ingame_ladder import Checks, open_terminal, pocket   # noqa: E402

SAVE = 'cc_m1_upgrade'
STATE = HERE / '.upgrade_m1.json'
DAYS = 5
SCALARS = ('iCash', 'iLoan', 'iOwner', 'iArrears', 'iTier', 'iDay', 'iWagonOk', 'iHands', 'iAssets')


def model(days):
    """The model's company after `days` ticks, with Primm's contract accepted on day 3."""
    c = cm.Company(live.SEED)
    c.found()
    c.auto = True
    t = tm.Terminal()
    rows = []
    for d in range(1, days + 1):
        r = c.tick()
        letter = c.field_letter()
        if letter:
            c.answer_letter(letter, 0, c.letter_buttons(letter))
        rows.append((r.cash, r.sales, r.costs, ingame_run.EVENTS[r.event], r.event_loss))
        if d == 3:
            c.terminal_visit()
            t.screen = tm.MEMOS
            row = next(i for i, (_, _, m, a) in enumerate(tm.memo_rows(c))
                       if m and m.kind == 'contract' and a == 0)
            tm.click(c, t, row)
    return c, rows


async def ledger(s, cells):
    """cells: the 12 stock cells (Goodsprings and Primm); the M1 warehouse is Goodsprings' 6, at 0 to 5 in both."""
    v = {k: int(await s.value('CCCore.%s' % k)) for k in SCALARS}
    v['wh'] = [int(await s.value('CCCore.aWh[%d]' % i)) for i in range(6)]
    v['stock'] = [int(await s.value('CCCore.aStock[%d]' % i)) for i in cells]
    v['staff'] = int(await s.value('ar_Size CCCore.aStaffName'))
    return v


async def day_rows(s, first, last, check, want):
    for d in range(first, last + 1):
        if (await s.menus()).get('messageBox'):
            await s.tool('fnv_ui_do', {'action': 'message', 'button': '0'})
            await asyncio.sleep(0.5)
        await s.next_day()
        await asyncio.sleep(0.5)
        got = (await ingame_run.read_days(s, d, first=d - 1))[0]
        check('day %d numbers' % d, got == want[d - 1], 'game %s model %s' % (got, want[d - 1]))


async def accept_contract(s):
    """Day 3: the contract offer on the Memos screen, accepted (the M1 terminal's rows)."""
    c, _ = model(3)
    await open_terminal(s)
    t = tm.Terminal()
    t.screen = tm.MEMOS
    row = next(i for i, (_, _, m, a) in enumerate(tm.memo_rows(c)) if m and m.kind == 'contract' and a == 0)
    for n in (3, row):
        await s.console('SetTerminalMenuItemFlags CCOfficeTerm %d 4' % n)
        await s.wait_for('GetTerminalMenuItemFlags CCOfficeTerm %d' % n, want=False)
        await asyncio.sleep(0.4)
    await s.tool('fnv_ui_do', {'action': 'close_all'})
    await s.to_game_mode()


async def step_m1(check):
    _, want = model(DAYS)
    async with live.session() as s:
        await s.to_game_mode()
        check('the M1 plugin is loaded (no M2 ledger)', await s.value('CCCore.iInit') < 5)
        await s.found(auto=1)
        await s.console('set CCCore.iShieldTest to 0')
        await day_rows(s, 1, 3, check, want)
        await accept_contract(s)
        check('the contract runs (M1 iConOn)', await s.value('CCCore.iConOn') == 1)
        await day_rows(s, 4, DAYS, check, want)
        v = await ledger(s, range(12))
        v['con'] = [int(await s.value('CCCore.%s' % k)) for k in ('iConPrice', 'iConNext', 'iConDone', 'iConMissed')]
        STATE.write_text(json.dumps(v, indent=1))
        out = await s.tool('fnv_test_save', {'action': 'save', 'name': SAVE})
        check('test save written', bool(out.get('ok')), json.dumps(out.get('error')))
        return await s.script_errors()


async def step_m2(check):
    old = json.loads(STATE.read_text())
    c, want = model(DAYS * 2)
    async with live.session() as s:
        out = await s.tool('fnv_test_save', {'action': 'load', 'name': SAVE})
        check('test save loaded', bool(out.get('ok')), json.dumps(out.get('error')))
        await s.to_game_mode()
        await s.wait_for('CCCore.iInit == 5', tries=60, pause=0.5)
        check('upgraded: iInit 5', True)
        check('48 warehouse cells', await s.value('ar_Size CCCore.aWh') == 48)
        # M1 stock cells town * 6 + good became town * 12 + good
        cells = [t * 12 + g for t in range(2) for g in range(6)]
        v = await ledger(s, cells)
        for k in SCALARS + ('wh', 'stock', 'staff'):
            check('kept %s %s' % (k, old[k]), v[k] == old[k], 'now %s' % (v[k],))
        con = [int(await s.value('CCCore.%s[0]' % k)) for k in ('aConPrice', 'aConNext', 'aConDone', 'aConMissed')]
        check('the contract moved into the arrays %s' % old['con'], con == old['con'], 'now %s' % con)
        check('the contract is Primm water on road 1', [int(await s.value('CCCore.%s[0]' % k))
                                                         for k in ('aConTown', 'aConGood', 'aConRoad')] == [1, 0, 1])
        check('M1 iConOn cleared', await s.value('CCCore.iConOn') == 0)
        check('staff have M2 numbers', await s.value('ar_Size CCCore.aStaffLoyal') == v['staff'])
        await day_rows(s, DAYS + 1, DAYS * 2, check, want)
        check('cash after day %d: %d' % (DAYS * 2, c.cash), int(await s.value('CCCore.iCash')) == c.cash)
        return await s.script_errors()


def main(argv):
    check = Checks()
    errors = asyncio.run({'m1': step_m1, 'm2': step_m2}[argv[0]](check))
    print('script errors: %d' % len(errors))
    for e in errors[:10]:
        print('  ', e)
    ok = not check.bad and not errors
    print('PASS' if ok else 'FAIL (%d checks)' % check.bad)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or ['m1']))

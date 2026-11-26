"""Check the office terminal in the game against tools/terminal_model.py (M1 task 1.4).

Opens a company terminal by script (CCTerm.iOpenNow places one at the player), reads every row label
back with JohnnyGuitar's GetTerminalMenuItemText, clicks rows the way the engine does (row flag 4)
and compares each screen with the model after the same clicks. Then it closes the terminal, runs one
day and checks that the orders queued on the terminal ran as the model says. Screenshots of each
screen go to docs/evidence/m1/. Needs a game with the company founded by tools/ingame_run.py (seed
1234, daily plan on), or a fresh game (it founds and runs 5 days). Run with fnv-mcp's Python:

    <fnv-mcp>/bridge/.venv/Scripts/python.exe tools/ingame_terminal.py
"""
import asyncio
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import company_model as cm                  # noqa: E402
import ingame_run                           # noqa: E402
import live                                 # noqa: E402
import terminal_model as tm                 # noqa: E402

EVIDENCE = HERE.parent / 'docs' / 'evidence' / 'm1'
COMPUTERS_MENU = 1057
BACK = 'back'
# (row, why): every screen, queueing, switching, cancelling, the daily plan toggle and a hidden row
CLICKS = [(5, 'open Prices'), (1, 'queue water'), (1, 'queue water'), (0, 'switch to PR > GS'),
          (3, 'queue ammo'), (0, 'switch back'), (BACK, 'back'),
          (10, 'open Orders'), (3, 'cancel all'), (2, 'accept the plan'), (BACK, 'back'),
          (11, 'open Settings'), (0, 'daily plan off'), (BACK, 'back'),
          (9, 'open Ledger'), (BACK, 'back'),
          (4, 'open Routes'), (BACK, 'back'),
          (13, 'hidden row: nothing happens'),
          (5, 'open Prices'), (2, 'queue powder'), (BACK, 'back')]


async def read_labels(s):
    rows = int(await s.value('CCTerm.iRows'))
    out = []
    for i in range(rows):
        lines = await s.console('GetTerminalMenuItemText CCOfficeTerm 1 %d' % i)
        got = [line.split('>> ', 1)[1] for line in lines if line.startswith('GetTerminalMenuItemText >> ')]
        out.append(got[-1] if got else None)
    return out


async def screenshot(s, name):
    # the terminal types about one character a frame: let the screen finish first
    await s.tool('fnv_wait_for', {'seconds': 10, 'clock': 'real', 'timeout': 30})
    out = await s.tool('fnv_screenshot', {'name': name, 'max_width': 1280})
    data = out.get('data') or {}
    path = next((v for k, v in data.items() if 'path' in k.lower() and isinstance(v, str)), None)
    if path and Path(path).exists():
        EVIDENCE.mkdir(parents=True, exist_ok=True)
        shutil.copy(path, EVIDENCE / ('%s.png' % name))
        return True
    return False


async def run():
    async with live.session() as s:
        await s.to_game_mode()
        if not await s.value('CCCore.iFounded'):
            await s.found(auto=1)
            for _ in range(5):
                await s.next_day()
        if await s.value('CCCore.iSeed') != live.SEED or not await s.value('CCCore.iAuto'):
            raise RuntimeError('the company was not founded by the test runner: start a fresh game')
        days = int(await s.value('ar_Size CCCore.aHistCash'))
        c = cm.Company(live.SEED)
        c.found()
        c.auto = True
        for _ in range(days):
            c.tick()
        t = tm.Terminal()
        print('day %d: opening the terminal' % days)

        await s.console('set CCTerm.iOpenNow to 1')
        for _ in range(40):
            if COMPUTERS_MENU in [m.get('id') for m in (await s.menus()).get('visible', [])]:
                break
            await asyncio.sleep(0.25)
        else:
            raise RuntimeError('the terminal did not open')
        await asyncio.sleep(1)

        bad, seen = 0, set()

        async def check(what):
            nonlocal bad
            want = tm.labels(c, t)
            got = await read_labels(s)
            ok = got == want
            bad += not ok
            print('%-28s screen %d, %d rows: %s' % (what, t.screen, len(got), 'same' if ok else 'DIFFERENT'))
            if not ok:
                for i in range(max(len(got), len(want))):
                    g = got[i] if i < len(got) else '-'
                    w = want[i] if i < len(want) else '-'
                    print('   %2d game  %s\n      model %s' % (i, g, w) if g != w else '   %2d same  %s' % (i, g))
            if t.screen not in seen:
                seen.add(t.screen)
                await screenshot(s, 'm1_terminal_screen%d' % t.screen)

        await check('opened')
        for row, why in CLICKS:
            if row == BACK:
                row = len(tm.labels(c, t)) - 1
            await s.console('SetTerminalMenuItemFlags CCOfficeTerm %d 4' % row)
            await s.wait_for('GetTerminalMenuItemFlags CCOfficeTerm %d' % row, want=False)
            await asyncio.sleep(0.4)
            tm.click(c, t, row)
            await check('row %d (%s)' % (row, why))

        await s.tool('fnv_ui_do', {'action': 'close_all'})
        await s.to_game_mode()
        queued = int(await s.value('ar_Size CCCore.aQueue'))
        print('orders queued in game %d, model %d' % (queued, len(c.queue_list)))
        bad += queued != len(c.queue_list)
        await s.next_day()
        r = c.tick()
        game = await ingame_run.read_days(s, days + 1, first=days)
        model = [(r.cash, r.sales, r.costs, ingame_run.EVENTS[r.event], r.event_loss)]
        bad += ingame_run.compare(game, model, first_day=days + 1)
        auto = await s.value('CCCore.iAuto')
        bad += auto != 0
        print('daily plan after the toggle: %d (want 0)' % auto)
        return bad, await s.script_errors()


def main():
    bad, errors = asyncio.run(run())
    print('script errors: %d' % len(errors))
    for e in errors[:10]:
        print('  ', e)
    print('MATCH' if not bad and not errors else 'DIFFERS (%d checks)' % bad)
    return 0 if not bad and not errors else 1


if __name__ == '__main__':
    sys.exit(main())

"""Check the post in the game against the model (M1 task 1.6): morning report, memos, field letters.

Needs a fresh game with MojaveCaravanCompany.esp loaded and no company (for example started with
coc GSProspectorSaloonInterior); it founds the company with the test seed and the daily plan on.

1. Nine days, no terminal visit: each day's numbers match tools/company_model.py, and each day's field
   letter (a message box) is the model's: the while-you-were-away letter on day 3, the bandit-sign
   letters on the road memo days (answered with the first button, "Keep it home", as the model does),
   nothing on the other days (at most one a day).
2. The terminal: opening it is a visit; the Post screen shows the report's two pages and the letters
   (labels and result text read back with GetTerminalMenuItemText), the Memos screen shows the prepay
   and road memos with their defaults. Pick "pay 300 off the loan" and "hire a gun for 25".
3. Day 10 runs with those answers and matches the model; the Post shows the new report.
4. A letter waits while a menu is open and shows when it closes; a second letter the same day waits.
Screenshots go to docs/evidence/m1/. Run with fnv-mcp's Python:

    <fnv-mcp>/bridge/.venv/Scripts/python.exe tools/ingame_post.py
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
import post_model as pm                     # noqa: E402
import terminal_model as tm                 # noqa: E402

EVIDENCE = HERE.parent / 'docs' / 'evidence' / 'm1'
COMPUTERS_MENU = 1057
DAYS = 9


class Checks:
    def __init__(self):
        self.bad = 0

    def __call__(self, what, ok, detail=''):
        self.bad += not ok
        print('%-60s %s%s' % (what, 'ok' if ok else 'FAILED', ('\n    ' + detail) if detail and not ok else ''))


def model_day(c):
    """One model day as the game runs it here: tick, then the field letter (a road letter gets button 0)."""
    r = c.tick()
    letter = c.field_letter()
    if letter and letter.kind == 'road':
        c.answer_letter(letter, 0)
    return r, letter


def row(r):
    return (r.cash, r.sales, r.costs, ingame_run.EVENTS[r.event], r.event_loss)


async def box(s, seconds):
    """The message box that shows within `seconds` (its text), pressed with button 0; None if none showed."""
    for _ in range(int(seconds / 0.25)):
        mb = (await s.menus()).get('messageBox')
        if mb:
            text = mb.get('text') if isinstance(mb, dict) else str(mb)
            await screenshot(s, 'm1_field_letter', wait=1)
            await s.tool('fnv_ui_do', {'action': 'message', 'button': '0'})
            await asyncio.sleep(0.5)
            return text or str(mb)
        await asyncio.sleep(0.25)
    return None


shots = set()


async def screenshot(s, name, wait=6):
    if name in shots:
        return
    shots.add(name)
    await s.tool('fnv_wait_for', {'seconds': wait, 'clock': 'real', 'timeout': 30})
    out = await s.tool('fnv_screenshot', {'name': name, 'max_width': 1280})
    data = out.get('data') or {}
    path = next((v for k, v in data.items() if 'path' in k.lower() and isinstance(v, str)), None)
    if path and Path(path).exists():
        EVIDENCE.mkdir(parents=True, exist_ok=True)
        shutil.copy(path, EVIDENCE / ('%s.png' % name))


async def read_rows(s, kind):
    rows = int(await s.value('CCTerm.iRows'))
    out = []
    for i in range(rows):
        lines = await s.console('GetTerminalMenuItemText CCOfficeTerm %d %d' % (kind, i))
        got = [line.split('>> ', 1)[1] if '>> ' in line else '' for line in lines
               if line.startswith('GetTerminalMenuItemText >>')]
        out.append(got[-1] if got else None)
    return out


async def open_terminal(s):
    await s.console('set CCTerm.iOpenNow to 1')
    for _ in range(40):
        if COMPUTERS_MENU in [m.get('id') for m in (await s.menus()).get('visible', [])]:
            await asyncio.sleep(1)
            return
        await asyncio.sleep(0.25)
    raise RuntimeError('the terminal did not open')


async def run():
    check = Checks()
    c = cm.Company(live.SEED)
    c.found()
    c.auto = True
    t = tm.Terminal()
    async with live.session() as s:
        await s.to_game_mode()
        await s.found(auto=1)

        # 1. nine days without a visit: numbers and field letters
        for d in range(1, DAYS + 1):
            await s.next_day()
            r, letter = model_day(c)
            want = pm.letter_text(letter) if letter else None
            got = await box(s, 5 if want else 3)
            game = (await ingame_run.read_days(s, d, first=d - 1))[0]
            check('day %d numbers' % d, game == row(r), 'game %s model %s' % (game, row(r)))
            check('day %d field letter: %s' % (d, letter.kind if letter else 'none'),
                  (got or '').strip() == (want or '').strip(), 'game %r\n    model %r' % (got, want))

        # 2. the terminal: a visit, the Post and Memos screens
        await open_terminal(s)
        c.terminal_visit()
        check('opening the terminal is a visit', int(await s.value('CCCore.iLastVisit')) == DAYS
              and int(await s.value('CCCore.iLetterKind')) == 0)

        async def compare(what):
            labels, results = await read_rows(s, 1), await read_rows(s, 2)
            want_l, want_r = tm.labels(c, t), tm.results(c, t)
            ok = labels == want_l and [x.strip() for x in results] == [x.strip() for x in want_r]
            detail = ''
            if not ok:
                detail = '\n    '.join('%2d game  %r | %r\n       model %r | %r' % (i, g, gr, w, wr) for i, (g, gr, w, wr)
                                       in enumerate(zip(labels + ['-'] * 9, results + ['-'] * 9,
                                                        want_l + ['-'] * 9, want_r + ['-'] * 9))
                                       if i < max(len(labels), len(want_l)))
            check(what, ok, detail)

        async def click(n):
            await s.console('SetTerminalMenuItemFlags CCOfficeTerm %d 4' % n)
            await s.wait_for('GetTerminalMenuItemFlags CCOfficeTerm %d' % n, want=False)
            await asyncio.sleep(0.4)
            tm.click(c, t, n)

        await compare('front page')
        await click(2)
        await compare('Post screen: report pages and letters')
        await screenshot(s, 'm1_post_screen')
        await click(0)                          # a text row: no redraw, nothing changes
        await compare('Post screen after selecting page 1')
        await click(len(tm.labels(c, t)) - 1)
        await click(3)
        await compare('Memos screen')
        await screenshot(s, 'm1_memos_screen')
        kinds = [m.kind for m in c.memos]
        check('prepay and road memos wait on day 9', kinds == ['prepay', 'road'], str(kinds))
        if kinds == ['prepay', 'road']:
            await click(1)                      # pay 300 off the loan
            await compare('Memos screen after "pay 300 off the loan"')
            await click(5)                      # hire a gun for 25
            await compare('Memos screen after "hire a gun for 25"')
            await screenshot(s, 'm1_memos_answered')
        await click(len(tm.labels(c, t)) - 1)
        await s.tool('fnv_ui_do', {'action': 'close_all'})
        await s.to_game_mode()

        # 3. day 10 with those answers
        await s.next_day()
        r, letter = model_day(c)
        got = await box(s, 5 if letter else 3)
        game = (await ingame_run.read_days(s, DAYS + 1, first=DAYS))[0]
        check('day 10 numbers with the answers', game == row(r), 'game %s model %s' % (game, row(r)))
        check('day 10: prepaid %d, a hired gun' % r.prepaid, r.prepaid == 300 and r.road_mode == cm.GUN)
        check('day 10 field letter', (got or '').strip() == (pm.letter_text(letter) if letter else '').strip(),
              '%r' % got)
        await open_terminal(s)
        c.terminal_visit()
        t.screen = tm.FRONT
        await click(2)
        await compare('Post screen on day 10')
        await screenshot(s, 'm1_post_day10')

        # 4. a letter waits while a menu is open, and only one shows a day
        await s.console('set CCCore.iLetterKind to 1')
        await asyncio.sleep(3)
        check('no letter while the terminal is open', not (await s.menus()).get('messageBox'))
        await s.tool('fnv_ui_do', {'action': 'close_all'})
        await s.tool('fnv_window', {'action': 'background'})    # not to_game_mode: it would press the box
        got = await box(s, 5)
        check('the waiting letter shows once the terminal is closed', got is not None)
        await s.console('set CCCore.iLetterKind to 1')
        got = await box(s, 4)
        check('a second letter the same day waits', got is None and int(await s.value('CCCore.iLetterKind')) == 1)
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

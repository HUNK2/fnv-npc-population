"""Check the debt ladder in the game against the model (M1 task 1.7).

Needs a fresh game with MojaveCaravanCompany.esp loaded and no company (for example started with
coc GSProspectorSaloonInterior); it founds the company with the test seed and the daily plan on. Cash
is forced low on some days, in the game (console) and in the model alike, to miss bills:

  days 1-6   normal days
  day 7      cash 50, busy shield on (CCCore.iShieldTest 1): the bills are missed, the notice is
             deferred and no letter reaches the player
  day 8      cash 0, shield on: still deferred, no clock; then the shield goes down (the player
             leaves the DLC's lands) and the runner finds them the same day: the notice letter is
             shown, which serves it (grace, strike 1 on day 8)
  days 9-11  cash 0: the final notice on day 11 (served + 3), a letter
  then       3,000 caps in the player's pocket; at the terminal the Notice screen, owner rescue
  days 12-14 cash 50: a forecast letter, then a second miss on probation (day 14) skips Grace (final
             notice letter); its "Sell the wagon" button is pressed
  days 15-16 cash 0: the seizure step (nothing left to take)
  then       the terminal: Notice screen, WALK AWAY selected once (confirm label), Routes (no wagon)
  days 17-18 cash 0: receivership on day 18 (served + 7), a closed letter, the closed terminal

Every day: cash, arrears, stage, strikes, served day, wagon and the day's numbers match the model; each
letter's text matches. Screenshots go to docs/evidence/m1/. Run with fnv-mcp's Python:

    <fnv-mcp>/bridge/.venv/Scripts/python.exe tools/ingame_ladder.py
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
STAGE = {'ok': 0, 'deferred': 1, 'grace': 2, 'final': 3, 'seized': 4, 'probation': 5, 'takeover': 6}
# day: (cash forced before the tick or None, shield, button pressed on that day's letter)
PLAN = {7: (50, True, 0), 8: (0, True, 0), 9: (0, False, 0), 10: (0, False, 0), 11: (0, False, 0),
        12: (50, False, 0), 13: (50, False, 0), 14: (50, False, 1), 15: (0, False, 0), 16: (0, False, 0),
        17: (0, False, 0), 18: (0, False, 0)}


class Checks:
    def __init__(self):
        self.bad = 0

    def __call__(self, what, ok, detail=''):
        self.bad += not ok
        print('%-62s %s%s' % (what, 'ok' if ok else 'FAILED', ('\n    ' + detail) if detail and not ok else ''))


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


async def box(s, seconds, button=0, shot=None):
    """The message box that shows within `seconds` (its text), pressed with `button`; None if none."""
    for _ in range(int(seconds / 0.25)):
        mb = (await s.menus()).get('messageBox')
        if mb:
            text = mb.get('text') if isinstance(mb, dict) else str(mb)
            if shot:
                await screenshot(s, shot, wait=1)
            await s.tool('fnv_ui_do', {'action': 'message', 'button': str(button)})
            await asyncio.sleep(0.7)
            return text or str(mb)
        await asyncio.sleep(0.25)
    return None


async def pocket(s):
    return int(await s.value('player.GetItemCount Caps001'))


async def state(s):
    v = {}
    for k in ('iCash', 'iArrears', 'iStage', 'iServedDay', 'iWagonOk', 'iEnded'):
        v[k] = int(await s.value('CCCore.%s' % k))
    n = int(await s.value('ar_Size CCCore.aStrikes'))
    strikes = [int(await s.value('CCCore.aStrikes[%d]' % i)) for i in range(n)]
    return (v['iCash'], v['iArrears'], v['iStage'], strikes, v['iServedDay'], v['iWagonOk'], v['iEnded'])


def model_state(c):
    return (c.cash, c.arrears, STAGE[c.stage], list(c.strikes), c.served_day if c.served_day is not None else 0,
            int(c.wagon_ok), int(c.ended))


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

        async def click(n):
            await s.console('SetTerminalMenuItemFlags CCOfficeTerm %d 4' % n)
            await s.wait_for('GetTerminalMenuItemFlags CCOfficeTerm %d' % n, want=False)
            await asyncio.sleep(0.4)
            c.pocket = await pocket(s)
            tm.click(c, t, n)

        async def visit():
            await open_terminal(s)
            c.terminal_visit()
            t.screen, t.confirm = tm.FRONT, False

        async def close():
            await s.tool('fnv_ui_do', {'action': 'close_all'})
            await s.to_game_mode()

        async def day(d):
            cash, shield, button = PLAN.get(d, (None, False, 0))
            if cash is not None:
                await s.console('set CCCore.iCash to %d' % cash)
                c.cash = cash
            await s.console('set CCCore.iShieldTest to %d' % (1 if shield else 0))
            c.shield = shield
            c.pocket = await pocket(s)
            await s.next_day()
            r = c.tick()
            letter = c.field_letter()
            want = pm.letter_text(letter) if letter else None
            buttons = c.letter_buttons(letter) if letter else None
            got = await box(s, 12 if want else 3, button)
            if want and got is None:
                dump = []
                for v in ('CCCore.iLetterKind', 'CCCore.iLetterShownDay', 'CCLetter.iShown', 'CCLetter.iKind',
                          'player.IsInCombat', 'CCCore.iShieldTest'):
                    dump.append('%s=%g' % (v, await s.value(v)))
                print('  no box on day %d: %s; menus %s' % (d, ' '.join(dump), await s.menus()))
            if letter:
                c.answer_letter(letter, button, buttons)
            await asyncio.sleep(0.5)
            game = (await ingame_run.read_days(s, d, first=d - 1))[0]
            row = (r.cash, r.sales, r.costs, ingame_run.EVENTS[r.event], r.event_loss)
            check('day %d numbers' % d, game == row, 'game %s model %s' % (game, row))
            check('day %d letter: %s%s' % (d, letter.kind if letter else 'none',
                                           ' ' + str(letter.values[0]) if letter and letter.kind == 'notice' else ''),
                  (got or '').strip() == (want or '').strip(), 'game %r\n    model %r' % (got, want))
            g, m = await state(s), model_state(c)
            check('day %d ladder: stage %s, strikes %s' % (d, c.stage, c.strikes), g == m,
                  'game  %s\n    model %s' % (g, m))

        for d in range(1, 12):
            await day(d)
            if d == 8:
                # the player leaves the DLC's lands: the deferred notice reaches them the same day
                await s.console('set CCCore.iShieldTest to 0')
                c.shield = False
                letter = c.field_letter()
                got = await box(s, 12, 0, shot='m1_notice_letter')
                check('day 8 shield down: the notice letter', letter is not None and letter.kind == 'notice'
                      and (got or '').strip() == pm.letter_text(letter).strip(),
                      'game %r\n    model %r' % (got, letter and pm.letter_text(letter)))
                g, m = await state(s), model_state(c)
                check('day 8 served: grace, strike [8]', g == m and c.strikes == [8],
                      'game  %s\n    model %s' % (g, m))

        # the terminal on day 11: the final notice and an owner rescue
        await s.console('player.additem Caps001 3000')
        await visit()
        await compare('day 11 front page (NOTICE row)')
        await click(12)
        await compare('day 11 Notice screen: final notice, cures')
        await screenshot(s, 'm1_notice_screen')
        await click(1)
        await compare('Notice screen after the owner rescue')
        check('owner rescue: probation, the strike stays', c.stage == 'probation' and c.strikes == [8])
        g, m = await state(s), model_state(c)
        check('owner rescue state', g == m, 'game  %s\n    model %s' % (g, m))
        await click(len(tm.labels(c, t)) - 1)
        await close()

        for d in (12, 13, 14, 15, 16):
            await day(d)
        check('the wagon was sold from the letter', not c.wagon_ok)

        # the terminal on day 16: seized stage, WALK AWAY once, Routes without a wagon
        await visit()
        await compare('day 16 front page')
        await click(12)
        await compare('day 16 Notice screen')
        walk = len(tm.labels(c, t)) - 2
        await click(walk)
        await compare('WALK AWAY selected once: confirm')
        await click(len(tm.labels(c, t)) - 1)
        await compare('BACK cancels the confirm')
        await click(4)
        await compare('Routes: no wagon')
        await click(0)
        await compare('Routes: no wagon bought while money is owed')
        await click(len(tm.labels(c, t)) - 1)
        await close()

        for d in (17, 18):
            await day(d)
        check('receivership on day 18', c.ended and c.end_reason == 'receivership')
        await visit()
        await compare('the closed company')
        await screenshot(s, 'm1_closed_terminal')
        await close()
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

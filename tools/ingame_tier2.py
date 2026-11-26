"""Check trust, the Ghost Town deed, tier 2, the Build screen and the office in the game against the model
(M1 task 1.9).

Needs a fresh game with MojaveCaravanCompany.esp loaded and no company (for example started with
coc GSProspectorSaloonInterior); it founds the company with the test seed and the daily plan on, and
completes Ghost Town Gunfight (CompleteQuest VMS16) first, as a test shortcut for the deed.

  every day   numbers, the letter shown, trust in both towns, the tier and cash match the model
  day 3       Primm's contract accepted on the Memos screen
  tier day    the tier letter; the office by the Prospector Saloon and the Primm stall are enabled
  then        the front page's CHAINS row opens Build; build the well rig and the purifier; three more
              days with the warehouse compared; through the office door, the office terminal's front
              page, and out again
Screenshots go to docs/evidence/m1/. Run with fnv-mcp's Python:

    <fnv-mcp>/bridge/.venv/Scripts/python.exe tools/ingame_tier2.py
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
from ingame_ladder import EVIDENCE, Checks, box, open_terminal, pocket, read_rows, screenshot  # noqa: E402

LAST_DAY = 20
WORLD = ('CCOfficeShackRef', 'CCOfficeDoorRef', 'CCPrimmStallCartRef', 'CCPrimmStallCrate1Ref',
         'CCPrimmStallCrate2Ref', 'CCPrimmStallBoardRef')
COMPUTERS_MENU = 1057


async def game_state(s):
    out = []
    for e in ('CCCore.aTrust[0]', 'CCCore.aTrust[1]', 'CCCore.iTier', 'CCCore.iCash'):
        out.append(int(await s.value(e)))
    return tuple(out)


def model_state(c):
    return (int(c.trust['GS']), int(c.trust['PR']), c.tier, c.cash)


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
        await s.console('CompleteQuest VMS16')
        c.ghost_town_done = True
        check('Ghost Town Gunfight reads as done', await s.value('GetQuestCompleted VMS16') == 1)

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
            check('day %d trust GS/PR, tier, cash %s' % (d, m), g == m, 'game %s' % (g,))
            return r

        tier_day = None
        for d in range(1, LAST_DAY + 1):
            r = await day(d)
            if d == 3:
                await visit()
                await click(3, 'day 3 Memos: the contract offer')
                row = next(i for i, (_, _, m, a) in enumerate(tm.memo_rows(c))
                           if m and m.kind == 'contract' and a == 0)
                await click(row, 'ACCEPT the contract')
                await back()
                await close()
            if r.tier_up:
                tier_day = d
                break
        check('tier 2 by day 14 (day %s)' % tier_day, tier_day is not None and tier_day <= 14)
        if tier_day is None:
            return check.bad, await s.script_errors()

        for ref in WORLD:
            check('%s is enabled' % ref, await s.value('%s.GetDisabled' % ref) == 0)

        # the Build screen
        await visit()
        await compare('front page at tier 2: CHAINS 0 of 4 built')
        await click(6, 'CHAINS opens Build')
        await screenshot(s, 'm1_build_screen')
        await click(3, 'build the well rig (a hand comes with it)')
        await click(1, 'build the purifier')
        check('owner money and cash after building', (int(await s.value('CCCore.iOwner')),
                                                      int(await s.value('CCCore.iCash'))) == (c.owner_funds, c.cash))
        check('one hand on the books', int(await s.value('CCCore.iHands')) == c.hands == 1)
        await back('BACK: CHAINS 2 of 4 built')
        await close()

        for d in range(tier_day + 1, tier_day + 4):
            await day(d)
            g = [int(await s.value('CCCore.aWh[%d]' % i)) for i in range(6)]
            m = [c.warehouse[x] for x in cm.GOODS]
            check('day %d warehouse %s' % (d, m), g == m, 'game %s' % g)

        # the office: in through the front door, its terminal, out again
        await s.console('CCOfficeDoorRef.Activate player 1')
        await s.wait_for('player.GetInCell CCOfficeCell', tries=120)
        await asyncio.sleep(3)
        await s.to_game_mode()
        check('through the front door into the office', True)
        # the picture from the middle of the room, facing the desk (the third-person camera at the
        # entry marker sees only the door corner)
        await s.tool('fnv_move', {'ref': 'player', 'position': [-80, -120, 5]})
        await s.console('player.SetAngle z 180')
        await screenshot(s, 'm1_office_inside')
        await s.console('CCOfficeTermRef.Activate player 1')
        for _ in range(40):
            if COMPUTERS_MENU in [m.get('id') for m in (await s.menus()).get('visible', [])]:
                break
            await asyncio.sleep(0.25)
        await asyncio.sleep(1)
        c.terminal_visit()
        t.screen, t.confirm = tm.FRONT, False
        await compare('the office terminal: front page')
        await close()
        await s.console('CCOfficeExitDoorRef.Activate player 1')
        await s.wait_for('player.GetInCell CCOfficeCell', want=False, tries=120)
        await asyncio.sleep(3)
        await s.to_game_mode()
        check('out again by the Prospector Saloon',
              abs(await s.value('player.GetPos x') - -66935) < 50 and abs(await s.value('player.GetPos y') - 2650) < 50)
        await screenshot(s, 'm1_office_exit')
        out = await s.tool('fnv_photo', {'action': 'ref', 'ref': 'CCOfficeShackRef', 'distance': 1400, 'size': 640,
                                         'angles': ['front', 'three_quarter', 'top'], 'name': 'm1_office_outside'})
        sheet = (out.get('data') or {}).get('sheet')
        if sheet and Path(sheet).exists():
            shutil.copy(sheet, EVIDENCE / 'm1_office_outside.png')
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

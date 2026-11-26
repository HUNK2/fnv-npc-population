"""M4 in the game against tools/company_model.py (late_model, ending_model): plan tasks 4.4 and 4.5.

Like tools/ingame_m3.py (the same days, numbers, letters and law state), with M4 on:
  tier 3      as in M3 (test shortcut on the day after tier 2: tier 3 and 6,000 caps in both)
  memos       a forward ticket is accepted with its advance, the quartermaster's deal is taken, an
              outfit's ask is lent at 4%; a failed outfit is left to its default (seized); each Memos
              screen with an M4 memo is compared before it is answered
  Contracts   compared on day 3 of each week while a ticket runs (the FWD rows)
  tier 4      test shortcut on day T4: tier 4, NCR standing 60, heat 0 in both (the quartermaster's
              offer follows); the Towns screen (SHARES) is compared
  tier 5      test shortcut on day T5: tier 5, favour 5 and two weeks' lead in Primm in both; Towns is
              compared, then PASS the first law and BUY the first share block
  the end     on the last day: Settings (RETIRE), the confirm, retire, the closed front page and the
              Post with the three "20 years on" pages
  every day   the late state: the quartermaster, favour, laws, blocks, the Primm lead, her fall, the
              tickets and the outfits

    <fnv-mcp>/bridge/.venv/Scripts/python.exe tools/ingame_m4.py [last day]
"""
import asyncio
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ingame_m3 as m3                      # noqa: E402  (its helpers; it switches forward offers off)
import late_model                           # noqa: E402
late_model.FWD_OPEN = 3                     # M4 is in this game: forward offers on again
import company_model as cm                  # noqa: E402
import ingame_run                           # noqa: E402
import live                                 # noqa: E402
import post_model as pm                     # noqa: E402
import terminal_model as tm                 # noqa: E402
from ingame_ladder import Checks, box, open_terminal, pocket, read_rows   # noqa: E402

LATE_VARS = ('iQm', 'iQmLoan', 'iFavour', 'iLaws', 'iBlocks', 'iLeadPrWeeks', 'iWonHer', 'iRivalOut',
             'iLentEver', 'iSeizedN', 'iForgivenN')
T4_AFTER, T5_AFTER = 8, 14           # days after the tier 3 shortcut, then after tier 4
ANSWER = {'forward': 1, 'patron': 0, 'lend': 1}


async def game_late(s):
    out = [int(await s.value('CCLate.%s' % k)) for k in LATE_VARS]
    out.append(int(await s.value('ar_Size CCLate.aTkTown')))
    out.append(int(await s.value('ar_Size CCLate.aOfName')))
    return tuple(out)


def model_late(c):
    return (int(c.qm), c.qm_loan, c.favour, len(c.laws), c.blocks, c.lead_pr_weeks, int(c.won_vs_her),
            int(c.rival_out), int(c.lent_ever), c.seized_n, c.forgiven_n, len(c.tickets), len(c.outfits))


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
        check('the late game is set up (CCLate.iInit 1)', await s.value('CCLate.iInit') == 1)

        async def compare(what):
            c.pocket = await pocket(s)
            labels, results = await read_rows(s, 1), await read_rows(s, 2)
            want_l, want_r = tm.labels(c, t), tm.results(c, t)
            gr, wr = [(x or '').strip() for x in results], [x.strip() for x in want_r]
            ok = labels == want_l and gr == wr
            detail = ''
            if not ok:
                detail = '\n    '.join('%2d game  %r\n       model %r' % (i, g, w) for i, (g, w)
                                       in enumerate(zip(labels + ['-'] * 16, want_l + ['-'] * 16))
                                       if i < max(len(labels), len(want_l)))
                detail += ''.join('\n    text %2d game  %r\n            model %r' % (i, a, b)
                                  for i, (a, b) in enumerate(zip(gr, wr)) if a != b)
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

        async def both(cmd, setter):
            await s.console(cmd)
            setter()

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
            g, m = await m3.game_state(s), m3.model_state(c)
            check('day %d trust x4, tier, cash %s' % (d, m), g == m, 'game %s' % (g,))
            return r

        async def hire(role):
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
            drivers = sum(1 for p in c.staff if p.role == 'driver')
            clerks = sum(1 for p in c.staff if p.role == 'clerk')
            need = [r for r, n in (('driver', len(c.wagons) - drivers), ('clerk', 1 - clerks)) if n > 0]
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

        async def memos(d):
            """Answer the M4 memos waiting (and an NCR bid low, a warrant with a fixer, as in M3)."""
            todo = [x for x in c.memos if x.pick is None and (x.kind in ANSWER or x.kind in ('ncr', 'warrant'))]
            if not todo:
                return
            await visit()
            await click(3, 'day %d Memos %s' % (d, [x.kind for x in c.memos]))
            for kind, pick in list(ANSWER.items()) + [('ncr', 1), ('warrant', 0)]:
                rows = tm.memo_rows(c)
                row = next((i for i, (_, _, x, a) in enumerate(rows)
                            if x and x.kind == kind and a == pick and x.pick is None), None)
                if row is not None:
                    await click(row, 'day %d answer the %s memo (%d)' % (d, kind, pick))
            await back()
            await close()

        tier_day = t3_day = t4_day = t5_day = None
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
                await click(4, 'Routes at tier 2')
                await click(1, 'buy the Sloan road wagon')
                await back()
                await click(6, 'Build')
                for row in (5, 3, 1):
                    await click(row, 'build %s' % cm.BUILD_ROWS[row - 1])
                await back()
                await click(13, 'Towns')
                await click(4, 'hire the bookkeeper (Normal)')
                await back()
                await close()
                await staff_up(d)
            elif tier_day and d == tier_day + 1:
                t3_day = d
                await s.console('set CCCore.iTier to 3')
                await s.console('set CCLaw.iInspNext to %d' % (d + 30))
                await s.console('set CCCore.iCash to CCCore.iCash + 6000')
                c.tier = 3
                c.inspect_next = d + 30
                c.cash += 6000
                await visit()
                await click(4, 'Routes at tier 3')
                await click(2, 'buy the Outpost road wagon')
                await back()
                await close()
                await staff_up(d)
            elif tier_day and (d - 1) % 7 == 0:
                await staff_up(d)
            if t3_day and d == t3_day + T4_AFTER:
                t4_day = d
                await both('set CCCore.iTier to 4', lambda: setattr(c, 'tier', 4))
                await both('set CCLaw.iStanding to 60', lambda: setattr(c, 'ncr_standing', 60))
                await both('set CCLaw.iHeat to 0', lambda: setattr(c, 'heat', 0))
                await visit()
                await click(13, 'day %d Towns at tier 4 (SHARES)' % d)
                await back()
                await close()
            if t4_day and d == t4_day + T5_AFTER:
                t5_day = d
                await both('set CCCore.iTier to 5', lambda: setattr(c, 'tier', 5))
                await both('set CCLate.iFavour to 5', lambda: setattr(c, 'favour', 5))
                await both('set CCLate.iLeadPrWeeks to 2', lambda: setattr(c, 'lead_pr_weeks', 2))
                await both('set CCCore.iCash to CCCore.iCash + 6000', lambda: setattr(c, 'cash', c.cash + 6000))
                await visit()
                await click(13, 'day %d Towns at tier 5 (SHARES, LAWS)' % d)
                await click(14, 'PASS the Free trade act')
                await click(13, 'BUY the first share block')
                await back()
                await close()
            if t3_day and d > t3_day:
                await memos(d)
                if c.tickets and d % 7 == 3:
                    await visit()
                    await click(8, 'day %d Contracts (forward tickets)' % d)
                    await back()
                    await close()
                gm = int(await s.value('ar_Size CCCore.aMemoKind'))
                check('day %d memos %s' % (d, [(x.kind, x.due) for x in c.memos]), gm == len(c.memos),
                      'game %d' % gm)
                g, m = await m3.game_law(s), m3.model_law(c)
                check('day %d law %s' % (d, m), g == m, 'game %s' % (g,))
                g, m = await game_late(s), model_late(c)
                check('day %d late %s' % (d, m), g == m, 'game %s' % (g,))
        # the end: retire and read the last letters
        check('tier 5 reached (day %s)' % t5_day, t5_day is not None)
        if t5_day:
            await visit()
            await click(11, 'Settings at tier 5 (RETIRE)')
            await click(1, 'RETIRE? (confirm)')
            await click(1, 'retired: the closed front page')
            check('the company is closed (iEnded 1, reason 5)',
                  (await s.value('CCCore.iEnded'), await s.value('CCCore.iEndReason')) == (1, 5))
            await click(2, 'the Post: the last letters')
            for i in range(len(tm.labels(c, t)) - 1):
                await click(i, 'read letter row %d' % i)
            await back('back to the closed front page')
            await close()
        errors = await s.script_errors()
    return check.bad, errors


def main(argv):
    last = int(argv[0]) if argv else 50
    bad, errors = asyncio.run(run(last))
    print('script errors: %d' % len(errors))
    for e in errors[:10]:
        print('  ', e)
    print('PASS' if not bad and not errors else 'FAIL (%d checks)' % bad)
    return 0 if not bad and not errors else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

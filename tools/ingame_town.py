"""Check lived-in Goodsprings in the game (T1) against tools/town_model.py.

    <fnv-mcp>/bridge/.venv/Scripts/python.exe tools/ingame_town.py [setup|away|here]

Needs a throwaway test game with LivedInMojave.esm (T1 build) loaded, started fresh (coc), never a
real save. It completes Doc Mitchell's intro (VCG01) by console, so the town quest starts.

  setup  the intro gate: nothing moves before VCG01; then the residents arrive home, enabled
  away   the player waits in Primm; at each test hour every resident is where the model says
         (T1.0 proof: a persistent actor follows its schedule while the player is away)
  here   the same with the player standing in Goodsprings: no clock jumps, the day runs in real
         time at timescale 60 (a game hour a minute; about 22 minutes), each place checked at hh:45
  walk   T1.5: the Pruitts walk out to the fields together at 07:00, watched from the porch; the
         next morning with Amos disabled, Lena and Cal still get there
  fight  T1.6: three geckos in the fields at 10:00: the alarm within 2 s, the residents who don't
         fight are home within 60 s, none of them killed
  gunfight  T1.7: Ghost Town Gunfight done for the town: the extra hand arrives
  gangers   T1.7: Run Goodsprings Run done for the Powder Gangers: a day later only Dutchy is left,
            out of GoodspringsFaction
"""
import asyncio
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import live                                 # noqa: E402
import gen_town                             # noqa: E402
import town_model as tm                     # noqa: E402

CORE_SPEC = HERE.parent / 'mod' / 'core' / 'core.spec.json'
HOURS = (2, 6, 9, 13, 16, 20)
SLACK = 500


class Checks:
    def __init__(self):
        self.bad = 0

    def __call__(self, what, ok, detail=''):
        self.bad += not ok
        print('%-58s %s%s' % (what, 'ok' if ok else 'FAILED', ('  ' + detail) if detail and not ok else ''))


async def where_is(s, r):
    """A short description of where the resident is now, for the report."""
    if await s.value('%s.GetDisabled' % r.ref):
        return 'disabled'
    for place, cell in gen_town.CELLS.items():
        if await s.value('%s.GetInCell %s' % (r.ref, cell)):
            return cell
    if await s.value('%s.GetInCell LIMHoldingCell' % r.ref):
        return 'holding cell'
    best = None
    for name in gen_town.MARKERS:
        d = await s.value('%s.GetDistance %sRef' % (r.ref, name))
        if best is None or d < best[1]:
            best = (name, d)
    return '%.0f from %s' % (best[1], best[0])


async def at_place(s, r, place):
    if place == tm.GONE:
        return bool(await s.value('%s.GetDisabled' % r.ref)) or bool(
            await s.value('%s.GetInCell LIMHoldingCell' % r.ref))
    if await s.value('%s.GetDisabled' % r.ref):
        return False
    if place in gen_town.CELLS:
        return bool(await s.value('%s.GetInCell %s' % (r.ref, gen_town.CELLS[place])))
    d = await s.value('%s.GetDistance %sRef' % (r.ref, place))
    return d <= gen_town.RADIUS.get(place, 300) + SLACK


async def setup(s, check):
    await s.to_game_mode()
    await asyncio.sleep(12)          # the town quest runs every 10 s
    check('nothing moves before the intro', bool(await s.value('LIMGSAmosRef.GetInCell LIMHoldingCell')) and
          bool(await s.value('LIMGSAmosRef.GetDisabled')))
    await s.console('set GameHour to 23')      # everyone's place is home at 23
    await s.console('CompleteQuest VCG01')
    await s.wait_for('LIMGoodsprings.iInit', tries=120, pause=0.5)
    for r in tm.CAST:
        if r.home in (1, 2, 3, 4):
            ok = bool(await s.value('%s.GetInCell %s' % (r.ref, gen_town.ARRIVE[r.home][0])))
            ok = ok and not await s.value('%s.GetDisabled' % r.ref)
            check('%s arrives home' % r.name, ok, await where_is(s, r))
    check('the gunfight hand waits', bool(await s.value('LIMGSTeaRef.GetDisabled')))


async def goto_hour(s, hour):
    """Move the clock forward to hour:03 the way a player's Wait does (the engine's one-hour step), not a
    console clock jump: after a jump unseen actors don't catch up (a sleep package keeps its end time,
    travellers lag). Jump (forward only) to an hour before, then wait across the hour."""
    now = await s.value('GameHour')
    ahead = (hour + 0.05 - now) % 24
    if ahead > 1:
        await s.tool('fnv_time', {'advance_hours': ahead - 1, 'mode': 'globals'})
    out = await s.tool('fnv_time', {'advance_hours': 1, 'mode': 'engine_wait', 'allow_unproven': True})
    if not out.get('ok'):
        raise RuntimeError('wait: %s' % out.get('error'))


async def schedule(s, check, away):
    if away:
        await s.console('player.MoveTo CCPrimmTermRef')
    else:
        await s.console('player.MoveTo LIMGSWatchRouteRef')
    await asyncio.sleep(3)
    await s.to_game_mode()
    if not away:
        await s.console('set TimeScale to 60')
    for hour in HOURS:
        if away:
            await goto_hour(s, hour)
            await asyncio.sleep(12)       # the town quest's travellers switch (10 s quest)
            await s.tool('fnv_time', {'advance_hours': 1 / 60, 'mode': 'globals'})   # packages re-evaluate
            await asyncio.sleep(4)
        else:
            # walk the clock in real time to hh:45: everyone has had 45 game minutes to walk there
            while True:
                now = await s.value('GameHour')
                if 0 <= now - (hour + 0.75) < 1:
                    break
                if (await s.menus()).get('inMenuMode'):
                    await s.to_game_mode()
                await asyncio.sleep(5)
        state = tm.town_state(tm.World(hour=hour))
        for r in tm.CAST:
            want = state.present[r.ref]
            ok = await at_place(s, r, want)
            check('%02d:00 %-14s at %s' % (hour, r.name, want[5:]), ok, '' if ok else await where_is(s, r))


PRUITTS = ('LIMGSAmosRef', 'LIMGSLenaRef', 'LIMGSCalRef')
FIELD_REACH = gen_town.RADIUS[tm.FIELDS] + SLACK


async def walk_out(s, check, who, label):
    """Watch the walk from the porch to the fields in real time (07:00 to 07:50 game time)."""
    await goto_hour(s, 6)
    await s.console('set GameHour to 6.75')            # forward: 06:45, a quarter hour before
    await s.console('player.MoveTo LIMGSPorch01Ref')
    await asyncio.sleep(3)
    await s.to_game_mode()
    spread, left, arrived = 0, False, set()
    for _ in range(150):                               # 2 s apart: 5 real minutes, past 07:50
        if await s.value('GameHour') >= 7.85:
            break
        if await s.value('%s.GetDistance LIMGSPorch01Ref' % who[0]) > 600:
            left = True
        if left and len(who) > 1 and len(arrived) < len(who):
            gaps = [await s.value('%s.GetDistance %s' % (a, b)) for i, a in enumerate(who) for b in who[i + 1:]]
            spread = max(spread, max(gaps))
        for r in who:
            if await s.value('%s.GetDistance LIMGSFieldsRef' % r) <= FIELD_REACH:
                arrived.add(r)
        await asyncio.sleep(2)
    check('%s: they leave the porch' % label, left)
    if len(who) > 1:
        check('%s: never more than 600 apart on the way (%.0f)' % (label, spread), spread <= 600)
    for r in who:
        check('%s: %s gets to the fields' % (label, tm.BY_REF[r].name), r in arrived,
              await where_is(s, tm.BY_REF[r]))


async def walk(s, check):
    await walk_out(s, check, PRUITTS, 'the family')
    await s.console('LIMGSAmosRef.Disable')
    await walk_out(s, check, PRUITTS[1:], 'Amos away')
    await s.console('LIMGSAmosRef.Enable')


async def fight(s, check):
    await goto_hour(s, 10)
    await s.console('player.MoveTo LIMGSFieldGateRef')
    await s.console('tgm')                             # the player only watches
    await asyncio.sleep(3)
    await s.to_game_mode()
    await asyncio.sleep(20)                            # the town settles at its morning places
    check('no alarm before the fight', not await s.value('LIMGSAlarm.iAlarm'))
    await s.console('LIMGSFieldsRef.PlaceAtMe LvlGecko 3')
    t0 = time.time()
    await s.wait_for('LIMGSAlarm.iAlarm', tries=40, pause=0.25)
    took = time.time() - t0
    check('the alarm within 2 s (%.1f s)' % took, took <= 2.0)
    away = [r for r in tm.CAST if not r.defender and r.home in tm.HOME]
    home = set()
    t0 = time.time()
    while time.time() - t0 < 60 and len(home) < len(away):
        for r in away:
            if r.ref not in home and await s.value('%s.GetInCell %s' % (r.ref, gen_town.CELLS[tm.HOME[r.home]])):
                home.add(r.ref)
        await asyncio.sleep(2)
    for r in away:
        check('%s runs home within 60 s' % r.name, r.ref in home, await where_is(s, r))
    await asyncio.sleep(60)                            # the defenders finish the geckos
    for r in tm.CAST:
        check('%s is alive' % r.name, not await s.value('%s.GetDead' % r.ref))
    await s.console('tgm')


async def gunfight(s, check):
    check('no extra hand before the gunfight', bool(await s.value('LIMGSTeaRef.GetDisabled')))
    await s.console('CompleteQuest VMS16')
    await s.to_game_mode()
    await s.wait_for('LIMGoodsprings.iGunfightWon', tries=60, pause=0.5)
    check('the extra hand arrives', not await s.value('LIMGSTeaRef.GetDisabled'))
    await goto_hour(s, 9)
    await asyncio.sleep(4)
    want = tm.town_state(tm.World(hour=9, gunfight=tm.GS_GUNFIGHT_WON)).present['LIMGSTeaRef']
    check('09:00 Tea Whitlock at %s' % want[5:], await at_place(s, tm.EXTRA_HAND, want),
          await where_is(s, tm.EXTRA_HAND))
    check('VMS16 completed', bool(await s.value('GetQuestCompleted VMS16')))


async def gangers(s, check):
    await s.console('SetStage VMS16b 100')
    await s.to_game_mode()                             # the reputation box stops quest scripts
    await s.wait_for('LIMGoodsprings.iGangers', tries=60, pause=0.5)
    await asyncio.sleep(12)
    check('the town waits a day', not await s.value('LIMGoodsprings.iGone'))
    await s.tool('fnv_time', {'advance_hours': 25, 'mode': 'engine_wait', 'allow_unproven': True})
    await s.to_game_mode()
    await s.wait_for('LIMGoodsprings.iGone', tries=60, pause=0.5)
    state = tm.town_state(tm.World(hour=int(await s.value('GameHour')), gunfight=tm.GS_GANGERS,
                                   gangers_since=25))
    for r in tm.CAST:
        if state.present[r.ref] == tm.GONE:
            check('%s has left town' % r.name, await at_place(s, r, tm.GONE), await where_is(s, r))
    check('Dutchy stays', not await s.value('LIMGSDutchyRef.GetDisabled'))
    check('Dutchy is out of GoodspringsFaction',
          not await s.value('LIMGSDutchyRef.GetInFaction GoodspringsFaction'))


async def run(what):
    check = Checks()
    async with live.session(CORE_SPEC) as s:
        if what == 'setup':
            await setup(s, check)
        else:
            if not await s.value('LIMGoodsprings.iInit'):
                await setup(s, check)
            if what in ('away', 'here'):
                await schedule(s, check, what == 'away')
                await s.console('set TimeScale to 30')
            else:
                modes = {'walk': walk, 'fight': fight, 'gunfight': gunfight, 'gangers': gangers}
                await modes[what](s, check)
        errors = await s.script_errors()
    print('script errors: %d' % len(errors))
    for e in errors[:10]:
        print('  ', e)
    print('PASS' if not check.bad and not errors else 'FAIL (%d checks)' % check.bad)
    return check.bad + len(errors)


if __name__ == '__main__':
    sys.exit(1 if asyncio.run(run(sys.argv[1] if len(sys.argv) > 1 else 'away')) else 0)

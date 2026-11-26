"""Run the company in the game for N days and compare each day with tools/company_model.py.

Founds the company in the running game (CCCore) with seed 1234 and the auto plan on, jumps the clock
one day at a time, reads the day history arrays and checks them against the model (no sheriff: a
fresh coc start has not done My Kind of Town). Needs a game started fresh with
MojaveCaravanCompany.esp loaded and the company not founded yet. Run with fnv-mcp's Python:

    <fnv-mcp>/bridge/.venv/Scripts/python.exe tools/ingame_run.py [days]

Never run it while the MCP server's own live tools are talking to the game (one companion pipe).
"""
import asyncio
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fnvmcp_call                          # noqa: E402  (sets up fnv-mcp's import path)
import company_model as cm                  # noqa: E402

SPEC = HERE.parent / 'mod' / 'company' / 'company.spec.json'
SEED = 1234
EVENTS = {'': 0, 'bandits_driven_off': 1, 'bandits_took_cargo': 2, 'bandits_wreck': 3}
FIELDS = ('aHistCash', 'aHistSales', 'aHistCosts', 'aHistEvent', 'aHistLoss')


def model_days(days):
    c = cm.Company(SEED, sheriff=False)
    c.found()
    rows = []
    for _ in range(days):
        for o in c.plan():
            c.queue(o)
        r = c.tick()
        rows.append((r.cash, r.sales, r.costs, EVENTS[r.event], r.event_loss))
    return rows


async def run(days):
    project = fnvmcp_call.Project.load(str(fnvmcp_call.PROJECT_FILE))
    spec = json.loads(SPEC.read_text(encoding='utf-8'))
    project = project.model_copy(update={'spec': SPEC, 'plugin': spec['plugin']})
    async with fnvmcp_call.Client(fnvmcp_call.make_server(project)) as client:
        async def tool(name, args):
            for _ in range(6):       # the MCP server holds the companion pipe for 20 s after its last call
                res = await client.call_tool(name, args)
                out = res.structured_content or {}
                if (out.get('error') or {}).get('code') != 'COMPANION_UNREACHABLE':
                    return out
                await asyncio.sleep(8)
            raise RuntimeError('%s: the companion pipe stayed busy' % name)

        async def console(line):
            out = await tool('fnv_console', {'line': line})
            if not out.get('ok'):
                raise RuntimeError('%s: %s' % (line, out.get('error')))
            return out['data'].get('output') or []

        async def read(days):
            game = []
            for i in range(days):
                row = []
                for f in FIELDS:
                    row.append(int(await value('CCCore.%s[%d]' % (f, i))))
                game.append(tuple(row))
            errors = await tool('fnv_script_errors', {'since': 'start'})
            return game, (errors.get('data') or {}).get('errors', [])

        async def value(expr):
            out = await console('printc "v=%%g" (%s)' % expr)
            got = [l[2:] for l in out if l.startswith('v=')]
            if not got:
                raise RuntimeError('no value for %s: %s' % (expr, out))
            return float(got[-1])

        # GameMode scripts stop while the pause menu is up (it opens when the game window loses focus)
        await tool('fnv_window', {'action': 'background'})
        # and while a message box is up: the DLC "has been loaded" boxes come one after another
        for _ in range(30):
            state = await tool('fnv_menu', {})
            data = state.get('data') or {}
            if data.get('messageBox'):
                await tool('fnv_ui_do', {'action': 'message', 'button': '0'})
                await asyncio.sleep(1)
            elif data.get('inMenuMode'):
                await tool('fnv_window', {'action': 'unpause'})
                await asyncio.sleep(1)
            else:
                break
        else:
            raise RuntimeError('the game stays in menu mode')
        founded, done = await value('CCCore.iFounded'), await value('ar_Size CCCore.aHistCash')
        if founded and await value('CCCore.iSeed') == SEED and done >= days:
            print('reading a finished run (%d days in the game)' % done)
            return await read(days)
        if founded and (done or await value('CCCore.iSeed') != SEED):
            raise RuntimeError('the company is already running: start a fresh game')
        await console('set CCCore.iSeed to %d' % SEED)
        await console('set CCCore.iAuto to 1')
        await console('set CCCore.iFoundNow to 1')
        for _ in range(40):
            if await value('CCCore.iFounded'):
                break
            await asyncio.sleep(0.25)
        else:
            raise RuntimeError('the company was not founded')
        print('founded: cash %d owner %d loan %d' % (await value('CCCore.iCash'), await value('CCCore.iOwner'),
                                                    await value('CCCore.iLoan')))
        for day in range(1, days + 1):
            await console('set GameHour to GameHour + 24')
            for _ in range(80):
                if await value('ar_Size CCCore.aHistCash') >= day:
                    break
                await asyncio.sleep(0.25)
            else:
                raise RuntimeError('day %d did not tick' % day)
        return await read(days)


def main(argv):
    days = int(argv[0]) if argv else 14
    game, errors = asyncio.run(run(days))
    model = model_days(days)
    bad = 0
    print('day  game (cash sales costs event loss)        model')
    for d, (g, m) in enumerate(zip(game, model), 1):
        mark = '' if g == m else '   <-- differs'
        bad += g != m
        print('%3d  %-38s %s%s' % (d, g, m, mark))
    print('script errors: %d' % len(errors))
    for e in errors[:10]:
        print('  ', e)
    print('MATCH' if not bad and not errors else 'DIFFERS on %d day(s)' % bad)
    return 0 if not bad and not errors else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

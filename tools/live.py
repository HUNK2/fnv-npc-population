"""A live session with the running game through fnv-mcp's tools, in-process (tools/fnvmcp_call.py).

Used by the in-game checks (ingame_run.py, ingame_terminal.py). Never run one while the MCP
server's own live tools are talking to the game: the companion pipe has one instance.
"""
import asyncio
import contextlib
import json
import sys
import time
from pathlib import Path

import fnvmcp_call

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import game_window                          # noqa: E402
COMPANY_SPEC = HERE.parent / 'mod' / 'company' / 'company.spec.json'
SEED = 1234
ARRIVAL_WINDOW = 105    # fnv-mcp closes message boxes for 90 s after a coc launch; margin for the load


class Session:
    def __init__(self, client):
        self.client = client

    async def tool(self, name, args):
        for _ in range(6):       # the MCP server holds the companion pipe for 20 s after its last call
            res = await self.client.call_tool(name, args)
            out = res.structured_content or {}
            if (out.get('error') or {}).get('code') != 'COMPANION_UNREACHABLE':
                return out
            await asyncio.sleep(8)
        raise RuntimeError('%s: the companion pipe stayed busy' % name)

    async def console(self, line):
        out = await self.tool('fnv_console', {'line': line})
        if not out.get('ok'):
            raise RuntimeError('%s: %s' % (line, out.get('error')))
        return out['data'].get('output') or []

    async def value(self, expr):
        for attempt in range(3):
            out = await self.console('printc "v=%%g" (%s)' % expr)
            got = [line[2:] for line in out if line.startswith('v=')]
            if got:
                return float(got[-1])
            await asyncio.sleep(0.5)
        raise RuntimeError('no value for %s: %s' % (expr, out))

    async def wait_for(self, expr, want=True, tries=80, pause=0.25):
        for _ in range(tries):
            v = await self.value(expr)
            if bool(v) == want:
                return v
            await asyncio.sleep(pause)
        raise RuntimeError('%s did not become %s' % (expr, want))

    async def menus(self):
        return (await self.tool('fnv_menu', {})).get('data') or {}

    async def to_game_mode(self):
        """Quest scripts stop while the pause menu or a message box is up: the pause menu opens on focus
        loss, and a fresh coc start shows the DLC "has been loaded" boxes one after another.

        After a coc launch fnv-mcp's companion closes every message box (every 0.3 s) for 90 s, which
        would close the mod's field letters too: wait until that window is over."""
        launched = (((await self.tool('fnv_status', {})).get('data') or {}).get('session') or {}).get('launchedAt')
        if launched:
            left = launched + ARRIVAL_WINDOW - time.time()
            if left > 0:
                print('waiting %.0f s for the launch message closer to stop' % left)
                await asyncio.sleep(left)
        await self.tool('fnv_window', {'action': 'background'})
        if game_window.wanted_monitor():
            game_window.move(game_window.wanted_monitor())
            await asyncio.sleep(0.5)
        game_window.focus()             # in the background the game drops to ~10 fps and game time crawls
        for _ in range(30):
            data = await self.menus()
            if data.get('messageBox'):
                await self.tool('fnv_ui_do', {'action': 'message', 'button': '0'})
                await asyncio.sleep(1)
            elif any(m.get('name') == 'DialogMenu' for m in data.get('menuStack') or []):
                # a vanilla NPC who greets the player on sight (Sunny Smiles in the saloon) opens a talk
                await self.tool('fnv_ui_do', {'action': 'close_all'})
                await asyncio.sleep(1)
            elif data.get('inMenuMode'):
                await self.tool('fnv_window', {'action': 'unpause'})
                await asyncio.sleep(1)
            else:
                return
        raise RuntimeError('the game stays in menu mode')

    async def found(self, auto=1):
        """Found the company with the test seed (needs a fresh game with no company)."""
        if await self.value('CCCore.iFounded'):
            raise RuntimeError('the company is already running: start a fresh game')
        await self.console('set CCCore.iSeed to %d' % SEED)
        await self.console('set CCCore.iFoundNow to 1')
        await self.wait_for('CCCore.iFounded')
        # founding turns the daily plan on (M1 1.10); a check that wants it off sets it after
        await self.console('set CCCore.iAuto to %d' % auto)

    async def next_day(self):
        """Jump one day. A field letter left open is pressed with its first button first ("Keep it home" for
        a road letter, the same as the memo's default): quest scripts stop while a message box is up."""
        if (await self.menus()).get('messageBox'):
            await self.tool('fnv_ui_do', {'action': 'message', 'button': '0'})
            await asyncio.sleep(0.5)
        day = int(await self.value('ar_Size CCCore.aHistCash'))
        await self.console('set GameHour to GameHour + 24')
        await self.wait_for('(ar_Size CCCore.aHistCash) > %d' % day)
        return day + 1

    async def script_errors(self):
        return ((await self.tool('fnv_script_errors', {'since': 'start'})).get('data') or {}).get('errors', [])


@contextlib.asynccontextmanager
async def session(spec=COMPANY_SPEC):
    project = fnvmcp_call.Project.load(str(fnvmcp_call.PROJECT_FILE))
    data = json.loads(Path(spec).read_text(encoding='utf-8'))
    project = project.model_copy(update={'spec': Path(spec), 'plugin': data['plugin']})
    async with fnvmcp_call.Client(fnvmcp_call.make_server(project)) as client:
        yield Session(client)

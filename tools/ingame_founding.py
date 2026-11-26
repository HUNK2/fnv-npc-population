"""Check the founding in the game (M1 task 1.5): Alice's agent, the letter of credit, the wagon yard.

Needs a fresh game with MojaveCaravanCompany.esp loaded and no company yet (for example started with
coc GSProspectorSaloonInterior). It changes that game for good (kills and revives Alice, sets Run
Goodsprings Run done), so use a throwaway test game, never a real save. Checks, in order:

1. Hollis Webb and the company terminal arrive at the agent's table in the Prospector Saloon;
   the wagon yard behind Chet's store is still disabled.
2. The pitch Hollis would give: the plain one; with Alice dead, Jason Tagg's office; with the Powder
   Gangers holding Goodsprings (Run Goodsprings Run done), the landlord one.
3. Signing with fewer than 500 caps is refused and founds nothing.
4. Signing with 600 caps takes 500 and founds the company: cash 2,500, loan 3,000, owner funds 0
   (the doc's day 0); the wagon, brahmin and chalkboard are enabled; Hollis now talks as the agent.

Run with fnv-mcp's Python:  <fnv-mcp>/bridge/.venv/Scripts/python.exe tools/ingame_founding.py
"""
import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import live                                 # noqa: E402

HOLLIS = 'CCAgentHollisRef'
YARD = ('CCWagonCartRef', 'CCBrahmin1Ref', 'CCBrahmin2Ref', 'CCChalkboardRef')
RECEIPT = live.fnvmcp_call.BRIDGE / 'build' / 'MojaveCaravanCompany.receipt.json'
PITCH, PITCH_TAGG, PITCH_GANG, OWNER = 'pitch', 'pitch_tagg', 'pitch_gang', 'owner'   # CCFoundAsk lines
POOR = 'Five hundred of your own'
SIGNED = 'Signed and witnessed'


class Checks:
    def __init__(self):
        self.bad = 0

    def __call__(self, what, ok, detail=''):
        self.bad += not ok
        print('%-58s %s%s' % (what, 'ok' if ok else 'FAILED', ('  ' + detail) if detail and not ok else ''))


def line_ids():
    """CCFoundAsk line key -> its FormID without the load-order byte (from the last build's receipt)."""
    ids = json.loads(RECEIPT.read_text(encoding='utf-8'))['formIds']
    return {k.split(':')[2]: v[2:].upper() for k, v in ids.items() if k.startswith('INFO:CCFoundAsk:')}


async def would_say(s, topic='CCFoundAsk'):
    """The key of the CCFoundAsk line the engine would pick now (fnv_dialogue tree wouldSay is its FormID)."""
    out = await s.tool('fnv_dialogue', {'action': 'tree', 'speaker': HOLLIS, 'topic': topic})
    form = str((out.get('data') or {}).get('wouldSay') or '').upper()
    return next((k for k, v in line_ids().items() if form.endswith(v)), form or 'nothing')


async def talk(s, choices):
    out = await s.tool('fnv_dialogue_choose', {'speaker': HOLLIS, 'choices': choices, 'close': True})
    if (out.get('error') or {}).get('code') == 'NO_DIALOGUE':
        # once after the Powder Ganger takeover the talk did not open; the next try did
        await asyncio.sleep(2)
        await s.to_game_mode()
        out = await s.tool('fnv_dialogue_choose', {'speaker': HOLLIS, 'choices': choices, 'close': True})
    return json.dumps(out)


async def caps(s):
    return int(await s.value('player.GetItemCount Caps001'))


async def run():
    check = Checks()
    async with live.session() as s:
        await s.to_game_mode()
        if await s.value('CCCore.iFounded'):
            raise RuntimeError('the company is already founded: start a fresh game')
        await s.wait_for('%s.GetInCell GSProspectorSaloonInterior' % HOLLIS)
        check('Hollis is in the Prospector Saloon', True)
        check('the terminal is in the Prospector Saloon',
              bool(await s.value('CCAgentTermRef.GetInCell GSProspectorSaloonInterior')))
        check('the Primm branch terminal is in Vikki and Vance',
              bool(await s.value('CCPrimmTermRef.GetInCell VikkiAndVance')))
        check('the wagon yard waits (disabled)',
              all([await s.value('%s.GetDisabled' % r) for r in YARD]))
        await s.console('player.MoveTo %s' % HOLLIS)
        await s.to_game_mode()

        said = await would_say(s)
        check('plain pitch', said == PITCH, said[:300])

        await s.console('AliceMcLaffertyREF.Kill')
        await s.wait_for('CCFounding.iAliceDead')
        said = await would_say(s)
        check("Alice dead: Jason Tagg's office", said == PITCH_TAGG, said[:300])
        await s.console('AliceMcLaffertyREF.Resurrect')
        await s.wait_for('CCFounding.iAliceDead', want=False)

        await s.console('SetStage VMS16b 100')
        await asyncio.sleep(1)
        await s.to_game_mode()          # the stage shows a reputation box: quest scripts wait under it
        await s.wait_for('CCFounding.iGangLandlord')
        said = await would_say(s)
        check('Powder Gangers hold Goodsprings: landlord pitch', said == PITCH_GANG, said[:300])

        have = await caps(s)
        if have:
            await s.console('player.RemoveItem Caps001 %d' % have)
        await s.console('player.AddItem Caps001 100')
        said = await talk(s, ['You lend money', "I'll sign"])
        check('100 caps: signing refused', POOR in said, said[:400])
        await s.to_game_mode()
        await asyncio.sleep(2)
        check('100 caps: no company, caps kept',
              not await s.value('CCCore.iFounded') and await caps(s) == 100)

        await s.console('player.AddItem Caps001 500')
        said = await talk(s, ['You lend money', 'What happens', "I'll sign"])
        check('600 caps: signed', SIGNED in said, said[:400])
        await s.to_game_mode()
        await s.wait_for('CCCore.iFounded')
        got = [int(await s.value('CCCore.%s' % v)) for v in ('iCash', 'iLoan', 'iOwner', 'iTier')]
        check('day 0: cash 2500, loan 3000, owner 0, tier 1', got == [2500, 3000, 0, 1], str(got))
        check('the player paid 500 caps', await caps(s) == 100)
        await s.wait_for('CCFounding.iYardOn')
        check('the wagon yard is enabled', not any([await s.value('%s.GetDisabled' % r) for r in YARD]))
        said = await would_say(s)
        check('Hollis talks as the agent after founding', said == OWNER, said[:300])
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

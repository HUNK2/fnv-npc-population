"""Write T1 Goodsprings into the core plugin's spec (mod/core/core.spec.json) from tools/town_model.py.

    python tools/gen_town.py

Every record it writes has an editor id starting LIMGS (or the two quests LIMGoodsprings and
LIMGSAlarm); it replaces those and leaves the rest of the spec alone. Layouts of the vanilla
records it patches are in docs/plans/2026-11-27-t1-goodsprings.md ("Records").
"""
import json
import math
from pathlib import Path

import town_model as tm

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / 'mod' / 'core' / 'core.spec.json'

# --- who looks like whom (vanilla bases with no actor template, no script) ----------------------
LOOKS = {
    'LIMGSAmosRef': ('1ESharecropperAAMTemplate', 'M'),
    'LIMGSLenaRef': ('VVault34SharecropperCF', 'F'),
    'LIMGSCalRef': ('UnderpassCitizen06', 'M'),
    'LIMGSJosephRef': ('RancherAAMTemplate', 'M'),
    'LIMGSAdaRef': ('NovacSettler01', 'F'),
    'LIMGSRuthRef': ('VOVNorthDwellerCFqChild', 'F'),
    'LIMGSHarlanRef': ('Boomer00FFarmer', 'F'),
    'LIMGSWesRef': ('VVault34SharecropperHM', 'M'),
    'LIMGSDutchyRef': ('UnderpassCitizen03', 'M'),
    'LIMGSMarisolRef': ('VVault34SharecropperAFAnne', 'F'),
    'LIMGSAbeRef': ('Boomer00MFarmer', 'M'),
    'LIMGSHectorRef': ('WestsideCitizenAAMTemplate', 'M'),
    'LIMGSProspectorRef': ('NVProspectorMale', 'M'),
    'LIMGSDrifterRef': ('UnderpassCitizen05', 'M'),
    'LIMGSTeaRef': ('UnderpassCitizen04', 'F'),
}
ACBS_FLAGS = {'M': 0x10, 'F': 0x11}                # auto-calc stats (+ female)
CHILD_FLAGS = 0x13      # female, essential, auto-calc (the child template's 0x200 'no low-level
                        # processing' froze her schedule while unseen; 0x08 respawn not wanted)

# --- places --------------------------------------------------------------------------------------
# exterior markers (WastelandNV): x, y, z, heading; z from the nearest vanilla ground objects (checked in T1.3)
MARKERS = {
    tm.FIELDS: (-72300, -3300, 8150, 0),
    'LIMGSFieldGate': (-71700, -3300, 8200, 270),
    tm.PORCH[1]: (-70550, -3799, 8307, 90),
    tm.PORCH[2]: (-71524, -856, 8231, 180),
    tm.PORCH[3]: (-68100, -1120, 8195, 280),
    tm.SPRING: (-69000, 2500, 8344, 0),
    tm.SCHOOLYARD: (-74520, -4450, 8205, 0),
    tm.GARDEN: (-68000, -1650, 8090, 0),
    tm.ROAD: (-69500, 1200, 8190, 0),
}
RADIUS = {tm.FIELDS: 500, tm.PORCH[1]: 250, tm.PORCH[2]: 250, tm.PORCH[3]: 250, tm.SPRING: 300,
          tm.SCHOOLYARD: 500, tm.GARDEN: 300, tm.ROAD: 2000}
# interiors the packages use whole ("in cell")
CELLS = {tm.HOME[1]: 'GSHouseInterior01', tm.HOME[2]: 'GSHouseInterior02', tm.HOME[3]: 'GSHouseInterior03',
         tm.HOME[4]: 'GSHouseInterior04', tm.SALOON: 'GSProspectorSaloonInterior', tm.STORE: 'GSGeneralStore',
         tm.WATCH_BED: 'GSProspectorSaloonInterior'}   # a rented room (the gas station's door is too far up the hill: he never left it)
# where each resident is moved on the first run (cell, x, y, z): beside their bed
ARRIVE = {
    1: ('GSHouseInterior01', 900, -400, 2340), 2: ('GSHouseInterior02', 1150, -250, 2340),
    3: ('GSHouseInterior03', 450, -350, 2340), 4: ('GSHouseInterior04', 700, -300, 2340),
    0: ('GSProspectorSaloonInterior', 220, 260, 3460), -1: ('GSProspectorSaloonInterior', 300, -300, 3460),
}
# extra beds (the homes have too few): moved in on the first run like the residents
BEDS = [
    ('LIMGSBed01a', 'NVBedrollR', 'GSHouseInterior01', 800, -560, 2336, 0),
    ('LIMGSBed01b', 'NVBedrollL', 'GSHouseInterior01', 700, -560, 2336, 0),
    ('LIMGSBed02a', 'NVBedrollR', 'GSHouseInterior02', 1100, -400, 2336, 0),
    ('LIMGSBed04a', 'NVBedrollR', 'GSHouseInterior04', 600, -500, 2336, 0),
    ('LIMGSBed04b', 'NVBedrollL', 'GSHouseInterior04', 500, -500, 2336, 0),
    ('LIMGSBedWatch', 'NVBedrollR', 'GSProspectorSaloonInterior', 250, 300, 3457, 0),
    ('LIMGSBedTrav1', 'NVBedrollR', 'GSProspectorSaloonInterior', 450, 300, 3457, 0),
    ('LIMGSBedTrav2', 'NVBedrollL', 'GSProspectorSaloonInterior', 350, 300, 3457, 0),
]
FIELD_STATICS = [   # crop rows and a sign around the fields marker (collisionless furrows)
    ('cropFurrowLongNV', -200, -150, 0), ('cropFurrowLongNV', -200, 0, 0), ('cropFurrowLongNV', -200, 150, 0),
    ('cropFurrowLongNV', 200, -150, 0), ('cropFurrowLongNV', 200, 0, 0), ('cropFurrowLongNV', 200, 150, 0),
    ('NVSharecropSign', 480, 300, 270),
]

# --- packages ------------------------------------------------------------------------------------
T_SANDBOX = '@GSSettlerCFSandboxPackage6x6'
T_SLEEP = '@GSSettlerAAMSleepPackage22x8'
T_TRAVEL = '@EasyPeteChairPackage8x4'
T_FOLLOW = '@DefaultFollowLinkedClose'
T_FLEE = '@EasyPeteHideInSaloonPackage'
F_GETQUESTVAR, F_GETDISABLED = 79, 35
ALARM_FLAGS = 0x2 | 0x2000 | 0x100000                 # must reach location, always run, ignore combat
ALARM_VAR = 1                                    # LIMGSAlarm's first variable (iAlarm)


def ctda(func, p1=0, p2=0, comp=1.0, op=0, run_on=0, ref=0):
    """One condition: op (0 ==, 1 !=, ...) in the top 3 bits of the first byte."""
    return {'tag': 'CTDA', 'append': True, 'pack': '<B3xfIIIII',
            'values': [op << 5, comp, func, p1, p2, run_on, ref]}


def psdt(hour, dur):
    return {'tag': 'PSDT', 'pack': '<bbBbi', 'values': [-1, -1, 0, hour, dur]}


def pldt(kind, target, radius=0):
    return {'tag': 'PLDT', 'pack': '<iIi', 'values': [kind, target, radius]}


def pack_record(template, *fields):
    return {'type': 'PACK', 'template': template,
            'fields': [{'tag': 'CTDA', 'remove': True}] + list(fields)}


def where(place):
    """The package location for a place: near a marker, or in a whole cell."""
    if place in CELLS:
        return pldt(1, '@' + CELLS[place])
    return pldt(0, '@' + place + 'Ref', RADIUS.get(place, 300))


def blocks(r):
    """(start hour, hours, place) runs of the resident's day, from town_model.place."""
    out, h = [], 0
    while h < 24:
        p = tm.place(r, h)
        n = 1
        while h + n < 24 and tm.place(r, h + n) == p:
            n += 1
        out.append((h, n, p))
        h += n
    # a run that ends at 24 and one that starts at 0 in the same place are one night
    if len(out) > 1 and out[0][2] == out[-1][2]:
        s, n, p = out.pop()
        h0, n0, _ = out.pop(0)
        out.append((s, n + n0, p))
    return out


def bed_place(r):
    return {0: tm.WATCH_BED, -1: tm.SALOON}.get(r.home, tm.HOME.get(r.home))


def asleep(r, h):
    """Sleeping hours: the watch sleeps all day in his bed; everyone else 22 to 6 (a child from 20)."""
    if r.home == 0:
        return True
    return h >= (20 if r.child else 22) or h < 6


def sleep_split(r, runs):
    """Split each run in its bed place into awake and asleep parts: (start, hours, place, asleep)."""
    out = []
    for start, hours, place in runs:
        if place != bed_place(r):
            out.append((start, hours, place, False))
            continue
        cur = None
        for i in range(hours):
            h = (start + i) % 24
            s = asleep(r, h)
            if cur and cur[3] == s:
                cur[1] += 1
            else:
                cur = [h, 1, place, s]
                out.append(cur)
    return [tuple(x) for x in out]


def packages_for(r, records):
    short = r.ref[len('LIMGS'):-len('Ref')]
    ids = []

    def add(name, rec):
        ed = 'LIMGS%s%s' % (short, name)
        records[ed] = rec
        ids.append('@' + ed)

    if r.home in tm.HOME:     # the alarm: run home (not the defenders, not the travellers)
        if not r.defender:
            # a travel package, not a flee one: the engine never picked the flee package (eligible, first on
            # the list, still the sandbox after EvaluatePackage); must reach, always run, ignore combat
            add('Alarm', pack_record(T_TRAVEL, pldt(1, '@' + CELLS[tm.HOME[r.home]]), psdt(-1, 0),
                                     {'tag': 'PKDT', 'patch': [[0, '<I', ALARM_FLAGS]]},
                                     ctda(F_GETQUESTVAR, '@LIMGSAlarm', ALARM_VAR)))
    for start, hours, place, night in sleep_split(r, blocks(r)):
        if place == tm.GONE:
            continue      # a traveller away by day is disabled by the town quest
        tag = '%02dx%d' % (start, hours)
        if r.ref in ('LIMGSLenaRef', 'LIMGSCalRef') and place == tm.FIELDS:
            # the family walks out with Amos for the first hour, then works the field
            add('Walk' + tag, pack_record(T_FOLLOW, psdt(start, 1),
                                          {'tag': 'PTDT', 'pack': '<iIif', 'values': [0, '@LIMGSAmosRef', 160, 0.0]},
                                          ctda(F_GETDISABLED, comp=0.0, run_on=2, ref='@LIMGSAmosRef')))
        if r.ref == tm.GROUP_LEADER and place == tm.FIELDS:
            add('Walk' + tag, pack_record(T_TRAVEL, pldt(0, '@LIMGSFieldGateRef'), psdt(start, 1)))
        if night:
            add('Sleep' + tag, pack_record(T_SLEEP, where(place), psdt(start, hours)))
        else:
            add('Be' + tag, pack_record(T_SANDBOX, where(place), psdt(start, hours)))
    # fallback: sandbox at home (or the saloon) at any hour
    home = tm.HOME.get(r.home) or (tm.WATCH_BED if r.home == 0 else tm.SALOON)
    add('Idle', pack_record(T_SANDBOX, where(home), psdt(-1, 0)))
    return ids


def npc_record(r, pkids):
    base, sex = LOOKS[r.ref]
    flags = CHILD_FLAGS if r.child else ACBS_FLAGS[sex]
    defend = r.defender
    items = [('@LL1NPCTownClothes100', 1), ('@CapsChange50', 1)]
    if defend:
        items.append(('@WithAmmoNVVarmintRifleLoot', 1))
    fields = [
        {'tag': 'FULL', 'text': r.name[0].upper() + r.name[1:]},
        {'tag': 'TPLT', 'remove': True},
        {'tag': 'SCRI', 'remove': True},
        {'tag': 'COED', 'remove': True},
        {'tag': 'CNTO', 'remove': True},
        {'tag': 'SNAM', 'remove': True},
        {'tag': 'PKID', 'remove': True},
        {'tag': 'ACBS', 'patch': [[0, '<I', flags], [22, '<H', 0]]},
        {'insert': [{'tag': 'SNAM', 'pack': '<IB3x', 'values': ['@GoodspringsFaction', 0]},
                    {'tag': 'SNAM', 'pack': '<IB3x', 'values': ['@LIMTownsfolkFaction', 0]}], 'after': 'ACBS'},
        {'insert': [{'tag': 'SCRI', 'form': '@LIMGSResidentScript'}] +
                   [{'tag': 'CNTO', 'pack': '<Ii', 'values': [i, n]} for i, n in items], 'after': 'EAMT'},
        # aggression 0 (unaggressive); confidence brave or cowardly; assistance helps allies (defenders)
        {'tag': 'AIDT', 'pack': '<BBBBB3xIbBBBi',
         'values': [0, 3 if defend else 0, 50, 50, 0, 0, -1, 0, 1 if defend else 0, 0, 0]},
        {'insert': [{'tag': 'PKID', 'form': p} for p in pkids], 'after': 'AIDT'},
    ]
    return {'type': 'NPC_', 'template': '@' + base, 'fields': fields}


# --- what each resident says when greeted (text only, no voice): (after the gunfight, any time) ----
GREETINGS = {
    'LIMGSAmosRef': ("You stood with us against those gangers. Walk my field any time.",
                     "Rows don't water themselves. Mind the furrows."),
    'LIMGSLenaRef': ("Folks still talk about the gunfight. Thank you for that.",
                     "Cal, quit gawking. Morning, stranger."),
    'LIMGSCalRef': ("Were you really in the gunfight? I watched from the window.",
                    "Pa says I get my own row next spring."),
    'LIMGSJosephRef': ("Water tastes sweeter with no gangers drinking it.",
                       "The well runs low every summer. Every single one."),
    'LIMGSAdaRef': ("You saved this town a funeral or two. Mending's free for you.",
                    "Got a tear in that coat? I can mend it. Cheap."),
    'LIMGSRuthRef': ("Mama says you're brave.", "Do you have a dog? Sunny has a dog."),
    'LIMGSHarlanRef': ("My Henry would have liked you.", "My Henry planted this garden. I keep it going."),
    'LIMGSWesRef': ("You handled yourself out there. Need a hand, ask.",
                    "Every bucket in this town came up on my arms."),
    'LIMGSDutchyRef': ("Guess the town's yours now, huh.", "Work's work. Don't much care who pays."),
    'LIMGSMarisolRef': ("Good shooting. I counted.", "Keep that gun holstered near the fields."),
    'LIMGSAbeRef': ("Fifty years I've worked dirt, and I never saw a fight like that.",
                    "Dirt don't lie. People do."),
    'LIMGSHectorRef': ("Quiet nights since the gangers ran. I like quiet.",
                       "Night watch. I sleep while you do your business."),
    'LIMGSTeaRef': ("Heard Goodsprings had work after the gunfight. Here I am.",
                    "Heard Goodsprings had work after the gunfight. Here I am."),
    'LIMGSProspectorRef': ("Heard about the gunfight clear up in the hills.",
                           "Nothing in those hills but rocks and more rocks."),
    'LIMGSDrifterRef': ("Town feels safer. Might stay a night more.", "Just passing through. Same as you."),
}


def greetings():
    infos = []
    for ref, (won, plain) in GREETINGS.items():
        who = {'function': 'GetIsID', 'param1': '@' + ref[:-3], 'op': '==', 'value': 1}
        key = ref[5:-3].lower()
        infos.append({'key': 'lim_%s_won' % key, 'quest': '@LIMGoodsprings', 'flags': ['goodbye'],
                      'conditions': [who, {'function': 'GetQuestVariable', 'param1': '@LIMGoodsprings',
                                           'param2': 2, 'op': '==', 'value': 1}],
                      'responses': [won]})
        infos.append({'key': 'lim_%s' % key, 'quest': '@LIMGoodsprings', 'flags': ['goodbye'],
                      'conditions': [who], 'responses': [plain]})
    return {'type': 'DIAL', 'override': True, 'infos': infos}


def grid(x, y):
    return [math.floor(x / 4096), math.floor(y / 4096)]


def main():
    spec = json.loads(SPEC.read_text(encoding='utf-8'))
    recs = spec['records']
    for k in [k for k in recs if k.startswith('LIMGS') or k in ('LIMGoodsprings', 'LIMGSAlarm')]:
        del recs[k]
    cast = list(tm.CAST) + [tm.EXTRA_HAND]
    for r in cast:
        pk = packages_for(r, recs)
        recs[r.ref[:-3]] = npc_record(r, pk)
    recs['GREETING'] = greetings()
    recs['LIMGSResidentScript'] = {'type': 'SCPT', 'source': 'scripts/LIMGSResidentScript.gek', 'script_type': 'object'}
    recs['LIMGoodspringsScript'] = {'type': 'SCPT', 'source': 'scripts/LIMGoodspringsScript.gek', 'script_type': 'quest'}
    recs['LIMGSAlarmScript'] = {'type': 'SCPT', 'source': 'scripts/LIMGSAlarmScript.gek', 'script_type': 'quest'}
    recs['LIMGoodsprings'] = {'type': 'QUST', 'fields': [
        {'tag': 'SCRI', 'form': '@LIMGoodspringsScript'}, {'tag': 'FULL', 'text': 'Lived-in Goodsprings'},
        {'tag': 'DATA', 'pack': '<BBBBf', 'values': [1, 40, 0, 0, 10.0]}]}
    recs['LIMGSAlarm'] = {'type': 'QUST', 'fields': [
        {'tag': 'SCRI', 'form': '@LIMGSAlarmScript'}, {'tag': 'FULL', 'text': 'Goodsprings alarm'},
        {'tag': 'DATA', 'pack': '<BBBBf', 'values': [1, 40, 0, 0, 1.0]}]}

    # the holding cell: every resident and the extra beds wait here until the first run
    cells = spec.setdefault('cells', {})
    objs = []
    for i, r in enumerate(cast):
        objs.append({'ref_id': r.ref[5:-3].lower(), 'base': '@' + r.ref[:-3], 'editor_id': r.ref,
                     'persistent': True, 'disabled': True, 'position': [i * 150, 0, 0]})
    for i, (ed, base, *_rest) in enumerate(BEDS):
        objs.append({'ref_id': ed[5:].lower(), 'base': '@' + base, 'editor_id': ed + 'Ref',
                     'persistent': True, 'position': [i * 150, 600, 0]})
    objs.append({'ref_id': 'gone', 'base': '@XMarker', 'editor_id': 'LIMGSHoldingRef', 'persistent': True,
                 'position': [0, -600, 0]})
    cells['LIMHoldingCell'] = {'name': 'Lived-in Mojave Holding', 'objects': objs}

    # exterior markers and field statics
    worlds = spec.setdefault('worlds', {}).setdefault('WastelandNV', {}).setdefault('cells', {})
    for k in [k for k in worlds if k.startswith('limgs')]:
        del worlds[k]
    for name, (x, y, z, h) in MARKERS.items():
        key = 'limgs_' + name[5:].lower()
        worlds[key] = {'grid': grid(x, y), 'objects': [
            {'ref_id': name[5:].lower(), 'base': '@XMarkerHeading', 'editor_id': name + 'Ref',
             'persistent': True, 'position': [x, y, z], 'rotation': [0, 0, h]}]}
    fx, fy, fz, _ = MARKERS[tm.FIELDS]
    worlds['limgs_fields']['objects'] += [
        {'ref_id': 'crop%d' % i, 'base': '@' + b, 'position': [fx + dx, fy + dy, fz], 'rotation': [0, 0, rz]}
        for i, (b, dx, dy, rz) in enumerate(FIELD_STATICS)]
    SPEC.write_text(json.dumps(spec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    n_pack = sum(1 for v in recs.values() if v.get('type') == 'PACK')
    print('wrote %d residents, %d packages, %d markers, %d beds' % (len(cast), n_pack, len(MARKERS), len(BEDS)))


if __name__ == '__main__':
    main()

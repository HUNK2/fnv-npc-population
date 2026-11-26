"""Lived-in Goodsprings (T1): who is where at each hour, and how the town reacts to the player.

The spec the core plugin follows (docs/towns-design.md). The game side reads the same tables: each
resident's package list is written from DAY, and the town quest LIMGoodsprings sets its state from
town_state() once a game hour.
"""
from dataclasses import dataclass, field

# places (marker editor ids in the core plugin)
HOME = {1: 'LIMGSHome01', 2: 'LIMGSHome02', 3: 'LIMGSHome03', 4: 'LIMGSHome04'}
FIELDS = 'LIMGSFields'
PORCH = {1: 'LIMGSPorch01', 2: 'LIMGSPorch02', 3: 'LIMGSPorch03'}
SALOON = 'LIMGSSaloon'
STORE = 'LIMGSStore'
SPRING = 'LIMGSSpring'
SCHOOLYARD = 'LIMGSSchoolyard'
GARDEN = 'LIMGSGarden'
ROAD = 'LIMGSWatchRoute'
WATCH_BED = 'LIMGSWatchBed'
GONE = 'LIMGSHolding'          # the holding cell: a resident who left town


@dataclass(frozen=True)
class Resident:
    ref: str
    name: str
    home: int                  # 1 to 4, 0 = the gas station back room (the watch), -1 = none (traveller)
    defender: bool
    child: bool = False
    persistent: bool = True
    gang_side: bool = False    # stays if the Powder Gangers run the town


CAST = (
    Resident('LIMGSAmosRef', 'Amos Pruitt', 1, True),
    Resident('LIMGSLenaRef', 'Lena Pruitt', 1, False),
    Resident('LIMGSCalRef', 'Cal Pruitt', 1, False),
    Resident('LIMGSJosephRef', 'Joseph Okafor', 2, False),
    Resident('LIMGSAdaRef', 'Ada Okafor', 2, False),
    Resident('LIMGSRuthRef', 'Ruth Okafor', 2, False, child=True),
    Resident('LIMGSHarlanRef', 'Widow Harlan', 3, False),
    Resident('LIMGSWesRef', 'Wes Harlan', 3, True),
    Resident('LIMGSDutchyRef', 'Dutchy', 4, False, gang_side=True),
    Resident('LIMGSMarisolRef', 'Marisol', 4, True),
    Resident('LIMGSAbeRef', 'Old Abe', 4, False),
    Resident('LIMGSHectorRef', 'Hector Vane', 0, True),
    Resident('LIMGSProspectorRef', 'a prospector', -1, False),
    Resident('LIMGSDrifterRef', 'a drifter', -1, False),
)
# the fourth hand who joins when Ghost Town Gunfight is won for the town
EXTRA_HAND = Resident('LIMGSTeaRef', 'Tea Whitlock', 4, False)
BY_REF = {r.ref: r for r in CAST + (EXTRA_HAND,)}
FIELD_GROUP = ('LIMGSAmosRef', 'LIMGSLenaRef', 'LIMGSCalRef', 'LIMGSDutchyRef', 'LIMGSMarisolRef',
               'LIMGSAbeRef', 'LIMGSTeaRef')
GROUP_LEADER = 'LIMGSAmosRef'


def _farm(r, h):
    if 5 <= h < 7:
        return PORCH[1]                               # they gather at the Pruitt porch
    if 7 <= h < 12 or 14 <= h < 18:
        return FIELDS
    if 12 <= h < 14:
        return HOME[r.home] if r.home in (1, 2, 3) else SALOON   # hands eat at the saloon
    if 18 <= h < 22:
        return PORCH[1] if r.home == 1 else SALOON
    return HOME[r.home]


def _okafor(r, h):
    if r.child:
        if 7 <= h < 12 or 14 <= h < 18:
            return SCHOOLYARD
        if 18 <= h < 20:
            return PORCH[2]
        return HOME[2]
    if 22 <= h or h < 6:
        return HOME[2]
    if 18 <= h < 22:
        return PORCH[2]
    if 12 <= h < 14:
        return HOME[2]
    if r.ref == 'LIMGSJosephRef':
        return SPRING if h < 12 else STORE
    return PORCH[2] if h < 12 else STORE


def _harlan(r, h):
    if 22 <= h or h < 6:
        return HOME[3]
    if 18 <= h < 22:
        return PORCH[3] if r.ref == 'LIMGSHarlanRef' else SALOON
    if 12 <= h < 14:
        return HOME[3]
    return GARDEN if r.ref == 'LIMGSHarlanRef' else SPRING   # Wes hauls water from the spring


def _watch(r, h):
    if 21 <= h or h < 5:
        return ROAD
    return WATCH_BED


def _traveller(r, h):
    if 18 <= h or h < 7:
        return SALOON
    return GONE                                      # on the road by day (not in town)


def place(r, h):
    """Where resident r is at hour h (0 to 23) on an ordinary day."""
    if r.home == -1:
        return _traveller(r, h)
    if r.home == 0:
        return _watch(r, h)
    if r.ref in FIELD_GROUP:
        return _farm(r, h)
    if r.home == 2:
        return _okafor(r, h)
    return _harlan(r, h)


# ------------------------------------------------------------------------------------ the town state
GS_GUNFIGHT_WON = 'won'        # VMS16 done for the town
GS_GANGERS = 'gangers'         # Run Goodsprings Run done for the Powder Gangers (VMS16b)
GS_NONE = 'none'

FAME_HIGH = 25                 # reputation points, vanilla Goodsprings fame/infamy scale
INFAMY_HIGH = 25


@dataclass
class World:
    """What the town quest reads from the game once an hour."""
    hour: int = 8
    gunfight: str = GS_NONE
    fame: int = 0
    infamy: int = 0
    hostile_hours: int = 99    # game hours since the last hostile act in town (99 = none recently)
    raining: bool = False
    company_tier: int = 0      # 0 = the company add-on is not installed or not founded
    gangers_since: int = 0     # game hours since VMS16b went the gangers' way


@dataclass
class TownState:
    alarm: bool = False
    present: dict = field(default_factory=dict)      # ref -> place
    doors_locked: bool = False
    children_inside: bool = False
    watch_shadows: bool = False
    greet_by_name: bool = False
    hireable: tuple = ()


ALARM_CLEARS = 1               # game hours without a hostile act


def town_state(w):
    s = TownState()
    s.alarm = w.hostile_hours < ALARM_CLEARS
    cast = list(CAST) + ([EXTRA_HAND] if w.gunfight == GS_GUNFIGHT_WON else [])
    families_gone = w.gunfight == GS_GANGERS and w.gangers_since >= 24
    for r in cast:
        if families_gone and not r.gang_side and r.home != -1:
            s.present[r.ref] = GONE
            continue
        p = place(r, w.hour)
        if s.alarm and not r.defender and r.home != -1:
            p = HOME[r.home] if r.home in HOME else WATCH_BED
        if w.raining and p in (FIELDS, GARDEN, SCHOOLYARD):
            p = HOME[r.home] if r.home in HOME else SALOON
        infamous = w.infamy >= INFAMY_HIGH and w.infamy > w.fame
        if infamous and r.child:
            p = HOME[r.home]
        s.present[r.ref] = p
    infamous = w.infamy >= INFAMY_HIGH and w.infamy > w.fame
    s.doors_locked = infamous and (w.hour >= 20 or w.hour < 6)
    s.children_inside = infamous
    s.watch_shadows = infamous
    s.greet_by_name = w.gunfight == GS_GUNFIGHT_WON or (w.fame >= FAME_HIGH and w.fame > w.infamy)
    if w.company_tier >= 2 and not families_gone:
        s.hireable = ('LIMGSWesRef', 'LIMGSMarisolRef')
    return s


def people_in_town(s):
    return sum(1 for p in s.present.values() if p != GONE)

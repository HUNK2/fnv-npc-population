"""The company model: the spec for every number the in-game company shows (M1 plan task 1.1, widened
in M2 task 2.1: 4 towns, site goods, 3 roads and up to 3 wagons, a warehouse per town).

Rules from docs/design.md. Everything the game must reproduce is kept simple enough to write in an
xNVSE script: whole caps rounded half up at the moment they are booked, stocks as doubles, seeded
rolls with the same integer formula, one round trip Goodsprings -> Primm -> Goodsprings a day.

Day d's tick (06:00) runs, in order: settle memos (answered or due), the bookkeeper's plan when
the player set it, pay arrears from cash, apply the queued orders (the trip: out leg, back leg,
the back leg with a possible event), workshops, accrue running costs, overnight restock, bills on
every 7th day, the debt ladder, tier check, then the post: tomorrow's forecast, new memos, letters
(plan task 1.6; texts in tools/post_model.py).
"""
from dataclasses import dataclass, field

GOODS = ('water', 'powder', 'ammo', 'dirty', 'herbs', 'materials')         # the M1 goods (price board order)
# M2: smoked meat has markets; brahmin, stone, sand and scrap are site goods (no market: the company's
# own sites make them for its own workshops). Game cells are town * 12 + good, in this order.
ALL_GOODS = GOODS + ('meat', 'brahmin', 'stone', 'sand', 'scrap')
SITE_GOODS = ('brahmin', 'stone', 'sand', 'scrap')
ANCHOR = {'water': 200, 'powder': 100, 'ammo': 200, 'dirty': 100, 'herbs': 60, 'materials': 150,
          'meat': 100, 'brahmin': 120, 'stone': 50, 'sand': 20, 'scrap': 30}
TOWNS = ('GS', 'PR', 'SL', 'MO')
TOWN_NAME = {'GS': 'Goodsprings', 'PR': 'Primm', 'SL': 'Sloan', 'MO': 'Mojave Outpost'}
# Starter trade (design: Goods and production chains): daily use, normal stock. A good missing from a
# town has no market there (design: a dash).
STARTER = {
    'GS': {'water': (4, 34), 'powder': (2, 18), 'ammo': (4, 4), 'dirty': (1, 30), 'herbs': (1, 15),
           'materials': (1, 0), 'meat': (4, 4)},
    'PR': {'water': (10, 14), 'powder': (4, 4), 'ammo': (2, 20), 'dirty': (2, 2), 'herbs': (1, 1),
           'materials': (1, 10), 'meat': (6, 12)},
    'SL': {'water': (6, 6), 'powder': (3, 3), 'ammo': (2, 2), 'dirty': (2, 2), 'materials': (2, 0),
           'meat': (4, 2)},
    'MO': {'water': (8, 12), 'powder': (2, 6), 'ammo': (4, 4), 'meat': (6, 6)},
}
PRIMM_AMMO_USE_NO_SHERIFF = 3
ROUTE = ('GS', 'PR')
# M2 roads (my call: three, all half a day each way, one round trip a day); wagon n runs road n.
ROADS = {1: ('GS', 'PR'), 2: ('GS', 'SL'), 3: ('PR', 'MO')}
ROAD_DANGER = {1: 60, 2: 30, 3: 60}
ROAD_TIER = {1: 1, 2: 2, 3: 3}         # the tier from which the road's wagon can be bought
TRUST_START = {'GS': 35, 'PR': 20, 'SL': 20, 'MO': 20}
SITE_LOAD = 4                          # a leg carries at most 4 crates of site goods (the rest is trade)
CRATES_PER_LEG = 8
MIN_MARGIN = 20
SHORTAGE_REFILL, GLUT_DRAIN = 0.25, 0.12

LOAN, OWN_MONEY = 3000, 500
WAGON, BRAHMIN_PAIR, HIRING_FEES, LICENCE = 400, 300, 150, 150
INTEREST, MIN_PRINCIPAL = 0.04, 300
WAGES = {'driver': 10, 'guard': 12}
FEED = 3 * 2
RENT_WEEK = 70
WEAR_PER_DAY = 7                 # 1% of the wagon and brahmin a day, not cash
LATE_FEE = 0.10

DANGER, COVER = 60, 45           # Powder Gangers on the Primm road; a driver and a guard
EVENT_EVERY = 3                  # a Peddler meets at most one event every 3 days
EVENT_CHANCE, EVENT_CHANCE_EARLY = 50, 25

MEMO_CAP = 3                     # at most 3 memos wait at once (design: Memos)
PREPAY = 300                     # the prepay memo offers this much off the loan
PREPAY_RUNWAY = 14               # ... when the cash left after it still covers 14 days
GUN_COST, GUN_COVER = 25, 30     # a hired gun for one trip: 25 caps, cover 45 -> 75
ROB_SHARE = 0.3                  # a robbery takes 30% of the strongbox, a wreck all of it (capped)
AWAY_DAYS = 3                    # the while-you-were-away letter after 3 days without a terminal visit
POST_KEEP = 3                    # the Post screen keeps the last 3 letters
LETTER_ORDER = ('closed', 'notice', 'forecast', 'away', 'road', 'loss', 'tier')    # which letter waits first
# Memo answers in order; the default is the cautious one (design: Memos).
MEMO_ANSWERS = {'road': ('send as planned', 'hire a gun for 25', 'keep the wagon home'),
                'prepay': ('pay 300 off the loan', 'keep the cash'),
                'contract': ('accept at %d', 'counter at %d', 'decline')}
MEMO_DEFAULT = {'road': 2, 'prepay': 1, 'contract': 2}
SEND, GUN, HOLD = 0, 1, 2        # road memo answers

# The debt ladder (plan task 1.7, design: Losing and coming back).
STRIKE_DAYS, STRIKES_TAKEOVER = 56, 3
GRACE_DAYS, FINAL_DAYS, SEIZE_DAYS, TAKEOVER_DAYS = 3, 5, 7, 7
PROBATION_DAYS = 14
FINAL_CURE = 0.4                 # at the final notice, cure down to 40% of the arrears, or lose the wagon
SEIZE_SHARE, SELL_SHARE = 0.6, 0.6   # the creditor and a buyer both pay 60% of the wagon's value
RESCUE_WEEKS, RESCUE_EVERY = 2, 28   # owner rescue: up to 2 weeks of bills, once a season
FORECAST_RUNWAY = 5              # the forecast warning when runway is under 5 days
SERVED = ('grace', 'final', 'seized', 'takeover')    # a served notice whose clock runs

# Contracts, standing orders and staff (plan task 1.8, its "My calls").
CONTRACT_GOOD, CONTRACT_CRATES, CONTRACT_EVERY, CONTRACT_DAYS = 'water', 4, 3, 28
CONTRACT_PREMIUM, COUNTER_PREMIUM, COUNTER_WALK = 0.09, 0.07, 50
CONTRACT_MISS = 0.10
OFFER_WEEKDAY, OFFER_EVERY = 3, 7          # an offer on the third day of a week, at most one a week
SLOTS = 3                                  # standing order slots at tier 1
SO_KINDS = ('keep', 'sell_above', 'max_pay')
ROLE_WAGE = {'driver': 10, 'guard': 12}
DRIVER_COVER, GUARD_COVER = 15, 30
SKIM_HONESTY, SKIM_SHARE = 30, 0.02
REF_CHECK = 10
FOUNDERS = (('Ruth Coyle', 'driver'), ('Dutch Haley', 'guard'))
STAFF_MAX = 10                   # the Staff screen's 14 rows: cover, 10 people, HIRE, BACK (and one spare)
NAMES = ('Abe Tolliver', 'Bess Marlowe', 'Cal Dunning', 'Dora Pike', 'Eli Varga', 'Fay Hollins',
         'Gus Merritt', 'Hank Ostrow', 'Ida Kesey', 'Jody Ramos', 'Kit Albrecht', 'Lou Danner',
         'Mae Corliss', 'Ned Ashby', 'Opal Reyes', 'Pete Lusk', 'Quinn Bodie', 'Rosa Tamez',
         'Sam Whitlow', 'Tess Garber', 'Ulla Brandt', 'Vic Moreau', 'Wes Calder', 'Zeke Pruitt',
         'Ada Fenn', 'Bo Hatch', 'Cora Lyle', 'Dale Mott', 'Edie Paxton', 'Floyd Skerritt',
         'Gail Norris', 'Hal Prentiss', 'Iris Okafor', 'Jed Burris', 'Kay Lindqvist', 'Lyle Sorensen',
         'Mona Tuck', 'Noel Harker', 'Ora Bastian', 'Russ Pell')
RUMOURS = ('Lost a cousin to the Powder Gangers.', 'Drove for the Crimson Caravan until a pay dispute.',
           'Says the NCR still owes back pay.', 'Sober three years, folks say.',
           'Owes money in Primm, they say.', 'Knows the Primm road by night.', 'Good shot, bad temper.',
           'Never missed a day at the Goodsprings well.', 'Came up from Mojave Outpost last month.',
           'Folks say they once rode with the Great Khans.', 'Has a sick mother in Sloan.',
           'Talks too much at the saloon.')

TIER2_WORTH, TIER2_TRUST = 1500, 50
TIER3_WORTH, TIER3_TRUST, TIER3_TOWNS = 18000, 50, 2   # 8000 in the design; M2 wagons and sites count in worth (balance_run: good player day 29-33)

# --- M2: town levels (design: Towns grow like Anno settlements; plan 2.2 my calls) -------------------
LEVELS = ('Camp', 'Hamlet', 'Village', 'Town')
START_LEVEL = {'GS': 1, 'PR': 2, 'SL': 0, 'MO': 0}
LEVEL_USE = 0.25                 # each level above the start adds a quarter to every good's daily use
BASICS = ('water', 'meat', 'powder')
BASIC_DAYS = 2                   # a basic is met when its stock covers 2 days of use
LEVEL_MET_DAYS, LEVEL_DROP_DAYS = 7, 14
LEVEL_MATERIALS = {1: 40, 2: 90, 3: 160}   # crates of building materials delivered to reach a level

# --- M2: staff numbers, traits, loyalty, managers ---------------------------------------------------
ROLE_WAGE.update({'trader': 20, 'clerk': 15})
# trait: (cover as a guard, wage, loyalty a week, skill bonus); one at hire, Steady is earned
TRAITS = {'Haggler': (0, 2, 0, 10), 'Cautious': (5, 0, -2, 0), 'Reckless': (10, 0, 0, -10),
          'Drinker': (0, -2, -3, 0), 'NCR veteran': (10, 3, 0, 0), 'Family man': (0, 2, 5, 0),
          'Ambitious': (0, 0, -3, 10), 'Steady': (5, 0, 2, 0)}
HIRE_TRAITS = ('Haggler', 'Cautious', 'Reckless', 'Drinker', 'NCR veteran', 'Family man', 'Ambitious')
LOYALTY_START = 55
OFFER_LOYALTY = {'low': -10, 'fair': 0, 'generous': 10}
OFFER_WAGE = {'low': -2, 'fair': 0, 'generous': 3}
LOYALTY_PAID, LOYALTY_MISSED = 5, -10
LOYALTY_RAISE_ASK, LOYALTY_LEAVE = 35, 20
RAISE, RAISE_LOYALTY, REFUSE_LOYALTY = 1.25, 20, -10
MEMO_ANSWERS['raise'] = ('give a raise of 25%', 'refuse')
MEMO_DEFAULT['raise'] = 1
# the lived-in Goodsprings residents who can be hired from tier 2 (tools/town_model.py hireable)
RESIDENT_HIRES = (('Wes Harlan', 'driver', 55, 80, 70, 'Steady'), ('Marisol', 'guard', 65, 75, 75, 'Cautious'))
MANAGERS = {'bookkeeper': 2, 'route': 3}          # manager: the tier that opens it
MANAGER_WAGE = 40
POLICIES = {'bookkeeper': ('Strict', 'Normal', 'Lenient'), 'route': ('Safe', 'Balanced', 'Fast')}
CATCH = {'Strict': 100, 'Normal': 50, 'Lenient': 0}
STRICT_CLERK_LOYALTY = -5
BALANCED_GUN_BELOW = 60          # the Balanced route manager hires a gun when the clean chance is under 60
CONTRACTS_OPEN = {1: 1, 2: 2, 3: 3}
BUY_FROM_PLAYER = {'water': 10, 'powder': 10}     # tier 2 perk: goods and bottles (or powders) a crate
BUY_SHARE, BUY_DAY_MAX = 0.8, 10
DELIVERY_TRUST, DEED_TRUST = 1, 10       # a leg that sells into a town; Ghost Town Gunfight (GS)
BUILD_ORDER = ('purifier', 'apothecary', 'well', 'forager')     # the Build screen's rows
WORKSHOP_COST, SITE_COST, HAND_WAGE = 300, 200, 14
WORKSHOPS = {                    # name: (inputs per batch, outputs per batch, output crates a day)
    'purifier': ({'dirty': 5}, {'water': 4}, 4),
    'apothecary': ({'herbs': 1}, {'powder': 1}, 4),
    'smokehouse': ({'brahmin': 1}, {'meat': 4}, 4),
    'stoneyard': ({'stone': 2, 'sand': 1}, {'materials': 2}, 4),
}
SITES = {'well': 'dirty', 'forager': 'herbs',   # raw sites, 4 crates a day each
         'corral': 'brahmin', 'sandpit': 'sand', 'scrapyard': 'scrap', 'quarry': 'stone'}
SITE_RATE = 4
# M2: where each building stands (its warehouse), the tier it needs, and a deed it waits for
WHERE = {'purifier': 'GS', 'apothecary': 'GS', 'well': 'GS', 'forager': 'GS', 'corral': 'GS',
         'smokehouse': 'PR', 'sandpit': 'PR', 'scrapyard': 'PR', 'quarry': 'SL', 'stoneyard': 'SL'}
BUILD_TIER = {'purifier': 2, 'apothecary': 2, 'well': 2, 'forager': 2, 'corral': 2, 'sandpit': 2,
              'scrapyard': 2, 'smokehouse': 3, 'quarry': 3, 'stoneyard': 3}
BUILD_DEED = {'quarry': 'quarry_junction', 'stoneyard': 'quarry_junction'}


def half_up(x):
    """Whole caps: round half up (the game uses floor(x + 0.5))."""
    import math
    return int(math.floor(x + 0.5))


def roll(seed, day, key):
    """The seeded roll, 0..99. The game computes the same value as ((day % 100) * 19 + (seed % 100) * 29
    + key * 31) % 100: its script numbers lose whole units above 2^24, and this sum is about 1.3e8."""
    return (day * 7919 + seed * 104729 + key * 31) % 100


def spread(trust):
    """10% at no trust, 2% at full trust."""
    return 0.10 - 0.08 * trust / 100


def restock(stock, normal):
    return stock + (normal - stock) * (SHORTAGE_REFILL if stock < normal else GLUT_DRAIN)


def duty(sales):
    """NCR duty on a week's sales: 2%, 3.5% on the part above 5,000, 5% above 20,000."""
    d = 0.02 * min(sales, 5000) + 0.035 * max(0, min(sales, 20000) - 5000) + 0.05 * max(0, sales - 20000)
    return half_up(d)


@dataclass
class Order:
    kind: str           # 'carry'
    town: str           # where the crate is loaded
    good: str
    qty: int = 1
    wagon: int = 1      # M2: the wagon (= its road) that carries it


@dataclass
class Wagon:
    road: int           # 2 or 3 (wagon 1 is the M1 wagon: Company.wagon_ok)
    ok: bool = True


@dataclass
class Memo:
    kind: str           # 'road', 'prepay', 'contract' or (M2) 'raise'
    day: int            # the day it was posted
    due: int            # the tick that settles it with the default if nobody answers
    pick: int = None    # the answer chosen at a terminal or in a field letter
    price: int = 0      # a contract offer's price a crate
    town: str = 'PR'    # M2: a contract offer's buyer, good and road; a raise memo's person (name)
    good: str = 'water'
    road: int = 1
    who: str = ''

    @property
    def answers(self):
        if self.kind == 'contract':
            a = MEMO_ANSWERS['contract']
            return (a[0] % self.price, a[1] % half_up(self.price * (1 + COUNTER_PREMIUM)), a[2])
        return MEMO_ANSWERS[self.kind]


@dataclass
class Contract:
    good: str
    crates: int
    every: int
    price: int
    start: int          # the day it was signed; deliveries until start + 28
    next_due: int
    done: int = 0
    missed: int = 0
    town: str = 'PR'    # M2: the buyer, the road that serves it and the town the crates load at
    road: int = 1
    origin: str = 'GS'


@dataclass
class StandingOrder:
    kind: str           # 'keep' (town, good, crates), 'sell_above' (good, price), 'max_pay' (good, price)
    town: str
    good: str
    value: int


@dataclass
class Person:
    name: str
    role: str           # 'driver', 'guard' (M1), 'trader' or 'clerk' (M2)
    skill: int
    honesty: int        # hidden until a reference check
    wage: int
    rumour: str = ''
    checked: bool = False
    nerve: int = 50     # M2
    loyalty: int = LOYALTY_START
    trait: str = ''
    reasons: list = field(default_factory=list)    # (text, change), the last 4 (the person's page)
    resident: bool = False                         # a lived-in towns resident (Wes, Marisol)


@dataclass
class Letter:
    day: int
    kind: str           # 'notice', 'closed', 'forecast', 'away', 'loss' or 'road' (in priority order)
    values: tuple       # the numbers the text needs (tools/post_model.py letter_text)


@dataclass
class DayReport:
    day: int
    sales: int = 0
    costs: int = 0
    loads: dict = field(default_factory=dict)       # (origin, good) -> crates delivered
    event: str = ''
    event_loss: int = 0
    bills: dict = None
    bills_paid: bool = None
    cash: int = 0
    notes: list = field(default_factory=list)
    wagon: bool = True          # the wagon ran today
    road_mode: int = 0          # SEND, GUN or HOLD (the wagon stayed home)
    prepaid: int = 0            # paid off the loan by a prepay memo
    crew: bool = True           # a driver was on the books
    contract: str = ''          # 'delivered' or 'missed' (+ ' completed' on the last one), or 'walked'
    signed: int = 0             # a contract signed today: its price a crate
    skim: int = 0               # skimmed by dishonest staff
    tier_up: bool = False       # the company reached a new tier today
    sold_to: dict = field(default_factory=dict)     # M2: (town, good) -> crates sold there

    @property
    def margin(self):
        return self.sales - self.costs


class Company:
    def __init__(self, seed, sheriff=False):
        self.seed, self.sheriff = seed, sheriff
        self.auto = False            # accept the bookkeeper's plan at every tick (game: CCCore.iAuto)
        self.use = {t: {g: float(u) for g, (u, n) in goods.items()} for t, goods in STARTER.items()}
        self.normal = {t: {g: float(n) for g, (u, n) in goods.items()} for t, goods in STARTER.items()}
        if not sheriff:
            self.use['PR']['ammo'] = float(PRIMM_AMMO_USE_NO_SHERIFF)
        self.stock = {t: dict(v) for t, v in self.normal.items()}
        self.trust = dict(TRUST_START)
        self.day, self.tier, self.founded, self.ended = 0, 0, False, False
        self.cash = self.owner_funds = self.owner_paid_in = self.loan = 0
        self.assets = 0
        self.queue_list, self.history = [], []
        self.week_sales = self.accrued_wages = self.accrued_feed = 0
        self.arrears, self.stage, self.served_day, self.stage_day = 0, 'ok', None, 0
        self.arrears_at_final = 0
        self.strikes = []
        self.shield = False          # the busy shield: the player is in a DLC's own lands (game: CCCore.iShield)
        self.from_probation = False  # the deferred miss happened on probation: serving it skips Grace
        self.end_reason = ''         # 'receivership', 'takeover' or 'walked'
        self.pocket = 0              # the player's own caps (the game reads them); owner rescue takes from here
        self.last_rescue = -99
        self.buildings = 0           # value of workshops and sites in self.assets (the rest is the wagon)
        self.forecast_bill_day = 0   # the bill day the last forecast letter warned about
        self.last_event_day = -99
        self.wagon_ok = True
        self.ghost_town_done = False
        self.ghost_town_paid = False     # its +10 Goodsprings trust was given (game: CCCore.iGhostPaid)
        self.wh = {t: {g: 0 for g in ALL_GOODS} for t in TOWNS}     # a warehouse per town (M2)
        self.warehouse = self.wh['GS']                                # the M1 name for Goodsprings'
        self.wagons = []                 # M2: wagons 2 and 3 (Wagon); wagon 1 is wagon_ok
        self.deeds = set()               # M2: 'quarry_junction' (the stone trade), 'sheriff' (Primm)
        self.workshops, self.sites, self.hands = [], [], 0
        self.memos, self.road_mode = [], SEND
        self.last_visit, self.away_posted = 0, False
        self.letter, self.letter_shown_day, self.post = None, -1, []
        self.contracts, self.last_offer = [], -99
        self.standing = [None] * SLOTS
        self.staff, self.candidates = [], []
        self.level = dict(START_LEVEL)                       # M2: town levels
        self.base_use = {t: dict(v) for t, v in self.use.items()}
        self.met_days = {t: 0 for t in TOWNS}
        self.unmet_days = {t: 0 for t in TOWNS}
        self.materials_in = {t: 0 for t in TOWNS}            # crates delivered since the last level
        self.managers = {}                                   # 'bookkeeper' / 'route' -> policy
        self.gangers_town = False                            # Goodsprings run by the Powder Gangers
        self.bought_today, self.bought_day = 0, 0

    # --- founding -------------------------------------------------------------------------------
    def found(self):
        """Sign Alice's letter of credit: 3,000 loan, 500 own money, then the setup (design: Money)."""
        self.founded, self.tier = True, 1
        self.loan, self.cash, self.owner_funds, self.owner_paid_in = LOAN, LOAN, OWN_MONEY, OWN_MONEY
        assets = WAGON + BRAHMIN_PAIR
        from_owner = min(self.owner_funds, assets)
        self.owner_funds -= from_owner
        self.cash -= (assets - from_owner) + HIRING_FEES + LICENCE
        self.assets = assets
        self.staff = [Person(n, role, 50, 60, ROLE_WAGE[role]) for n, role in FOUNDERS]
        self.auto = True             # the daily plan starts on: the company works while you are away

    # --- prices ---------------------------------------------------------------------------------
    def has_market(self, town, good):
        return good in self.stock[town]

    def mult(self, town, good, stock=None):
        s = self.stock[town][good] if stock is None else stock
        r = s / (3 * self.use[town][good])
        return 0.5 + 1 / (1 + r)

    def mid_exact(self, town, good):
        return ANCHOR[good] * self.mult(town, good)

    def mid(self, town, good):
        return half_up(self.mid_exact(town, good))

    def price(self, town, good, side, stock=None):
        """'buy': what the company pays the town for a crate; 'sell': what the town pays the company."""
        m = ANCHOR[good] * self.mult(town, good, stock)
        s = max(0.02, spread(self.trust[town]) - self.trader_cut())
        return half_up(m * (1 + s) if side == 'buy' else m * (1 - s))

    def trader_cut(self):
        """M2: the best trader's Skill takes 1 point off the spread for each 10 over 50."""
        best = max([self.eff_skill(p) for p in self.staff if p.role == 'trader'] or [50])
        return max(0, best - 50) // 10 / 100

    @staticmethod
    def eff_skill(p):
        return p.skill + (TRAITS[p.trait][3] if p.trait else 0)

    # --- the bookkeeper's plan --------------------------------------------------------------------
    def contract_due(self, day, road=None):
        return any(c.next_due == day and (road is None or c.road == road) for c in self.contracts)

    def plan(self, trip_day=None):
        """The bookkeeper's plan for the trip of `trip_day` (default: tomorrow's). For each leg: first the
        standing orders that keep the destination stocked (a crate that does not lose money), then
        greedy: the best crate by margin while it pays MIN_MARGIN. Up to 8 crates a leg, less the
        contract's crates on a delivery day. Standing orders also bar a sale below a price and a
        purchase above one. Own warehouse crates cost nothing to load."""
        trip_day = self.day + 1 if trip_day is None else trip_day
        orders = []
        cash = self.cash
        floor_ = {o.good: o.value for o in self.standing if o and o.kind == 'sell_above'}
        ceil_ = {o.good: o.value for o in self.standing if o and o.kind == 'max_pay'}
        whs = {t: dict(v) for t, v in self.wh.items()}
        stocks = {t: dict(v) for t, v in self.stock.items()}
        for w, road in self.running_roads():
          for origin, dest in (ROADS[road], ROADS[road][::-1]):
            so, sd = stocks[origin], stocks[dest]
            wh = whs[origin]
            cap = CRATES_PER_LEG - self.contract_crates(trip_day, road, origin)
            n = 0
            # site goods first: toward the workshop that uses them, through Goodsprings (the hub)
            for g in SITE_GOODS:
                while n < cap and n < SITE_LOAD and wh[g] > 0 and self.site_goes(g, origin, dest):
                    wh[g] -= 1
                    whs[dest][g] += 1
                    n += 1
                    orders.append(Order('carry', origin, g, 1, w))

            def offer(g):
                if not self.has_market(dest, g):
                    return None
                sale = self.price(dest, g, 'sell', sd[g])
                own = wh[g] > 0
                if not own and not self.has_market(origin, g):
                    return None
                cost = 0 if own else self.price(origin, g, 'buy', so[g])
                if not own and (cost > cash or cost > ceil_.get(g, 10 ** 9)):
                    return None
                if sale < floor_.get(g, 0):
                    return None
                return sale - cost, own, cost

            def take(g, own, cost):
                nonlocal cash, n
                if own:
                    wh[g] -= 1
                else:
                    so[g] -= 1
                    cash -= cost
                sd[g] += 1
                n += 1
                orders.append(Order('carry', origin, g, 1, w))  # one order per crate, in pick order

            for o in self.standing:
                if o and o.kind == 'keep' and o.town == dest:
                    while n < cap and sd[o.good] < o.value:
                        got = offer(o.good)
                        if got is None or got[0] < 0:
                            break
                        take(o.good, got[1], got[2])
            while n < cap:
                best = None
                for g in ALL_GOODS:
                    if g in SITE_GOODS:
                        continue
                    got = offer(g)
                    if got is not None and (best is None or got[0] > best[0]):
                        best = (got[0], g, got[1], got[2])
                if best is None or best[0] < MIN_MARGIN:
                    break
                take(best[1], best[2], best[3])
        return orders

    def running_roads(self):
        """(wagon, road) for every wagon that runs: its wagon is whole and a driver is free for it."""
        drivers = sum(1 for p in self.staff if p.role == 'driver')
        slots = 1 + sum(1 for p in self.staff if p.role == 'clerk')     # each clerk runs one more wagon
        out = []
        if self.wagon_ok and drivers > 0:
            out.append((1, 1))
            drivers -= 1
        for i, wg in enumerate(self.wagons):
            if wg.ok and drivers > 0 and len(out) < slots:
                out.append((i + 2, wg.road))
                drivers -= 1
        return out

    def site_goes(self, g, origin, dest):
        """Does a crate of site good g travel origin -> dest? Toward the town of the workshop that uses
        it; through Goodsprings when no road joins the two."""
        users = [WHERE[w] for w in self.workshops if g in WORKSHOPS[w][0]]
        if not users or origin in users:
            return False
        if dest in users:
            return True
        return dest == 'GS' and not any(set(ROADS[r]) == {origin, u} for r in ROADS for u in users)

    def contract_crates(self, day, road, origin):
        """Crates the contracts due on `day` load on this road's leg out of `origin`."""
        return sum(c.crates for c in self.contracts
                   if c.next_due == day and c.road == road and c.origin == origin)

    def queue(self, order):
        self.queue_list.append(order)

    # --- the day ----------------------------------------------------------------------------------
    def tick(self):
        self.day += 1
        d = self.day
        r = DayReport(d)
        if self.ended:
            return r
        self._settle_memos(r)
        if self.auto:
            self.queue_list = self.plan(d)
        self._pay_arrears(r)
        r.wagon, r.road_mode, r.crew = self.wagon_ok, self.road_mode, self.has_driver()
        running = dict((road, w) for w, road in self.running_roads())
        ev_road = self.event_road(d)
        for road in sorted(ROADS):
            w = running.get(road)
            mode = self.road_mode if road == ev_road else SEND
            if w is None or mode == HOLD:
                if w is not None and road == ev_road and self.event_fires(d):
                    self.last_event_day = d         # the bandits waited for a wagon that stayed home
                self._contract(r, False, road)
                continue
            if mode == GUN:
                pay = min(GUN_COST, self.cash)
                self.cash -= pay
                r.costs += pay
            sales0 = r.sales                    # the road's takings: its contract and its out leg
            loaded = self._contract(r, True, road)
            out, back = ROADS[road], ROADS[road][::-1]
            for origin, dest in (out, back):
                if origin == back[0] and road == ev_road:
                    self._event(r, r.sales - sales0, road)
                self._leg(r, origin, dest, [o for o in self.queue_list if o.town == origin and o.wagon == w],
                          CRATES_PER_LEG - (loaded.get(origin, 0)))
        self._skim(r)
        self.queue_list = []
        self.road_mode = SEND
        self.run_workshops()
        self.accrued_wages += self.daily_wages()
        self.accrued_feed += FEED
        self.assets = max(0, self.assets - WEAR_PER_DAY)
        for t in self.stock:
            for g in self.stock[t]:
                self.stock[t][g] = restock(self.stock[t][g], self.normal[t][g])
        if d % 7 == 0:
            self._bills(r)
            self._week_people(r)
        if d % 7 == 1:
            self._new_candidates()
        self._levels(r)
        self._ladder(r)
        if self.ghost_town_done and not self.ghost_town_paid:
            self.ghost_town_paid = True
            self.trust['GS'] = min(100, self.trust['GS'] + DEED_TRUST)
        self._tier_check(r)
        r.cash = self.cash
        self.history.append(r)
        road = self._post_memos(r)
        self._post_letters(r, road)
        return r

    def _leg(self, r, origin, dest, orders, cap=CRATES_PER_LEG):
        crates = []
        wh = self.wh[origin]
        for o in orders:
            for _ in range(o.qty):
                if len(crates) >= cap:
                    break
                if o.good in SITE_GOODS:          # carried to a workshop's warehouse, never sold
                    if wh[o.good] > 0:
                        wh[o.good] -= 1
                        self.wh[dest][o.good] += 1
                        crates.append((o.good, None))
                    continue
                if wh[o.good] > 0:
                    wh[o.good] -= 1
                    crates.append((o.good, 0))
                    continue
                cost = self.price(origin, o.good, 'buy')
                if cost > self.cash:
                    continue
                self.cash -= cost
                r.costs += cost
                self.stock[origin][o.good] -= 1
                crates.append((o.good, cost))
        sold = False
        for g, cost in crates:
            if cost is None:
                continue
            sold = True
            sale = self.price(dest, g, 'sell')
            self.cash += sale
            r.sales += sale
            self.week_sales += sale
            self.stock[dest][g] += 1
            r.loads[(origin, g)] = r.loads.get((origin, g), 0) + 1
            r.sold_to[(dest, g)] = r.sold_to.get((dest, g), 0) + 1
            if g == 'materials':
                self.materials_in[dest] += 1
        if sold:
            self.trust[dest] = min(100, self.trust[dest] + DELIVERY_TRUST)

    def event_fires(self, d):
        """Does the director place a bandit event on day d's return leg? Known a day ahead (the forecast):
        at most one every 3 days, none on bill day or the day before, none on the first trip (day 1 has
        no forecast before it)."""
        if d < 2 or d - self.last_event_day < EVENT_EVERY or d % 7 in (0, 6):
            return False
        chance = EVENT_CHANCE_EARLY if d <= 10 else EVENT_CHANCE
        return roll(self.seed, d, 1) < chance

    def forecast(self):
        """Tomorrow's likeliest trouble: 'bandits' (an event meets the return leg), 'quiet' or 'no_wagon'."""
        if not self.wagon_ok or not self.has_driver():
            return 'no_wagon'
        return 'bandits' if self.event_fires(self.day + 1) else 'quiet'

    def event_road(self, d):
        """The road whose return leg the director's event meets on day d (one of the running roads)."""
        roads = sorted(road for _, road in self.running_roads()) or [1]
        return roads[roll(self.seed, d, 5) % len(roads)] if len(roads) > 1 else roads[0]

    def clean_chance(self, cover, danger=DANGER):
        """Percent chance the crew drives the bandits off: r^2 / (1 + r^2), r = cover / danger."""
        ratio = cover / danger
        return half_up(100 * ratio * ratio / (1 + ratio * ratio))

    def _event(self, r, takings=None, road=1):
        """Before the return leg: the director may send bandits at the wagon. They rob the strongbox, the
        cash from the day's Primm sales: 30% of it, or all of it in a wreck, never more than 3 days of
        running costs at tier 1. The loss is booked as a cost of the day."""
        d = self.day
        if not self.event_fires(d):
            return
        self.last_event_day = d
        cover = self.cover() + (GUN_COVER if r.road_mode == GUN else 0)
        if roll(self.seed, d, 2) < self.clean_chance(cover, ROAD_DANGER[road]):
            r.event = 'bandits_driven_off'
            if self.tier >= 2:                  # M2: a guard with no trait who held the road earns Steady
                g = next((p for p in self.staff if p.role == 'guard' and not p.trait), None)
                if g is not None:
                    g.trait = 'Steady'
                    r.notes.append('%s held the road: Steady' % g.name)
            return
        takings = r.sales if takings is None else takings
        if takings <= 0:
            r.event = 'bandits_empty'
            return
        wreck = roll(self.seed, d, 3) < 33
        loss = min(takings if wreck else half_up(ROB_SHARE * takings), 3 * self.daily_burn())
        if self.shield:                         # in a DLC's lands paper losses stay under a day's profit
            loss = min(loss, max(0, self.history[-1].margin if self.history else 0))
        self.cash -= loss
        r.costs += loss
        r.event = 'bandits_wreck' if wreck else 'bandits_took_cargo'
        r.event_loss = loss

    def run_workshops(self):
        for site in self.sites:
            self.wh[WHERE[site]][SITES[site]] += SITE_RATE
        for w in self.workshops:
            ins, outs, cap = WORKSHOPS[w]
            wh = self.wh[WHERE[w]]
            (good_out, per), = outs.items()
            made = 0
            while all(wh[g] >= n for g, n in ins.items()) and made + per <= cap:
                for g, n in ins.items():
                    wh[g] -= n
                wh[good_out] += per
                made += per

    def daily_wages(self):
        return (sum(p.wage for p in self.staff) + HAND_WAGE * self.hands
                + MANAGER_WAGE * len(self.managers))

    # --- staff (plan task 1.8) ---------------------------------------------------------------------
    def has_driver(self):
        return any(p.role == 'driver' for p in self.staff)

    def cover(self):
        """The crew's cover on the road: 15 for the driver, 30 a guard plus a fifth of skill over 50."""
        if not self.has_driver():
            return 0
        return DRIVER_COVER + sum(GUARD_COVER + (p.skill - 50) // 5 + (TRAITS[p.trait][0] if p.trait else 0)
                                  for p in self.staff if p.role == 'guard')

    def _skim(self, r):
        """Staff with honesty under 30 each take 2% of the day's sales (only a reference check shows it)."""
        n = sum(1 for p in self.staff if p.honesty < SKIM_HONESTY)
        if n and r.sales > 0:
            take = min(self.cash, n * half_up(SKIM_SHARE * r.sales))
            self.cash -= take
            r.costs += take
            r.skim = take

    def _new_candidates(self):
        """3 to 6 people asking for work, posted on day 1 of each week (seeded)."""
        d = self.day
        used = {p.name for p in self.staff}
        self.candidates = []
        for i in range(3 + roll(self.seed, d, 20) % 4):
            k = roll(self.seed, d, 21 + i) % len(NAMES)
            while NAMES[k] in used:
                k = (k + 1) % len(NAMES)
            used.add(NAMES[k])
            rr = roll(self.seed, d, 30 + i)
            if self.tier < 2:
                role = 'driver' if rr < 25 else 'guard'
            else:
                role = 'driver' if rr < 25 else 'guard' if rr < 70 else 'trader' if rr < 85 else 'clerk'
            skill = 30 + roll(self.seed, d, 40 + i) % 50
            honesty = 10 + roll(self.seed, d, 50 + i) % 85
            wage = ROLE_WAGE[role] + max(0, (skill - 50) // 10)
            nerve = 20 + roll(self.seed, d, 70 + i) % 70
            tr = roll(self.seed, d, 80 + i)
            trait = HIRE_TRAITS[tr % len(HIRE_TRAITS)] if self.tier >= 2 and tr < 70 else ''
            if trait:
                wage += TRAITS[trait][1]
            self.candidates.append(Person(NAMES[k], role, skill, honesty, wage,
                                          RUMOURS[roll(self.seed, d, 60 + i) % len(RUMOURS)],
                                          nerve=nerve, trait=trait))
        if self.tier >= 2 and not self.gangers_town:
            for name, role, skill, hon, nerve, trait in RESIDENT_HIRES:
                if name not in used:
                    self.candidates.append(Person(name, role, skill, hon, ROLE_WAGE[role] + TRAITS[trait][1],
                                                  'Lives in Goodsprings.', nerve=nerve, trait=trait,
                                                  resident=True))

    def can_hire(self, i):
        c = self.candidates[i]
        if len(self.staff) >= STAFF_MAX:
            return False
        drivers = sum(1 for p in self.staff if p.role == 'driver')
        return not (c.role == 'driver' and drivers >= 1 + len(self.wagons))     # a driver per wagon

    def hire(self, i, offer='fair'):
        """Hire candidate i with a Low, Fair or Generous offer (M2: wage and starting loyalty)."""
        if not 0 <= i < len(self.candidates) or not self.can_hire(i):
            return False
        p = self.candidates.pop(i)
        p.wage = max(1, p.wage + OFFER_WAGE[offer])
        p.loyalty = LOYALTY_START + OFFER_LOYALTY[offer]
        if offer != 'fair':
            p.reasons = [('%s offer' % offer, OFFER_LOYALTY[offer])]
        self.staff.append(p)
        return True

    def fire(self, i):
        if not 0 <= i < len(self.staff):
            return False
        self.staff.pop(i)
        return True

    def reference_check(self, i):
        """10 caps: the honesty band of a candidate."""
        c = self.candidates[i]
        if c.checked or self.cash < REF_CHECK:
            return False
        self.cash -= REF_CHECK
        c.checked = True
        return True

    @staticmethod
    def honesty_band(p):
        return 'low' if p.honesty < 35 else 'fair' if p.honesty < 70 else 'high'

    # --- M2: loyalty, managers ------------------------------------------------------------------------
    @staticmethod
    def _loyal(p, change, why):
        p.loyalty = max(0, min(100, p.loyalty + change))
        p.reasons = (p.reasons + [(why, change)])[-4:]

    def _week_people(self, r):
        """Bill day: loyalty for pay (and traits), the bookkeeper's check for skimmers, raise memos and
        people who leave."""
        catch = CATCH.get(self.managers.get('bookkeeper'), 0)
        for i, p in enumerate(list(self.staff)):
            self._loyal(p, LOYALTY_PAID if r.bills_paid else LOYALTY_MISSED,
                        'paid on time' if r.bills_paid else 'wages late')
            if p.trait and TRAITS[p.trait][2]:
                self._loyal(p, TRAITS[p.trait][2], p.trait.lower())
            if p.trait == 'Ambitious':
                p.skill = min(90, p.skill + 1)
            if p.role == 'clerk' and self.managers.get('bookkeeper') == 'Strict':
                self._loyal(p, STRICT_CLERK_LOYALTY, 'a strict bookkeeper')
            if p.honesty < SKIM_HONESTY and catch and roll(self.seed, self.day, 90 + i) < catch:
                self.staff.remove(p)
                r.notes.append('%s was caught skimming and let go' % p.name)
                continue
            if p.loyalty < LOYALTY_LEAVE:
                self.staff.remove(p)
                r.notes.append('%s left the company' % p.name)
            elif p.loyalty < LOYALTY_RAISE_ASK and not any(m.kind == 'raise' and m.who == p.name
                                                           for m in self.memos):
                self.post_memo(Memo('raise', self.day, self.day + 3, who=p.name))

    def can_hire_manager(self, kind):
        return self.tier >= MANAGERS[kind] and kind not in self.managers and not self.ended

    def hire_manager(self, kind, policy):
        if not self.can_hire_manager(kind) or policy not in POLICIES[kind]:
            return False
        self.managers[kind] = policy
        return True

    def set_policy(self, kind, policy):
        if kind in self.managers and policy in POLICIES[kind]:
            self.managers[kind] = policy

    def route_manager_pick(self):
        """The route manager answers a road memo when it is posted (None: no manager)."""
        pol = self.managers.get('route')
        if pol is None:
            return None
        if pol == 'Safe':
            return HOLD
        if pol == 'Fast':
            return SEND
        road = self.event_road(self.day + 1)
        return GUN if self.clean_chance(self.cover(), ROAD_DANGER[road]) < BALANCED_GUN_BELOW else SEND

    # --- M2: town levels ---------------------------------------------------------------------------------
    def basics_met(self, t):
        return all(self.stock[t][g] >= BASIC_DAYS * self.use[t][g] for g in BASICS if self.has_market(t, g))

    def _set_level(self, t, lv):
        self.level[t] = lv
        k = 1 + LEVEL_USE * (lv - START_LEVEL[t])
        self.use[t] = {g: u * k for g, u in self.base_use[t].items()}
        if t == 'PR' and not self.sheriff and 'ammo' in self.use[t]:
            self.use[t]['ammo'] = PRIMM_AMMO_USE_NO_SHERIFF * k

    def _levels(self, r):
        """After the day's trade: 7 met days and the building materials raise a level; 14 unmet days drop
        one (never below the level the town started at)."""
        for t in TOWNS:
            if self.basics_met(t):
                self.met_days[t] += 1
                self.unmet_days[t] = 0
            else:
                self.met_days[t] = 0
                self.unmet_days[t] += 1
            lv = self.level[t]
            if (lv < len(LEVELS) - 1 and self.met_days[t] >= LEVEL_MET_DAYS
                    and self.materials_in[t] >= LEVEL_MATERIALS[lv + 1]):
                self._set_level(t, lv + 1)
                self.materials_in[t] = 0
                self.met_days[t] = 0
                r.notes.append('%s grew to a %s' % (TOWN_NAME[t], LEVELS[lv + 1]))
            elif lv > START_LEVEL[t] and self.unmet_days[t] >= LEVEL_DROP_DAYS:
                self._set_level(t, lv - 1)
                self.unmet_days[t] = 0
                r.notes.append('%s slipped back to a %s' % (TOWN_NAME[t], LEVELS[lv - 1]))

    # --- M2: the tier 2 perk: the company buys trade goods from the player ----------------------------
    def buy_price_from_player(self, good):
        return half_up(BUY_SHARE * ANCHOR[good])

    def buy_from_player(self, good, crates=1):
        """At a branch from tier 2: a crate is 10 bottles of purified water or 10 healing powders, paid at
        0.8 of the anchor from operating cash, at most 10 crates a day; it goes to the Goodsprings
        warehouse. Returns the crates bought."""
        if self.tier < 2 or good not in BUY_FROM_PLAYER or self.ended:
            return 0
        if self.bought_day != self.day:
            self.bought_day, self.bought_today = self.day, 0
        price = self.buy_price_from_player(good)
        n = max(0, min(crates, BUY_DAY_MAX - self.bought_today, self.cash // price))
        self.cash -= n * price
        self.pocket += n * price
        self.warehouse[good] += n
        self.bought_today += n
        return n

    # --- the supply contract (plan task 1.8) ---------------------------------------------------------
    def offer_price(self):
        """Primm's sell price for water at normal stock, plus 9%."""
        g = CONTRACT_GOOD
        return half_up((1 + CONTRACT_PREMIUM) * self.price('PR', g, 'sell', self.normal['PR'][g]))

    def _sign(self, price, r, m=None):
        town, good, road = (m.town, m.good, m.road) if m else ('PR', CONTRACT_GOOD, 1)
        origin = [t for t in ROADS[road] if t != town][0]
        self.contracts.append(Contract(good, CONTRACT_CRATES, CONTRACT_EVERY, price, self.day, self.day,
                                       town=town, road=road, origin=origin))
        r.signed = price

    def contract_offer(self):
        """M2: (town, good, road) of this week's offer. Tier 1: Primm water (the M1 contract). From tier 2:
        the biggest standing shortage (3 days of use less the normal stock) at either end of a road the
        company runs, for a good the other end sells or a workshop there makes, not under contract."""
        if self.tier < 2:
            return ('PR', CONTRACT_GOOD, 1)
        best = None
        taken = {(c.town, c.good) for c in self.contracts}
        for _, road in self.running_roads():
            for town in ROADS[road]:
                origin = [t for t in ROADS[road] if t != town][0]
                for g in ALL_GOODS:
                    if g in SITE_GOODS or (town, g) in taken or not self.has_market(town, g):
                        continue
                    made = any(WHERE[w] == origin and g in WORKSHOPS[w][1] for w in self.workshops)
                    if not (self.has_market(origin, g) or made):
                        continue
                    short = 3 * self.use[town][g] - self.normal[town][g]
                    if best is None or short > best[0]:
                        best = (short, town, g, road)
        return best[1:] if best else None

    def offer_price_for(self, town, good):
        return half_up((1 + CONTRACT_PREMIUM) * self.price(town, good, 'sell', self.normal[town][good]))

    def _contract(self, r, runs, road=1):
        """Every contract this road serves that is due today. Returns {origin: crates loaded}."""
        loaded = {}
        for c in [c for c in self.contracts if c.road == road and c.next_due == self.day]:
            n = self._deliver(r, runs, c)
            loaded[c.origin] = loaded.get(c.origin, 0) + n
        return loaded

    def _deliver(self, r, runs, c):
        """A delivery day: load the crates on the Goodsprings leg (warehouse first, then bought at
        Goodsprings), sell them at the contract price without moving Primm's stock. A delivery the
        wagon cannot make is a miss: 10% of its value and Primm trust -3. Returns crates loaded."""
        loaded = 0
        o = c.origin
        if runs:
            own = min(self.wh[o][c.good], c.crates)
            stock, cost = self.stock[o][c.good], 0
            for _ in range(c.crates - own):
                cost += self.price(o, c.good, 'buy', stock)
                stock -= 1
            if cost <= self.cash:
                self.wh[o][c.good] -= own
                for _ in range(c.crates - own):
                    p = self.price(o, c.good, 'buy')
                    self.cash -= p
                    r.costs += p
                    self.stock[o][c.good] -= 1
                sale = c.crates * c.price
                self.cash += sale
                r.sales += sale
                self.week_sales += sale
                self.trust[c.town] = min(100, self.trust[c.town] + 1)
                c.done += 1
                r.contract = 'delivered'
                loaded = c.crates
        if not loaded:
            pay = min(self.cash, half_up(CONTRACT_MISS * c.crates * c.price))
            self.cash -= pay
            r.costs += pay
            self.trust[c.town] = max(0, self.trust[c.town] - 3)
            c.missed += 1
            r.contract = 'missed'
        c.next_due += c.every
        if c.next_due >= c.start + CONTRACT_DAYS:
            self.trust[c.town] = min(100, self.trust[c.town] + 3)
            self.contracts.remove(c)
            r.contract += ' completed'
        return loaded

    # --- standing orders (plan task 1.8) --------------------------------------------------------------
    def set_order(self, slot, kind, town='PR', good='water', value=None):
        """Set a slot (kind None empties it). Values default to 8 crates or the good's anchor price."""
        if kind is None:
            self.standing[slot] = None
            return
        if value is None:
            value = 8 if kind == 'keep' else ANCHOR[good]
        self.standing[slot] = StandingOrder(kind, town, good, value)

    def daily_burn(self):
        """Caps a day the company spends whatever it sells (for runway and loss caps)."""
        instalment = half_up(INTEREST * self.loan) + min(MIN_PRINCIPAL, self.loan)
        return half_up(self.daily_wages() + FEED + (RENT_WEEK + instalment) / 7)

    def week_running_costs(self):
        return 7 * self.daily_wages() + 7 * FEED + RENT_WEEK + half_up(INTEREST * self.loan)

    def runway(self):
        return self.cash // max(1, self.daily_burn())

    # --- bills and the debt ladder -------------------------------------------------------------------
    def _bills(self, r):
        bill = {'wages': self.accrued_wages, 'duty': duty(self.week_sales), 'rent': RENT_WEEK,
                'feed': self.accrued_feed, 'interest': half_up(INTEREST * self.loan),
                'principal': min(MIN_PRINCIPAL, self.loan)}
        if self.day % 28 == 0:
            bill['licence'] = LICENCE
        r.bills = bill
        total = sum(bill.values())
        self.accrued_wages = self.accrued_feed = self.week_sales = 0
        if self.cash >= total:
            self.cash -= total
            self.loan -= bill['principal']
            r.bills_paid = True
            return
        r.bills_paid = False
        paid = 0
        for k in ('wages', 'duty', 'rent', 'feed', 'licence', 'interest', 'principal'):
            amount = bill.get(k, 0)
            take = min(amount, self.cash)
            self.cash -= take
            paid += take
            if k == 'principal':
                self.loan -= take
        rest = total - paid
        self.arrears += rest + half_up(LATE_FEE * rest)
        if self.stage in ('ok', 'probation'):
            self.from_probation = self.stage == 'probation'
            self.stage, self.stage_day = 'deferred', self.day
            r.notes.append('bills missed: notice deferred')

    # served notices: a deferred notice reaches the player at a terminal or in a field letter
    def recent_strikes(self):
        return [s for s in self.strikes if self.day - s < STRIKE_DAYS]

    def serve_outcome(self):
        """The stage a deferred notice becomes when it is served now."""
        if self.arrears == 0:
            return 'probation'
        if len(self.recent_strikes()) + 1 >= STRIKES_TAKEOVER:
            return 'takeover'
        return 'final' if self.from_probation else 'grace'

    def serve(self):
        """Serve a deferred notice: it becomes a strike whoever pays it later (design: Strikes)."""
        if self.stage != 'deferred':
            return False
        stage = self.serve_outcome()
        self.strikes = self.recent_strikes() + [self.day]
        self.served_day, self.from_probation = self.day, False
        if stage == 'probation':
            self.stage, self.stage_day = 'probation', self.day
        elif stage == 'final':                  # a second miss on probation skips Grace
            self.stage, self.served_day, self.arrears_at_final = 'final', self.day - GRACE_DAYS, self.arrears
        else:
            self.stage = stage
        return True

    visit = serve

    def _pay_arrears(self, r):
        if self.arrears and self.cash > 0:
            take = min(self.cash, self.arrears)
            self.cash -= take
            self.arrears -= take
            if self.arrears == 0:
                self._cured(r)

    def _cured(self, r=None):
        """Arrears paid: probation. A deferred notice stays to be served (it is still a strike)."""
        if self.stage == 'deferred':
            return
        if self.stage == 'takeover' and self.strikes:
            self.strikes = self.strikes[1:]         # curing a takeover clears the oldest strike
        self.stage, self.stage_day = 'probation', self.day
        if r is not None:
            r.notes.append('notice cured')

    def days_left(self):
        """Days until the open notice's next step (the final notice, seizure, the end)."""
        since = self.day - self.served_day if self.served_day is not None else 0
        step = {'grace': GRACE_DAYS, 'final': FINAL_DAYS, 'seized': SEIZE_DAYS, 'takeover': TAKEOVER_DAYS,
                'probation': PROBATION_DAYS}
        if self.stage == 'probation':
            return max(0, PROBATION_DAYS - (self.day - self.stage_day))
        return max(0, step.get(self.stage, 0) - since)

    def final_need(self):
        """At the final notice: what must be paid now to keep the wagon (arrears down to 40%)."""
        import math
        return max(0, self.arrears - math.floor(FINAL_CURE * self.arrears_at_final))

    def _ladder(self, r):
        if self.stage in ('ok', 'deferred'):
            return
        if self.stage == 'probation':
            if self.day - self.stage_day >= PROBATION_DAYS:
                self.stage = 'ok'
            return
        if self.shield:
            self.served_day += 1                   # clocks stop in a DLC's own lands
            return
        since = self.day - self.served_day
        if self.stage == 'grace' and since >= GRACE_DAYS:
            self.stage, self.arrears_at_final = 'final', self.arrears
            r.notes.append('final notice')
        elif self.stage == 'final' and since >= FINAL_DAYS:
            if self.final_need() > 0 and self.wagon_ok:
                value = half_up(SEIZE_SHARE * self.wagon_value())
                self.assets -= self.wagon_value()
                self.wagon_ok = False
                self.arrears = max(0, self.arrears - value)
                r.notes.append('seized: the wagon and brahmin, %d caps against the arrears' % value)
            self.stage = 'seized'
            if self.arrears == 0:
                self._cured(r)
        elif self.stage in ('seized', 'takeover') and since >= SEIZE_DAYS and self.arrears > 0:
            self._end(r, 'receivership' if self.stage == 'seized' else 'takeover')

    def _end(self, r, reason):
        self.ended, self.end_reason = True, reason
        if r is not None:
            r.notes.append({'receivership': 'receivership: the office is now a Crimson Caravan branch',
                            'takeover': 'takeover: Alice took the office',
                            'walked': 'wound up by the owner'}[reason])

    # cures (design: Cures at Final notice); each one works at a terminal or from a notice letter
    def wagon_value(self):
        return max(0, self.assets - self.buildings) if self.wagon_ok else 0

    def rescue_cap(self):
        return RESCUE_WEEKS * (self.week_running_costs() + min(MIN_PRINCIPAL, self.loan))

    def rescue_amount(self):
        """What an owner rescue would pay now (0: not offered). Not for a takeover, once a season."""
        if self.stage not in ('grace', 'final', 'seized') or self.arrears <= 0:
            return 0
        if self.day - self.last_rescue < RESCUE_EVERY:
            return 0
        return min(self.arrears, self.rescue_cap())

    def owner_rescue(self):
        """Pay up to 2 weeks of bills from the owner's pocket: cures the notice (if it covers it), the
        strike stays, and the money is owner money (never toward a tier). False if not possible."""
        pay = self.rescue_amount()
        if pay <= 0 or self.pocket < pay:
            return False
        self.pocket -= pay
        self.owner_paid_in += pay
        self.arrears -= pay
        self.last_rescue = self.day
        if self.arrears == 0:
            self._cured()
        return True

    def sell_value(self):
        return half_up(SELL_SHARE * self.wagon_value()) if self.stage in SERVED and self.wagon_ok else 0

    def sell_wagon(self):
        """Sell the wagon and brahmin to a buyer at 60%; the money pays the arrears at once."""
        value = self.sell_value()
        if value <= 0:
            return False
        self.assets -= self.wagon_value()
        self.wagon_ok = False
        self.cash += value
        take = min(self.cash, self.arrears)
        self.cash -= take
        self.arrears -= take
        if self.arrears == 0:
            self._cured()
        return True

    def can_walk_away(self):
        return self.stage in SERVED and not self.ended

    def walk_away(self):
        """Wind the company up: on better terms than receivership (the successor chapter is M2+)."""
        if not self.can_walk_away():
            return False
        self._end(None, 'walked')
        return True

    def can_buy_wagon(self):
        return not self.wagon_ok and self.arrears == 0 and self.cash + self.owner_funds >= WAGON + BRAHMIN_PAIR

    def buy_wagon(self):
        """A new wagon and brahmin pair (700) after a seizure or a sale, once nothing is owed."""
        if not self.can_buy_wagon():
            return False
        cost = WAGON + BRAHMIN_PAIR
        from_owner = min(self.owner_funds, cost)
        self.owner_funds -= from_owner
        self.cash -= cost - from_owner
        self.assets += cost
        self.wagon_ok = True
        return True

    def notice_actions(self):
        """The cures a notice letter offers as buttons after 'Later', in order."""
        acts = []
        if self.rescue_amount() > 0:
            acts.append('rescue')
        if self.sell_value() > 0:
            acts.append('sell')
        return acts

    def forecast_short(self):
        """The forecast warning: runway under 5 days and no notice open. The shortfall on bill day
        (the bill estimate less cash, at least 1), or 0 when there is no warning."""
        if self.stage not in ('ok', 'probation') or self.runway() >= FORECAST_RUNWAY:
            return 0
        import post_model
        return max(1, post_model.bill_estimate(self) - self.cash)

    def history_text(self):
        return ' '.join(n for r in self.history for n in r.notes)

    # --- the post: memos and letters (plan task 1.6) -----------------------------------------------
    def post_memo(self, memo):
        """A new memo waits at the office unless 3 already wait; then it is not posted and its default stands."""
        if len(self.memos) >= MEMO_CAP:
            return False
        self.memos.append(memo)
        return True

    def answer(self, memo, pick):
        """The player picks an answer at a terminal or in a field letter; it applies at the next tick."""
        if 0 <= pick < len(memo.answers):
            memo.pick = pick

    def memo_default(self, m):
        """The answer an unanswered memo takes. A road memo on a contract delivery day sends the wagon:
        keeping it home would miss the delivery."""
        if m.kind == 'road' and self.contract_due(m.due):
            return SEND
        return MEMO_DEFAULT[m.kind]

    def _settle_memos(self, r):
        """At the tick, every answered memo and every memo due today is settled (unanswered: the default)."""
        keep = []
        for m in self.memos:
            if m.pick is None and m.due > self.day:
                keep.append(m)
                continue
            a = self.memo_default(m) if m.pick is None else m.pick
            if m.kind == 'road':
                self.road_mode = a
            elif m.kind == 'contract':
                if a == 0:
                    self._sign(m.price, r, m)
                elif a == 1:
                    if roll(self.seed, self.day, 4) < COUNTER_WALK:
                        r.contract = 'walked'
                    else:
                        self._sign(half_up(m.price * (1 + COUNTER_PREMIUM)), r, m)
            elif m.kind == 'raise':
                p = next((x for x in self.staff if x.name == m.who), None)
                if p is not None and a == 0:
                    p.wage = half_up(p.wage * RAISE)
                    self._loyal(p, RAISE_LOYALTY, 'a raise')
                elif p is not None:
                    self._loyal(p, REFUSE_LOYALTY, 'a raise refused')
            elif m.kind == 'prepay' and a == 0:
                pay = min(PREPAY, self.loan, self.cash)
                self.cash -= pay
                self.loan -= pay
                r.prepaid = pay
        self.memos = keep

    def _post_memos(self, r):
        """After the day: the road memo when bandits meet tomorrow's return leg, the prepay memo after
        paid bills when the cash allows. Returns whether a road memo was posted."""
        road = False
        if self.forecast() == 'bandits':
            road = self.post_memo(Memo('road', self.day, self.day + 1, road=self.event_road(self.day + 1)))
            pick = self.route_manager_pick()
            if road and pick is not None:
                self.memos[-1].pick = pick
                road = False                    # the manager answered it: no letter
        if (r.bills_paid and self.loan > 0 and not any(m.kind == 'prepay' for m in self.memos)
                and self.cash - PREPAY >= PREPAY_RUNWAY * self.daily_burn()):
            self.post_memo(Memo('prepay', self.day, self.day + 3))
        if (len(self.contracts) < CONTRACTS_OPEN[min(self.tier, 3)] and self.stage == 'ok'
                and self.wagon_ok and self.has_driver()
                and not any(m.kind == 'contract' for m in self.memos)
                and self.day % 7 == OFFER_WEEKDAY and self.day - self.last_offer >= OFFER_EVERY):
            offer = self.contract_offer()
            if offer is not None:
                town, good, road = offer
                price = self.offer_price() if self.tier < 2 else self.offer_price_for(town, good)
                if self.post_memo(Memo('contract', self.day, self.day + 1, price=price, town=town, good=good,
                                       road=road)):
                    self.last_offer = self.day
        return road

    def notice_values(self):
        """(stage, arrears, to pay, days left, strikes) for a notice letter. A deferred notice is written
        as it will be once served (serving happens when the letter is shown)."""
        import math
        if self.stage == 'deferred':
            st = self.serve_outcome()
            days = {'grace': GRACE_DAYS, 'final': FINAL_DAYS - GRACE_DAYS, 'takeover': TAKEOVER_DAYS,
                    'probation': PROBATION_DAYS}[st]
            need = self.arrears - math.floor(FINAL_CURE * self.arrears) if st == 'final' else self.arrears
            return (st, self.arrears, need, days, len(self.recent_strikes()) + 1)
        need = self.final_need() if self.stage == 'final' else self.arrears
        return (self.stage, self.arrears, need, self.days_left(), len(self.recent_strikes()))

    def _post_letters(self, r, road):
        """Letters of the day go to the Post; the most urgent one waits to be shown in the field
        (LETTER_ORDER). A waiting while-you-were-away letter is kept; a deferred notice is rewritten at
        every tick until it is served; any other waiting letter is stale after a tick."""
        import post_model
        new = []
        if self.ended:
            new.append(Letter(self.day, 'closed', (self.end_reason,)))
        elif (self.stage == 'deferred' and r.bills_paid is False) or any(
                n == 'final notice' or n.startswith('seized') for n in r.notes):
            new.append(Letter(self.day, 'notice', self.notice_values()))
        short = self.forecast_short()
        bill_day = self.day + post_model.days_to_bills(self)
        if short and self.forecast_bill_day != bill_day:
            self.forecast_bill_day = bill_day
            new.append(Letter(self.day, 'forecast', (short, post_model.days_to_bills(self))))
        if self.day - self.last_visit >= AWAY_DAYS and not self.away_posted:
            self.away_posted = True
            days = [h for h in self.history if h.day > self.last_visit]
            new.append(Letter(self.day, 'away', (self.day - self.last_visit, self.last_visit + 1,
                                                 sum(h.sales for h in days), sum(h.costs for h in days),
                                                 self.cash, self.runway(), len(self.memos))))
        if road:
            cover = self.cover()
            dg = ROAD_DANGER[self.event_road(self.day + 1)]       # M2: the danger of the road at risk
            new.append(Letter(self.day, 'road', (dg, cover, self.clean_chance(cover, dg),
                                                 int(self.contract_due(self.day + 1)))))
        if r.event in ('bandits_took_cargo', 'bandits_wreck'):
            new.append(Letter(self.day, 'loss', (r.event, r.event_loss)))
        if r.tier_up:
            new.append(Letter(self.day, 'tier', (self.tier,)))
        self.post = (self.post + new)[-POST_KEEP:]
        waiting = list(new)
        if self.stage == 'deferred' and not any(x.kind == 'notice' for x in new):
            waiting.append(Letter(self.day, 'notice', self.notice_values()))     # rewritten, not re-posted
        if self.letter and self.letter.kind in ('away', 'tier'):
            waiting.append(self.letter)
        waiting.sort(key=lambda x: LETTER_ORDER.index(x.kind))                # stable: new letters first
        self.letter = waiting[0] if waiting else None

    def terminal_visit(self):
        """The player opens a company terminal: a deferred notice is served there and the post is read,
        so no field letter waits."""
        self.serve()
        self.last_visit, self.away_posted, self.letter = self.day, False, None

    def field_letter(self, in_combat=False, in_menu=False):
        """The letter shown in the field now, if any: out of combat and menus, at most one a game day,
        none in a DLC's own lands (no runner finds you there). Showing a deferred notice serves it."""
        if self.letter is None or in_combat or in_menu or self.shield or self.letter_shown_day == self.day:
            return None
        letter, self.letter, self.letter_shown_day = self.letter, None, self.day
        if letter.kind == 'notice':
            self.serve()
        return letter

    def letter_buttons(self, letter):
        """The actions behind a letter's buttons, in order (texts in tools/post_model.py)."""
        if letter.kind == 'road':
            return ['hold', 'send', 'gun', 'later']
        if letter.kind == 'notice':
            acts = [a for a in self.notice_actions()
                    if a != 'rescue' or self.pocket >= self.rescue_amount()]
            return ['later'] + acts
        return ['ok']

    def answer_letter(self, letter, button, buttons=None):
        """Apply a letter's button. `buttons` is what letter_buttons gave when the box was shown."""
        acts = buttons if buttons is not None else self.letter_buttons(letter)
        if not 0 <= button < len(acts):
            return
        a = acts[button]
        if a in ('hold', 'send', 'gun'):
            memo = next((m for m in self.memos if m.kind == 'road'), None)
            if memo:
                self.answer(memo, {'hold': HOLD, 'send': SEND, 'gun': GUN}[a])
        elif a == 'rescue':
            self.owner_rescue()
        elif a == 'sell':
            self.sell_wagon()

    @property
    def contract(self):
        """The first open contract (M1 had one)."""
        return self.contracts[0] if self.contracts else None

    @contract.setter
    def contract(self, c):
        if c is None:
            self.contracts = self.contracts[1:]
        elif self.contracts:
            self.contracts[0] = c
        else:
            self.contracts = [c]

    # --- worth and tiers --------------------------------------------------------------------------
    def net_worth(self):
        stock_value = sum(ANCHOR[g] * n for wh in self.wh.values() for g, n in wh.items())
        return self.cash + self.owner_funds + stock_value + self.assets - self.loan - self.arrears

    def earned_worth(self):
        return self.net_worth() - self.owner_paid_in

    def tier_two_ready(self):
        recent = [s for s in self.strikes if self.day - s < 56]
        return (self.tier == 1 and self.earned_worth() >= TIER2_WORTH and not recent
                and self.trust['GS'] >= TIER2_TRUST and self.ghost_town_done)

    def tier_three_ready(self):
        recent = [s for s in self.strikes if self.day - s < 56]
        liked = sum(1 for t in TOWNS if self.trust[t] >= TIER3_TRUST)
        return (self.tier == 2 and self.earned_worth() >= TIER3_WORTH and not recent
                and liked >= TIER3_TOWNS and (self.sheriff or 'sheriff' in self.deeds))

    def _tier_check(self, r):
        if self.tier_two_ready():
            self.tier = 2
            r.notes.append('tier 2: Outfit')
            r.tier_up = True
            self.last_event_day = self.day      # no bad event for the 2 days after a new tier (design)
        elif self.tier_three_ready():
            self.tier = 3
            r.notes.append('tier 3: Caravan company')
            r.tier_up = True
            self.last_event_day = self.day

    def build_cost(self, name):
        return WORKSHOP_COST if name in WORKSHOPS else SITE_COST

    def built(self, name):
        return name in self.workshops or name in self.sites

    def can_build(self, name):
        """From its tier (2 or 3) and deed, each once, paid from owner money first, then cash."""
        deed = BUILD_DEED.get(name)
        return (self.tier >= BUILD_TIER[name] and not self.ended and not self.built(name)
                and (deed is None or deed in self.deeds)
                and self.cash + self.owner_funds >= self.build_cost(name))

    # --- more wagons (M2) -----------------------------------------------------------------------------
    def can_buy_road(self, road):
        """A wagon for road 2 (tier 2) or 3 (tier 3): 700 from owner money first, then cash."""
        return (road in (2, 3) and self.tier >= ROAD_TIER[road] and not self.ended
                and not any(w.road == road for w in self.wagons)
                and self.cash + self.owner_funds >= WAGON + BRAHMIN_PAIR)

    def buy_road(self, road):
        if not self.can_buy_road(road):
            return False
        cost = WAGON + BRAHMIN_PAIR
        from_owner = min(self.owner_funds, cost)
        self.owner_funds -= from_owner
        self.cash -= cost - from_owner
        self.assets += cost
        self.buildings += cost          # not wagon 1: a seizure takes the first wagon only
        self.wagons.append(Wagon(road))
        return True

    def build(self, name):
        if name in WORKSHOPS:
            self.workshops.append(name)
            cost = WORKSHOP_COST
        else:
            self.sites.append(name)
            self.hands += 1
            cost = SITE_COST
        from_owner = min(self.owner_funds, cost)
        self.owner_funds -= from_owner
        self.cash -= cost - from_owner
        self.assets += cost
        self.buildings += cost

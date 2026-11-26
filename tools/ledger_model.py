"""Reference model of the company ledger maths (the spec for the in-game CCLedger functions).

The rules are the design doc's "Money" section. run_first_week() reproduces the doc's worked first
week (Numbers section): one wagon, 8 crates a leg, one Goodsprings-Primm round trip a day, a greedy
player who loads the best crate while its margin is at least MIN_MARGIN, bandits take one crate on
day 5's return leg, and the Powder Gangers' news raises Primm ammo by 1.4 on days 4 and 5.
"""
from dataclasses import dataclass, field

ANCHOR = {'water': 200, 'powder': 100, 'ammo': 200, 'meat': 100}   # caps per crate
DEPTH_K = 2               # town depth scale (the economy report's tuning knob)
TOWNS = {                 # good -> (daily use, normal stock), before the depth scale
    'GS': {'water': (2, 17), 'powder': (1, 9), 'ammo': (2, 2), 'meat': (2, 2)},
    'PR': {'water': (5, 7), 'powder': (2, 2), 'ammo': (1, 10), 'meat': (3, 6)},
}
SPREAD = 0.06
CRATES_PER_LEG = 8
MIN_MARGIN = 20
SHORTAGE_REFILL = 0.25    # share of the gap to normal stock closed each day when short
GLUT_DRAIN = 0.12         # ... and when over-stocked
WAGES_PER_DAY = {'driver': 10, 'guard': 12}
FEED_PER_BRAHMIN_DAY = 3
DEPOT_RENT_WEEK = 70
DUTY_RATE = 0.02
WEAR_PER_DAY = 0.01 * 700
LOAN, OWN_MONEY, SETUP = 3000, 500, 1000
INTEREST_WEEK = 0.04
PRINCIPAL_WEEK = 300


def price_mult(stock, daily_use):
    """m = 0.5 + 1 / (1 + r), r = stock / (3 x daily use)."""
    r = stock / (3 * daily_use)
    return 0.5 + 1 / (1 + r)


def ask(anchor, mult, spread=SPREAD):
    """What the company pays a town for one crate."""
    return anchor * mult * (1 + spread)


def bid(anchor, mult, spread=SPREAD):
    """What a town pays the company for one crate."""
    return anchor * mult * (1 - spread)


def restock(stock, normal):
    """One day of the town's own supply and use pulling stock back toward normal."""
    return stock + (normal - stock) * (SHORTAGE_REFILL if stock < normal else GLUT_DRAIN)


@dataclass
class Leg:
    origin: str
    dest: str
    crates: dict = field(default_factory=dict)
    cost: float = 0.0
    sale: float = 0.0
    lost: float = 0.0

    @property
    def margin(self):
        return self.sale - self.cost


@dataclass
class Week:
    legs: list
    day_margins: list
    sales: float
    cogs: float

    @property
    def gross(self):
        return self.sales - self.cogs

    @property
    def wages(self):
        return 7 * sum(WAGES_PER_DAY.values())

    @property
    def feed(self):
        return 7 * 2 * FEED_PER_BRAHMIN_DAY

    @property
    def duty(self):
        return DUTY_RATE * self.sales

    @property
    def wear(self):
        return 7 * WEAR_PER_DAY

    @property
    def operating_profit(self):
        return self.gross - self.wages - self.feed - DEPOT_RENT_WEEK - self.duty - self.wear

    @property
    def interest(self):
        return INTEREST_WEEK * LOAN

    @property
    def net_profit(self):
        return self.operating_profit - self.interest


def _plan_leg(stock, use, origin, dest, news):
    """Greedy loading: the best crate by margin, while it pays at least MIN_MARGIN, up to the wagon size."""
    s_o, s_d, load = dict(stock[origin]), dict(stock[dest]), []
    for _ in range(CRATES_PER_LEG):
        best = None
        for g in ANCHOR:
            m = bid(ANCHOR[g], price_mult(s_d[g], use[dest][g])) * news.get((dest, g), 1.0) \
                - ask(ANCHOR[g], price_mult(s_o[g], use[origin][g]))
            if best is None or m > best[0]:
                best = (m, g)
        if best[0] < MIN_MARGIN:
            break
        load.append(best[1])
        s_o[best[1]] -= 1
        s_d[best[1]] += 1
    return load


def run_first_week():
    use = {t: {g: u * DEPTH_K for g, (u, n) in goods.items()} for t, goods in TOWNS.items()}
    normal = {t: {g: n * DEPTH_K for g, (u, n) in goods.items()} for t, goods in TOWNS.items()}
    stock = {t: dict(v) for t, v in normal.items()}
    stock = {t: {g: float(x) for g, x in v.items()} for t, v in stock.items()}
    news, legs, day_margins, sales, cogs = {}, [], [], 0.0, 0.0
    for day in range(1, 8):
        day_margin = 0.0
        for origin, dest in (('GS', 'PR'), ('PR', 'GS')):
            load = _plan_leg(stock, use, origin, dest, news)
            leg = Leg(origin, dest)
            for g in load:
                leg.cost += ask(ANCHOR[g], price_mult(stock[origin][g], use[origin][g]))
                stock[origin][g] -= 1
            for g in load:
                leg.sale += bid(ANCHOR[g], price_mult(stock[dest][g], use[dest][g])) * news.get((dest, g), 1.0)
                stock[dest][g] += 1
                leg.crates[g] = leg.crates.get(g, 0) + 1
            if day == 5 and origin == 'PR' and load:      # bandits take the last crate
                g = load[-1]
                leg.lost = bid(ANCHOR[g], price_mult(stock[dest][g] - 1, use[dest][g]))
                leg.sale -= leg.lost
                stock[dest][g] -= 1
            sales += leg.sale
            cogs += leg.cost
            day_margin += leg.margin
            legs.append(leg)
        day_margins.append(day_margin)
        for t in stock:
            for g in stock[t]:
                stock[t][g] = restock(stock[t][g], normal[t][g])
        if day == 3:
            news[('PR', 'ammo')] = 1.4
        if day == 6:
            news.pop(('PR', 'ammo'), None)
    return Week(legs, day_margins, sales, cogs)

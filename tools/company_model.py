"""M1 company model: the spec for every number the in-game company shows (plan task 1.1).

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

GOODS = ('water', 'powder', 'ammo', 'dirty', 'herbs', 'materials')
ANCHOR = {'water': 200, 'powder': 100, 'ammo': 200, 'dirty': 100, 'herbs': 60, 'materials': 150}
# Starter trade (design: Goods and production chains): daily use, normal stock.
STARTER = {
    'GS': {'water': (4, 34), 'powder': (2, 18), 'ammo': (4, 4), 'dirty': (1, 30), 'herbs': (1, 15),
           'materials': (1, 0)},
    'PR': {'water': (10, 14), 'powder': (4, 4), 'ammo': (2, 20), 'dirty': (2, 2), 'herbs': (1, 1),
           'materials': (1, 10)},
}
PRIMM_AMMO_USE_NO_SHERIFF = 3
ROUTE = ('GS', 'PR')
TRUST_START = {'GS': 35, 'PR': 20}
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
# Memo answers in order; the default is the cautious one (design: Memos).
MEMO_ANSWERS = {'road': ('send as planned', 'hire a gun for 25', 'keep the wagon home'),
                'prepay': ('pay 300 off the loan', 'keep the cash')}
MEMO_DEFAULT = {'road': 2, 'prepay': 1}
SEND, GUN, HOLD = 0, 1, 2        # road memo answers

TIER2_WORTH, TIER2_TRUST = 1500, 50
WORKSHOP_COST, SITE_COST, HAND_WAGE = 300, 200, 14
WORKSHOPS = {                    # name: (inputs per batch, outputs per batch, output crates a day)
    'purifier': ({'dirty': 5}, {'water': 4}, 4),
    'apothecary': ({'herbs': 1}, {'powder': 1}, 4),
}
SITES = {'well': 'dirty', 'forager': 'herbs'}   # raw sites, 4 crates a day each
SITE_RATE = 4


def half_up(x):
    """Whole caps: round half up (the game uses floor(x + 0.5))."""
    import math
    return int(math.floor(x + 0.5))


def roll(seed, day, key):
    """The seeded roll, 0..99; the game uses the same integer formula."""
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


@dataclass
class Memo:
    kind: str           # 'road' or 'prepay'
    day: int            # the day it was posted
    due: int            # the tick that settles it with the default if nobody answers
    pick: int = None    # the answer chosen at a terminal or in a field letter

    @property
    def answers(self):
        return MEMO_ANSWERS[self.kind]


@dataclass
class Letter:
    day: int
    kind: str           # 'away', 'road' or 'loss'
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

    @property
    def margin(self):
        return self.sales - self.costs


class Company:
    def __init__(self, seed, sheriff=False, present=True):
        self.seed, self.sheriff, self.present = seed, sheriff, present
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
        self.shield = False
        self.last_event_day = -99
        self.wagon_ok = True
        self.ghost_town_done = False
        self.warehouse = {g: 0 for g in GOODS}
        self.workshops, self.sites, self.hands = [], [], 0
        self.memos, self.road_mode = [], SEND
        self.last_visit, self.away_posted = 0, False
        self.letter, self.letter_shown_day, self.post = None, -1, []

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

    # --- prices ---------------------------------------------------------------------------------
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
        s = spread(self.trust[town])
        return half_up(m * (1 + s) if side == 'buy' else m * (1 - s))

    # --- the bookkeeper's plan --------------------------------------------------------------------
    def plan(self):
        """Greedy: for each leg, the best crate by margin while it pays MIN_MARGIN, up to 8 a leg.
        Own warehouse crates cost nothing to load and go first when they pay."""
        orders = []
        cash = self.cash
        for origin, dest in (ROUTE, ROUTE[::-1]):
            so, sd = dict(self.stock[origin]), dict(self.stock[dest])
            wh = dict(self.warehouse) if origin == 'GS' else {g: 0 for g in GOODS}
            for _ in range(CRATES_PER_LEG):
                best = None
                for g in GOODS:
                    sale = self.price(dest, g, 'sell', sd[g])
                    own = wh[g] > 0
                    cost = 0 if own else self.price(origin, g, 'buy', so[g])
                    if not own and cost > cash:
                        continue
                    m = sale - cost
                    if best is None or m > best[0]:
                        best = (m, g, own, cost)
                if best is None or best[0] < MIN_MARGIN:
                    break
                m, g, own, cost = best
                if own:
                    wh[g] -= 1
                else:
                    so[g] -= 1
                    cash -= cost
                sd[g] += 1
                orders.append(Order('carry', origin, g, 1))     # one order per crate, in pick order
        return orders

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
            self.queue_list = self.plan()
        self._pay_arrears(r)
        r.wagon, r.road_mode = self.wagon_ok, self.road_mode
        if self.wagon_ok and self.road_mode == HOLD:
            if self.event_fires(d):
                self.last_event_day = d             # the bandits waited for a wagon that stayed home
        elif self.wagon_ok:
            if self.road_mode == GUN:
                pay = min(GUN_COST, self.cash)
                self.cash -= pay
                r.costs += pay
            for origin, dest in (ROUTE, ROUTE[::-1]):
                if origin == 'PR':
                    self._event(r)
                self._leg(r, origin, dest, [o for o in self.queue_list if o.town == origin])
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
        self._ladder(r)
        self._tier_check(r)
        r.cash = self.cash
        self.history.append(r)
        road = self._post_memos(r)
        self._post_letters(r, road)
        return r

    def _leg(self, r, origin, dest, orders):
        crates = []
        for o in orders:
            for _ in range(o.qty):
                if origin == 'GS' and self.warehouse[o.good] > 0:
                    self.warehouse[o.good] -= 1
                    crates.append((o.good, 0))
                    continue
                cost = self.price(origin, o.good, 'buy')
                if cost > self.cash:
                    continue
                self.cash -= cost
                r.costs += cost
                self.stock[origin][o.good] -= 1
                crates.append((o.good, cost))
        for g, _ in crates:
            sale = self.price(dest, g, 'sell')
            self.cash += sale
            r.sales += sale
            self.week_sales += sale
            self.stock[dest][g] += 1
            r.loads[(origin, g)] = r.loads.get((origin, g), 0) + 1

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
        if not self.wagon_ok:
            return 'no_wagon'
        return 'bandits' if self.event_fires(self.day + 1) else 'quiet'

    def clean_chance(self, cover):
        """Percent chance the crew drives the bandits off: r^2 / (1 + r^2), r = cover / danger."""
        ratio = cover / DANGER
        return half_up(100 * ratio * ratio / (1 + ratio * ratio))

    def _event(self, r):
        """Before the return leg: the director may send bandits at the wagon. They rob the strongbox, the
        cash from the day's Primm sales: 30% of it, or all of it in a wreck, never more than 3 days of
        running costs at tier 1. The loss is booked as a cost of the day."""
        d = self.day
        if not self.event_fires(d):
            return
        self.last_event_day = d
        cover = COVER + (GUN_COVER if r.road_mode == GUN else 0)
        if roll(self.seed, d, 2) < self.clean_chance(cover):
            r.event = 'bandits_driven_off'
            return
        takings = r.sales
        if takings <= 0:
            r.event = 'bandits_empty'
            return
        wreck = roll(self.seed, d, 3) < 33
        loss = min(takings if wreck else half_up(ROB_SHARE * takings), 3 * self.daily_burn())
        self.cash -= loss
        r.costs += loss
        r.event = 'bandits_wreck' if wreck else 'bandits_took_cargo'
        r.event_loss = loss

    def run_workshops(self):
        for site in self.sites:
            self.warehouse[SITES[site]] += SITE_RATE
        for w in self.workshops:
            ins, outs, cap = WORKSHOPS[w]
            (good_in, need), = ins.items()
            (good_out, per), = outs.items()
            made = 0
            while self.warehouse[good_in] >= need and made + per <= cap:
                self.warehouse[good_in] -= need
                self.warehouse[good_out] += per
                made += per

    def daily_wages(self):
        return sum(WAGES.values()) + HAND_WAGE * self.hands

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
            self.stage, self.stage_day = 'deferred', self.day
            if self.present and not self.shield:
                self.visit()

    def visit(self):
        """The player reaches a terminal (or a runner finds them): a deferred notice is served."""
        if self.stage == 'deferred':
            self.stage, self.served_day = 'grace', self.day
            self.strikes = [s for s in self.strikes if self.day - s < 56] + [self.day]

    def _pay_arrears(self, r):
        if self.arrears and self.cash > 0:
            take = min(self.cash, self.arrears)
            self.cash -= take
            self.arrears -= take
            if self.arrears == 0:
                self._cured(r)

    def _cured(self, r):
        self.stage, self.stage_day = 'probation', self.day
        r.notes.append('notice cured')

    def _ladder(self, r):
        if self.stage in ('ok', 'deferred'):
            return
        if self.stage == 'probation':
            if self.day - self.stage_day >= 14:
                self.stage = 'ok'
            return
        if self.shield:
            self.served_day += 1                   # clocks stop in a DLC's own lands
            return
        since = self.day - self.served_day
        if self.stage == 'grace' and since >= 3:
            self.stage, self.arrears_at_final = 'final', self.arrears
        elif self.stage == 'final' and since >= 5:
            if self.arrears > 0.4 * self.arrears_at_final:
                value = half_up(0.6 * self.assets)
                self.assets = 0
                self.wagon_ok = False
                self.arrears = max(0, self.arrears - value)
                r.notes.append('seized: the wagon and brahmin, %d caps against the arrears' % value)
            self.stage = 'seized'
            if self.arrears == 0:
                self._cured(r)
        elif self.stage == 'seized' and since >= 7 and self.arrears > 0:
            self.ended = True
            r.notes.append('receivership: the office is now a Crimson Caravan branch')

    def owner_rescue(self):
        """Up to 2 weeks of bills from the owner's pocket: cures the notice, the strike stays."""
        self.owner_paid_in += self.arrears
        self.arrears = 0
        self.stage, self.stage_day = 'probation', self.day

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

    def _settle_memos(self, r):
        """At the tick, every answered memo and every memo due today is settled (unanswered: the default)."""
        keep = []
        for m in self.memos:
            if m.pick is None and m.due > self.day:
                keep.append(m)
                continue
            a = MEMO_DEFAULT[m.kind] if m.pick is None else m.pick
            if m.kind == 'road':
                self.road_mode = a
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
            road = self.post_memo(Memo('road', self.day, self.day + 1))
        if (r.bills_paid and self.loan > 0 and not any(m.kind == 'prepay' for m in self.memos)
                and self.cash - PREPAY >= PREPAY_RUNWAY * self.daily_burn()):
            self.post_memo(Memo('prepay', self.day, self.day + 3))
        return road

    def _post_letters(self, r, road):
        """Letters of the day go to the Post; the first one waits to be shown in the field. A waiting
        while-you-were-away letter is kept; any other waiting letter is stale after a tick."""
        new = []
        if self.day - self.last_visit >= AWAY_DAYS and not self.away_posted:
            self.away_posted = True
            days = [h for h in self.history if h.day > self.last_visit]
            new.append(Letter(self.day, 'away', (self.day - self.last_visit, self.last_visit + 1,
                                                 sum(h.sales for h in days), sum(h.costs for h in days),
                                                 self.cash, self.runway(), len(self.memos))))
        if road:
            new.append(Letter(self.day, 'road', (DANGER, COVER)))
        if r.event in ('bandits_took_cargo', 'bandits_wreck'):
            new.append(Letter(self.day, 'loss', (r.event, r.event_loss)))
        self.post = (self.post + new)[-POST_KEEP:]
        if not (self.letter and self.letter.kind == 'away'):
            self.letter = new[0] if new else None

    def terminal_visit(self):
        """The player opens a company terminal: the post is read there, so no field letter waits."""
        self.last_visit, self.away_posted, self.letter = self.day, False, None

    def field_letter(self, in_combat=False, in_menu=False):
        """The letter shown in the field now, if any: out of combat and menus, at most one a game day."""
        if self.letter is None or in_combat or in_menu or self.letter_shown_day == self.day:
            return None
        letter, self.letter, self.letter_shown_day = self.letter, None, self.day
        return letter

    def answer_letter(self, letter, button):
        """A road letter's buttons: 0 keep it home, 1 send as planned, 2 hire a gun, 3 later."""
        if letter.kind != 'road' or button == 3:
            return
        memo = next((m for m in self.memos if m.kind == 'road'), None)
        if memo:
            self.answer(memo, (HOLD, SEND, GUN)[button])

    # --- worth and tiers --------------------------------------------------------------------------
    def net_worth(self):
        stock_value = sum(ANCHOR[g] * n for g, n in self.warehouse.items())
        return self.cash + self.owner_funds + stock_value + self.assets - self.loan - self.arrears

    def earned_worth(self):
        return self.net_worth() - self.owner_paid_in

    def tier_two_ready(self):
        recent = [s for s in self.strikes if self.day - s < 56]
        return (self.tier == 1 and self.earned_worth() >= TIER2_WORTH and not recent
                and self.trust['GS'] >= TIER2_TRUST and self.ghost_town_done)

    def _tier_check(self, r):
        if self.tier_two_ready():
            self.tier = 2
            r.notes.append('tier 2: Outfit')

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

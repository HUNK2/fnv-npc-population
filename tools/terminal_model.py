"""M1 office terminal model (plan task 1.4): the exact row labels of every screen and what a click does.

The game's terminal (CCOfficeTerm, drawn by CCTermDraw) must show these labels to the character, so
tools/ingame_terminal.py can compare them. One terminal form, a pool of 14 rows: a screen is a list
of labels (rows past the list are hidden by the row condition CCTerm.iRows > n) and every click is
(screen, row). A row shows at most 39 characters on screen (the rest is cut, seen live), so labels stay within 39.
"""
import company_model as cm
from company_model import GOODS, half_up

FRONT, PRICES, LEDGER, ORDERS, ROUTES, SETTINGS = range(6)
MAX_ROWS = 14
ROW_WIDTH = 39
# Good names padded to one width, as the game writes them (fixed text in each Console line).
NAMES = {'water': 'water      ', 'powder': 'powder     ', 'ammo': 'ammo       ', 'dirty': 'dirty water',
         'herbs': 'herbs      ', 'materials': 'materials  '}
TOWNS = ('GS', 'PR')
STAGES = {'ok': 'none', 'deferred': 'deferred', 'grace': 'SERVED', 'final': 'FINAL', 'seized': 'SEIZED',
          'probation': 'probation'}
EVENTS = {'': '', 'bandits_driven_off': '  driven off', 'bandits_took_cargo': '  bandits -%d',
          'bandits_wreck': '  WRECKED -%d'}


class Terminal:
    """The terminal's own state (quest CCTerm): which screen is up and the Prices direction."""

    def __init__(self):
        self.screen = FRONT
        self.direction = 0          # 0: Goodsprings > Primm, 1: Primm > Goodsprings


def days_to_bills(c):
    return 7 - c.day % 7


def bill_estimate(c):
    """The next weekly bill if the rest of the week goes like a quiet day (design: the front page)."""
    due = c.day + days_to_bills(c)
    est = (7 * c.daily_wages() + 7 * cm.FEED + cm.RENT_WEEK + half_up(cm.INTEREST * c.loan)
           + min(cm.MIN_PRINCIPAL, c.loan) + cm.duty(c.week_sales))
    return est + (cm.LICENCE if due % 28 == 0 else 0)


def best_margin(c, origin=0):
    """(good, margin) of the best crate on a leg at today's stock, first good on a tie."""
    o, d = TOWNS[origin], TOWNS[1 - origin]
    best = None
    for g in GOODS:
        m = c.price(d, g, 'sell') - c.price(o, g, 'buy')
        if best is None or m > best[1]:
            best = (g, m)
    return best


def queued(c, origin):
    return sum(1 for o in c.queue_list if o.town == TOWNS[origin])


def last_report(c):
    return c.history[-1] if c.history else None


def labels(c, t):
    """Row labels of the screen that is up."""
    if not c.founded:
        return ["No company yet: see Alice's agent."]
    if t.screen == FRONT:
        r = last_report(c)
        g, m = best_margin(c)
        rows = ['CASH %d BILLS %dd:%d RUNWAY %dd' % (c.cash, days_to_bills(c), bill_estimate(c), c.runway()),
                'PLAN     accept the plan (%d crates)' % len(c.plan()),
                ('POST     day %d: net %d' % (r.day, r.margin)) if r else 'POST     nothing yet',
                'MEMOS    none waiting',
                'ROUTES   wagon %s' % ('home' if c.wagon_ok else 'seized'),
                'PRICES   best GS>PR: %s %d' % (NAMES[g].strip(), m),
                'CHAINS   none yet (tier 2)',
                'STAFF    %d on the books' % (2 + c.hands),
                'CONTRACTS none running',
                'LEDGER   loan %d, week sales %d' % (c.loan, c.week_sales),
                'ORDERS   %d pending (apply at 06:00)' % len(c.queue_list),
                'SETTINGS']
        return rows
    if t.screen == PRICES:
        o, d = TOWNS[t.direction], TOWNS[1 - t.direction]
        rows = ['%s > %s  buy/sell  (select to switch)' % (o, d)]
        for g in GOODS:
            b, s = c.price(o, g, 'buy'), c.price(d, g, 'sell')
            rows.append('%s %d/%d  margin %d  [%d]' % (NAMES[g], b, s, s - b,
                                                                    sum(1 for q in c.queue_list
                                                                        if q.town == o and q.good == g)))
        return rows + ['BACK']
    if t.screen == LEDGER:
        return ['DAY %d  CASH %d  OWNER %d' % (c.day, c.cash, c.owner_funds),
                'LOAN %d  ARREARS %d' % (c.loan, c.arrears),
                'NOTICE %s' % STAGES[c.stage],
                'WEEK SALES %d' % c.week_sales,
                'NEXT BILLS in %dd: about %d' % (days_to_bills(c), bill_estimate(c)),
                'COSTS %d a week, %d a day' % (c.week_running_costs(), c.daily_burn()),
                'NET WORTH %d  EARNED %d' % (c.net_worth(), c.earned_worth()),
                'BACK']
    if t.screen == ORDERS:
        return ['GS > PR  %d crates' % queued(c, 0),
                'PR > GS  %d crates' % queued(c, 1),
                'ACCEPT the plan (%d crates)' % len(c.plan()),
                'CANCEL all pending orders',
                'BACK']
    if t.screen == ROUTES:
        rows = ['WAGON 1  %s  driver and guard' % ('home' if c.wagon_ok else 'SEIZED')]
        for r in c.history[-3:][::-1]:
            ev = EVENTS[r.event] % r.event_loss if '%' in EVENTS[r.event] else EVENTS[r.event]
            rows.append('DAY %d  net %d%s' % (r.day, r.margin, ev))
        return rows + ['BACK']
    if t.screen == SETTINGS:
        return ['PLAN EVERY DAY   %s' % ('ON' if c.auto else 'OFF'), 'BACK']
    raise ValueError(t.screen)


def click(c, t, row):
    """What selecting a row does. Rows past the screen's labels are hidden: a click there does nothing."""
    rows = labels(c, t)
    if not c.founded or row >= len(rows):
        return
    if t.screen == FRONT:
        if row == 1:
            c.queue_list = c.plan()
        else:
            t.screen = {4: ROUTES, 5: PRICES, 9: LEDGER, 10: ORDERS, 11: SETTINGS}.get(row, FRONT)
        return
    if row == len(rows) - 1:                    # BACK is always the last row
        t.screen = FRONT
        return
    if t.screen == PRICES:
        if row == 0:
            t.direction = 1 - t.direction
        elif queued(c, t.direction) < cm.CRATES_PER_LEG:
            c.queue(cm.Order('carry', TOWNS[t.direction], GOODS[row - 1], 1))
    elif t.screen == ORDERS:
        if row == 2:
            c.queue_list = c.plan()
        elif row == 3:
            c.queue_list = []
    elif t.screen == SETTINGS and row == 0:
        c.auto = not c.auto

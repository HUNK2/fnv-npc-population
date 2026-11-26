"""M1 office terminal model (plan task 1.4): the exact row labels of every screen and what a click does.

The game's terminal (CCOfficeTerm, drawn by CCTermDraw) must show these labels to the character, so
tools/ingame_terminal.py can compare them. One terminal form, a pool of 14 rows: a screen is a list
of labels (rows past the list are hidden by the row condition CCTerm.iRows > n) and every click is
(screen, row). A row shows at most 39 characters on screen (the rest is cut, seen live), so labels stay within 39.
"""
import company_model as cm
import post_model as pm
from company_model import GOODS
from post_model import bill_estimate, days_to_bills   # noqa: F401 (used by the tests and the game check)

FRONT, PRICES, LEDGER, ORDERS, ROUTES, SETTINGS, POST, MEMOS, NOTICE = range(9)
MAX_ROWS = 14
ROW_WIDTH = 39
# Good names padded to one width, as the game writes them (fixed text in each Console line).
NAMES = {'water': 'water      ', 'powder': 'powder     ', 'ammo': 'ammo       ', 'dirty': 'dirty water',
         'herbs': 'herbs      ', 'materials': 'materials  '}
TOWNS = ('GS', 'PR')
STAGES = {'ok': 'none', 'deferred': 'deferred', 'grace': 'SERVED', 'final': 'FINAL', 'seized': 'SEIZED',
          'probation': 'probation', 'takeover': 'TAKEOVER'}
CLOSED = {'receivership': 'the lender took the office', 'takeover': 'the lender took the office',
          'walked': 'you wound it up'}
EVENTS = {'': '', 'bandits_driven_off': '  driven off', 'bandits_took_cargo': '  bandits -%d',
          'bandits_wreck': '  WRECKED -%d', 'bandits_empty': '  nothing taken'}


class Terminal:
    """The terminal's own state (quest CCTerm): which screen is up and the Prices direction."""

    def __init__(self):
        self.screen = FRONT
        self.direction = 0          # 0: Goodsprings > Primm, 1: Primm > Goodsprings
        self.confirm = False        # WALK AWAY was selected once; a second select winds the company up


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


def memos_row(c):
    if not c.memos:
        return 'MEMOS    none waiting'
    return 'MEMOS    %d waiting, %d due tomorrow' % (len(c.memos), sum(1 for m in c.memos if m.due - c.day <= 1))


def memo_rows(c):
    """(label, result text, memo, answer index or None) for each Memos screen row before BACK."""
    if not c.memos:
        return [('No memos waiting.', '', None, None)]
    rows = []
    for m in c.memos:
        rows.append((pm.memo_title(c, m), pm.memo_text(c, m), m, None))
        rows += [(pm.answer_label(m, i), '', m, i) for i in range(len(m.answers))]
    return rows


def notice_row(c):
    """The front page's NOTICE row: the forecast warning, or the open notice and its clock."""
    short = c.forecast_short()
    if short:
        return 'WARNING  short ~%d on bill day' % short
    d = c.days_left()
    return {'ok': 'NOTICE   none',
            'deferred': 'NOTICE   unread: %d owed' % c.arrears,
            'probation': 'NOTICE   probation, %dd left' % d,
            'grace': 'NOTICE   SERVED: %d owed, %dd' % (c.arrears, d),
            'final': 'NOTICE   FINAL: pay %d in %dd' % (c.final_need(), d),
            'seized': 'NOTICE   SEIZED: %d owed, %dd' % (c.arrears, d),
            'takeover': 'NOTICE   TAKEOVER: %d owed, %dd' % (c.arrears, d)}[c.stage]


def notice_rows(c, t):
    """(label, result text, action) for each Notice screen row before BACK."""
    if c.stage in cm.SERVED or c.stage == 'probation':
        text = pm.notice_text(c.notice_values())
    elif c.forecast_short():
        text = pm.forecast_text(c.forecast_short(), days_to_bills(c))
    else:
        text = 'No notice. The bills are paid on time.'
    rows = [('OWED %d  STRIKES %d of 3' % (c.arrears, len(c.recent_strikes())), text, None)]
    if c.stage in cm.SERVED:
        if c.rescue_amount() > 0:
            rows.append(('RESCUE  pay %d (you have %d)' % (c.rescue_amount(), c.pocket), '', 'rescue'))
        if c.sell_value() > 0:
            rows.append(('SELL wagon and brahmin  +%d' % c.sell_value(), '', 'sell'))
        rows.append(('WALK AWAY  select again to confirm' if t.confirm else 'WALK AWAY  wind the company up',
                     '', 'walk'))
    return rows


def post_rows(c):
    """(label, result text) for each Post screen row before BACK: the report's pages, then letters newest first."""
    pages = pm.report_pages(c)
    if not pages:
        return [('No post yet.', '')]
    d = c.history[-1].day
    rows = [('REPORT day %d  page 1' % d, pages[0]), ('REPORT day %d  page 2' % d, pages[1])]
    return rows + [(pm.letter_title(x), pm.letter_text(x)) for x in c.post[::-1]]


def results(c, t):
    """The result text of each row of the screen that is up (shown when the row is selected)."""
    if c.founded and t.screen == POST:
        return [text for _, text in post_rows(c)] + ['']
    if c.founded and t.screen == MEMOS:
        return [row[1] for row in memo_rows(c)] + ['']
    if c.founded and not c.ended and t.screen == NOTICE:
        return [row[1] for row in notice_rows(c, t)] + ['']
    return [''] * len(labels(c, t))


def labels(c, t):
    """Row labels of the screen that is up."""
    if not c.founded:
        return ["No company yet: see Alice's agent."]
    if c.ended:
        return ['CLOSED: %s' % CLOSED[c.end_reason], 'DAY %d  CASH %d  OWED %d' % (c.day, c.cash, c.arrears)]
    if t.screen == FRONT:
        r = last_report(c)
        g, m = best_margin(c)
        rows = ['CASH %d BILLS %dd:%d RUNWAY %dd' % (c.cash, days_to_bills(c), bill_estimate(c), c.runway()),
                'PLAN     accept the plan (%d crates)' % len(c.plan()),
                ('POST     day %d: net %d' % (r.day, r.margin)) if r else 'POST     nothing yet',
                memos_row(c),
                'ROUTES   wagon %s' % ('home' if c.wagon_ok else 'none'),
                'PRICES   best GS>PR: %s %d' % (NAMES[g].strip(), m),
                'CHAINS   none yet (tier 2)',
                'STAFF    %d on the books' % (2 + c.hands),
                'CONTRACTS none running',
                'LEDGER   loan %d, week sales %d' % (c.loan, c.week_sales),
                'ORDERS   %d pending (apply at 06:00)' % len(c.queue_list),
                'SETTINGS',
                notice_row(c)]
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
        rows = ['WAGON 1  home  driver and guard' if c.wagon_ok else
                'WAGON 1  none: BUY one for %d' % (cm.WAGON + cm.BRAHMIN_PAIR)]
        for r in c.history[-3:][::-1]:
            ev = EVENTS[r.event] % r.event_loss if '%' in EVENTS[r.event] else EVENTS[r.event]
            rows.append('DAY %d  net %d%s' % (r.day, r.margin, ev))
        return rows + ['BACK']
    if t.screen == SETTINGS:
        return ['PLAN EVERY DAY   %s' % ('ON' if c.auto else 'OFF'), 'BACK']
    if t.screen == POST:
        return [label for label, _ in post_rows(c)] + ['BACK']
    if t.screen == MEMOS:
        return [row[0] for row in memo_rows(c)] + ['BACK']
    if t.screen == NOTICE:
        return [row[0] for row in notice_rows(c, t)] + ['BACK']
    raise ValueError(t.screen)


def click(c, t, row):
    """What selecting a row does. Rows past the screen's labels are hidden: a click there does nothing."""
    rows = labels(c, t)
    if not c.founded or c.ended or row >= len(rows):
        return
    confirm, t.confirm = t.confirm, False
    if t.screen == FRONT:
        if row == 1:
            c.queue_list = c.plan()
        else:
            t.screen = {2: POST, 3: MEMOS, 4: ROUTES, 5: PRICES, 9: LEDGER, 10: ORDERS, 11: SETTINGS,
                        12: NOTICE}.get(row, FRONT)
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
    elif t.screen == ROUTES and row == 0:
        c.buy_wagon()
    elif t.screen == NOTICE:
        act = notice_rows(c, t)[row][2]
        if act == 'rescue':
            c.owner_rescue()
        elif act == 'sell':
            c.sell_wagon()
        elif act == 'walk':
            if confirm:
                c.walk_away()
            else:
                t.confirm = True
    elif t.screen == SETTINGS and row == 0:
        c.auto = not c.auto
    elif t.screen == MEMOS:
        _, _, m, i = memo_rows(c)[row]
        if i is not None:
            c.answer(m, i)

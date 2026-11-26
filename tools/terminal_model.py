"""M1 office terminal model (plan task 1.4): the exact row labels of every screen and what a click does.

The game's terminal (CCOfficeTerm, drawn by CCTermDraw) must show these labels to the character, so
tools/ingame_terminal.py can compare them. One terminal form, a pool of 14 rows: a screen is a list
of labels (rows past the list are hidden by the row condition CCTerm.iRows > n) and every click is
(screen, row). A row shows at most 39 characters on screen (the rest is cut, seen live), so labels stay within 39.
"""
import company_model as cm
import law_model as law
import post_model as pm
from company_model import GOODS
from post_model import bill_estimate, days_to_bills   # noqa: F401 (used by the tests and the game check)

FRONT, PRICES, LEDGER, ORDERS, ROUTES, SETTINGS, POST, MEMOS, NOTICE = range(9)
STAFF, HIRE, CANDIDATE, CONTRACTS, STANDING, SLOT, BUILD = range(9, 16)
TOWNS_SCREEN = 16               # M2 (tier 2): the towns' levels and trust, and the managers
# BACK on a screen reached from another screen goes back there; otherwise to the front page.
PARENT = {HIRE: STAFF, CANDIDATE: HIRE, SLOT: STANDING, STANDING: ORDERS}
SO_LABEL = {None: 'empty', 'keep': 'keep stocked', 'sell_above': 'sell above', 'max_pay': 'pay at most'}
SO_KIND_CYCLE = (None, 'keep', 'sell_above', 'max_pay')
PRICE_STEP = 5
MAX_ROWS = 14
ROW_WIDTH = 39
# Good names padded to one width, as the game writes them (fixed text in each Console line).
NAMES = {'water': 'water      ', 'powder': 'powder     ', 'ammo': 'ammo       ', 'dirty': 'dirty water',
         'herbs': 'herbs      ', 'materials': 'materials  '}
TOWNS = ('GS', 'PR')
STAGES = {'ok': 'none', 'deferred': 'deferred', 'grace': 'SERVED', 'final': 'FINAL', 'seized': 'SEIZED',
          'probation': 'probation', 'takeover': 'TAKEOVER'}
CLOSED = {'receivership': 'the lender took the office', 'takeover': 'the lender took the office',
          'walked': 'you wound it up', 'revoked': 'the NCR revoked the licence'}
# The Build screen (tier 2): what each building does, padded as the game writes it.
BUILD_TEXT = {'purifier': 'PURIFIER   5 dirty > 4 water  ', 'apothecary': 'APOTHECARY 1 herbs > 1 powder ',
              'well': 'WELL RIG   4 dirty water a day', 'forager': 'FORAGER    4 herbs a day      ',
              'corral': 'CORRAL     4 brahmin a day    ', 'sandpit': 'SAND PIT   4 sand a day, PR   ',
              'scrapyard': 'SCRAP YARD 4 scrap a day, PR  ', 'smokehouse': 'SMOKEHOUSE 1 brahmin > 4 meat ',
              'quarry': 'QUARRY     4 stone a day, SL  ', 'stoneyard': 'STONE YARD stone, sand > mats '}
EVENTS = {'': '', 'bandits_driven_off': '  driven off', 'bandits_took_cargo': '  bandits -%d',
          'bandits_wreck': '  WRECKED -%d', 'bandits_empty': '  nothing taken'}


class Terminal:
    """The terminal's own state (quest CCTerm): which screen is up and the Prices direction."""

    def __init__(self):
        self.screen = FRONT
        self.direction = 0          # 0: Goodsprings > Primm, 1: Primm > Goodsprings
        self.confirm = False        # WALK AWAY (or FIRE) was selected once; a second select does it
        self.pick = 0               # the staff member, candidate or standing order slot being looked at


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
        rows += [(pm.answer_label(m, i, c), '', m, i) for i in range(len(m.answers))]
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


def person_label(p):
    """'Ruth Coyle  driver s50 10/d' (31 characters at most)."""
    return '%s  %s s%d %d/d' % (p.name, p.role, p.skill, p.wage)


def staff_rows(c, t):
    """(label, action) for each Staff screen row before BACK."""
    rows = [('COVER %d on the road%s' % (c.cover(), '' if c.has_driver() else ': NO DRIVER'), None)]
    for i, p in enumerate(c.staff):
        label = ('FIRE %s? select again' % p.name) if t.confirm and t.pick == i else person_label(p)
        rows.append((label[:ROW_WIDTH], ('fire', i)))
    rows.append(('HIRE     %d asking for work' % len(c.candidates), 'hire'))
    return rows


def candidate_rows(c, t):
    """(label, result text, action) for the Candidate screen rows before BACK."""
    p = c.candidates[t.pick]
    m2 = c.tier >= 2               # M2: Nerve and the trait shown, three offers
    text = (p.rumour + (' Nerve %d.' % p.nerve if m2 else '') + (' %s.' % p.trait if p.trait else '')
            + (' Honesty: %s.' % c.honesty_band(p) if p.checked else ''))
    rows = [(person_label(p), text, None)]
    if c.can_hire(t.pick) and m2:
        for offer in ('fair', 'low', 'generous'):
            rows.append(('HIRE %s, %d a day' % (offer, max(1, p.wage + cm.OFFER_WAGE[offer])),
                         'Loyalty starts at %d.' % (cm.LOYALTY_START + cm.OFFER_LOYALTY[offer]), ('hire', offer)))
    elif c.can_hire(t.pick):
        rows.append(('HIRE for %d a day' % p.wage, '', 'hire'))
    elif len(c.staff) >= cm.STAFF_MAX:
        rows.append(('HIRE: the books are full (%d)' % cm.STAFF_MAX, '', None))
    elif c.wagons:
        rows.append(('HIRE: a driver for each wagon', '', None))
    else:
        rows.append(('HIRE: one driver is enough', '', None))
    rows.append((('HONESTY  %s' % c.honesty_band(p)) if p.checked else 'REFERENCE CHECK  %d caps' % cm.REF_CHECK,
                 '', None if p.checked else 'check'))
    return rows


def contract_row(c):
    k = c.contract
    if k is None:
        return 'CONTRACTS none running'
    import post_model as pm
    return 'CONTRACTS %s %d/%d to %s' % (pm.GOOD_NAME[k.good], k.done, k.days // k.every, k.town)


def contract_rows(c):
    """The first contract's buyer's trust, then 3 rows for each running contract (M2: up to 3; a buyer
    other than Primm is named after the price)."""
    import post_model as pm
    k = c.contract
    town = k.town if k else 'PR'
    rows = ['%s TRUST %d' % (cm.TOWN_NAME[town].upper(), c.trust[town])]
    if k is None:
        offer = any(m.kind == 'contract' for m in c.memos)
        return rows + ['An offer is waiting in Memos.' if offer else 'No contract running.']
    for k in c.contracts:
        rows += ['%s %d crates every %dd at %d%s' % (pm.GOOD_NAME[k.good].upper(), k.crates, k.every, k.price,
                                                     '' if k.town == 'PR' else ' to ' + k.town),
                 'NEXT day %d  ENDS day %d' % (k.next_due, k.start + k.days),
                 'DELIVERED %d  MISSED %d' % (k.done, k.missed)]
    return rows


def slot_label(c, i):
    o = c.standing[i]
    if o is None:
        return 'SLOT %d  empty' % (i + 1)
    if o.kind == 'keep':
        return 'SLOT %d  keep %s %d %s' % (i + 1, o.town, o.value, o.good)
    return 'SLOT %d  %s %s %d' % (i + 1, SO_LABEL[o.kind], o.good, o.value)


def slot_rows(c, t):
    o = c.standing[t.pick]
    kind = o.kind if o else None
    rows = ['KIND   %s' % SO_LABEL[kind]]
    if o:
        rows += ['TOWN   %s' % o.town if kind == 'keep' else 'TOWN   any',
                 'GOOD   %s' % o.good,
                 'MORE   %s %d' % ('crates' if kind == 'keep' else 'price', o.value),
                 'LESS']
    return rows


def slot_click(c, t, row):
    o = c.standing[t.pick]
    if row == 0:
        kind = SO_KIND_CYCLE[(SO_KIND_CYCLE.index(o.kind if o else None) + 1) % len(SO_KIND_CYCLE)]
        c.set_order(t.pick, kind, o.town if o else 'PR', o.good if o else 'water')
        return
    if o is None:
        return
    step = 1 if o.kind == 'keep' else PRICE_STEP
    if row == 1 and o.kind == 'keep':
        o.town = 'GS' if o.town == 'PR' else 'PR'
    elif row == 2:
        o.good = GOODS[(GOODS.index(o.good) + 1) % len(GOODS)]
        if o.kind != 'keep':
            o.value = cm.ANCHOR[o.good]
    elif row == 3:
        o.value = min(o.value + step, cm.CRATES_PER_LEG if o.kind == 'keep' else 995)
    elif row == 4:
        o.value = max(o.value - step, 1 if o.kind == 'keep' else 5)


def chains_row(c):
    if c.tier < 2:
        return 'CHAINS   none yet (tier 2)'
    open_ = [b for b in cm.BUILD_ROWS if cm.BUILD_TIER[b] <= c.tier]
    return 'CHAINS   %d of %d built' % (sum(c.built(b) for b in open_), len(open_))


def towns_row(c):
    liked = sum(1 for t in cm.TOWNS if c.trust[t] >= cm.TIER3_TRUST)
    if c.tier >= 3:                     # M3: heat and NCR standing (the front page has no room left)
        return 'TOWNS    %d trusted, heat %d, NCR %d' % (liked, c.heat, c.ncr_standing)
    return 'TOWNS    %d trusted, managers %d of 2' % (liked, len(c.managers))


def law_rows(c):
    """M3 (tier 3): the rival, the back room, Crimson Cover and the NCR, under the Towns screen's sell rows."""
    if c.tier < 3:
        return []
    war = ('  war %s to day %d' % (c.war_town, c.war_until)) if c.war_town and c.day <= c.war_until else ''
    on = {True: 'ON', False: 'OFF'}
    return ['RIVAL    anger %d%s' % (c.aggr, war),
            'DECLARE  %d%% of sales (select)' % round(100 * (1 - law.HIDE[c.hide])),
            'SEALED   crates %s, %d a run' % (on[c.sealed], law.SEALED_PAY),
            'COVER    Crimson Cover %s, %d a wagon' % (on[c.insured], law.COVER_PREMIUM),
            'NCR      standing %d, inspect day %d' % (c.ncr_standing, c.inspect_next)]


LAW_CLICK = {1: 'cycle_hide', 2: 'toggle_sealed', 3: 'toggle_cover'}


def wagon_rows(c):
    """The M2 Wagons screen (tier 2): wagon 1 as in M1, then a row for the Sloan road and the Outpost road:
    its wagon (runs or idle), BUY one, or the tier that opens it."""
    rows = [('WAGON 1  home  cover %d' % c.cover() if c.has_driver() else 'WAGON 1  home  NO DRIVER')
            if c.wagon_ok else 'WAGON 1  none: BUY one for %d' % (cm.WAGON + cm.BRAHMIN_PAIR)]
    running = [road for _, road in c.running_roads()]
    for road in (2, 3):
        name = pm.ROAD_NAME[road]
        mine = [i for i, w in enumerate(c.wagons) if w.road == road]
        if mine:
            rows.append('WAGON %d  %s  %s' % (mine[0] + 2, name, 'runs' if road in running else 'idle'))
        elif c.tier < cm.ROAD_TIER[road]:
            rows.append('%s  opens at tier %d' % (name.upper(), cm.ROAD_TIER[road]))
        else:
            rows.append('%s  BUY a wagon for %d' % (name.upper(), cm.WAGON + cm.BRAHMIN_PAIR))
    return rows


def town_rows(c):
    return ['%-15s %-8s trust %d' % (cm.TOWN_NAME[t], cm.LEVELS[c.level[t]], c.trust[t]) for t in cm.TOWNS]


MANAGER_LABEL = {'bookkeeper': 'BOOKKEEPER', 'route': 'ROUTE MGR '}


def manager_rows(c):
    """One row a manager: the policy (select: the next one), HIRE at 40 a day, or the tier that opens it."""
    rows = []
    for kind in cm.MANAGERS:
        if kind in c.managers:
            rows.append('%s  %s  (select: change)' % (MANAGER_LABEL[kind], c.managers[kind]))
        elif c.tier < cm.MANAGERS[kind]:
            rows.append('%s  opens at tier %d' % (MANAGER_LABEL[kind], cm.MANAGERS[kind]))
        else:
            rows.append('%s  HIRE, %d a day' % (MANAGER_LABEL[kind], cm.MANAGER_WAGE))
    return rows


SELL_NAME = {'water': 'purified water', 'powder': 'healing powder'}


def sell_rows(c):
    """The tier 2 perk: sell the company a crate (10 bottles or 10 powders) at 0.8 of the anchor."""
    if c.tier < 2:
        return []
    rows = []
    for g, n in cm.BUY_FROM_PLAYER.items():
        left = cm.BUY_DAY_MAX - (c.bought_today if c.bought_day == c.day else 0)
        rows.append('SELL %d %s: %d (%d left)' % (n, SELL_NAME[g], c.buy_price_from_player(g), left))
    return rows


def sell_click(c, good):
    if c.carried[good] >= cm.BUY_FROM_PLAYER[good] and c.buy_from_player(good, 1):
        c.carried[good] -= cm.BUY_FROM_PLAYER[good]


def manager_click(c, kind):
    """Hire with the middle policy (Normal, Balanced); once hired, each select moves to the next policy."""
    pols = cm.POLICIES[kind]
    if kind in c.managers:
        c.set_policy(kind, pols[(pols.index(c.managers[kind]) + 1) % len(pols)])
    else:
        c.hire_manager(kind, pols[1])


def build_rows(c):
    """The Build screen: money first, then a row per building (its cost, or BUILT), then BACK. Before
    tier 2 it shows what tier 2 needs instead."""
    if c.tier < 2:
        strikes = len(c.recent_strikes())
        return ['TIER 2 (Outfit) NEEDS ALL OF THESE:',
                'WORTH    %d of %d earned' % (c.earned_worth(), cm.TIER2_WORTH),
                'TRUST    Goodsprings %d of %d' % (c.trust['GS'], cm.TIER2_TRUST),
                'DEED     Ghost Town Gunfight: %s' % ('done' if c.ghost_town_done else 'not yet'),
                'STRIKES  %d in 56 days (needs 0)' % strikes,
                'BACK']
    rows = ['MONEY  cash %d, own money %d' % (c.cash, c.owner_funds)]
    for b in cm.BUILD_ROWS:
        if c.built(b):
            state = 'BUILT'
        elif cm.BUILD_TIER[b] > c.tier:
            state = 'tier %d' % cm.BUILD_TIER[b]
        elif cm.BUILD_DEED.get(b) and cm.BUILD_DEED[b] not in c.deeds:
            state = 'deed'
        else:
            state = '%d' % c.build_cost(b)
        rows.append('%s %s' % (BUILD_TEXT[b], state))
    return rows + ['BACK']


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
    if c.founded and not c.ended and t.screen == CANDIDATE:
        return [row[1] for row in candidate_rows(c, t)] + ['']
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
                chains_row(c),
                'STAFF    %d on the books, cover %d' % (len(c.staff) + c.hands, c.cover()),
                contract_row(c),
                'LEDGER   loan %d, week sales %d' % (c.loan, c.week_sales),
                'ORDERS   %d pending (apply at 06:00)' % len(c.queue_list),
                'SETTINGS',
                notice_row(c)]
        if c.tier >= 2:
            rows.append(towns_row(c))
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
                'STANDING ORDERS  %d of %d set' % (sum(1 for o in c.standing if o), cm.SLOTS),
                'BACK']
    if t.screen == ROUTES and c.tier >= 2:
        rows = wagon_rows(c)
        for r in c.history[-3:][::-1]:
            ev = EVENTS[r.event] % r.event_loss if '%' in EVENTS[r.event] else EVENTS[r.event]
            rows.append('DAY %d  net %d%s' % (r.day, r.margin, ev))
        return rows + ['BACK']
    if t.screen == ROUTES:
        rows = [('WAGON 1  home  cover %d' % c.cover() if c.has_driver() else 'WAGON 1  home  NO DRIVER')
                if c.wagon_ok else
                'WAGON 1  none: BUY one for %d' % (cm.WAGON + cm.BRAHMIN_PAIR)]
        for r in c.history[-3:][::-1]:
            ev = EVENTS[r.event] % r.event_loss if '%' in EVENTS[r.event] else EVENTS[r.event]
            rows.append('DAY %d  net %d%s' % (r.day, r.margin, ev))
        return rows + ['BACK']
    if t.screen == TOWNS_SCREEN:
        return town_rows(c) + manager_rows(c) + sell_rows(c) + law_rows(c) + ['BACK']
    if t.screen == SETTINGS:
        return ['PLAN EVERY DAY   %s' % ('ON' if c.auto else 'OFF'), 'BACK']
    if t.screen == POST:
        return [label for label, _ in post_rows(c)] + ['BACK']
    if t.screen == MEMOS:
        return [row[0] for row in memo_rows(c)] + ['BACK']
    if t.screen == NOTICE:
        return [row[0] for row in notice_rows(c, t)] + ['BACK']
    if t.screen == STAFF:
        return [row[0] for row in staff_rows(c, t)] + ['BACK']
    if t.screen == HIRE:
        return [person_label(p) for p in c.candidates] + ['BACK']
    if t.screen == CANDIDATE:
        return [row[0] for row in candidate_rows(c, t)] + ['BACK']
    if t.screen == CONTRACTS:
        return contract_rows(c) + ['BACK']
    if t.screen == STANDING:
        return [slot_label(c, i) for i in range(cm.SLOTS)] + ['BACK']
    if t.screen == BUILD:
        return build_rows(c)
    if t.screen == SLOT:
        return slot_rows(c, t) + ['BACK']
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
            t.screen = {2: POST, 3: MEMOS, 4: ROUTES, 5: PRICES, 7: STAFF, 8: CONTRACTS, 9: LEDGER,
                        10: ORDERS, 11: SETTINGS, 12: NOTICE, 13: TOWNS_SCREEN}.get(row, FRONT)
            if row == 6:
                t.screen = BUILD
        return
    if row == len(rows) - 1:                    # BACK is always the last row
        t.screen = PARENT.get(t.screen, FRONT)
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
        elif row == 4:
            t.screen = STANDING
    elif t.screen == STANDING:
        t.pick, t.screen = row, SLOT
    elif t.screen == SLOT:
        slot_click(c, t, row)
    elif t.screen == BUILD:
        if 1 <= row <= len(cm.BUILD_ROWS) and c.can_build(cm.BUILD_ROWS[row - 1]):
            c.build(cm.BUILD_ROWS[row - 1])
    elif t.screen == STAFF:
        act = staff_rows(c, t)[row][1]
        if act == 'hire':
            t.screen = HIRE
        elif act:
            if confirm and t.pick == act[1]:
                c.fire(act[1])
            else:
                t.pick, t.confirm = act[1], True
    elif t.screen == HIRE:
        t.pick, t.screen = row, CANDIDATE
    elif t.screen == CANDIDATE:
        act = candidate_rows(c, t)[row][2]
        if act == 'hire' or (act and act[0] == 'hire'):
            c.hire(t.pick, 'fair' if act == 'hire' else act[1])
            t.screen = HIRE
        elif act == 'check':
            c.reference_check(t.pick)
    elif t.screen == ROUTES and row == 0:
        c.buy_wagon()
    elif t.screen == ROUTES and c.tier >= 2 and row in (1, 2):
        c.buy_road(row + 1)
    elif t.screen == TOWNS_SCREEN and row >= len(cm.TOWNS):
        k = row - len(cm.TOWNS)
        if k < len(cm.MANAGERS):
            manager_click(c, list(cm.MANAGERS)[k])
        elif k < len(cm.MANAGERS) + len(sell_rows(c)):
            sell_click(c, list(cm.BUY_FROM_PLAYER)[k - len(cm.MANAGERS)])
        elif k - len(cm.MANAGERS) - len(sell_rows(c)) in LAW_CLICK:
            getattr(c, LAW_CLICK[k - len(cm.MANAGERS) - len(sell_rows(c))])()
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

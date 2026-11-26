"""M4 model: the late game (docs/plans/2026-11-28-m4-ending.md, "My calls (M4)").

A mixin for company_model.Company, like law_model.LawMixin. Forward contracts start at tier 3; the
NCR quartermaster and lending at tier 4; share blocks from tier 4; laws and the ending at tier 5.

Each tick, in Company.tick's order:
  settle memos      a forward ticket accepted (with or without an advance), the quartermaster's deal,
                    a loan to an outfit, a failed outfit seized or forgiven
  the legs          crates of a ticket's good carried into its town go to the ticket first
  bills (day 7k)    the quartermaster's interest and repayment
  the week (7k)     the outfits' instalments, the quartermaster's string, leading Primm
  the day           a ticket missed on its due day
  tier check        tier 5
  the post          the forward offer (day 2 of a week), the quartermaster's offer, an outfit's ask
"""

# --- forward contracts (design: Forward contracts) -------------------------------------------------
FWD_WEEKDAY, FWD_CRATES, FWD_DAYS, FWD_OPEN = 2, 12, 10, 3
FWD_MISS, FWD_ADVANCE = 0.25, 0.5
FWD_PREMIUM = 1.1                         # a ticket pays 10% over the normal sell price
FWD_DONE_TRUST, FWD_MISS_TRUST = 3, -5

# --- the NCR quartermaster (design: Patrons with strings) -------------------------------------------
QM_STANDING, QM_LOAN, QM_RATE, QM_REPAY = 60, 10000, 0.02, 500
QM_HEAT, QM_BROKEN_STANDING, QM_KEPT_DAYS = 20, -30, 28

# --- lending (design: Lending: you become Alice) ------------------------------------------------------
LEND_EVERY, LEND_WEEKDAY, LEND_WEEKS, LEND_OPEN = 14, 4, 8, 2
LEND_AMOUNTS = (1000, 2000, 3000)
LEND_RATES = (0.02, 0.04, 0.08)          # gentle, fair, harsh
LEND_MISS = (10, 20, 35)                 # in 100, a week
LEND_FAILS = 2                           # misses in a row
SEIZE_SHARE, SEIZE_TRUST, FORGIVE_TRUST, LEND_AGGR = 0.5, -10, 10, 5
OUTFITS = (('Harlan Freight', 'GS'), ('Primm Haulers', 'PR'), ('Sloan Stone Co.', 'SL'), ('Outpost Supply', 'MO'))

# --- tier 5 and the end of the rivalry ------------------------------------------------------------------
TIER5_WORTH, LEAD_TOWNS = 80000, 3
HER_SHARE = {'GS': 0.10, 'PR': 0.12, 'SL': 0.10, 'MO': 0.15}
BLOCK_PRICE = (5000, 10000, 15000)
LEAD_WEEKS = 2                           # lead her in Primm 14 days in a row (two bill days)

# --- laws (tier 5) -----------------------------------------------------------------------------------------
LAW_COST, LAW_EVERY = 5, 28
LAWS = ('duty', 'licence', 'audit')      # Free trade act (duty halved), Carrier act (no licence), Press audit
AUDIT_AGGR = -20

ROLL_FWD, ROLL_LEND, ROLL_MISS = 8, 9, 10    # roll keys (1-7 are M1 to M3's)


def _cm():
    import company_model
    return company_model


class Ticket:
    """A forward contract: `crates` of `good` into `town` by day `due` at `price` a crate."""

    def __init__(self, town, good, price, start, due, advance=0):
        self.town, self.good, self.price = town, good, price
        self.start, self.due = start, due
        self.crates, self.filled = FWD_CRATES, 0
        self.advance = advance           # the part of the advance not yet earned back

    def value(self):
        return self.crates * self.price


class Outfit:
    def __init__(self, name, town, amount, rate):
        self.name, self.town = name, town
        self.amount, self.rate = amount, rate
        self.left = amount               # principal still owed
        self.weeks = LEND_WEEKS
        self.misses = 0


class LateMixin:
    def _late_init(self):
        self.tickets = []
        self.last_fwd = -99
        self.qm, self.qm_offered, self.qm_loan, self.qm_since = False, False, 0, 0
        self.outfits = []
        self.lent_ever = False
        self.seized_n, self.forgiven_n = 0, 0  # failed outfits (the ending)
        self.last_lend = -99
        self.favour, self.laws, self.last_law = 0, [], -99
        self.blocks, self.lead_pr_weeks, self.won_vs_her, self.rival_out = 0, 0, False, False
        self.side = ''                   # the side taken at the Dam (the ending only): NCR, House, Legion, Independent
        self.ending = None               # the three closing pages, once written

    # --- debts the late game adds to net worth --------------------------------------------------------
    def late_debt(self):
        return self.qm_loan + sum(t.advance for t in self.tickets)

    # --- forward contracts -------------------------------------------------------------------------------
    def _fwd_take(self, r, dest, g):
        """A crate of g carried into dest: to the first open ticket for it, paid at the ticket's price
        (the part still owed on its advance is kept back). Returns True when the ticket took it."""
        t = next((x for x in self.tickets if x.town == dest and x.good == g and x.filled < x.crates), None)
        if t is None:
            return False
        t.filled += 1
        back = min(t.advance, t.price)
        t.advance -= back
        pay = t.price - back
        self.cash += pay
        r.sales += pay
        self.week_sales += pay
        self.sold_week[dest] += 1
        r.fwd_crates += 1
        if t.filled == t.crates:
            self.trust[dest] = min(100, self.trust[dest] + FWD_DONE_TRUST)
            self.tickets.remove(t)
            r.fwd = 'filled'
        return True

    def fwd_offer(self):
        """(town, good) for this week's forward offer: a market good of a town on a running road, not
        under a ticket, picked by the seeded roll among them in a fixed order."""
        towns = []
        for _, road in self.running_roads():
            for t in _cm().ROADS[road]:
                if t not in towns:
                    towns.append(t)
        def source(t, g):            # a running road's other end sells it for less than the ticket pays
            return any(t in _cm().ROADS[road] and self.has_market(o, g)
                       and self.price(o, g, 'buy', self.normal[o][g]) < self.fwd_price(t, g)
                       for _, road in self.running_roads() for o in _cm().ROADS[road] if o != t)
        cands = [(t, g) for t in _cm().TOWNS if t in towns for g in _cm().GOODS + ('meat',)
                 if self.has_market(t, g) and source(t, g)
                 and not any(x.town == t and x.good == g for x in self.tickets)]
        if not cands:
            return None
        return cands[_cm().roll(self.seed, self.day, ROLL_FWD) % len(cands)]

    def fwd_price(self, town, good):
        return _cm().half_up(FWD_PREMIUM * self.price(town, good, 'sell', self.normal[town][good]))

    def _post_fwd(self, r):
        if (self.tier >= 3 and self.stage == 'ok' and len(self.tickets) < FWD_OPEN
                and self.day % 7 == FWD_WEEKDAY and self.day - self.last_fwd >= 7
                and not any(m.kind == 'forward' for m in self.memos)):
            offer = self.fwd_offer()
            if offer is None:
                return
            town, good = offer
            price = self.fwd_price(town, good)
            if self.post_memo(_cm().Memo('forward', self.day, self.day + 1, price=price, town=town, good=good)):
                self.last_fwd = self.day

    def _settle_fwd(self, r, m, a):
        if a == 2:
            return
        adv = _cm().half_up(FWD_ADVANCE * FWD_CRATES * m.price) if a == 1 else 0
        self.tickets.append(Ticket(m.town, m.good, m.price, self.day, self.day + FWD_DAYS, adv))
        self.cash += adv
        r.fwd = 'signed'
        r.fwd_adv = adv

    def _day_fwd(self, r):
        for t in [x for x in self.tickets if self.day >= x.due]:
            unfilled = (t.crates - t.filled) * t.price
            pay = min(self.cash, _cm().half_up(FWD_MISS * unfilled))
            self.cash -= pay
            r.costs += pay
            self.arrears += t.advance
            self.trust[t.town] = max(0, self.trust[t.town] + FWD_MISS_TRUST)
            self.tickets.remove(t)
            r.fwd, r.fwd_pay = 'missed', pay

    # --- the quartermaster ----------------------------------------------------------------------------------
    def _post_qm(self, r):
        if (self.tier >= 4 and not self.qm_offered and self.ncr_standing >= QM_STANDING and not self.outlaw
                and not any(m.kind == 'patron' for m in self.memos)):
            if self.post_memo(_cm().Memo('patron', self.day, self.day + 3, price=QM_LOAN)):
                self.qm_offered = True

    def _settle_qm(self, r, a):
        if a == 0:
            self.qm, self.qm_loan, self.qm_since = True, QM_LOAN, self.day
            self.cash += QM_LOAN
            r.patron = 'signed'

    def qm_bill(self):
        """The quartermaster's weekly bill: interest and a repayment (0 without his loan)."""
        if not self.qm_loan:
            return 0, 0
        return _cm().half_up(QM_RATE * self.qm_loan), min(QM_REPAY, self.qm_loan)

    def _qm_paid(self, take):
        """`take` of this week's patron bill was paid: interest first, the rest repays his loan."""
        interest, _ = self.qm_bill()
        self.qm_loan -= max(0, take - interest)

    def _qm_string(self, r):
        if self.qm and (self.heat >= QM_HEAT or self.outlaw):
            self.qm = False
            self.arrears += self.qm_loan
            self.qm_loan = 0
            self.ncr_standing = max(0, self.ncr_standing + QM_BROKEN_STANDING)
            r.patron = 'broken'

    def patron_kept(self):
        return self.qm and self.day - self.qm_since >= QM_KEPT_DAYS

    # --- lending ------------------------------------------------------------------------------------------------
    def _post_lend(self, r):
        if (self.tier >= 4 and len(self.outfits) < LEND_OPEN and self.day % 7 == LEND_WEEKDAY
                and self.day - self.last_lend >= LEND_EVERY and not any(m.kind == 'lend' for m in self.memos)):
            free = [o for o in OUTFITS if not any(x.name == o[0] for x in self.outfits)]
            k = _cm().roll(self.seed, self.day, ROLL_LEND)
            name, town = free[k % len(free)]
            amount = LEND_AMOUNTS[k % len(LEND_AMOUNTS)]
            if self.post_memo(_cm().Memo('lend', self.day, self.day + 2, price=amount, town=town, who=name)):
                self.last_lend = self.day

    def _settle_lend(self, r, m, a):
        if a == 3 or self.cash < m.price:
            return
        self.cash -= m.price
        self.outfits.append(Outfit(m.who, m.town, m.price, a))
        if not self.lent_ever:
            self.lent_ever = True
            self.aggr = min(100, self.aggr + LEND_AGGR)
        r.lent = m.price

    def _week_lend(self, r):
        for i, o in enumerate(list(self.outfits)):
            if _cm().roll(self.seed, self.day, ROLL_MISS + i) < LEND_MISS[o.rate]:
                o.misses += 1
                r.outfit_miss += 1
                if o.misses >= LEND_FAILS and not any(m.kind == 'outfit' and m.who == o.name for m in self.memos):
                    self.post_memo(_cm().Memo('outfit', self.day, self.day + 3, price=o.left, town=o.town, who=o.name))
                continue
            o.misses = 0
            part = min(o.left, _cm().half_up(o.amount / LEND_WEEKS))
            interest = _cm().half_up(LEND_RATES[o.rate] * o.left)
            o.left -= part
            o.weeks -= 1
            self.cash += part + interest
            r.sales += interest
            r.lend_in += part + interest
            if o.left <= 0 or o.weeks <= 0:
                self.outfits.remove(o)

    def _settle_outfit(self, r, m, a):
        o = next((x for x in self.outfits if x.name == m.who), None)
        if o is None:
            return
        self.outfits.remove(o)
        if a == 0:
            got = min(o.left, _cm().half_up(SEIZE_SHARE * o.amount))
            self.cash += got
            self.trust[o.town] = max(0, self.trust[o.town] + SEIZE_TRUST)
            r.outfit, r.outfit_got = 'seized', got
            self.seized_n += 1
        else:
            self.trust[o.town] = min(100, self.trust[o.town] + FORGIVE_TRUST)
            r.outfit = 'forgiven'
            self.forgiven_n += 1

    # --- leading her, share blocks, tier 5 -----------------------------------------------------------------------
    def lead_towns(self):
        return [t for t in _cm().TOWNS if self.last_share.get(t, 0) > HER_SHARE[t]]

    def _week_lead(self, r):
        self.lead_pr_weeks = self.lead_pr_weeks + 1 if 'PR' in self.lead_towns() else 0

    def block_ready(self):
        """The next share block's deed is done (blocks are bought in order)."""
        if self.tier < 4 or self.rival_out or self.blocks >= 3:
            return False
        return (self.lead_pr_weeks >= LEAD_WEEKS, self.won_vs_her, self.blocks >= 2)[self.blocks]

    def buy_block(self):
        if not self.block_ready() or self.cash < BLOCK_PRICE[self.blocks]:
            return False
        self.cash -= BLOCK_PRICE[self.blocks]
        self.assets += BLOCK_PRICE[self.blocks]
        self.blocks += 1
        if self.blocks == 3:
            self.rival_out = True
            self.aggr = 0
        return True

    def tier_five_ready(self):
        return (self.tier == 4 and self.earned_worth() >= TIER5_WORTH and len(self.lead_towns()) >= LEAD_TOWNS
                and (self.blocks == 3 or self.patron_kept()) and not self.outlaw and not self.recent_strikes())

    # --- laws ------------------------------------------------------------------------------------------------------
    def next_law(self):
        return next((x for x in LAWS if x not in self.laws), None)

    def pass_law(self):
        law = self.next_law()
        if (self.tier < 5 or law is None or self.favour < LAW_COST or self.day - self.last_law < LAW_EVERY
                or self.ended):
            return False
        self.favour -= LAW_COST
        self.last_law = self.day
        self.laws.append(law)
        if law == 'audit':
            self.aggr = max(0, self.aggr + AUDIT_AGGR)
        return True

    def law_duty(self, d):
        """The week's NCR duty after the Free trade act (halved, rounded half up)."""
        return _cm().half_up(d / 2) if 'duty' in self.laws else d

    # --- the tick's hooks -----------------------------------------------------------------------------------------
    def _settle_late(self, r, m, a):
        if m.kind == 'forward':
            self._settle_fwd(r, m, a)
        elif m.kind == 'patron':
            self._settle_qm(r, a)
        elif m.kind == 'lend':
            self._settle_lend(r, m, a)
        elif m.kind == 'outfit':
            self._settle_outfit(r, m, a)

    def _week_late(self, r):
        self._week_lend(r)
        if self.tier >= 4:
            self._qm_string(r)
            self._week_lead(r)

    def _post_late(self, r):
        self._post_fwd(r)
        self._post_qm(r)
        self._post_lend(r)

    # --- the ending ----------------------------------------------------------------------------------------------------
    def retire(self):
        if self.tier < 5 or self.ended:
            return False
        self._end(None, 'retired')
        self.post = (self.post + [_cm().Letter(self.day, 'closed', ('retired',))] + self.ending_letters()
                     )[-_cm().POST_KEEP:]
        return True

    def ending_letters(self):
        """The three closing pages as Post letters (title, lines)."""
        return [_cm().Letter(self.day, 'ending', page) for page in (self.ending or [])]

    def _write_ending(self):
        import ending_model
        if self.ending is None:
            self.ending = ending_model.pages(self)

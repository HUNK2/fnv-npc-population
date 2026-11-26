"""M3 model: the rival and the law (docs/plans/2026-11-28-m3-rival-law.md, "My calls (M3)").

A mixin for company_model.Company. Everything here starts at tier 3 (the Caravan company), so the M1
and M2 numbers are unchanged below it; the licence and duty were already in M1's weekly bills.

Each tick, in Company.tick's order:
  settle memos      an NCR bid is won or lost; a warrant memo is bribed away or the raid runs
  the roads         the Outpost toll on road 3 (free at tier 4); a sealed-crate run on road 1 (every
                    3 days at most, when set); an insured road loss is paid back 60% the same day
  bills (day 7k)    duty on the declared share of sales, the licence by tier, the cover premium
  the week (7k)     shares, aggression, the rival's one move (price war or a poach warning), NCR
                    standing +1 for bills paid
  the law (daily)   a poach that was warned, heat, an inspection when due, a warrant at heat 80
  tier check        tier 4: worth, loan repaid, licence paid, NCR standing 50, an NCR contract done
  the post          the NCR offer (one a week) as a memo
"""

# --- the rival (design: The Crimson Caravan) -----------------------------------------------------
AGGR_START = 20
SHARE_HIGH, SHARE_LOW = 0.25, 0.05       # a week's share of a town's use, the company's crates only
AGGR_HIGH, AGGR_LOW, AGGR_WIN = 10, -5, 5
MOVE_AGGR = 30                           # price war and poach from aggression 30
WAR_DAYS, WAR_CUT, WAR_CUT_COVERED = 5, 0.15, 0.20   # Crimson Cover gives her your manifests
POACH_LOYALTY = 40

# --- the NCR (design: The NCR, the law and the dodgy side) ---------------------------------------
STANDING_START = 30
LICENCE_TIER = {0: 150, 1: 150, 2: 150, 3: 400, 4: 900}
TOLL, TOLL_ROAD = 20, 3
INSPECT_EVERY, INSPECT_NOTICED, NOTICED_HEAT = 30, 10, 20
FAULT_STANDING, FINE_SHARE = -5, 0.05
DUTY_STANDING, NCR_STANDING = 1, 2
NCR_TOWN, NCR_GOOD, NCR_ROAD = 'MO', 'ammo', 3
NCR_CRATES, NCR_EVERY, NCR_DAYS = 4, 3, 14
NCR_HIGH, NCR_LOW = 1.3, 1.2             # the company's two bids; the Caravan bids 1.25 ...
CRIMSON_BIDS = 40                        # ... once her aggression is 40, so only the low bid wins then
NCR_WEEKDAY = 5
FREEZE_HEAT = 60

# --- the back room and heat ----------------------------------------------------------------------
HIDE = (0.0, 0.1, 0.2)                   # declare 100, 90 or 80% of sales
HIDE_HEAT = 2                            # a week, per 10% hidden
SEALED_PAY, SEALED_EVERY, SEALED_HEAT = 50, 3, 5
SEARCH_CHANCE, SEARCH_FINE, SEARCH_HEAT = 10, 100, 10
HEAT_FALL, HEAT_FALL_CLEAN, CLEAN_DAYS = 1, 2, 7
WARRANT_HEAT, RAID_DAYS, RAID_REST, REVOKE_DAYS = 80, 7, 7, 28
RAID_STRENGTH, RAID_HEAT, RAID_SEIZE = 60, 50, 0.2
FIXER = 300                              # the warrant memo: pay a fixer to lose the papers

# --- insurance -------------------------------------------------------------------------------------
COVER_PREMIUM, COVER_PAYS = 40, 0.6      # a running wagon a week; 60% of a road loss

TIER4_WORTH, TIER4_STANDING = 40000, 50

ROLL_SEARCH = 7                          # roll keys 1-5, 20-90 are M1/M2's


def _cm():
    import company_model
    return company_model


class LawMixin:
    def _law_init(self):
        self.heat, self.clean_days = 0, 0
        self.heat_gain = 0
        self.aggr = AGGR_START
        self.ncr_standing = STANDING_START
        self.sold_week = {t: 0 for t in ('GS', 'PR', 'SL', 'MO')}
        self.last_share = {t: 0.0 for t in self.sold_week}
        self.war_town, self.war_until = None, 0
        self.poach_name, self.poach_day = '', 0
        self.hide = 0                    # index into HIDE
        self.sealed = False
        self.sealed_last = -99
        self.hidden_since = 0            # caps hidden from duty since the last inspection
        self.faults = 0
        self.inspect_next = 0            # set on the tier 3 day
        self.insured = False
        self.outlaw = False
        self.raid_last = -99             # a raid (or a bribed warrant): no warrant for 7 days after
        self.raids = []                  # days of real raids (paper)
        self.ncr_done = 0                # NCR contract deliveries
        self.last_ncr_offer = -99

    # --- prices --------------------------------------------------------------------------------------
    def war_cut(self, town):
        if self.war_town == town and self.day <= self.war_until:
            return WAR_CUT_COVERED if self.insured else WAR_CUT
        return 0.0

    # --- the roads -----------------------------------------------------------------------------------
    def _toll(self, r, road):
        if road == TOLL_ROAD and self.tier < 4:
            pay = min(TOLL, self.cash)
            self.cash -= pay
            r.costs += pay
            r.toll += pay

    def _sealed_run(self, r, road):
        """Road 1's wagon carries a sealed crate when set, at most every 3 days (tier 3)."""
        if road != 1 or not self.sealed or self.tier < 3 or self.day - self.sealed_last < SEALED_EVERY:
            return
        self.sealed_last = self.day
        self.cash += SEALED_PAY
        r.sales += SEALED_PAY                    # not declared: it never reaches week_sales
        self.heat_gain += SEALED_HEAT
        r.sealed = 1
        if _cm().roll(self.seed, self.day, ROLL_SEARCH) < SEARCH_CHANCE:
            pay = min(SEARCH_FINE, self.cash)
            self.cash -= pay
            r.costs += pay
            self.heat_gain += SEARCH_HEAT
            r.sealed = 2
            r.notes.append('a patrol searched the wagon: fined %d' % pay)

    def _claim(self, r, loss):
        if self.insured and loss > 0:
            pay = _cm().half_up(COVER_PAYS * loss)
            self.cash += pay
            r.sales += pay
            r.claim = pay

    # --- bills -----------------------------------------------------------------------------------------
    def licence_fee(self):
        return LICENCE_TIER[min(self.tier, 4)]

    def declared(self, sales):
        """(declared, hidden) of a week's sales."""
        hidden = _cm().half_up(HIDE[self.hide] * sales)
        return sales - hidden, hidden

    def premium(self):
        return COVER_PREMIUM * len(self.running_roads()) if self.insured else 0

    # --- the week ----------------------------------------------------------------------------------------
    def town_use(self, t):
        return sum(self.use[t].values())

    def shares(self):
        return {t: self.sold_week[t] / (7 * self.town_use(t)) for t in self.sold_week}

    def _week_law(self, r):
        if self.tier >= 3:
            if r.bills_paid:
                self.ncr_standing = min(100, self.ncr_standing + DUTY_STANDING)
            sh = self.shares()
            top = max(sh, key=lambda t: (sh[t], -('GS', 'PR', 'SL', 'MO').index(t)))
            if sh[top] > SHARE_HIGH and sh[top] > self.last_share[top]:      # over 25% and rising
                self.aggr = min(100, self.aggr + AGGR_HIGH)
            elif sh[top] < SHARE_LOW:
                self.aggr = max(0, self.aggr + AGGR_LOW)
            if self.aggr >= MOVE_AGGR:
                if sh[top] > SHARE_HIGH and self.day > self.war_until:
                    self.war_town, self.war_until = top, self.day + WAR_DAYS
                    r.rival, r.who = 'war', top
                    r.notes.append('rival: price war in %s' % top)
                else:
                    low = [p for p in self.staff if p.loyalty < POACH_LOYALTY]
                    if low:
                        p = min(low, key=lambda x: x.loyalty)
                        self.poach_name, self.poach_day = p.name, self.day + 1
                        r.rival, r.who = 'poach', p.name
                        r.notes.append('rival: Alice is courting %s' % p.name)
            self.last_share = sh
        self.sold_week = {t: 0 for t in self.sold_week}

    # --- the law, daily ---------------------------------------------------------------------------------
    def _day_law(self, r):
        d = self.day
        if self.poach_name and d >= self.poach_day:
            p = next((x for x in self.staff if x.name == self.poach_name), None)
            if p is not None and p.loyalty < POACH_LOYALTY:
                self.staff.remove(p)
                r.notes.append('%s left for the Crimson Caravan' % p.name)
                r.rival, r.who = 'poached', p.name
            self.poach_name = ''
        if self.heat_gain > 0:
            self.heat = min(100, self.heat + self.heat_gain)
            self.clean_days = 0
        else:
            self.clean_days += 1
            self.heat = max(0, self.heat - (HEAT_FALL_CLEAN if self.clean_days >= CLEAN_DAYS else HEAT_FALL))
        self.heat_gain = 0
        if self.tier < 3:
            return
        if d >= self.inspect_next:
            self._inspect(r)
        if (self.heat >= WARRANT_HEAT and d - self.raid_last >= RAID_REST
                and not any(m.kind == 'warrant' for m in self.memos)):
            if self.post_memo(_cm().Memo('warrant', d, d + RAID_DAYS)):
                r.notes.append('a warrant was served')
                r.warrant = True

    def _inspect(self, r):
        fault = self.hidden_since > 0 or self.arrears > 0
        if fault:
            self.faults += 1
            self.ncr_standing = max(0, self.ncr_standing + FAULT_STANDING)
            if self.faults > 1:
                week = sum(h.sales for h in self.history[-6:]) + r.sales
                pay = min(self.cash, _cm().half_up(FINE_SHARE * week))
                self.cash -= pay
                r.costs += pay
                r.fine = pay
        r.inspected = 2 if fault else 1
        self.hidden_since = 0
        self.inspect_next = self.day + (INSPECT_NOTICED if self.heat >= NOTICED_HEAT else INSPECT_EVERY)

    def _raid(self, r):
        """On paper: guard cover against raid strength 60. A second raid within 28 days revokes the licence."""
        d = self.day
        if self.cover() >= RAID_STRENGTH:
            self.outlaw = True
            self.ncr_standing = 0
            r.raid = 'won'
        else:
            pay = _cm().half_up(RAID_SEIZE * self.cash)
            self.cash -= pay
            r.costs += pay
            r.raid, r.raid_loss = 'seized', pay
        second = any(d - x <= REVOKE_DAYS for x in self.raids)
        self.raids.append(d)
        self.heat = RAID_HEAT
        self.raid_last = d
        if second:
            self._end(r, 'revoked')

    def _settle_warrant(self, r, a):
        if a == 0 and self.cash >= FIXER:
            self.cash -= FIXER
            r.costs += FIXER
            self.heat = RAID_HEAT
            self.raid_last = self.day
            r.raid = 'bribed'
        else:
            self._raid(r)

    # --- NCR contracts -----------------------------------------------------------------------------------
    def ncr_base(self):
        return self.price(NCR_TOWN, NCR_GOOD, 'sell', self.normal[NCR_TOWN][NCR_GOOD])

    def ncr_bids(self, base):
        hu = _cm().half_up
        return hu(NCR_HIGH * base), hu(NCR_LOW * base)

    def _post_ncr(self, r):
        roads = [road for _, road in self.running_roads()]
        if (self.tier >= 3 and self.heat < FREEZE_HEAT and not self.outlaw and NCR_ROAD in roads
                and self.day % 7 == NCR_WEEKDAY and self.day - self.last_ncr_offer >= 7
                and not any(c.ncr for c in self.contracts)
                and not any(m.kind == 'ncr' for m in self.memos)):
            m = _cm().Memo('ncr', self.day, self.day + 1, price=self.ncr_base(), town=NCR_TOWN, good=NCR_GOOD,
                           road=NCR_ROAD)
            if self.post_memo(m):
                self.last_ncr_offer = self.day

    def _settle_ncr(self, r, m, a):
        hi, lo = self.ncr_bids(m.price)
        if a == 2:
            return
        if a == 0 and self.aggr >= CRIMSON_BIDS:
            r.notes.append('the Crimson Caravan won the NCR bid')
            r.ncr = 'lost'
            return
        price = hi if a == 0 else lo
        origin = [t for t in _cm().ROADS[NCR_ROAD] if t != NCR_TOWN][0]
        self.contracts.append(_cm().Contract(NCR_GOOD, NCR_CRATES, NCR_EVERY, price, self.day, self.day,
                                             town=NCR_TOWN, road=NCR_ROAD, origin=origin, days=NCR_DAYS, ncr=True))
        self.aggr = min(100, self.aggr + AGGR_WIN)
        r.signed = price
        r.con = (NCR_TOWN, NCR_GOOD)
        r.ncr = 'won'

    def _ncr_delivered(self, c):
        if c.ncr:
            self.ncr_standing = min(100, self.ncr_standing + NCR_STANDING)
            self.ncr_done += 1

    # --- tier 4 --------------------------------------------------------------------------------------------
    def tier_four_ready(self):
        return (self.tier == 3 and self.earned_worth() >= TIER4_WORTH and self.loan == 0 and self.arrears == 0
                and self.ncr_standing >= TIER4_STANDING and self.ncr_done >= 1 and not self.outlaw
                and not self.recent_strikes())

    def _tier3_day(self):
        self.inspect_next = self.day + INSPECT_EVERY

    # --- the player's settings (the Towns screen's law rows) ------------------------------------------------
    def cycle_hide(self):
        if self.tier >= 3:
            self.hide = (self.hide + 1) % len(HIDE)

    def toggle_sealed(self):
        if self.tier >= 3:
            self.sealed = not self.sealed

    def toggle_cover(self):
        if self.tier >= 3:
            self.insured = not self.insured

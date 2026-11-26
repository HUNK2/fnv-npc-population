"""M3 model tests (docs/plans/2026-11-28-m3-rival-law.md): the rival, the NCR, the back room, heat,
raids, Crimson Cover and tier 4. Everything starts at tier 3; below it the M1/M2 numbers are unchanged.

    python tools/test_m3_law.py
"""
import unittest

import company_model as cm
import law_model as law


def tier3(seed=1234, **kw):
    c = cm.Company(seed, sheriff=True)
    c.found()
    c.auto = True
    c.tier = 3
    c._tier3_day()
    for k, v in kw.items():
        setattr(c, k, v)
    return c


def staff(c, role, loyalty=55, name='Test Hand'):
    p = cm.Person(name, role, 50, 60, cm.ROLE_WAGE[role], loyalty=loyalty)
    c.staff.append(p)
    return p


class BelowTierThree(unittest.TestCase):
    def test_tier_two_company_has_no_law(self):
        c = cm.Company(1234)
        c.found()
        c.auto = True
        c.sealed, c.hide, c.insured = True, 2, True     # set, but closed below tier 3
        for _ in range(28):
            r = c.tick()
            self.assertEqual((r.toll, r.sealed, r.inspected, r.rival), (0, 0, 0, ''))
        self.assertEqual(c.aggr, law.AGGR_START)
        self.assertEqual(c.ncr_standing, law.STANDING_START)

    def test_licence_by_tier(self):
        c = tier3()
        self.assertEqual(c.licence_fee(), 400)
        c.tier = 4
        self.assertEqual(c.licence_fee(), 900)
        c.tier = 2
        self.assertEqual(c.licence_fee(), cm.LICENCE)


class Rival(unittest.TestCase):
    def test_war_cuts_sell_prices_in_its_town_only(self):
        c = tier3()
        before = (c.price('PR', 'water', 'sell'), c.price('GS', 'water', 'sell'), c.price('PR', 'water', 'buy'))
        c.day, c.war_town, c.war_until = 10, 'PR', 12
        self.assertEqual(c.price('PR', 'water', 'sell'),
                         cm.half_up(cm.ANCHOR['water'] * c.mult('PR', 'water') * (1 - max(0.02, cm.spread(c.trust['PR'])))
                                    * (1 - law.WAR_CUT)))
        self.assertLess(c.price('PR', 'water', 'sell'), before[0])
        self.assertEqual(c.price('GS', 'water', 'sell'), before[1])
        self.assertEqual(c.price('PR', 'water', 'buy'), before[2])
        c.day = 13
        self.assertEqual(c.price('PR', 'water', 'sell'), before[0])

    def test_covered_war_cuts_deeper(self):
        c = tier3(insured=True)
        c.day, c.war_town, c.war_until = 10, 'PR', 12
        self.assertEqual(c.war_cut('PR'), law.WAR_CUT_COVERED)

    def test_aggression_rises_with_a_rising_share_and_starts_a_war(self):
        c = tier3(aggr=25)
        c.day = 7
        c.sold_week['PR'] = 50          # 50 / (7 * Primm's use) is well over 25%
        r = cm.DayReport(7, bills_paid=True)
        c._week_law(r)
        self.assertEqual(c.aggr, 35)
        self.assertEqual((r.rival, c.war_town, c.war_until), ('war', 'PR', 7 + law.WAR_DAYS))
        self.assertEqual(c.sold_week['PR'], 0)

    def test_a_steady_share_does_not_raise_aggression(self):
        c = tier3(aggr=25)
        c.last_share['PR'] = 1.0
        c.day = 7
        c.sold_week['PR'] = 50
        c._week_law(cm.DayReport(7))
        self.assertEqual(c.aggr, 25)

    def test_small_and_quiet_cools_her(self):
        c = tier3(aggr=25)
        c.day = 7
        c._week_law(cm.DayReport(7))
        self.assertEqual(c.aggr, 20)

    def test_poach_is_warned_a_day_ahead_and_a_raise_saves_them(self):
        c = tier3(aggr=40)
        p = staff(c, 'guard', loyalty=30, name='Low Loyal')
        c.day = 7
        r = cm.DayReport(7)
        c._week_law(r)                  # no share over 25%: no war, so the poach
        self.assertEqual((r.rival, c.poach_name, c.poach_day), ('poach', 'Low Loyal', 8))
        c.day = 8
        p.loyalty = 50                  # a raise in between
        r = cm.DayReport(8)
        c._day_law(r)
        self.assertIn(p, c.staff)
        self.assertEqual(c.poach_name, '')

    def test_poach_takes_them_next_day(self):
        c = tier3(aggr=40)
        p = staff(c, 'guard', loyalty=30, name='Low Loyal')
        c.day = 7
        c._week_law(cm.DayReport(7))
        c.day = 8
        r = cm.DayReport(8)
        c._day_law(r)
        self.assertNotIn(p, c.staff)
        self.assertEqual(r.rival, 'poached')

    def test_contract_price_stays_during_a_war(self):
        """Review focus 1: a price war in Primm while a contract runs there."""
        c = tier3()
        c.contracts.append(cm.Contract('water', 4, 3, 250, 1, 2, town='PR', road=1, origin='GS'))
        c.war_town, c.war_until = 'PR', 99
        c.cash = 5000
        c.day = 2
        r = cm.DayReport(2)
        c._contract(r, True, 1)
        self.assertEqual(r.sales, 4 * 250)


class NCR(unittest.TestCase):
    def test_toll_on_the_outpost_road_until_tier_four(self):
        c = tier3()
        r = cm.DayReport(1)
        c._toll(r, 3)
        c._toll(r, 1)
        self.assertEqual(r.toll, law.TOLL)
        c.tier = 4
        c._toll(r, 3)
        self.assertEqual(r.toll, law.TOLL)

    def test_bids(self):
        c = tier3()
        base = c.ncr_base()
        m = cm.Memo('ncr', 5, 6, price=base, town='MO', good='ammo', road=3)
        self.assertEqual(m.answers[:2], ('bid %d a crate' % cm.half_up(1.3 * base), 'bid %d a crate' % cm.half_up(1.2 * base)))
        self.assertEqual(c.memo_default(m), 2)

    def test_high_bid_loses_to_an_angry_caravan(self):
        c = tier3(aggr=law.CRIMSON_BIDS)
        m = cm.Memo('ncr', 5, 6, price=100, town='MO', good='ammo', road=3)
        r = cm.DayReport(6)
        c._settle_ncr(r, m, 0)
        self.assertEqual((r.ncr, c.contracts), ('lost', []))
        c._settle_ncr(r, m, 1)
        self.assertEqual(r.ncr, 'won')
        k = c.contracts[0]
        self.assertEqual((k.town, k.good, k.price, k.days, k.ncr, k.origin, k.road), ('MO', 'ammo', 120, 14, True, 'PR', 3))
        self.assertEqual(c.aggr, law.CRIMSON_BIDS + law.AGGR_WIN)

    def test_high_bid_wins_when_she_is_calm(self):
        c = tier3(aggr=20)
        m = cm.Memo('ncr', 5, 6, price=100, town='MO', good='ammo', road=3)
        r = cm.DayReport(6)
        c._settle_ncr(r, m, 0)
        self.assertEqual(c.contracts[0].price, 130)

    def test_ncr_delivery_raises_standing(self):
        c = tier3()
        k = cm.Contract('ammo', 4, 3, 300, 1, 2, town='MO', road=3, origin='PR', days=14, ncr=True)
        c.contracts.append(k)
        c.cash, c.day = 5000, 2
        c._contract(cm.DayReport(2), True, 3)
        self.assertEqual((c.ncr_standing, c.ncr_done), (law.STANDING_START + 2, 1))

    def test_ncr_contract_ends_after_14_days(self):
        c = tier3()
        k = cm.Contract('ammo', 4, 3, 300, 1, 13, town='MO', road=3, origin='PR', days=14, ncr=True)
        c.contracts.append(k)
        c.cash, c.day = 5000, 13
        r = cm.DayReport(13)
        c._contract(r, True, 3)
        self.assertEqual(c.contracts, [])
        self.assertTrue(r.contract.endswith('completed'))

    def test_offer_needs_the_outpost_wagon_and_low_heat(self):
        c = tier3()
        c.day = 5
        c._post_ncr(cm.DayReport(5))
        self.assertFalse(any(m.kind == 'ncr' for m in c.memos))     # no Outpost wagon
        c.wagons.append(cm.Wagon(3))
        staff(c, 'driver')
        staff(c, 'clerk')
        c.heat = law.FREEZE_HEAT
        c._post_ncr(cm.DayReport(5))
        self.assertFalse(any(m.kind == 'ncr' for m in c.memos))
        c.heat = 0
        c._post_ncr(cm.DayReport(5))
        self.assertTrue(any(m.kind == 'ncr' for m in c.memos))

    def test_inspection_fault_then_fine(self):
        c = tier3()
        c.cash = 10000
        c.day = c.inspect_next
        c.hidden_since = 50
        r = cm.DayReport(c.day, sales=1000)
        c._inspect(r)
        self.assertEqual((c.faults, r.fine, c.ncr_standing, r.inspected), (1, 0, 25, 2))
        self.assertEqual(c.inspect_next, c.day + 30)
        c.hidden_since = 10
        c.heat = 20
        r = cm.DayReport(c.day, sales=1000)
        c._inspect(r)
        self.assertEqual((c.faults, r.fine), (2, 50))
        self.assertEqual(c.inspect_next, c.day + 10)

    def test_clean_inspection(self):
        c = tier3()
        r = cm.DayReport(1)
        c._inspect(r)
        self.assertEqual((c.faults, r.inspected, c.ncr_standing), (0, 1, law.STANDING_START))


class BackRoom(unittest.TestCase):
    def test_hidden_sales_cut_duty_and_add_heat(self):
        c = tier3(hide=2)
        c.week_sales = 4000
        c.day = 7
        r = cm.DayReport(7)
        c._bills(r)
        self.assertEqual(r.bills['duty'], cm.duty(3200))
        self.assertEqual((c.hidden_since, c.heat_gain), (800, 4))

    def test_sealed_run_every_three_days_on_road_one(self):
        c = tier3(sealed=True)
        got = []
        for d in range(1, 8):
            c.day = d
            r = cm.DayReport(d)
            c._sealed_run(r, 1)
            c._sealed_run(r, 2)
            got.append(r.sealed)
        self.assertEqual([g > 0 for g in got], [True, False, False, True, False, False, True])

    def test_search_fines_and_heats(self):
        c = tier3(sealed=True)
        c.cash = 1000
        d = next(d for d in range(1, 500) if cm.roll(c.seed, d, law.ROLL_SEARCH) < law.SEARCH_CHANCE)
        c.day = d
        r = cm.DayReport(d)
        c._sealed_run(r, 1)
        self.assertEqual((r.sealed, r.sales, r.costs, c.heat_gain), (2, 50, 100, 15))

    def test_heat_falls_faster_after_a_clean_week(self):
        c = tier3(heat=30)
        for d in range(1, 10):
            c.day = d
            c._day_law(cm.DayReport(d))
        self.assertEqual(c.heat, 30 - 6 - 2 * 3)

    def test_two_gains_on_one_day_add_up(self):
        """Review focus 4 (my call: no daily cap): a search and hidden sales on one bill day."""
        c = tier3(heat=10)
        c.heat_gain = law.SEALED_HEAT + law.SEARCH_HEAT + 4
        c.day = 7
        c._day_law(cm.DayReport(7))
        self.assertEqual(c.heat, 29)

    def test_warrant_at_heat_80(self):
        c = tier3(heat=81)          # falls 1 on a day without gain, then the check
        c.day = 5
        r = cm.DayReport(5)
        c._day_law(r)
        m = [m for m in c.memos if m.kind == 'warrant']
        self.assertEqual(len(m), 1)
        self.assertEqual((m[0].due, r.warrant), (5 + law.RAID_DAYS, True))

    def test_fixer_clears_the_warrant(self):
        c = tier3(heat=85)
        c.cash, c.day = 1000, 12
        r = cm.DayReport(12)
        c._settle_warrant(r, 0)
        self.assertEqual((c.cash, c.heat, r.raid, c.raids), (700, law.RAID_HEAT, 'bribed', []))

    def test_raid_seizes_a_fifth_of_cash_when_cover_is_short(self):
        c = tier3(heat=85)
        c.cash, c.day = 1000, 12
        r = cm.DayReport(12)
        c._settle_warrant(r, 1)
        self.assertEqual((c.cash, r.raid, c.heat, c.raids), (800, 'seized', law.RAID_HEAT, [12]))
        self.assertFalse(c.ended)

    def test_raid_won_makes_an_outlaw(self):
        c = tier3(heat=85)
        staff(c, 'guard')
        self.assertGreaterEqual(c.cover(), law.RAID_STRENGTH)
        r = cm.DayReport(12)
        c._raid(r)
        self.assertEqual((r.raid, c.outlaw, c.ncr_standing), ('won', True, 0))

    def test_second_raid_in_28_days_revokes(self):
        c = tier3()
        c.raids = [10]
        c.day = 30
        r = cm.DayReport(30)
        c._raid(r)
        self.assertEqual((c.ended, c.end_reason), (True, 'revoked'))

    def test_no_warrant_within_7_days_of_a_raid(self):
        c = tier3(heat=90)
        c.raid_last, c.day = 10, 14
        c._day_law(cm.DayReport(14))
        self.assertFalse(any(m.kind == 'warrant' for m in c.memos))


class Cover(unittest.TestCase):
    def test_claim_pays_60_percent(self):
        c = tier3(insured=True)
        r = cm.DayReport(1)
        c._claim(r, 101)
        self.assertEqual((r.claim, r.sales), (61, 61))

    def test_premium_with_the_bills(self):
        c = tier3(insured=True)
        c.day = 7
        r = cm.DayReport(7)
        c._bills(r)
        self.assertEqual(r.bills['cover'], law.COVER_PREMIUM * len(c.running_roads()))


class TierFour(unittest.TestCase):
    def test_gate(self):
        c = tier3()
        c.cash, c.loan = law.TIER4_WORTH + c.owner_paid_in + 10000, 0
        c.ncr_standing = 50
        self.assertFalse(c.tier_four_ready())         # no NCR delivery yet
        c.ncr_done = 1
        self.assertTrue(c.tier_four_ready())
        c.outlaw = True
        self.assertFalse(c.tier_four_ready())

    def test_good_player_reaches_tier_four(self):
        import balance_run
        o = balance_run.play('good', 100, 1234)
        self.assertIsNotNone(o['tier4'])
        self.assertLessEqual(o['tier4'], 63)
        o = balance_run.play('dodgy', 100, 1234)
        self.assertIsNotNone(o['tier4'])
        raids = o['raids']
        self.assertFalse(any(b - a <= 28 for a, b in zip(raids, raids[1:])))


if __name__ == '__main__':
    unittest.main()

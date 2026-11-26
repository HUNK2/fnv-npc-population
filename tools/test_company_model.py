"""Tests for the M1 company model (plan docs/plans/2026-11-27-m1-one-road.md, task 1.1).

Values come from docs/design.md: Starter trade, Money, Growth, The road, Losing and coming back,
Numbers (balance targets)."""
import unittest

import company_model as cm


def fresh(seed=1234, sheriff=False, **kw):
    c = cm.Company(seed, sheriff=sheriff, **kw)
    c.found()
    return c


def play(c, days, accept=True):
    reports = []
    for _ in range(days):
        if accept:
            for o in c.plan():
                c.queue(o)
        reports.append(c.tick())
    return reports


class StarterPrices(unittest.TestCase):
    def test_mid_prices_match_the_starter_table(self):
        c = fresh()
        self.assertEqual(c.mid('GS', 'water'), 152)
        self.assertEqual(c.mid('PR', 'water'), 236)
        self.assertEqual(c.mid('GS', 'herbs'), 40)
        self.assertEqual(c.mid('PR', 'materials'), 110)
        self.assertEqual(c.mid('GS', 'materials'), 225)

    def test_primm_ammo_depends_on_the_sheriff(self):
        self.assertEqual(fresh(sheriff=False).mid('PR', 'ammo'), 162)
        self.assertEqual(fresh(sheriff=True).mid('PR', 'ammo'), 146)

    def test_spread_shrinks_with_trust(self):
        c = fresh()
        self.assertAlmostEqual(cm.spread(0), 0.10)
        self.assertAlmostEqual(cm.spread(100), 0.02)
        s = cm.spread(c.trust['PR'])
        self.assertEqual(c.price('PR', 'water', 'sell'), cm.half_up(c.mid_exact('PR', 'water') * (1 - s)))
        self.assertLess(c.price('PR', 'water', 'sell'), c.mid('PR', 'water'))
        self.assertGreater(c.price('GS', 'water', 'buy'), c.mid('GS', 'water'))

    def test_whole_caps_half_up(self):
        self.assertEqual(cm.half_up(2.5), 3)
        self.assertEqual(cm.half_up(-2.5), -2)
        self.assertEqual(cm.half_up(151.49), 151)

    def test_nightly_recovery(self):
        self.assertAlmostEqual(cm.restock(10, 30), 15.0)
        self.assertAlmostEqual(cm.restock(40, 30), 38.8)


class Founding(unittest.TestCase):
    def test_day_zero_money(self):
        c = fresh()
        self.assertEqual(c.cash, 2500)
        self.assertEqual(c.loan, 3000)
        self.assertEqual(c.owner_funds, 0)
        self.assertEqual(c.net_worth(), 200)
        self.assertEqual(c.earned_worth(), -300)
        self.assertEqual(c.tier, 1)


class Balance(unittest.TestCase):
    def test_day_one_of_a_fresh_route_pays(self):
        r = play(fresh(), 1)[0]
        self.assertGreaterEqual(r.margin, 500)
        self.assertLessEqual(r.margin, 800)

    def test_a_tired_route_alone_is_positive_but_thin(self):
        c = fresh(seed=7)
        reports = play(c, 21)
        week3 = sum(r.margin for r in reports[14:21]) - c.week_running_costs()
        self.assertGreater(week3, 100)
        self.assertLess(week3, 400)

    def test_passive_player_stalls_rather_than_goes_broke(self):
        for seed in (1, 2, 3, 4, 5):
            c = fresh(seed=seed)
            play(c, 28)
            self.assertFalse(c.ended, 'seed %d ended the company' % seed)
            self.assertIn(c.tier, (1, 2))

    def test_worst_event_at_tier_1_is_capped_at_three_days_of_runway(self):
        for seed in range(1, 60):
            c = fresh(seed=seed)
            for r in play(c, 21):
                if r.event_loss:
                    self.assertLessEqual(r.event_loss, 3 * c.daily_burn() + 1, 'seed %d day %d' % (seed, r.day))


class Bills(unittest.TestCase):
    def test_day_seven_bills(self):
        c = fresh()
        reports = play(c, 7)
        bill = reports[6].bills
        sales = sum(r.sales for r in reports)
        self.assertEqual(bill['interest'], 120)
        self.assertEqual(bill['principal'], 300)
        self.assertEqual(bill['wages'], 7 * 22)
        self.assertEqual(bill['feed'], 7 * 6)
        self.assertEqual(bill['rent'], 70)
        self.assertEqual(bill['duty'], cm.duty(sales))
        self.assertTrue(reports[6].bills_paid)
        self.assertEqual(c.loan, 2700)

    def test_progressive_duty(self):
        self.assertEqual(cm.duty(4000), 80)
        self.assertEqual(cm.duty(6000), 100 + 35)
        self.assertEqual(cm.duty(25000), 100 + 525 + 250)


class DebtLadder(unittest.TestCase):
    def broke(self, present=True):
        c = fresh(present=present)
        c.cash = 50          # far short of the day-7 bill
        for _ in range(6):
            c.tick()
            c.cash = min(c.cash, 50)
        r = c.tick()         # day 7
        return c, r

    def test_a_miss_serves_a_notice_and_a_strike_when_present(self):
        c, r = self.broke()
        self.assertFalse(r.bills_paid)
        self.assertGreater(c.arrears, 0)
        self.assertEqual(c.strikes, [7])
        self.assertEqual(c.stage, 'grace')

    def test_away_defers_without_a_strike_until_served(self):
        c, r = self.broke(present=False)
        self.assertEqual(c.strikes, [])
        self.assertEqual(c.stage, 'deferred')
        c.visit()
        self.assertEqual(c.strikes, [7])
        self.assertEqual(c.stage, 'grace')

    def test_ladder_runs_final_notice_seizure_receivership(self):
        c, _ = self.broke()
        stages = []
        for _ in range(7):
            c.cash = 0
            c.tick()
            stages.append(c.stage)
        self.assertEqual(stages[2], 'final')       # day 10 = served + 3
        self.assertIn('seized', c.history_text())  # day 12 = served + 5
        self.assertTrue(c.ended)                   # day 14 = served + 7

    def test_owner_rescue_cures_the_notice_but_keeps_the_strike(self):
        c, _ = self.broke()
        c.owner_rescue()
        self.assertEqual(c.arrears, 0)
        self.assertEqual(c.stage, 'probation')
        self.assertEqual(c.strikes, [7])

    def test_busy_shield_stops_the_clock(self):
        c, _ = self.broke()
        c.shield = True
        for _ in range(10):
            c.cash = 0
            c.tick()
        self.assertFalse(c.ended)
        self.assertEqual(c.stage, 'grace')


class Determinism(unittest.TestCase):
    def test_same_seed_same_days(self):
        a = [(r.margin, r.event) for r in play(fresh(seed=99), 21)]
        b = [(r.margin, r.event) for r in play(fresh(seed=99), 21)]
        self.assertEqual(a, b)

    def test_rolls_match_the_in_game_formula(self):
        self.assertEqual(cm.roll(1234, 5, 1), (5 * 7919 + 1234 * 104729 + 31) % 100)


class TierTwo(unittest.TestCase):
    def test_gate_needs_worth_trust_and_the_deed(self):
        c = fresh()
        c.cash += 5000          # money alone is not enough
        self.assertFalse(c.tier_two_ready())
        c.trust['GS'] = 50
        self.assertFalse(c.tier_two_ready())
        c.ghost_town_done = True
        self.assertTrue(c.tier_two_ready())

    def test_purifier_turns_five_dirty_into_four_water(self):
        c = fresh()
        c.tier = 2
        c.build('purifier')
        c.warehouse['dirty'] = 5
        c.run_workshops()
        self.assertEqual(c.warehouse['dirty'], 0)
        self.assertEqual(c.warehouse['water'], 4)


if __name__ == '__main__':
    unittest.main()

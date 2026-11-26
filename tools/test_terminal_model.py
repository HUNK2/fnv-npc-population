"""Tests for the M1 office terminal model (plan task 1.4)."""
import unittest

import company_model as cm
import terminal_model as tm


def founded(days=0, auto=True, road=cm.SEND):
    """A company run for some days; every road memo is answered `road` (send: bandits can hit)."""
    c = cm.Company(1234)
    c.found()
    c.auto = auto
    for _ in range(days):
        for m in c.memos:
            if m.kind == 'road':
                c.answer(m, road)
        c.tick()
    return c


class Labels(unittest.TestCase):
    def test_before_founding_one_row_points_at_the_agent(self):
        c = cm.Company(1234)
        self.assertEqual(tm.labels(c, tm.Terminal()), ["No company yet: see Alice's agent."])

    def test_front_page_on_founding_day(self):
        c = founded()
        rows = tm.labels(c, tm.Terminal())
        self.assertEqual(len(rows), 12)
        burn = c.daily_burn()
        self.assertEqual(rows[0], 'CASH 2500 BILLS 7d:%d RUNWAY %dd' % (tm.bill_estimate(c), 2500 // burn))
        self.assertEqual(rows[2], 'POST     nothing yet')
        self.assertEqual(rows[-1], 'SETTINGS')

    def test_bill_estimate_is_a_quiet_week_and_the_licence_every_28_days(self):
        c = founded()
        quiet = 7 * 22 + 7 * 6 + 70 + 120 + 300
        self.assertEqual(tm.bill_estimate(c), quiet)
        c = founded(21)
        self.assertEqual(tm.bill_estimate(c), 7 * 22 + 7 * 6 + 70 + cm.half_up(0.04 * c.loan)
                         + min(300, c.loan) + cm.duty(c.week_sales) + 150)

    def test_every_row_of_every_screen_fits_one_line_over_28_days(self):
        c = founded()
        t = tm.Terminal()
        for _ in range(29):
            for screen in range(8):
                for direction in (0, 1):
                    t.screen, t.direction = screen, direction
                    rows = tm.labels(c, t)
                    self.assertLessEqual(len(rows), tm.MAX_ROWS)
                    for row in rows:
                        self.assertLessEqual(len(row), tm.ROW_WIDTH, row)
            c.tick()

    def test_rows_fit_with_large_numbers(self):
        c = founded(9)
        c.cash, c.loan, c.week_sales, c.arrears, c.owner_funds = 123456, 3000, 99999, 12345, 99999
        t = tm.Terminal()
        for screen in range(8):
            t.screen = screen
            for row in tm.labels(c, t):
                self.assertLessEqual(len(row), tm.ROW_WIDTH, row)

    def test_prices_rows_are_the_model_prices(self):
        c = founded()
        t = tm.Terminal()
        t.screen = tm.PRICES
        rows = tm.labels(c, t)
        b, s = c.price('GS', 'water', 'buy'), c.price('PR', 'water', 'sell')
        self.assertEqual(rows[1], 'water       %d/%d  margin %d  [0]' % (b, s, s - b))
        t.direction = 1
        self.assertTrue(tm.labels(c, t)[0].startswith('PR > GS  buy/sell'))

    def test_routes_lists_the_last_three_days_newest_first_with_events(self):
        c = founded(5)
        t = tm.Terminal()
        t.screen = tm.ROUTES
        rows = tm.labels(c, t)
        self.assertEqual(len(rows), 5)
        r5 = c.history[4]
        self.assertEqual(r5.event, 'bandits_took_cargo')
        self.assertEqual(rows[1], 'DAY 5  net %d  bandits -%d' % (r5.margin, r5.event_loss))
        self.assertTrue(rows[3].startswith('DAY 3 '))


class Clicks(unittest.TestCase):
    def test_front_rows_open_their_screens_and_back_returns(self):
        c, t = founded(), tm.Terminal()
        for row, screen in ((2, tm.POST), (3, tm.MEMOS), (4, tm.ROUTES), (5, tm.PRICES), (9, tm.LEDGER),
                            (10, tm.ORDERS), (11, tm.SETTINGS)):
            tm.click(c, t, row)
            self.assertEqual(t.screen, screen)
            tm.click(c, t, len(tm.labels(c, t)) - 1)
            self.assertEqual(t.screen, tm.FRONT)

    def test_info_rows_and_hidden_rows_do_nothing(self):
        c, t = founded(), tm.Terminal()
        for row in (0, 6, 7, 8, 12, 13):
            tm.click(c, t, row)
            self.assertEqual(t.screen, tm.FRONT)
        self.assertEqual(c.queue_list, [])
        t.screen = tm.SETTINGS
        tm.click(c, t, 5)
        self.assertEqual(t.screen, tm.SETTINGS)

    def test_plan_row_queues_the_plan(self):
        c, t = founded(auto=False), tm.Terminal()
        plan = c.plan()
        tm.click(c, t, 1)
        self.assertEqual(c.queue_list, plan)
        self.assertEqual(tm.labels(c, t)[10], 'ORDERS   %d pending (apply at 06:00)' % len(plan))

    def test_prices_queue_one_crate_a_click_at_most_8_a_leg(self):
        c, t = founded(auto=False), tm.Terminal()
        t.screen = tm.PRICES
        for _ in range(10):
            tm.click(c, t, 1)
        self.assertEqual([(o.town, o.good) for o in c.queue_list], [('GS', 'water')] * 8)
        tm.click(c, t, 0)
        tm.click(c, t, 3)
        self.assertEqual((c.queue_list[-1].town, c.queue_list[-1].good), ('PR', 'ammo'))
        self.assertTrue(tm.labels(c, t)[3].endswith('[1]'))

    def test_orders_cancel_and_accept(self):
        c, t = founded(auto=False), tm.Terminal()
        t.screen = tm.PRICES
        tm.click(c, t, 2)
        t.screen = tm.ORDERS
        self.assertEqual(tm.labels(c, t)[0], 'GS > PR  1 crates')
        tm.click(c, t, 3)
        self.assertEqual(c.queue_list, [])
        tm.click(c, t, 2)
        self.assertEqual(c.queue_list, c.plan())

    def test_settings_toggles_the_daily_plan(self):
        c, t = founded(auto=False), tm.Terminal()
        t.screen = tm.SETTINGS
        tm.click(c, t, 0)
        self.assertTrue(c.auto)
        self.assertEqual(tm.labels(c, t)[0], 'PLAN EVERY DAY   ON')

    def test_manual_orders_run_at_the_tick_and_clear(self):
        c, t = founded(auto=False), tm.Terminal()
        t.screen = tm.PRICES
        tm.click(c, t, 1)
        cost, sale = c.price('GS', 'water', 'buy'), c.price('PR', 'water', 'sell')
        r = c.tick()
        self.assertEqual((r.costs, r.sales), (cost, sale))
        self.assertEqual(c.queue_list, [])


if __name__ == '__main__':
    unittest.main()

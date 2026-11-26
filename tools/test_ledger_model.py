import unittest

import ledger_model as lm


class PriceRules(unittest.TestCase):
    def test_price_mult_at_three_days_of_stock_is_one(self):
        self.assertAlmostEqual(lm.price_mult(30, 10), 1.0)

    def test_price_mult_bounds(self):
        self.assertAlmostEqual(lm.price_mult(0, 4), 1.5)
        self.assertLess(lm.price_mult(10_000, 4), 0.51)

    def test_doc_example_goodsprings_water(self):
        # Money section example: Goodsprings water, use 4/day, stock 34 -> m 0.76, mid 152, ask 161
        m = lm.price_mult(34, 4)
        self.assertAlmostEqual(m, 0.76, places=2)
        self.assertEqual(round(200 * m), 152)
        self.assertEqual(round(lm.ask(200, m)), 161)

    def test_restock_moves_toward_normal(self):
        self.assertAlmostEqual(lm.restock(10, 30), 15.0)
        self.assertAlmostEqual(lm.restock(40, 30), 38.8)


class WorkedFirstWeek(unittest.TestCase):
    """The design doc's Numbers section, 'The first week, simulated'."""

    @classmethod
    def setUpClass(cls):
        cls.week = lm.run_first_week()

    def test_day_margins(self):
        # the report rounds each leg, then adds the two legs of a day
        legs = [round(l.margin) for l in self.week.legs]
        self.assertEqual([legs[i] + legs[i + 1] for i in range(0, 14, 2)], [746, 288, 94, 94, -117, 124, 91])
        for exact, shown in zip(self.week.day_margins, [746, 288, 94, 94, -117, 124, 91]):
            self.assertAlmostEqual(exact, shown, delta=1)

    def test_leg_margins(self):
        self.assertEqual([round(l.margin) for l in self.week.legs],
                         [380, 366, 238, 50, 71, 23, 69, 25, 48, -165, 69, 55, 66, 25])

    def test_statement(self):
        w = self.week
        self.assertEqual(round(w.sales), 8178)
        self.assertEqual(round(w.cogs), 6857)
        self.assertAlmostEqual(w.gross, 1321, delta=1)
        self.assertEqual(round(w.duty), 164)
        self.assertAlmostEqual(w.operating_profit, 842, delta=1)
        self.assertAlmostEqual(w.net_profit, 722, delta=1)

    def test_end_of_week_net_worth(self):
        # cash 2,500 after setup + day margins - wages - feed - rent - duty - interest - principal;
        # assets 700 less wear; debt 3,000 less principal
        w = self.week
        cash = 2500 + sum(w.day_margins) - w.wages - w.feed - lm.DEPOT_RENT_WEEK - w.duty - w.interest \
            - lm.PRINCIPAL_WEEK
        net_worth = cash + (700 - w.wear) - (lm.LOAN - lm.PRINCIPAL_WEEK)
        self.assertAlmostEqual(cash, 2972, delta=1)
        self.assertAlmostEqual(net_worth, 923, delta=1)


if __name__ == '__main__':
    unittest.main()

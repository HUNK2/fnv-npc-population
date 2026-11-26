"""M2 task 2.6 (model side): the Wagons screen, the Towns screen and the managers."""
import unittest

import company_model as cm
import terminal_model as tm


def tier(n, cash=5000):
    c = cm.Company(1234)
    c.found()
    c.tier = n
    c.cash = cash
    return c


class Screens(unittest.TestCase):
    def test_front_has_towns_row_from_tier_2_only(self):
        t = tm.Terminal()
        self.assertEqual(len(tm.labels(tier(1), t)), 13)
        rows = tm.labels(tier(2), t)
        self.assertEqual(len(rows), 14)
        self.assertTrue(rows[13].startswith('TOWNS'))

    def test_every_row_fits(self):
        for n in (2, 3):
            c = tier(n)
            for screen in (tm.FRONT, tm.ROUTES, tm.TOWNS_SCREEN):
                t = tm.Terminal()
                t.screen = screen
                for row in tm.labels(c, t):
                    self.assertLessEqual(len(row), tm.ROW_WIDTH, row)

    def test_wagons_screen_buys_the_sloan_road(self):
        c, t = tier(2), tm.Terminal()
        tm.click(c, t, 4)
        self.assertEqual(t.screen, tm.ROUTES)
        rows = tm.labels(c, t)
        self.assertEqual(rows[1], 'SLOAN ROAD  BUY a wagon for %d' % (cm.WAGON + cm.BRAHMIN_PAIR))
        self.assertEqual(rows[2], 'OUTPOST ROAD  opens at tier 3')
        tm.click(c, t, 2)                       # not open yet: nothing
        self.assertEqual(len(c.wagons), 0)
        tm.click(c, t, 1)
        self.assertEqual([w.road for w in c.wagons], [2])
        self.assertTrue(tm.labels(c, t)[1].startswith('WAGON 2  Sloan road  '))

    def test_towns_screen_and_managers(self):
        c, t = tier(3), tm.Terminal()
        tm.click(c, t, 13)
        self.assertEqual(t.screen, tm.TOWNS_SCREEN)
        rows = tm.labels(c, t)
        self.assertTrue(rows[0].startswith('Goodsprings'))
        self.assertEqual(rows[4], 'BOOKKEEPER  HIRE, %d a day' % cm.MANAGER_WAGE)
        tm.click(c, t, 4)
        self.assertEqual(c.managers['bookkeeper'], 'Normal')
        tm.click(c, t, 4)
        self.assertEqual(c.managers['bookkeeper'], 'Lenient')
        tm.click(c, t, 4)
        self.assertEqual(c.managers['bookkeeper'], 'Strict')
        tm.click(c, t, 5)
        self.assertEqual(c.managers['route'], 'Balanced')
        tm.click(c, t, 8)                       # BACK
        self.assertEqual(t.screen, tm.FRONT)

    def test_route_manager_waits_for_tier_3(self):
        c, t = tier(2), tm.Terminal()
        t.screen = tm.TOWNS_SCREEN
        self.assertEqual(tm.labels(c, t)[5], 'ROUTE MGR   opens at tier 3')
        tm.click(c, t, 5)
        self.assertNotIn('route', c.managers)

    def test_selling_the_company_a_crate(self):
        c, t = tier(2), tm.Terminal()
        t.screen = tm.TOWNS_SCREEN
        self.assertEqual(tm.labels(c, t)[6], 'SELL 10 purified water: 160 (10 left)')
        tm.click(c, t, 6)                       # nothing carried: nothing sold
        self.assertEqual(c.warehouse['water'], 0)
        c.carried['water'] = 25
        cash = c.cash
        tm.click(c, t, 6)
        tm.click(c, t, 6)
        tm.click(c, t, 6)                       # 5 bottles left: not a crate
        self.assertEqual((c.warehouse['water'], c.carried['water'], c.cash), (2, 5, cash - 320))
        self.assertEqual(tm.labels(c, t)[7], 'SELL 10 healing powder: 80 (8 left)')


if __name__ == '__main__':
    unittest.main()

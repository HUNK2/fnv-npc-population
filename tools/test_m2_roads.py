"""M2 task 2.1: Sloan and the Mojave Outpost, three roads and wagons, site goods to the workshops."""
import unittest

import company_model as cm


def founded(seed=7):
    c = cm.Company(seed)
    c.found()
    return c


def tier3(seed=7, drivers=3):
    c = founded(seed)
    c.tier = 3
    c.cash += 20000
    c.staff += [cm.Person('Driver %d' % i, 'driver', 50, 60, 10) for i in range(drivers - 1)]
    c.staff += [cm.Person('Clerk %d' % i, 'clerk', 50, 60, 15) for i in range(2)]   # a clerk per extra wagon
    return c


class Markets(unittest.TestCase):
    def test_starter_prices_in_the_new_towns(self):
        c = founded()
        self.assertEqual(c.mid('SL', 'water'), 250)
        self.assertEqual(c.mid('MO', 'water'), 233)
        self.assertEqual(c.mid('SL', 'meat'), 136)
        self.assertEqual(c.mid('MO', 'meat'), 125)
        self.assertEqual(c.mid('PR', 'meat'), 110)

    def test_a_dash_is_no_market(self):
        c = founded()
        self.assertFalse(c.has_market('MO', 'dirty'))
        self.assertFalse(c.has_market('SL', 'herbs'))
        self.assertTrue(c.has_market('SL', 'materials'))
        for g in cm.SITE_GOODS:
            self.assertFalse(any(c.has_market(t, g) for t in cm.TOWNS))


class Wagons(unittest.TestCase):
    def test_roads_open_by_tier(self):
        c = founded()
        c.cash += 5000
        self.assertFalse(c.can_buy_road(2))
        c.tier = 2
        self.assertTrue(c.can_buy_road(2))
        self.assertFalse(c.can_buy_road(3))
        c.tier = 3
        self.assertTrue(c.buy_road(3))
        self.assertFalse(c.can_buy_road(3))

    def test_a_wagon_needs_a_free_driver(self):
        c = tier3(drivers=2)
        c.buy_road(2)
        c.buy_road(3)
        self.assertEqual(c.running_roads(), [(1, 1), (2, 2)])
        c.staff.append(cm.Person('Third', 'driver', 50, 60, 10))
        self.assertEqual(c.running_roads(), [(1, 1), (2, 2), (3, 3)])

    def test_every_running_wagon_trades_its_own_road(self):
        c = tier3()
        c.buy_road(2)
        c.buy_road(3)
        towns = set()
        for _ in range(4):
            r = c.tick()
            towns |= {t for t, g in r.sold_to}
        self.assertEqual(towns, {'GS', 'PR', 'SL', 'MO'})
        self.assertGreater(c.trust['SL'] + c.trust['MO'], 40)

    def test_one_director_for_all_roads(self):
        c = tier3()
        c.buy_road(2)
        c.buy_road(3)
        days = []
        for _ in range(60):
            for m in c.memos:
                if m.kind == 'road':
                    c.answer(m, cm.SEND)
            r = c.tick()
            if r.event:
                days.append(r.day)
        self.assertTrue(days)
        self.assertTrue(all(b - a >= cm.EVENT_EVERY for a, b in zip(days, days[1:])), days)

    def test_one_wagon_keeps_the_m1_road(self):
        c = founded()
        for _ in range(5):
            c.tick()
        self.assertTrue(all(o in ('GS', 'PR') for r in c.history for o, g in r.loads))


class SiteGoods(unittest.TestCase):
    def stone_company(self):
        c = tier3()
        c.deeds.add('quarry_junction')
        for b in ('sandpit', 'quarry', 'stoneyard'):
            self.assertTrue(c.can_build(b), b)
            c.build(b)
        c.buy_road(2)
        return c

    def test_buildings_wait_for_their_tier_and_deed(self):
        c = founded()
        c.tier = 2
        c.cash += 5000
        self.assertTrue(c.can_build('sandpit'))
        self.assertFalse(c.can_build('smokehouse'))
        c.tier = 3
        self.assertTrue(c.can_build('smokehouse'))
        self.assertFalse(c.can_build('quarry'))
        c.deeds.add('quarry_junction')
        self.assertTrue(c.can_build('quarry'))

    def test_sand_goes_primm_goodsprings_sloan_and_is_never_sold(self):
        c = self.stone_company()
        self.assertTrue(c.site_goes('sand', 'PR', 'GS'))
        self.assertTrue(c.site_goes('sand', 'GS', 'SL'))
        self.assertFalse(c.site_goes('sand', 'GS', 'PR'))
        self.assertFalse(c.site_goes('stone', 'SL', 'GS'))
        made = 0
        for _ in range(8):
            before = c.wh['SL']['materials']
            r = c.tick()
            self.assertFalse(any(g in cm.SITE_GOODS for o, g in r.loads), r.loads)
            made += max(0, c.wh['SL']['materials'] - before)
        self.assertGreater(c.wh['SL']['sand'] + made, 0)
        self.assertGreater(made + sum(n for (o, g), n in [(k, v) for r in c.history for k, v in r.loads.items()]
                                      if g == 'materials'), 0)

    def test_the_smokehouse_needs_brahmin_from_the_corral(self):
        c = tier3()
        c.build('corral')
        c.build('smokehouse')
        for _ in range(4):
            c.tick()
        meat = c.wh['PR']['meat'] + sum(n for r in c.history for (o, g), n in r.loads.items() if g == 'meat')
        self.assertGreater(meat, 0)


if __name__ == '__main__':
    unittest.main()

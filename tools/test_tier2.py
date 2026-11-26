"""M1 task 1.9: trust gains, the Ghost Town deed, tier 2, the tier letter and the Build screen."""
import unittest

import company_model as cm
import post_model as pm
import terminal_model as tm


def founded(days=0, ghost=False):
    c = cm.Company(1234)
    c.found()
    c.auto = True
    c.ghost_town_done = ghost
    for _ in range(days):
        c.tick()
    return c


def outfit():
    c = founded()
    c.tier = 2
    return c


class Trust(unittest.TestCase):
    def test_a_leg_that_sells_into_a_town_is_a_delivery_there(self):
        c = founded()
        gs, pr = c.trust['GS'], c.trust['PR']
        r = c.tick()
        into_pr = any(o == 'GS' for o, _ in r.loads)
        into_gs = any(o == 'PR' for o, _ in r.loads)
        self.assertEqual(c.trust['PR'], pr + into_pr)
        self.assertEqual(c.trust['GS'], gs + into_gs)

    def test_a_wagon_kept_home_delivers_nothing(self):
        c = founded()
        c.auto = False
        c.road_mode = cm.HOLD
        gs, pr = c.trust['GS'], c.trust['PR']
        c.tick()
        self.assertEqual((c.trust['GS'], c.trust['PR']), (gs, pr))

    def test_trust_stops_at_100(self):
        c = founded()
        c.trust['PR'] = 100
        c.tick()
        self.assertEqual(c.trust['PR'], 100)

    def test_ghost_town_gunfight_gives_goodsprings_10_once(self):
        c = founded()
        c.auto = False
        c.road_mode = cm.HOLD
        c.ghost_town_done = True
        gs = c.trust['GS']
        c.tick()
        self.assertEqual(c.trust['GS'], gs + 10)
        c.road_mode = cm.HOLD
        c.tick()
        self.assertEqual(c.trust['GS'], gs + 10)


class Gate(unittest.TestCase):
    def test_a_good_player_reaches_tier_2_by_day_14(self):
        c = founded(ghost=True)
        day = None
        for d in range(1, 29):
            c.tick()
            for m in list(c.memos):
                if m.kind == 'contract':
                    c.answer(m, 0)
            if c.tier == 2:
                day = d
                break
        self.assertIsNotNone(day)
        self.assertLessEqual(day, 14)

    def test_without_the_deed_there_is_no_tier_2(self):
        c = founded()
        c.cash += 5000
        c.trust['GS'] = 80
        c.tick()
        self.assertEqual(c.tier, 1)

    def test_the_tier_day_posts_the_tier_letter_and_it_waits(self):
        c = founded(ghost=True)
        c.cash += 5000
        c.trust['GS'] = 60
        r = c.tick()
        self.assertTrue(r.tier_up)
        self.assertEqual(c.tier, 2)
        self.assertTrue(any(x.kind == 'tier' for x in c.post))
        # a more urgent letter goes first; the tier letter is still waiting a day later
        if c.letter.kind != 'tier':
            c.field_letter()
        c.letter_shown_day = -1
        c.tick()
        kinds = [c.letter.kind] if c.letter else []
        self.assertTrue('tier' in kinds or any(x.kind == 'tier' for x in c.post))

    def test_tier_letter_text(self):
        letter = cm.Letter(9, 'tier', (2,))
        self.assertEqual(pm.letter_title(letter), 'LETTER day 9  an Outfit now')
        self.assertIn('Build screen', pm.letter_text(letter))
        self.assertLessEqual(len(pm.letter_text(letter)), 200)


class Build(unittest.TestCase):
    def test_nothing_builds_at_tier_1(self):
        c = founded()
        self.assertFalse(c.can_build('purifier'))

    def test_build_takes_owner_money_first_and_only_once(self):
        c = outfit()
        cash, own = c.cash, c.owner_funds
        c.build('purifier')
        self.assertEqual(c.owner_funds, max(0, own - 300))
        self.assertEqual(c.cash, cash - max(0, 300 - own))
        self.assertFalse(c.can_build('purifier'))

    def test_a_site_comes_with_a_hand(self):
        c = outfit()
        wages = c.daily_wages()
        c.build('well')
        self.assertEqual(c.hands, 1)
        self.assertEqual(c.daily_wages(), wages + cm.HAND_WAGE)

    def test_well_and_purifier_make_water_for_the_wagon(self):
        c = outfit()
        for b in ('well', 'purifier'):
            c.build(b)
        c.tick()
        c.tick()
        self.assertGreater(c.warehouse['water'] + c.history[-1].loads.get(('GS', 'water'), 0), 0)

    def test_no_money_no_building(self):
        c = outfit()
        c.cash, c.owner_funds = 100, 50
        self.assertFalse(c.can_build('well'))


class Screen(unittest.TestCase):
    def test_chains_row_at_tier_1_opens_the_tier_2_checklist(self):
        c, t = founded(), tm.Terminal()
        self.assertEqual(tm.labels(c, t)[6], 'CHAINS   none yet (tier 2)')
        tm.click(c, t, 6)
        self.assertEqual(t.screen, tm.BUILD)

    def test_chains_row_at_tier_2_opens_build(self):
        c, t = outfit(), tm.Terminal()
        self.assertEqual(tm.labels(c, t)[6], 'CHAINS   0 of 7 built')
        tm.click(c, t, 6)
        self.assertEqual(t.screen, tm.BUILD)
        rows = tm.labels(c, t)
        self.assertEqual(rows[0], 'MONEY  cash %d, own money %d' % (c.cash, c.owner_funds))
        self.assertEqual(rows[1], 'PURIFIER   5 dirty > 4 water   300')
        self.assertEqual(rows[3], 'WELL RIG   4 dirty water a day 200')
        self.assertEqual(rows[-1], 'BACK')
        self.assertTrue(all(len(x) <= tm.ROW_WIDTH for x in rows))

    def test_selecting_a_building_builds_it(self):
        c, t = outfit(), tm.Terminal()
        t.screen = tm.BUILD
        tm.click(c, t, 2)
        self.assertEqual(c.workshops, ['apothecary'])
        self.assertEqual(tm.labels(c, t)[2], 'APOTHECARY 1 herbs > 1 powder  BUILT')
        tm.click(c, t, 2)
        self.assertEqual(c.workshops, ['apothecary'])
        tm.click(c, t, len(cm.BUILD_ROWS) + 1)          # BACK
        self.assertEqual(t.screen, tm.FRONT)
        self.assertEqual(tm.labels(c, t)[6], 'CHAINS   1 of 7 built')


if __name__ == '__main__':
    unittest.main()

"""M1 task 1.10: the fixes from the milestone review (daily plan on, the road memo on contract days and
its odds, the tier 2 checklist, the tier-up calm, the staff cap)."""
import unittest

import company_model as cm
import post_model as pm
import terminal_model as tm


def founded():
    c = cm.Company(1234)
    c.found()
    return c


def with_contract(c):
    """Sign Primm's contract now (as if accepted): deliveries every 3 days from tomorrow."""
    r = cm.DayReport(c.day)
    c._sign(200, r)
    c.contract.start = c.contract.next_due = c.day + 1    # signed at a tick, it delivers from that day
    return c


class DailyPlan(unittest.TestCase):
    def test_the_daily_plan_starts_on(self):
        self.assertTrue(founded().auto)

    def test_a_company_left_alone_for_five_weeks_keeps_going(self):
        c = founded()
        for _ in range(35):
            c.tick()
        self.assertFalse(c.ended)
        self.assertEqual(c.stage, 'ok')
        self.assertGreater(sum(h.sales for h in c.history), 0)


class RoadMemo(unittest.TestCase):
    def test_default_is_home_without_a_delivery(self):
        c = founded()
        m = cm.Memo('road', c.day, c.day + 1)
        self.assertEqual(c.memo_default(m), cm.HOLD)
        self.assertTrue(pm.memo_text(c, m).endswith('Unanswered, it stays home.'))

    def test_default_is_send_on_a_contract_delivery_day(self):
        c = with_contract(founded())
        m = cm.Memo('road', c.day, c.contract.next_due)
        self.assertEqual(c.memo_default(m), cm.SEND)
        self.assertTrue(pm.memo_text(c, m).endswith("Unanswered, it goes: Primm's water is due."))
        self.assertEqual(pm.answer_label(m, 0, c), '  [ ] send as planned (default)')
        self.assertEqual(pm.answer_label(m, 2, c), '  [ ] keep the wagon home')

    def test_an_unanswered_road_memo_on_a_delivery_day_sends_the_wagon(self):
        c = with_contract(founded())
        due = c.contract.next_due
        while c.day < due - 1:
            c.tick()
        c.memos.append(cm.Memo('road', c.day, due))
        r = c.tick()
        self.assertEqual(r.road_mode, cm.SEND)
        self.assertTrue(r.contract.startswith('delivered'))

    def test_the_memo_gives_the_odds(self):
        c = founded()
        text = pm.memo_text(c, cm.Memo('road', c.day, c.day + 1))
        self.assertEqual(text, 'Bandit sign on the Primm road tomorrow: about 60 strong, our cover 45: 36 in 100 '
                               'to get through clean, 61 with a gun (25). Send, hire a gun, or keep it home? '
                               'Unanswered, it stays home.')

    def test_texts_fit_200_characters(self):
        c = with_contract(founded())
        for due in (c.day + 1, c.contract.next_due):
            self.assertLessEqual(len(pm.memo_text(c, cm.Memo('road', c.day, due))), 200)
        for due in (0, 1):
            letter = cm.Letter(c.day, 'road', (60, 45, 36, due))
            self.assertLessEqual(len(pm.letter_text(letter)), 200)

    def test_the_road_letter_names_the_odds_and_the_delivery(self):
        letter = cm.Letter(3, 'road', (60, 45, 36, 1))
        self.assertEqual(pm.letter_text(letter), 'Bandit sign on the Primm road tomorrow: about 60 strong, our '
                                                 'cover 45: 36 in 100 to get through clean. Keep the wagon home '
                                                 "tomorrow? Primm's water is due tomorrow.")


class TierChecklist(unittest.TestCase):
    def test_tier_1_build_screen_lists_what_tier_2_needs(self):
        c, t = founded(), tm.Terminal()
        tm.click(c, t, 6)
        self.assertEqual(tm.labels(c, t), [
            'TIER 2 (Outfit) NEEDS ALL OF THESE:',
            'WORTH    %d of 1500 earned' % c.earned_worth(),
            'TRUST    Goodsprings 35 of 50',
            'DEED     Ghost Town Gunfight: not yet',
            'STRIKES  0 in 56 days (needs 0)',
            'BACK'])
        for row in tm.labels(c, t):
            self.assertLessEqual(len(row), 39)
        tm.click(c, t, 1)                        # nothing to build yet
        self.assertEqual(c.workshops + c.sites, [])
        tm.click(c, t, 5)
        self.assertEqual(t.screen, tm.FRONT)


class TierCalm(unittest.TestCase):
    def test_no_bandits_for_two_days_after_a_new_tier(self):
        for seed in range(1, 60):
            c = cm.Company(seed)
            c.found()
            c.ghost_town_done = True
            for _ in range(40):
                r = c.tick()
                if r.tier_up:
                    self.assertFalse(c.event_fires(c.day + 1))
                    self.assertFalse(c.event_fires(c.day + 2))
                    break


class StaffCap(unittest.TestCase):
    def test_hiring_stops_at_ten(self):
        c = founded()
        while len(c.staff) < cm.STAFF_MAX:
            c.staff.append(cm.Person('Extra %d' % len(c.staff), 'guard', 50, 60, 12))
        c.candidates = [cm.Person('Late Comer', 'guard', 60, 60, 13, 'rumour')]
        self.assertFalse(c.can_hire(0))
        self.assertFalse(c.hire(0))
        t = tm.Terminal()
        t.screen, t.pick = tm.CANDIDATE, 0
        self.assertEqual(tm.labels(c, t)[1], 'HIRE: the books are full (10)')
        t.screen = tm.STAFF
        self.assertLessEqual(len(tm.labels(c, t)), 14)


if __name__ == '__main__':
    unittest.main()

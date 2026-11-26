"""Tests for the M1 post: morning report, memos, field letters (plan task 1.6)."""
import unittest

import company_model as cm
import post_model as pm
import terminal_model as tm


def founded(seed=1234, auto=True):
    c = cm.Company(seed)
    c.found()
    c.auto = auto
    return c


def run(c, days, road=None, visit=True):
    """Tick `days` days. road: answer every road memo with it (None: leave it to the default).
    visit: the player opens a terminal every morning (no away letter)."""
    for _ in range(days):
        if road is not None:
            for m in c.memos:
                if m.kind == 'road':
                    c.answer(m, road)
        c.tick()
        if visit:
            c.terminal_visit()
    return c


class Report(unittest.TestCase):
    def test_after_a_tick_the_post_screen_shows_two_pages_of_at_most_200_characters(self):
        c = run(founded(), 1)
        t = tm.Terminal()
        tm.click(c, t, 2)
        self.assertEqual(t.screen, tm.POST)
        self.assertEqual(tm.labels(c, t)[:2], ['REPORT day 1  page 1', 'REPORT day 1  page 2'])
        p1, p2 = tm.results(c, t)[:2]
        self.assertEqual((p1, p2), pm.report_pages(c))
        self.assertTrue(p1.startswith('Boss. The wagon took '))
        self.assertTrue(p2.startswith('Day 1: sales %d, costs %d, net %d.' % (
            c.history[0].sales, c.history[0].costs, c.history[0].margin)))
        self.assertLessEqual(max(len(p1), len(p2)), pm.MAX_TEXT)

    def test_no_post_before_the_first_tick(self):
        c = founded()
        t = tm.Terminal()
        t.screen = tm.POST
        self.assertEqual(tm.labels(c, t), ['No post yet.', 'BACK'])

    def test_every_text_fits_200_characters_over_100_days_and_with_huge_numbers(self):
        for seed in (1234, 7, 99, 5150):
            for road in (None, cm.SEND, cm.GUN):
                c = founded(seed)
                for _ in range(100):
                    run(c, 1, road=road, visit=c.day % 5 == 0)
                    texts = list(pm.report_pages(c)) + [pm.letter_text(x) for x in c.post]
                    texts += [pm.memo_text(c, m) for m in c.memos]
                    for text in texts:
                        self.assertLessEqual(len(text), pm.MAX_TEXT, text)
        c = run(founded(), 7, road=cm.GUN)
        c.cash, c.loan, c.arrears = 999999, 99999, 99999
        c.history[-1].sales = c.history[-1].costs = 99999
        c.history[-1].event, c.history[-1].event_loss, c.history[-1].road_mode = 'bandits_wreck', 9999, cm.GUN
        c.history[-1].bills, c.history[-1].bills_paid = {'wages': 99999}, False
        for text in pm.report_pages(c):
            self.assertLessEqual(len(text), pm.MAX_TEXT, text)

    def test_every_loss_was_forecast_the_day_before(self):
        for seed in (1234, 7, 99, 5150, 42):
            c = founded(seed)
            forecast = 'quiet'
            for _ in range(60):
                run(c, 1, road=cm.SEND)
                r = c.history[-1]
                if r.event_loss:
                    self.assertEqual(forecast, 'bandits', 'seed %d day %d' % (seed, r.day))
                forecast = c.forecast()

    def test_page_two_names_tomorrows_trouble(self):
        c = founded()
        while c.forecast() != 'bandits':
            run(c, 1)
        self.assertTrue(pm.report_pages(c)[1].endswith(
            'Tomorrow: bandit sign on the Primm road, about 60 strong, our cover 45.'))


class Memos(unittest.TestCase):
    def test_a_road_memo_comes_with_every_bandit_forecast(self):
        c = founded()
        for _ in range(30):
            run(c, 1)
            roads = [m for m in c.memos if m.kind == 'road']
            self.assertEqual(len(roads), 1 if c.forecast() == 'bandits' else 0)

    def test_unanswered_road_memo_keeps_the_wagon_home_and_spends_the_event(self):
        c = founded()
        while c.forecast() != 'bandits':
            run(c, 1)
        m = next(m for m in c.memos if m.kind == 'road')
        self.assertEqual((m.due, m.pick), (c.day + 1, None))
        cash = c.cash
        r = c.tick()
        self.assertEqual(r.road_mode, cm.HOLD)
        self.assertEqual((r.loads, r.sales, r.costs, r.event, r.event_loss), ({}, 0, 0, '', 0))
        self.assertEqual(c.last_event_day, c.day)
        self.assertEqual(c.cash, cash)
        self.assertEqual(c.memos, [])
        self.assertTrue(pm.report_pages(c)[0].startswith('Boss. The wagon stayed home today'))

    def test_a_hired_gun_costs_25_and_raises_the_cover(self):
        self.assertEqual(founded().clean_chance(cm.COVER), 36)
        self.assertEqual(founded().clean_chance(cm.COVER + cm.GUN_COVER), 61)
        c = founded()
        while c.forecast() != 'bandits':
            run(c, 1)
        c.answer(next(m for m in c.memos if m.kind == 'road'), cm.GUN)
        r = c.tick()
        self.assertEqual(r.road_mode, cm.GUN)
        self.assertIn(' We hired a gun for the road.', pm.report_pages(c)[0])
        self.assertTrue(r.event)

    def test_bandits_rob_the_strongbox_at_most_three_days_of_costs(self):
        seen = 0
        for seed in (1234, 7, 99, 5150, 42):
            c = founded(seed)
            for _ in range(60):
                run(c, 1, road=cm.SEND)
                r = c.history[-1]
                if r.event in ('bandits_took_cargo', 'bandits_wreck'):
                    seen += 1
                    self.assertGreater(r.event_loss, 0)
                    self.assertLessEqual(r.event_loss, 3 * c.daily_burn() + 1)
        self.assertGreater(seen, 5)

    def test_prepay_memo_after_paid_bills_default_keeps_the_cash_at_the_deadline(self):
        c = founded()
        run(c, 7)
        m = next(m for m in c.memos if m.kind == 'prepay')
        self.assertEqual(m.due, 10)
        loan = c.loan
        run(c, 2)
        self.assertIn(m, c.memos)
        run(c, 1)
        self.assertNotIn(m, c.memos)
        self.assertEqual(c.loan, loan)
        self.assertFalse(any(r.prepaid for r in c.history))

    def test_answered_prepay_pays_at_the_next_tick(self):
        c = founded()
        run(c, 7)
        m = next(m for m in c.memos if m.kind == 'prepay')
        loan, cash = c.loan, c.cash
        t = tm.Terminal()
        t.screen = tm.MEMOS
        row = tm.labels(c, t).index(pm.answer_label(m, 0))
        tm.click(c, t, row)
        self.assertEqual(m.pick, 0)
        self.assertTrue(tm.labels(c, t)[row].startswith('  [x] pay 300 off the loan'))
        self.assertEqual(c.loan, loan)
        r = c.tick()
        self.assertEqual((r.prepaid, c.loan), (300, loan - 300))
        self.assertNotIn(m, c.memos)
        self.assertLess(c.cash, cash)

    def test_at_most_3_memos_wait(self):
        c = founded()
        for i in range(5):
            posted = c.post_memo(cm.Memo('prepay', c.day, c.day + 3))
            self.assertEqual(posted, i < cm.MEMO_CAP)
        self.assertEqual(len(c.memos), 3)
        t = tm.Terminal()
        t.screen = tm.MEMOS
        rows = tm.labels(c, t)
        self.assertEqual(len(rows), 3 * 3 + 1)
        self.assertLessEqual(len(rows), tm.MAX_ROWS)
        self.assertEqual(tm.labels(c, tm.Terminal())[3], 'MEMOS    3 waiting, 0 due tomorrow')

    def test_three_road_style_memos_still_fit_the_screen(self):
        c = founded()
        for _ in range(3):
            c.post_memo(cm.Memo('road', c.day, c.day + 1))
        t = tm.Terminal()
        t.screen = tm.MEMOS
        self.assertEqual(len(tm.labels(c, t)), 3 * 4 + 1)
        for row in tm.labels(c, t):
            self.assertLessEqual(len(row), tm.ROW_WIDTH, row)

    def test_memo_rows_show_the_default_and_title_rows_do_nothing(self):
        c = founded()
        c.post_memo(cm.Memo('road', 0, 1))
        t = tm.Terminal()
        t.screen = tm.MEMOS
        self.assertEqual(tm.labels(c, t), ['BANDIT SIGN, PRIMM ROAD  due 1d', '  [ ] send as planned',
                                           '  [ ] hire a gun for 25', '  [ ] keep the wagon home (default)', 'BACK'])
        self.assertEqual(tm.results(c, t)[0], pm.memo_text(c, c.memos[0]))
        tm.click(c, t, 0)
        self.assertIsNone(c.memos[0].pick)


class Letters(unittest.TestCase):
    def road_day(self):
        c = founded()
        while c.forecast() != 'bandits':
            run(c, 1)
        return c

    def test_a_road_letter_waits_and_shows_only_out_of_combat_and_menus(self):
        c = self.road_day()
        self.assertEqual(c.letter, None)                # read at the terminal this morning
        c = founded()
        while True:
            c.tick()                                    # no visit after the tick that posts the memo
            if c.forecast() == 'bandits':
                break
            c.terminal_visit()
        self.assertEqual(c.letter.kind, 'road')
        self.assertIsNone(c.field_letter(in_combat=True))
        self.assertIsNone(c.field_letter(in_menu=True))
        letter = c.field_letter()
        self.assertEqual(letter.kind, 'road')
        self.assertIsNone(c.field_letter())

    def test_at_most_one_field_letter_a_day(self):
        c = founded()
        c.letter = cm.Letter(0, 'loss', ('bandits_took_cargo', 50))
        self.assertIsNotNone(c.field_letter())
        c.letter = cm.Letter(0, 'loss', ('bandits_took_cargo', 60))
        self.assertIsNone(c.field_letter())
        c.tick()
        c.letter = cm.Letter(1, 'loss', ('bandits_took_cargo', 70))
        self.assertIsNotNone(c.field_letter())

    def test_road_letter_buttons_answer_the_memo(self):
        for button, pick in ((0, cm.HOLD), (1, cm.SEND), (2, cm.GUN), (3, None)):
            c = founded()
            while c.forecast() != 'bandits':
                run(c, 1)
            letter = cm.Letter(c.day, 'road', (cm.DANGER, cm.COVER))
            c.answer_letter(letter, button)
            self.assertEqual(next(m for m in c.memos if m.kind == 'road').pick, pick)
        self.assertEqual(pm.BUTTONS['road'].split('|')[:3], ['Keep it home', 'Send as planned', 'Hire a gun (25)'])

    def test_while_you_were_away_after_3_days_once_per_absence(self):
        c = founded()
        run(c, 2, visit=False)
        self.assertFalse(any(x.kind == 'away' for x in c.post))
        run(c, 1, visit=False)
        self.assertEqual(c.letter.kind, 'away')
        days, since, sales, costs, cash, runway, memos = c.letter.values
        self.assertEqual((days, since, cash), (3, 1, c.cash))
        self.assertEqual(sales, sum(r.sales for r in c.history))
        self.assertEqual(costs, sum(r.costs for r in c.history))
        self.assertTrue(pm.letter_text(c.letter).startswith('Boss, you have been away 3 days. Since day 1:'))
        run(c, 4, visit=False)
        self.assertEqual(sum(1 for x in c.post if x.kind == 'away'), 1)
        self.assertEqual(c.letter.kind, 'away')         # kept until shown or read at a terminal
        c.terminal_visit()
        self.assertIsNone(c.letter)
        run(c, 3, visit=False)
        self.assertEqual(c.letter.kind, 'away')
        self.assertEqual(c.letter.values[:2], (3, 8))

    def test_post_lists_the_last_3_letters_newest_first(self):
        c = founded()
        run(c, 30, visit=False)
        t = tm.Terminal()
        t.screen = tm.POST
        rows = tm.labels(c, t)
        self.assertEqual(len(rows), 2 + min(3, len(c.post)) + 1)
        self.assertEqual(rows[2], pm.letter_title(c.post[-1]))
        self.assertEqual(tm.results(c, t)[2], pm.letter_text(c.post[-1]))


if __name__ == '__main__':
    unittest.main()

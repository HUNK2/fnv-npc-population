"""Tests for the debt ladder, strikes, cures and the busy shield (M1 plan task 1.7).

Rules from docs/design.md, Losing and coming back: the served-notice rule, the ladder on days 0/3/5/7
after serving, probation, strikes over 56 days, the takeover, the cures, the busy shield."""
import unittest

import company_model as cm
import post_model as pm
import terminal_model as tm


def fresh(seed=1234):
    c = cm.Company(seed)
    c.found()
    return c


def days(c, n, cash=None):
    """Tick n days; with `cash`, the company's cash is held at most that (sales spent elsewhere)."""
    out = []
    for _ in range(n):
        if cash is not None:
            c.cash = min(c.cash, cash)
        out.append(c.tick())
        if cash is not None:
            c.cash = min(c.cash, cash)
    return out


def broke(c=None, serve=True):
    """A company that misses day 7's bills; the notice is served by its field letter when `serve`."""
    c = c or fresh()
    days(c, 7 - c.day % 7, cash=50)
    if serve:
        letter = c.field_letter()
        assert letter and letter.kind == 'notice', letter
    return c


class Serving(unittest.TestCase):
    def test_a_miss_defers_until_the_notice_reaches_the_player(self):
        c = broke(serve=False)
        self.assertFalse(c.history[-1].bills_paid)
        self.assertEqual(c.stage, 'deferred')
        self.assertEqual(c.strikes, [])
        self.assertGreater(c.arrears, 0)
        days(c, 3, cash=0)
        self.assertEqual(c.stage, 'deferred')          # no clock while it is not served

    def test_the_field_letter_serves_it(self):
        c = broke()
        self.assertEqual(c.stage, 'grace')
        self.assertEqual(c.strikes, [7])
        self.assertEqual(c.served_day, 7)

    def test_a_terminal_visit_serves_it(self):
        c = broke(serve=False)
        days(c, 2, cash=0)
        c.terminal_visit()
        self.assertEqual((c.stage, c.strikes, c.served_day), ('grace', [9], 9))
        self.assertIsNone(c.letter)

    def test_paid_before_it_is_served_is_still_a_strike(self):
        c = broke(serve=False)
        c.cash = 5000
        c.tick()                                        # day 8: the arrears are paid from cash
        self.assertEqual((c.arrears, c.stage), (0, 'deferred'))
        c.terminal_visit()
        self.assertEqual((c.stage, c.strikes), ('probation', [8]))

    def test_a_deferred_notice_letter_is_rewritten_every_day(self):
        c = broke(serve=False)
        first = c.letter
        days(c, 1, cash=0)
        self.assertEqual(c.letter.kind, 'notice')
        self.assertEqual(c.letter.day, 8)
        self.assertEqual(sum(1 for x in c.post if x.kind == 'notice'), 1)   # posted once
        self.assertEqual(first.values[0], 'grace')


class Ladder(unittest.TestCase):
    def test_final_notice_seizure_receivership_on_days_3_5_7(self):
        c = broke()
        stages = []
        for _ in range(7):
            days(c, 1, cash=0)
            stages.append(c.stage)
        self.assertEqual(stages, ['grace', 'grace', 'final', 'final', 'seized', 'seized', 'seized'])
        self.assertFalse(c.wagon_ok)
        self.assertTrue(c.ended)
        self.assertEqual(c.end_reason, 'receivership')
        self.assertEqual(c.letter.kind, 'closed')

    def test_paying_down_at_the_final_notice_keeps_the_wagon(self):
        c = broke()
        days(c, 3, cash=0)
        self.assertEqual(c.stage, 'final')
        need = c.final_need()
        self.assertGreater(need, 0)
        c.arrears -= need                                # paid down to 40%
        days(c, 2, cash=0)
        self.assertTrue(c.wagon_ok)
        self.assertEqual(c.stage, 'seized')              # the step passes without a seizure

    def test_stage_letters_are_posted(self):
        c = broke()
        days(c, 3, cash=0)
        self.assertEqual(c.letter.kind, 'notice')
        self.assertEqual(c.letter.values[0], 'final')
        days(c, 2, cash=0)
        self.assertEqual(c.letter.values[0], 'seized')

    def test_probation_lasts_14_days_and_a_second_miss_skips_grace(self):
        c = broke()
        c.cash = 5000
        c.tick()                                          # day 8: cured
        self.assertEqual(c.stage, 'probation')
        days(c, 6, cash=50)                               # day 14: missed again on probation
        letter = c.field_letter()
        self.assertEqual(letter.values[0], 'final')
        self.assertEqual(c.stage, 'final')
        self.assertEqual(c.days_left(), 2)                # seizure in 2 days, not 5
        days(c, 2, cash=0)
        self.assertFalse(c.wagon_ok)

    def test_probation_ends(self):
        c = broke()
        c.cash = 5000
        c.tick()
        days(c, 14)
        self.assertEqual(c.stage, 'ok')

    def test_third_strike_in_56_days_is_a_takeover(self):
        c = fresh()
        c.strikes = [1, 3]
        c.day = 6
        broke(c)
        self.assertEqual(c.stage, 'takeover')
        self.assertEqual(c.rescue_amount(), 0)            # never with owner money
        self.assertEqual(c.letter_buttons(cm.Letter(7, 'notice', ())), ['later', 'sell'])
        days(c, 7, cash=0)
        self.assertTrue(c.ended)
        self.assertEqual(c.end_reason, 'takeover')

    def test_curing_a_takeover_clears_the_oldest_strike(self):
        c = fresh()
        c.strikes = [1, 3]
        c.day = 6
        broke(c)
        c.cash = 5000
        c.tick()
        self.assertEqual(c.stage, 'probation')
        self.assertEqual(c.strikes, [3, 7])

    def test_strikes_count_56_days(self):
        c = fresh()
        c.strikes = [1]
        c.day = 62
        self.assertEqual(c.recent_strikes(), [])


class Cures(unittest.TestCase):
    def test_owner_rescue_from_the_pocket(self):
        c = broke()
        owed, worth = c.arrears, c.earned_worth()
        c.pocket = owed - 1
        self.assertFalse(c.owner_rescue())                 # not enough caps on you
        c.pocket = owed + 10
        self.assertTrue(c.owner_rescue())
        self.assertEqual((c.arrears, c.pocket, c.stage), (0, 10, 'probation'))
        self.assertEqual(c.strikes, [7])                   # the strike stays
        self.assertEqual(c.earned_worth(), worth)          # owner money never counts toward a tier

    def test_owner_rescue_once_a_season(self):
        c = broke()
        c.pocket = 10000
        c.owner_rescue()
        c.tick()
        days(c, 6, cash=50)                                # day 14: missed again
        c.field_letter()
        self.assertEqual(c.rescue_amount(), 0)
        self.assertNotIn('rescue', c.letter_buttons(cm.Letter(14, 'notice', ())))

    def test_owner_rescue_is_capped_at_two_weeks_of_bills(self):
        c = broke()
        c.arrears = 5000
        self.assertEqual(c.rescue_amount(), c.rescue_cap())
        self.assertEqual(c.rescue_cap(), 2 * (c.week_running_costs() + 300))

    def test_sell_the_wagon(self):
        c = broke()
        value = cm.half_up(0.6 * c.wagon_value())
        self.assertEqual(c.sell_value(), value)
        owed, cash = c.arrears, c.cash
        self.assertTrue(c.sell_wagon())
        self.assertFalse(c.wagon_ok)
        self.assertEqual(c.arrears, max(0, owed - cash - value))
        self.assertEqual(c.sell_value(), 0)

    def test_buy_a_wagon_back_once_nothing_is_owed(self):
        c = broke()
        c.sell_wagon()
        self.assertFalse(c.can_buy_wagon())
        c.arrears, c.cash = 0, 900
        self.assertTrue(c.buy_wagon())
        self.assertTrue(c.wagon_ok)
        self.assertEqual(c.cash, 200)

    def test_walk_away(self):
        c = fresh()
        self.assertFalse(c.walk_away())                    # only with a served notice
        broke(c)
        self.assertTrue(c.walk_away())
        self.assertEqual((c.ended, c.end_reason), (True, 'walked'))

    def test_notice_letter_buttons_answer(self):
        c = broke(serve=False)
        c.pocket = 5000
        letter = c.field_letter()
        buttons = c.letter_buttons(letter)
        self.assertEqual(buttons, ['later', 'rescue', 'sell'])
        c.answer_letter(letter, 1, buttons)
        self.assertEqual(c.stage, 'probation')


class Forecast(unittest.TestCase):
    def test_runway_under_5_days_warns_once_a_bill_cycle(self):
        c = fresh()
        days(c, 7)
        self.assertEqual(c.forecast_short(), 0)
        c.cash = 4 * c.daily_burn()
        self.assertEqual(c.forecast_short(), pm.bill_estimate(c) - c.cash)
        c.tick()
        self.assertEqual(c.letter.kind, 'forecast')
        n = sum(1 for x in c.post if x.kind == 'forecast')
        c.cash = 4 * c.daily_burn()
        c.tick()
        self.assertEqual(sum(1 for x in c.post if x.kind == 'forecast'), n)
        self.assertTrue(tm.notice_row(c).startswith('WARNING'))

    def test_no_warning_while_a_notice_is_open(self):
        c = broke()
        c.cash = 0
        self.assertEqual(c.forecast_short(), 0)


class Shield(unittest.TestCase):
    def test_clocks_stop_in_dlc_lands(self):
        c = broke()
        c.shield = True
        days(c, 10, cash=0)
        self.assertFalse(c.ended)
        self.assertEqual(c.stage, 'grace')
        self.assertEqual(c.days_left(), 3)

    def test_no_runner_finds_you_there(self):
        c = broke(serve=False)
        c.shield = True
        days(c, 2, cash=0)
        self.assertIsNone(c.field_letter())
        self.assertEqual(c.stage, 'deferred')

    def test_paper_losses_are_capped_at_a_days_profit(self):
        for seed in range(1, 40):
            c = fresh(seed)
            c.shield = True
            for _ in range(20):
                prev = c.history[-1].margin if c.history else 0
                for m in c.memos:
                    c.answer(m, cm.SEND)
                c.queue_list = c.plan()
                r = c.tick()
                self.assertLessEqual(r.event_loss, max(0, prev), 'seed %d day %d' % (seed, r.day))


class Texts(unittest.TestCase):
    def test_notice_texts_fit(self):
        for st in ('grace', 'final', 'seized', 'takeover', 'probation'):
            t = pm.notice_text((st, 12345, 12345, 7, 3))
            self.assertLessEqual(len(t), pm.MAX_TEXT, t)
        for reason in ('receivership', 'takeover', 'walked'):
            self.assertLessEqual(len(pm.letter_text(cm.Letter(1, 'closed', (reason,)))), pm.MAX_TEXT)
        self.assertLessEqual(len(pm.letter_text(cm.Letter(1, 'forecast', (12345, 7)))), pm.MAX_TEXT)

    def test_notice_screen_rows_fit(self):
        c = broke()
        c.pocket = 99999
        t = tm.Terminal()
        t.screen = tm.NOTICE
        for row in tm.labels(c, t):
            self.assertLessEqual(len(row), tm.ROW_WIDTH, row)
        self.assertLessEqual(len(tm.notice_row(c)), tm.ROW_WIDTH)


if __name__ == '__main__':
    unittest.main()

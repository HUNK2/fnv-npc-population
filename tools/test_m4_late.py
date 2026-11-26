"""M4 model tests (docs/plans/2026-11-28-m4-ending.md): forward contracts, the NCR quartermaster, lending,
share blocks, laws, tier 5 and the ending pages. Below tier 3 nothing changes.

    python tools/test_m4_late.py
"""
import unittest

import company_model as cm
import ending_model as em
import late_model as late


def tier(n, seed=1234, **kw):
    c = cm.Company(seed, sheriff=True)
    c.found()
    c.auto = True
    c.tier = n
    c._tier3_day()
    for k, v in kw.items():
        setattr(c, k, v)
    return c


def ticket(c, town='PR', good='water', price=100, advance=0, due=None):
    t = late.Ticket(town, good, price, c.day, c.day + late.FWD_DAYS if due is None else due, advance)
    c.tickets.append(t)
    return t


class Forward(unittest.TestCase):
    def test_no_offer_below_tier_three(self):
        c = cm.Company(1234)
        c.found()
        c.auto = True
        for _ in range(21):
            c.tick()
            self.assertFalse(any(m.kind == 'forward' for m in c.memos))

    def test_offer_on_day_two_of_a_week(self):
        c = tier(3)
        c.day = 8                       # the post after tick 9 ... post on day 9 % 7 == 2
        r = cm.DayReport(9)
        c.day = 9
        c._post_fwd(r)
        m = [x for x in c.memos if x.kind == 'forward']
        self.assertEqual(len(m), 1)
        self.assertEqual(m[0].price, c.fwd_price(m[0].town, m[0].good))

    def test_ticket_takes_crates_before_the_market(self):
        c = tier(3)
        t = ticket(c, price=100)
        r = cm.DayReport(1)
        cash, stock = c.cash, c.stock['PR']['water']
        self.assertTrue(c._fwd_take(r, 'PR', 'water'))
        self.assertEqual(c.cash - cash, 100)
        self.assertEqual(c.stock['PR']['water'], stock)         # not sold to the market
        self.assertEqual((t.filled, r.fwd_crates, r.sales), (1, 1, 100))
        self.assertFalse(c._fwd_take(r, 'PR', 'meat'))

    def test_filled_pays_and_trusts(self):
        c = tier(3)
        t = ticket(c, price=50)
        t.filled = late.FWD_CRATES - 1
        trust = c.trust['PR']
        r = cm.DayReport(1)
        c._fwd_take(r, 'PR', 'water')
        self.assertEqual(c.tickets, [])
        self.assertEqual(r.fwd, 'filled')
        self.assertEqual(c.trust['PR'], trust + late.FWD_DONE_TRUST)

    def test_advance_is_earned_back_by_crates(self):
        c = tier(3)
        m = cm.Memo('forward', c.day, c.day + 1, price=100, town='PR', good='water')
        r = cm.DayReport(1)
        cash = c.cash
        c._settle_fwd(r, m, 1)
        adv = cm.half_up(0.5 * 12 * 100)
        self.assertEqual((c.cash - cash, r.fwd_adv, c.tickets[0].advance), (adv, adv, adv))
        cash = c.cash
        c._fwd_take(r, 'PR', 'water')
        self.assertEqual(c.cash, cash)                          # the first crates repay the advance
        self.assertEqual(c.tickets[0].advance, adv - 100)

    def test_miss_charges_a_quarter_and_owes_the_advance(self):
        c = tier(3)
        t = ticket(c, price=100, advance=600, due=c.day)
        t.filled = 4
        cash, arrears, trust = c.cash, c.arrears, c.trust['PR']
        r = cm.DayReport(c.day)
        c._day_fwd(r)
        self.assertEqual(r.fwd, 'missed')
        self.assertEqual(c.cash, cash - cm.half_up(0.25 * 8 * 100))
        self.assertEqual(c.arrears, arrears + 600)
        self.assertEqual(c.trust['PR'], max(0, trust + late.FWD_MISS_TRUST))
        self.assertEqual(c.tickets, [])

    def test_at_most_three_open(self):
        c = tier(3)
        for g in ('water', 'meat', 'ammo'):
            ticket(c, good=g)
        c.day = 9
        c._post_fwd(cm.DayReport(9))
        self.assertFalse(any(m.kind == 'forward' for m in c.memos))

    def test_planner_routes_ticket_crates(self):
        c = tier(3)
        c.cash = 5000
        g = next(x for x in ('water', 'ammo', 'meat', 'powder') if c.has_market('PR', x) and c.has_market('GS', x))
        ticket(c, 'PR', g, price=c.price('GS', g, 'buy') + 50)
        orders = [o for o in c.plan() if o.town == 'GS']
        self.assertGreaterEqual(sum(1 for o in orders if o.good == g), 1)

    def test_advance_counts_against_worth(self):
        c = tier(3)
        w = c.net_worth()
        ticket(c, advance=500)
        self.assertEqual(c.net_worth(), w - 500)


class Quartermaster(unittest.TestCase):
    def test_offered_at_tier_four_with_standing(self):
        c = tier(4, ncr_standing=59)
        c._post_qm(cm.DayReport(1))
        self.assertFalse(c.qm_offered)
        c.ncr_standing = 60
        c._post_qm(cm.DayReport(1))
        self.assertTrue(c.qm_offered)
        self.assertEqual([m.kind for m in c.memos], ['patron'])

    def test_bill_and_repay(self):
        c = tier(4)
        c._settle_qm(cm.DayReport(1), 0)
        self.assertEqual(c.qm_loan, late.QM_LOAN)
        self.assertEqual(c.qm_bill(), (200, 500))
        c._qm_paid(700)
        self.assertEqual(c.qm_loan, late.QM_LOAN - 500)
        c._qm_paid(150)                                         # interest only, partly paid
        self.assertEqual(c.qm_loan, late.QM_LOAN - 500)

    def test_broken_string_makes_the_rest_arrears(self):
        c = tier(4, ncr_standing=80)
        c._settle_qm(cm.DayReport(1), 0)
        c.qm_loan = 5000                                        # half repaid
        arrears = c.arrears
        c.heat = late.QM_HEAT
        r = cm.DayReport(7)
        c._qm_string(r)
        self.assertEqual((c.qm, c.qm_loan, r.patron), (False, 0, 'broken'))
        self.assertEqual(c.arrears, arrears + 5000)
        self.assertEqual(c.ncr_standing, 50)

    def test_kept_after_28_days(self):
        c = tier(4)
        c._settle_qm(cm.DayReport(1), 0)
        c.day += 27
        self.assertFalse(c.patron_kept())
        c.day += 1
        self.assertTrue(c.patron_kept())


class Lending(unittest.TestCase):
    def test_lend_and_repay(self):
        c = tier(4)
        c.cash = 10000
        m = cm.Memo('lend', c.day, c.day + 2, price=2000, town='PR', who='Primm Haulers')
        aggr = c.aggr
        c._settle_lend(cm.DayReport(1), m, 1)
        self.assertEqual(c.cash, 8000)
        self.assertEqual(c.aggr, aggr + late.LEND_AGGR)
        o = c.outfits[0]
        self.assertEqual((o.amount, o.left, o.rate), (2000, 2000, 1))

    def test_refuse_or_short_of_cash(self):
        c = tier(4)
        c.cash = 500
        m = cm.Memo('lend', c.day, c.day + 2, price=1000, town='PR', who='Primm Haulers')
        c._settle_lend(cm.DayReport(1), m, 0)
        c._settle_lend(cm.DayReport(1), m, 3)
        self.assertEqual(c.outfits, [])

    def test_seize_never_exceeds_principal_owed(self):
        c = tier(4)
        o = late.Outfit('Primm Haulers', 'PR', 3000, 2)
        o.left = 400
        c.outfits.append(o)
        cash = c.cash
        r = cm.DayReport(1)
        c._settle_outfit(r, cm.Memo('outfit', 1, 4, price=400, town='PR', who='Primm Haulers'), 0)
        self.assertEqual(r.outfit_got, 400)
        self.assertEqual(c.cash - cash, 400)
        o = late.Outfit('Harlan Freight', 'GS', 3000, 2)
        c.outfits.append(o)
        r = cm.DayReport(1)
        c._settle_outfit(r, cm.Memo('outfit', 1, 4, who='Harlan Freight', town='GS'), 0)
        self.assertEqual(r.outfit_got, 1500)                    # half its value

    def test_forgive_raises_trust(self):
        c = tier(4)
        c.outfits.append(late.Outfit('Harlan Freight', 'GS', 1000, 0))
        t = c.trust['GS']
        c._settle_outfit(cm.DayReport(1), cm.Memo('outfit', 1, 4, who='Harlan Freight', town='GS'), 1)
        self.assertEqual(c.trust['GS'], min(100, t + late.FORGIVE_TRUST))
        self.assertEqual(c.forgiven_n, 1)

    def test_two_misses_post_the_failure_memo(self):
        c = tier(4)
        o = late.Outfit('Harlan Freight', 'GS', 1000, 2)
        o.misses = 1
        c.outfits.append(o)
        for d in range(7, 400, 7):                              # a week whose roll misses
            c.day = d
            if cm.roll(c.seed, d, late.ROLL_MISS) < late.LEND_MISS[2]:
                break
        c._week_lend(cm.DayReport(c.day))
        self.assertEqual([m.kind for m in c.memos], ['outfit'])


class SharesLawsTierFive(unittest.TestCase):
    def test_blocks_in_order(self):
        c = tier(4)
        c.cash = 50000
        self.assertFalse(c.buy_block())
        c.lead_pr_weeks = late.LEAD_WEEKS
        self.assertTrue(c.buy_block())
        self.assertFalse(c.buy_block())                         # the NCR bid deed is not done
        c.won_vs_her = True
        self.assertTrue(c.buy_block())
        self.assertTrue(c.buy_block())
        self.assertEqual((c.blocks, c.rival_out, c.aggr), (3, True, 0))
        self.assertEqual(c.cash, 50000 - sum(late.BLOCK_PRICE))

    def test_rival_out_stops_her_moves(self):
        c = tier(4, rival_out=True, aggr=0)
        c.last_share = {t: 0 for t in cm.TOWNS}
        c.sold_week = {t: 999 for t in cm.TOWNS}
        r = cm.DayReport(7)
        r.bills_paid = True
        c._week_law(r)
        self.assertEqual((c.aggr, r.rival), (0, ''))

    def test_tier_five_gate(self):
        c = tier(4)
        c.cash, c.loan = late.TIER5_WORTH + c.owner_paid_in + 10000, 0
        c.last_share = {'GS': 0.2, 'PR': 0.2, 'SL': 0.2, 'MO': 0.0}
        self.assertFalse(c.tier_five_ready())                   # no blocks, no patron
        c.blocks = 3
        self.assertTrue(c.tier_five_ready())
        c.last_share['SL'] = 0.05
        self.assertFalse(c.tier_five_ready())                   # leads only 2 towns

    def test_laws(self):
        c = tier(5, favour=10)
        self.assertTrue(c.pass_law())
        self.assertEqual(c.laws, ['duty'])
        self.assertFalse(c.pass_law())                          # once a season
        self.assertEqual(c.law_duty(101), 51)                   # the Free trade act halves the duty
        c.day = 28 * 3
        self.assertTrue(c.pass_law())
        c.week_sales = 1000
        r = cm.DayReport(c.day)
        c._bills(r)
        self.assertNotIn('licence', r.bills)                    # the Carrier act
        self.assertEqual(r.bills['duty'], cm.half_up(cm.duty(1000) / 2))

    def test_good_player_reaches_tier_five(self):
        import balance_run
        o = balance_run.play('good', 120, 1234)
        self.assertIsNotNone(o['tier5'])
        self.assertLessEqual(o['tier5'], 100)
        self.assertNotIn('missed', o['fwd'])

    def test_ncr_delivery_gives_favour(self):
        c = tier(4)
        k = cm.Contract('ammo', 4, 3, 100, 1, 1, town='MO', road=3, origin='PR', days=14, ncr=True)
        c._ncr_delivered(k)
        self.assertEqual(c.favour, 1)


class Ending(unittest.TestCase):
    def test_retire_only_at_tier_five(self):
        c = tier(4)
        self.assertFalse(c.retire())
        c.tier = 5
        self.assertTrue(c.retire())
        self.assertEqual((c.ended, c.end_reason), (True, 'retired'))
        self.assertEqual(len(c.ending), 3)
        self.assertFalse(c.retire())

    def test_every_reason_writes_three_pages(self):
        for reason in ('receivership', 'takeover', 'walked', 'revoked', 'retired'):
            c = tier(3)
            c._end(cm.DayReport(1), reason)
            self.assertEqual(len(c.ending), 3, reason)
            self.assertTrue(c.ending[0][1][0].startswith('Twenty years on'), reason)
            for title, lines in c.ending:
                self.assertTrue(lines)
                for ln in lines:
                    self.assertNotIn('%', ln)

    def test_written_once(self):
        c = tier(5)
        c.retire()
        first = c.ending
        c._write_ending()
        self.assertIs(c.ending, first)

    def test_two_seeds_differ(self):
        texts = set()
        for seed in (1234, 77, 9001):
            c = tier(5, seed)
            c.retire()
            texts.add(str(c.ending))
        self.assertGreater(len(texts), 1)

    def test_ending_pages_survive_the_days_other_letters(self):
        # a receivership on a day the player has been away (and a robbery): the three pages stay
        c = tier(3)
        c.day = 20
        r = cm.DayReport(c.day)
        c._end(r, 'receivership')
        c.last_visit, c.away_posted = c.day - 5, False
        r.event, r.event_loss, r.ev_road = 'bandits_took_cargo', 50, 0
        c._post_letters(r, road=False)
        self.assertEqual([x.kind for x in c.post], ['ending'] * 3)

    def test_about_sixty_lines(self):
        self.assertGreaterEqual(em.line_count(), 55)



class Screens(unittest.TestCase):
    def test_contracts_list_tickets(self):
        import terminal_model as tm
        c = tier(3)
        ticket(c, 'PR', 'water')
        self.assertIn('FWD PR water 0/12 by %d' % (c.day + late.FWD_DAYS), tm.contract_rows(c))

    def test_shares_and_laws_rows(self):
        import terminal_model as tm
        c = tier(3)
        self.assertEqual(tm.late_rows(c), [])
        c.tier = 4
        self.assertEqual(tm.late_rows(c), ['SHARES   0 of 3: lead in Primm 14 days'])
        c.lead_pr_weeks = late.LEAD_WEEKS
        self.assertEqual(tm.late_rows(c), ['SHARES   0 of 3: BUY a block for 5000'])
        c.tier, c.favour = 5, 6
        self.assertEqual(tm.late_rows(c)[1], 'LAWS     favour 6: PASS Free trade act')

    def test_share_row_click_buys(self):
        import terminal_model as tm
        c = tier(4)
        c.cash, c.lead_pr_weeks = 20000, late.LEAD_WEEKS
        t = tm.Terminal() if hasattr(tm, 'Terminal') else None
        if t is None:
            self.skipTest('no Terminal state class')
        t.screen = tm.TOWNS_SCREEN
        rows = tm.labels(c, t)
        tm.click(c, t, rows.index('SHARES   0 of 3: BUY a block for 5000'))
        self.assertEqual(c.blocks, 1)

    def test_retire_needs_confirm_and_post_stays_open(self):
        import terminal_model as tm
        c = tier(5)
        if not hasattr(tm, 'Terminal'):
            self.skipTest('no Terminal state class')
        t = tm.Terminal()
        t.screen = tm.SETTINGS
        tm.click(c, t, 1)
        self.assertFalse(c.ended)
        self.assertEqual(tm.labels(c, t)[1], 'RETIRE?  select again to hand it on')
        tm.click(c, t, 1)
        self.assertTrue(c.ended)
        self.assertEqual(tm.labels(c, t)[2], 'POST     the last letters')
        tm.click(c, t, 2)
        rows = tm.labels(c, t)
        self.assertEqual([r for r in rows if '20 years on' in r], ['LETTER day %d  20 years on' % c.day] * 3)


    def test_new_texts_fit(self):
        import post_model as pm
        import terminal_model as tm
        c = tier(5, favour=12)
        for k, kw in (('forward', dict(price=250, town='MO', good='materials')), ('patron', dict(price=10000)),
                      ('lend', dict(price=3000, town='SL', who='Sloan Stone Co.')),
                      ('outfit', dict(price=3000, town='SL', who='Sloan Stone Co.'))):
            m = cm.Memo(k, 100, 103, **kw)
            self.assertLessEqual(len(pm.memo_title(c, m)), 39, k)
            self.assertLessEqual(len(pm.memo_text(c, m)), pm.MAX_TEXT, k)
            for i in range(len(m.answers)):
                self.assertLessEqual(len(pm.answer_label(m, i, c)), 39, k)
        ticket(c, 'MO', 'materials', due=999)
        rows = tm.forward_rows(c) + tm.late_rows(c)
        c.rival_out = True
        rows += tm.late_rows(c)
        for r in rows:
            self.assertLessEqual(len(r), 39, r)
        self.assertLessEqual(len(pm.TIER5_TEXT), pm.MAX_TEXT)

    def test_ending_pages_fit(self):
        for seed in range(1, 40):
            for reason in ('receivership', 'takeover', 'walked', 'revoked', 'retired'):
                c = tier(5, seed, staff=[], poached_name='Bess Marlowe', laws=['duty'], qm=True, seized_n=2,
                         lent_ever=True)
                c._end(None, reason)
                for title, lines in c.ending:
                    self.assertLessEqual(len(' '.join(lines)), 200)
                    self.assertTrue(lines)


if __name__ == '__main__':
    unittest.main()

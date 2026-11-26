"""M1 1.8: supply contracts, standing orders, paper staff and hiring (company, post and terminal models)."""
import unittest

import company_model as cm
import post_model as pm
import terminal_model as tm


def founded(days=0, seed=1234):
    c = cm.Company(seed)
    c.found()
    c.auto = True
    for _ in range(days):
        c.tick()
    return c


def answer_all(c, kind, pick):
    for m in c.memos:
        if m.kind == kind:
            c.answer(m, pick)


class Staff(unittest.TestCase):
    def test_founders_give_the_old_cover_and_wages(self):
        c = founded()
        self.assertEqual([(p.name, p.role) for p in c.staff], list(cm.FOUNDERS))
        self.assertEqual(c.cover(), 45)
        self.assertEqual(c.daily_wages(), 22)

    def test_candidates_come_on_day_1_of_each_week(self):
        c = founded(1)
        self.assertTrue(3 <= len(c.candidates) <= 6)
        names = [p.name for p in c.candidates]
        self.assertEqual(len(set(names)), len(names))
        self.assertFalse(set(names) & {n for n, _ in cm.FOUNDERS})
        for p in c.candidates:
            self.assertIn(p.role, ('driver', 'guard'))
            self.assertTrue(30 <= p.skill < 80 and 10 <= p.honesty < 95)
            self.assertEqual(p.wage, cm.ROLE_WAGE[p.role] + max(0, (p.skill - 50) // 10))
            self.assertIn(p.rumour, cm.RUMOURS)
        first = names
        for _ in range(6):
            c.tick()
        self.assertEqual(c.day, 7)
        self.assertEqual([p.name for p in c.candidates], first)     # same list all week
        c.tick()
        self.assertNotEqual([p.name for p in c.candidates], first)

    def test_hiring_a_guard_raises_cover_and_wages(self):
        c = founded(1)
        i = next(k for k, p in enumerate(c.candidates) if p.role == 'guard')
        g = c.candidates[i]
        self.assertTrue(c.hire(i))
        self.assertEqual(c.cover(), 45 + 30 + (g.skill - 50) // 5)
        self.assertEqual(c.daily_wages(), 22 + g.wage)
        self.assertNotIn(g, c.candidates)

    def test_only_one_driver(self):
        c = founded(1)
        c.candidates.append(cm.Person('Test Driver', 'driver', 60, 60, 11))
        i = len(c.candidates) - 1
        self.assertFalse(c.can_hire(i))
        self.assertFalse(c.hire(i))
        c.fire(0)                                   # Ruth, the driver
        self.assertTrue(c.hire(i))

    def test_no_driver_keeps_the_wagon_home(self):
        c = founded(2)
        c.fire(0)
        self.assertEqual(c.cover(), 0)
        cash = c.cash
        r = c.tick()
        self.assertFalse(r.crew)
        self.assertEqual(r.loads, {})
        self.assertEqual(r.sales, 0)
        self.assertEqual(r.event, '')
        self.assertLess(c.cash, cash + 1)
        self.assertIn('no driver', pm.report_pages(c)[0])
        self.assertNotEqual(c.forecast(), 'bandits')

    def test_reference_check(self):
        c = founded(1)
        cash = c.cash
        self.assertTrue(c.reference_check(0))
        self.assertEqual(c.cash, cash - cm.REF_CHECK)
        self.assertFalse(c.reference_check(0))              # already checked: no second charge
        self.assertEqual(c.cash, cash - cm.REF_CHECK)
        self.assertIn(c.honesty_band(c.candidates[0]), ('low', 'fair', 'high'))

    def test_dishonest_staff_skim_two_percent_of_sales(self):
        a, b = founded(2), founded(2)
        b.staff.append(cm.Person('Sly Hand', 'guard', 50, 20, 0))
        a.staff.append(cm.Person('Good Hand', 'guard', 50, 80, 0))
        ra, rb = a.tick(), b.tick()
        self.assertGreater(ra.sales, 0)
        self.assertEqual(ra.sales, rb.sales)
        self.assertEqual(rb.skim, cm.half_up(cm.SKIM_SHARE * rb.sales))
        self.assertEqual(rb.costs - ra.costs, rb.skim)
        self.assertEqual(ra.skim, 0)


class Contracts(unittest.TestCase):
    def test_offer_on_day_3_declined_by_default(self):
        c = founded(3)
        offers = [m for m in c.memos if m.kind == 'contract']
        self.assertEqual(len(offers), 1)
        m = offers[0]
        self.assertEqual((m.day, m.due), (3, 4))
        self.assertEqual(m.price, c.offer_price())
        self.assertEqual(m.answers[0], 'accept at %d' % m.price)
        self.assertEqual(MEMO_DEFAULT_CONTRACT, 2)
        c.tick()
        self.assertIsNone(c.contract)
        self.assertFalse(any(m.kind == 'contract' for m in c.memos))
        for _ in range(5):
            c.tick()
            self.assertFalse(any(m.kind == 'contract' for m in c.memos))
        c.tick()                                                    # day 10: the next offer
        self.assertTrue(any(m.kind == 'contract' for m in c.memos))

    def test_offer_price_is_primm_sell_at_normal_stock_plus_9(self):
        c = founded()
        want = cm.half_up(1.09 * c.price('PR', 'water', 'sell', c.normal['PR']['water']))
        self.assertEqual(c.offer_price(), want)

    def test_accepted_contract_delivers_every_3_days_for_28(self):
        c = founded(3)
        answer_all(c, 'contract', 0)
        price = c.memos[-1].price
        trust = c.trust['PR']
        r = c.tick()                                                # day 4: signed and first delivery
        self.assertEqual(r.signed, price)
        self.assertEqual(r.contract, 'delivered')
        self.assertIsNotNone(c.contract)
        self.assertEqual(c.contract.next_due, 7)
        self.assertEqual(c.trust['PR'], trust + 1)
        gs = sum(n for (o, _), n in r.loads.items() if o == 'GS')
        self.assertLessEqual(gs, cm.CRATES_PER_LEG - cm.CONTRACT_CRATES)
        self.assertIn('Primm got its water', pm.report_pages(c)[0])
        days = {4}
        while c.contract is not None:
            r = c.tick()
            if r.contract:
                days.add(r.day)
        self.assertEqual(sorted(days), list(range(4, 4 + cm.CONTRACT_DAYS, 3)))
        self.assertTrue(r.contract.endswith('completed'))

    def test_delivery_sells_at_the_contract_price_without_moving_primm(self):
        c = founded(3)
        answer_all(c, 'contract', 0)
        price = c.memos[-1].price
        c.auto = False                                  # nothing else on the wagon
        before = c.stock['PR']['water']
        r = c.tick()
        self.assertEqual(r.sales, cm.CONTRACT_CRATES * price)
        # Primm's stock only restocks overnight toward normal; no contract crate is added to it
        self.assertAlmostEqual(c.stock['PR']['water'], cm.restock(before, c.normal['PR']['water']))

    def test_a_kept_home_delivery_is_a_miss(self):
        c = founded(3)
        answer_all(c, 'contract', 0)
        c.tick()                                        # day 4: delivered
        for _ in range(2):
            c.tick()
        c.road_mode = cm.HOLD                            # day 7: kept home
        trust, cash = c.trust['PR'], c.cash
        r = c.tick()
        self.assertEqual(r.contract, 'missed')
        self.assertEqual(c.trust['PR'], trust - 3)
        self.assertEqual(c.contract.missed, 1)
        miss = cm.half_up(cm.CONTRACT_MISS * cm.CONTRACT_CRATES * c.contract.price)
        self.assertLessEqual(miss, r.costs)

    def test_counter_walks_or_signs_higher(self):
        walked = signed = 0
        for seed in range(1, 40):
            c = founded(3, seed)
            m = next((x for x in c.memos if x.kind == 'contract'), None)
            if m is None:
                continue
            c.answer(m, 1)
            r = c.tick()
            if r.contract == 'walked':
                walked += 1
                self.assertIsNone(c.contract)
            else:
                signed += 1
                self.assertEqual(c.contract.price, cm.half_up(m.price * 1.07))
        self.assertTrue(walked and signed)

    def test_no_offer_while_a_notice_is_open(self):
        c = founded(2)
        c.stage, c.served_day = 'grace', c.day
        c.tick()
        self.assertFalse(any(m.kind == 'contract' for m in c.memos))


MEMO_DEFAULT_CONTRACT = cm.MEMO_DEFAULT['contract']


class StandingOrders(unittest.TestCase):
    def test_keep_primm_stocked_loads_that_good_first(self):
        c = founded(2)
        before = [o.good for o in c.plan() if o.town == 'GS'].count('herbs')
        c.set_order(0, 'keep', 'PR', 'herbs', 8)
        self.assertGreaterEqual(c.price('PR', 'herbs', 'sell'), c.price('GS', 'herbs', 'buy'))
        gs = [o.good for o in c.plan() if o.town == 'GS']
        n = 0
        while n < len(gs) and gs[n] == 'herbs':
            n += 1
        self.assertGreater(n, before)
        # it stops when Primm holds 8 or the next crate would lose money
        stock = c.stock['PR']['herbs'] + n
        lose = c.price('PR', 'herbs', 'sell', stock) < c.price('GS', 'herbs', 'buy', c.stock['GS']['herbs'] - n)
        self.assertTrue(stock >= 8 or lose)

    def test_max_pay_bars_dear_goods(self):
        c = founded(2)
        plan = c.plan()
        g = plan[0].good
        c.set_order(0, 'max_pay', good=g, value=1)
        self.assertNotIn(g, [o.good for o in c.plan() if o.town == plan[0].town])

    def test_sell_above_bars_cheap_sales(self):
        c = founded(2)
        plan = c.plan()
        g = plan[0].good
        c.set_order(0, 'sell_above', good=g, value=995)
        self.assertNotIn(g, [o.good for o in c.plan() if o.town == plan[0].town])

    def test_empty_slots_change_nothing(self):
        a, b = founded(2), founded(2)
        b.set_order(1, 'keep')
        b.set_order(1, None)
        self.assertEqual(a.plan(), b.plan())


class Screens(unittest.TestCase):
    def test_front_rows(self):
        c, t = founded(1), tm.Terminal()
        rows = tm.labels(c, t)
        self.assertEqual(rows[7], 'STAFF    2 on the books, cover 45')
        self.assertEqual(rows[8], 'CONTRACTS none running')
        for r in rows:
            self.assertLessEqual(len(r), tm.ROW_WIDTH, r)

    def test_staff_hire_candidate_and_back(self):
        c, t = founded(1), tm.Terminal()
        tm.click(c, t, 7)
        self.assertEqual(t.screen, tm.STAFF)
        rows = tm.labels(c, t)
        self.assertEqual(rows[0], 'COVER 45 on the road')
        self.assertEqual(rows[1], tm.person_label(c.staff[0]))
        self.assertEqual(rows[3], 'HIRE     %d asking for work' % len(c.candidates))
        tm.click(c, t, 3)
        self.assertEqual(t.screen, tm.HIRE)
        self.assertEqual(tm.labels(c, t)[:-1], [tm.person_label(p) for p in c.candidates])
        i = next(k for k, p in enumerate(c.candidates) if p.role == 'guard')
        name = c.candidates[i].name
        tm.click(c, t, i)
        self.assertEqual(t.screen, tm.CANDIDATE)
        self.assertEqual(tm.results(c, t)[0], c.candidates[i].rumour)
        cash = c.cash
        tm.click(c, t, 2)                                   # reference check
        self.assertEqual(c.cash, cash - 10)
        self.assertTrue(tm.labels(c, t)[2].startswith('HONESTY  '))
        self.assertIn('Honesty:', tm.results(c, t)[0])
        tm.click(c, t, 1)                                   # hire
        self.assertEqual(t.screen, tm.HIRE)
        self.assertIn(name, [p.name for p in c.staff])
        tm.click(c, t, len(tm.labels(c, t)) - 1)
        self.assertEqual(t.screen, tm.STAFF)
        tm.click(c, t, len(tm.labels(c, t)) - 1)
        self.assertEqual(t.screen, tm.FRONT)

    def test_fire_needs_two_selects(self):
        c, t = founded(1), tm.Terminal()
        tm.click(c, t, 7)
        tm.click(c, t, 2)                                   # Dutch, the guard
        self.assertEqual(tm.labels(c, t)[2], 'FIRE Dutch Haley? select again')
        self.assertEqual(len(c.staff), 2)
        tm.click(c, t, 2)
        self.assertEqual([p.name for p in c.staff], ['Ruth Coyle'])
        self.assertEqual(tm.labels(c, t)[0], 'COVER 15 on the road')

    def test_a_second_driver_cannot_be_hired_on_screen(self):
        c, t = founded(1), tm.Terminal()
        c.candidates[0] = cm.Person('Test Driver', 'driver', 60, 60, 11)
        t.screen, t.pick = tm.CANDIDATE, 0
        self.assertEqual(tm.labels(c, t)[1], 'HIRE: one driver is enough')
        tm.click(c, t, 1)
        self.assertEqual(len(c.staff), 2)

    def test_contracts_screen(self):
        c, t = founded(3), tm.Terminal()
        tm.click(c, t, 8)
        self.assertEqual(tm.labels(c, t), ['PRIMM TRUST %d' % c.trust['PR'], 'An offer is waiting in Memos.', 'BACK'])
        answer_all(c, 'contract', 0)
        c.tick()
        k = c.contract
        self.assertEqual(tm.labels(c, t), ['PRIMM TRUST %d' % c.trust['PR'],
                                           'WATER 4 crates every 3d at %d' % k.price,
                                           'NEXT day 7  ENDS day 32', 'DELIVERED 1  MISSED 0', 'BACK'])
        t.screen = tm.FRONT
        self.assertEqual(tm.labels(c, t)[8], 'CONTRACTS water 1/9 to PR')

    def test_memos_screen_shows_the_offer(self):
        c, t = founded(3), tm.Terminal()
        tm.click(c, t, 3)
        rows = tm.labels(c, t)
        m = next(x for x in c.memos if x.kind == 'contract')
        self.assertIn('PRIMM WANTS WATER  due 1d', rows)
        self.assertIn('  [ ] decline (default)', rows)
        for r in rows:
            self.assertLessEqual(len(r), tm.ROW_WIDTH, r)
        self.assertLessEqual(len(pm.memo_text(c, m)), 200)

    def test_standing_orders_from_orders(self):
        c, t = founded(1), tm.Terminal()
        tm.click(c, t, 10)
        self.assertEqual(tm.labels(c, t)[4], 'STANDING ORDERS  0 of 3 set')
        tm.click(c, t, 4)
        self.assertEqual(t.screen, tm.STANDING)
        self.assertEqual(tm.labels(c, t), ['SLOT 1  empty', 'SLOT 2  empty', 'SLOT 3  empty', 'BACK'])
        tm.click(c, t, 0)
        self.assertEqual((t.screen, t.pick), (tm.SLOT, 0))
        self.assertEqual(tm.labels(c, t), ['KIND   empty', 'BACK'])
        tm.click(c, t, 0)                                   # keep stocked
        self.assertEqual(tm.labels(c, t), ['KIND   keep stocked', 'TOWN   PR', 'GOOD   water', 'MORE   crates 8',
                                           'LESS', 'BACK'])
        tm.click(c, t, 4)
        tm.click(c, t, 4)
        tm.click(c, t, 2)
        tm.click(c, t, 1)
        o = c.standing[0]
        self.assertEqual((o.kind, o.town, o.good, o.value), ('keep', 'GS', 'powder', 6))
        tm.click(c, t, 0)                                   # sell above: the good's anchor price
        self.assertEqual(tm.labels(c, t)[3], 'MORE   price %d' % c.standing[0].value)
        tm.click(c, t, 3)
        self.assertEqual(c.standing[0].value, cm.ANCHOR['powder'] + 5)
        tm.click(c, t, 5)                                   # BACK to the slot list
        self.assertEqual(tm.labels(c, t)[0], 'SLOT 1  sell above powder %d' % (cm.ANCHOR['powder'] + 5))
        tm.click(c, t, 3)                                   # BACK to Orders
        self.assertEqual(t.screen, tm.ORDERS)
        self.assertEqual(tm.labels(c, t)[4], 'STANDING ORDERS  1 of 3 set')


if __name__ == '__main__':
    unittest.main()

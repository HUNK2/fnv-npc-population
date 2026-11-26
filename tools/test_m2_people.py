"""M2 task 2.2: town levels, staff numbers, traits and loyalty, managers, contracts per town, tier 3, the
tier 2 perk (docs/plans/2026-11-28-m2-chains-people.md, My calls)."""
import unittest

import company_model as cm


def founded(seed=7):
    c = cm.Company(seed)
    c.found()
    return c


def person(name, role='guard', skill=50, honesty=60, wage=12, trait=''):
    return cm.Person(name, role, skill, honesty, wage, trait=trait)


class Levels(unittest.TestCase):
    def test_start_levels(self):
        c = founded()
        self.assertEqual([cm.LEVELS[c.level[t]] for t in cm.TOWNS], ['Hamlet', 'Village', 'Camp', 'Camp'])

    def test_seven_met_days_and_materials_raise_a_level(self):
        c = founded()
        use0 = c.use['SL']['water']
        c.materials_in['SL'] = 40
        r = cm.DayReport(c.day)
        for _ in range(7):
            for g in cm.BASICS:
                if c.has_market('SL', g):
                    c.stock['SL'][g] = 10 * c.use['SL'][g]
            c._levels(r)
        self.assertEqual(c.level['SL'], 1)
        self.assertEqual(c.use['SL']['water'], use0 * 1.25)
        self.assertEqual(c.materials_in['SL'], 0)
        self.assertIn('Sloan grew to a Hamlet', r.notes)

    def test_no_materials_no_level(self):
        c = founded()
        r = cm.DayReport(c.day)
        for _ in range(10):
            for g in cm.BASICS:
                c.stock['MO'][g] = 10 * c.use['MO'][g]
            c._levels(r)
        self.assertEqual(c.level['MO'], 0)

    def test_fourteen_unmet_days_drop_one_but_never_below_the_start(self):
        c = founded()
        c._set_level('GS', 2)
        r = cm.DayReport(c.day)
        for _ in range(30):
            for g in cm.BASICS:
                c.stock['GS'][g] = 0
            c._levels(r)
        self.assertEqual(c.level['GS'], 1)
        self.assertEqual(c.use['GS']['water'], c.base_use['GS']['water'])

    def test_a_level_drop_keeps_the_contract_as_signed(self):
        c = founded()
        c.contracts.append(cm.Contract('water', 3, 3, 222, 1, 1, town='SL', road=2, origin='GS'))
        c._set_level('SL', 1)
        r = cm.DayReport(c.day)
        for _ in range(15):
            for g in cm.BASICS:
                c.stock['SL'][g] = 0
            c._levels(r)
        self.assertEqual(c.level['SL'], 0)
        self.assertEqual((c.contracts[0].price, c.contracts[0].crates), (222, 3))

    def test_materials_sold_count_toward_the_level(self):
        c = founded()
        before = dict(c.materials_in)
        for _ in range(14):
            c.tick()
        sold = sum(n for h in c.history for (t, g), n in h.sold_to.items() if g == 'materials' and t == 'PR')
        self.assertEqual(c.materials_in['PR'] - before['PR'], sold)


class People(unittest.TestCase):
    def test_tier1_candidates_keep_the_m1_shape(self):
        c = founded()
        c.tick()
        self.assertTrue(c.candidates)
        self.assertTrue(all(p.trait == '' and p.role in ('driver', 'guard') for p in c.candidates))

    def test_tier2_candidates_have_traits_traders_clerks_and_residents(self):
        roles, traits, names = set(), set(), set()
        for seed in range(1, 30):
            c = founded(seed)
            c.tier = 2
            c.day = 6
            c.tick()                           # day 7: no; day 1 of a week is when candidates come
            while c.day % 7 != 1:
                c.tick()
            roles |= {p.role for p in c.candidates}
            traits |= {p.trait for p in c.candidates}
            names |= {p.name for p in c.candidates}
        self.assertTrue({'trader', 'clerk'} <= roles, roles)
        self.assertGreater(len(traits - {''}), 3)
        self.assertTrue({'Wes Harlan', 'Marisol'} <= names)

    def test_offers_set_wage_and_loyalty(self):
        c = founded()
        c.candidates = [person('A', wage=12), person('B', wage=12)]
        c.hire(0, 'generous')
        c.hire(0, 'low')
        a, b = c.staff[-2:]
        self.assertEqual((a.wage, a.loyalty), (15, 65))
        self.assertEqual((b.wage, b.loyalty), (10, 45))
        self.assertEqual(b.reasons, [('low offer', -10)])

    def test_loyalty_paid_missed_raise_memo_and_leaving(self):
        c = founded()
        p = person('Ruthie')
        p.loyalty = 40
        c.staff.append(p)
        r = cm.DayReport(c.day)
        r.bills_paid = False
        c._week_people(r)
        self.assertEqual(p.loyalty, 30)
        self.assertTrue(any(m.kind == 'raise' and m.who == 'Ruthie' for m in c.memos))
        self.assertEqual(p.reasons[-1], ('wages late', -10))
        c._week_people(r)
        self.assertEqual(p.loyalty, 20)
        c._week_people(r)
        self.assertNotIn(p, c.staff)
        self.assertIn('Ruthie left the company', r.notes)

    def test_a_raise_answered_yes(self):
        c = founded()
        p = person('Ruthie', wage=12)
        p.loyalty = 30
        c.staff.append(p)
        m = cm.Memo('raise', c.day, c.day + 3, who='Ruthie')
        c.memos.append(m)
        c.answer(m, 0)
        c.tick()
        self.assertEqual(p.wage, 15)
        self.assertGreaterEqual(p.loyalty, 50)

    def test_trait_cover_and_haggler_spread(self):
        c = founded()
        base = c.cover()
        c.staff.append(person('Vet', 'guard', trait='NCR veteran'))
        self.assertEqual(c.cover() - base, cm.GUARD_COVER + 10)
        s0 = c.price('PR', 'water', 'sell')
        c.staff.append(person('Hag', 'trader', skill=70, trait='Haggler'))
        self.assertGreater(c.price('PR', 'water', 'sell'), s0)
        self.assertAlmostEqual(c.trader_cut(), 0.03)

    def test_clerks_are_wagon_slots(self):
        c = founded()
        c.tier = 3
        c.cash += 5000
        c.buy_road(2)
        c.staff.append(person('D2', 'driver'))
        self.assertEqual(c.running_roads(), [(1, 1)])
        c.staff.append(person('C1', 'clerk'))
        self.assertEqual(c.running_roads(), [(1, 1), (2, 2)])

    def test_a_resident_hire_leaves_with_the_town(self):
        c = founded()
        c.tier = 2
        c.gangers_town = True
        while c.day % 7 != 0:
            c.tick()
        c.tick()
        self.assertFalse(any(p.resident for p in c.candidates))


class Managers(unittest.TestCase):
    def test_tiers_open_managers(self):
        c = founded()
        self.assertFalse(c.can_hire_manager('bookkeeper'))
        c.tier = 2
        self.assertTrue(c.hire_manager('bookkeeper', 'Strict'))
        self.assertFalse(c.can_hire_manager('route'))
        c.tier = 3
        self.assertTrue(c.hire_manager('route', 'Safe'))
        self.assertEqual(c.daily_wages() - sum(p.wage for p in c.staff) - cm.HAND_WAGE * c.hands,
                         2 * cm.MANAGER_WAGE)

    def test_a_strict_bookkeeper_finds_the_skimmer(self):
        c = founded()
        c.tier = 2
        c.hire_manager('bookkeeper', 'Strict')
        sk = person('Sly', 'clerk', honesty=cm.SKIM_HONESTY - 1)
        c.staff.append(sk)
        r = cm.DayReport(c.day)
        r.bills_paid = True
        c._week_people(r)
        self.assertNotIn(sk, c.staff)
        self.assertIn('Sly was caught skimming and let go', r.notes)

    def test_a_lenient_bookkeeper_never_does(self):
        c = founded()
        c.tier = 2
        c.hire_manager('bookkeeper', 'Lenient')
        sk = person('Sly', 'clerk', honesty=cm.SKIM_HONESTY - 1)
        c.staff.append(sk)
        r = cm.DayReport(c.day)
        r.bills_paid = True
        for _ in range(10):
            c._week_people(r)
        self.assertIn(sk, c.staff)

    def test_route_manager_answers_road_memos(self):
        for pol, want in (('Safe', cm.HOLD), ('Fast', cm.SEND)):
            c = founded()
            c.tier = 3
            c.hire_manager('route', pol)
            self.assertEqual(c.route_manager_pick(), want)
        c = founded()
        c.tier = 3
        c.hire_manager('route', 'Balanced')
        self.assertEqual(c.route_manager_pick(),
                         cm.GUN if c.clean_chance(c.cover(), 60) < cm.BALANCED_GUN_BELOW else cm.SEND)

    def test_with_a_route_manager_no_road_letter(self):
        c = founded()
        c.tier = 3
        c.hire_manager('route', 'Fast')
        for _ in range(40):
            c.tick()
            self.assertFalse(any(m.kind == 'road' and m.pick is None for m in c.memos))


class Contracts(unittest.TestCase):
    def test_tier1_offer_is_the_m1_contract(self):
        self.assertEqual(founded().contract_offer(), ('PR', 'water', 1))

    def test_tier2_offer_is_the_biggest_shortage_on_a_running_road(self):
        c = founded()
        c.tier = 2
        town, good, road = c.contract_offer()
        self.assertIn(town, cm.ROADS[road])
        self.assertTrue(c.has_market(town, good))
        self.assertNotIn(good, cm.SITE_GOODS)
        self.assertEqual(road, 1)              # one wagon: only Goodsprings - Primm runs

    def test_open_contracts_by_tier(self):
        self.assertEqual([cm.CONTRACTS_OPEN[t] for t in (1, 2, 3)], [1, 2, 3])
        c = founded()
        c.tier = 2
        c.contracts.append(cm.Contract('water', 3, 3, 220, 1, 1))
        c.day = 6
        c.last_offer = -99
        offers = []
        for _ in range(8):
            c.tick()
            offers += [m for m in c.memos if m.kind == 'contract' and m not in offers]
            for m in offers:
                c.answer(m, 0)
        self.assertEqual(len(offers), 1)
        self.assertEqual(len(c.contracts), 2)
        self.assertEqual((c.contracts[1].town, c.contracts[1].good), (offers[0].town, offers[0].good))
        c.day += 6
        for _ in range(14):                    # tier 2: two open, no third offer
            c.tick()
            self.assertFalse(any(m.kind == 'contract' for m in c.memos))


class Tier3AndPerk(unittest.TestCase):
    def test_tier3_needs_worth_two_liked_towns_and_a_sheriff(self):
        c = founded()
        c.tier = 2
        c.earned_worth = lambda: 19000
        c.trust.update({'GS': 60, 'PR': 60})
        c.sheriff = False
        self.assertFalse(c.tier_three_ready())
        c.sheriff = True
        self.assertTrue(c.tier_three_ready())
        c.trust['PR'] = 40
        self.assertFalse(c.tier_three_ready())

    def test_the_company_buys_water_from_the_player(self):
        c = founded()
        self.assertEqual(c.buy_from_player('water', 2), 0)      # tier 1: no
        c.tier = 2
        cash, wh = c.cash, c.warehouse['water']
        self.assertEqual(c.buy_from_player('water', 2), 2)
        self.assertEqual(c.cash, cash - 2 * 160)
        self.assertEqual(c.warehouse['water'], wh + 2)
        self.assertEqual(c.buy_from_player('ammo', 1), 0)
        c.cash += 10000
        self.assertEqual(c.buy_from_player('powder', 20), 8)    # 10 a day


class Texts(unittest.TestCase):
    def test_m2_texts_name_road_town_and_good_and_fit(self):
        import post_model as pm
        c = founded()
        c.tier = 3
        c.contracts.append(cm.Contract('meat', 4, 3, 140, 1, 2, town='MO', road=3, origin='PR'))
        c.staff.append(person('Ruthie'))
        memos = [cm.Memo('road', 1, 2, road=3), cm.Memo('contract', 1, 2, price=140, town='MO', good='meat', road=3),
                 cm.Memo('raise', 1, 4, who='Ruthie')]
        texts = [pm.memo_text(c, m) for m in memos] + [pm.memo_title(c, m) for m in memos]
        texts += [pm.letter_text(cm.Letter(1, 'road', (60, 45, 36, 1, 3, ('MO', 'meat')))),
                  pm.letter_text(cm.Letter(1, 'loss', ('bandits_wreck', 90, 2))),
                  pm.letter_text(cm.Letter(1, 'tier', (3,)))]
        self.assertIn('Outpost road', texts[0])
        self.assertIn("Mojave Outpost's store wants 4 crates of smoked meat", texts[1])
        self.assertIn('Ruthie asks for a raise', texts[2])
        self.assertIn("Mojave Outpost's smoked meat is due tomorrow", texts[6])
        self.assertIn('Sloan road', texts[7])
        for x in texts:
            self.assertLessEqual(len(x), pm.MAX_TEXT, x)

    def test_m1_texts_unchanged(self):
        import post_model as pm
        self.assertEqual(pm.letter_text(cm.Letter(1, 'road', (60, 45, 36, 1))),
                         'Bandit sign on the Primm road tomorrow: about 60 strong, our cover 45: 36 in 100 to get '
                         "through clean. Keep the wagon home tomorrow? Primm's water is due tomorrow.")

    def test_a_resident_on_staff_leaves_with_goodsprings(self):
        c = founded()
        p = person('Marisol')
        p.resident = True
        c.staff.append(p)
        c.gangers_town = True
        r = c.tick()
        self.assertNotIn(p, c.staff)
        self.assertIn('Marisol left with Goodsprings', r.notes)


if __name__ == '__main__':
    unittest.main()

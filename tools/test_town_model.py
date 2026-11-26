"""T1.1: the Goodsprings town model (docs/towns-design.md)."""
import unittest

import town_model as tm


def at(hour, **kw):
    return tm.town_state(tm.World(hour=hour, **kw))


class Day(unittest.TestCase):
    def test_morning_the_field_group_is_at_the_fields(self):
        s = at(8)
        for ref in ('LIMGSAmosRef', 'LIMGSLenaRef', 'LIMGSCalRef', 'LIMGSDutchyRef', 'LIMGSMarisolRef',
                    'LIMGSAbeRef'):
            self.assertEqual(s.present[ref], tm.FIELDS, ref)

    def test_dawn_the_group_gathers_at_the_pruitt_porch(self):
        s = at(6)
        self.assertEqual({s.present[r] for r in tm.FIELD_GROUP if r in s.present}, {tm.PORCH[1]})

    def test_noon_families_eat_at_home_and_hands_at_the_saloon(self):
        s = at(13)
        self.assertEqual(s.present['LIMGSAmosRef'], tm.HOME[1])
        self.assertEqual(s.present['LIMGSAdaRef'], tm.HOME[2])
        self.assertEqual(s.present['LIMGSDutchyRef'], tm.SALOON)

    def test_midnight_everyone_is_home_but_the_watch_and_the_travellers(self):
        s = at(0)
        for r in tm.CAST:
            want = {0: tm.ROAD, -1: tm.SALOON}.get(r.home, tm.HOME.get(r.home))
            self.assertEqual(s.present[r.ref], want, r.name)

    def test_the_watch_sleeps_by_day(self):
        self.assertEqual(at(10).present['LIMGSHectorRef'], tm.WATCH_BED)
        self.assertEqual(at(22).present['LIMGSHectorRef'], tm.ROAD)

    def test_the_girl_plays_at_the_schoolyard_and_is_home_by_dusk(self):
        self.assertEqual(at(9).present['LIMGSRuthRef'], tm.SCHOOLYARD)
        self.assertEqual(at(19).present['LIMGSRuthRef'], tm.PORCH[2])
        self.assertEqual(at(21).present['LIMGSRuthRef'], tm.HOME[2])

    def test_travellers_are_in_town_only_at_night(self):
        self.assertEqual(at(10).present['LIMGSProspectorRef'], tm.GONE)
        self.assertEqual(at(20).present['LIMGSProspectorRef'], tm.SALOON)

    def test_never_crowded(self):
        for h in range(24):
            for g in (tm.GS_NONE, tm.GS_GUNFIGHT_WON):
                self.assertLessEqual(tm.people_in_town(at(h, gunfight=g)), 15)

    def test_every_resident_has_a_place_every_hour(self):
        for h in range(24):
            s = at(h, gunfight=tm.GS_GUNFIGHT_WON)
            self.assertEqual(len(s.present), len(tm.CAST) + 1)
            self.assertNotIn(None, s.present.values())


class Weather(unittest.TestCase):
    def test_rain_empties_the_fields(self):
        s = at(9, raining=True)
        self.assertNotIn(tm.FIELDS, s.present.values())
        self.assertNotIn(tm.SCHOOLYARD, s.present.values())
        self.assertEqual(s.present['LIMGSDutchyRef'], tm.HOME[4])


class Fights(unittest.TestCase):
    def test_on_alarm_defenders_stay_and_the_rest_go_home(self):
        s = at(9, hostile_hours=0)
        self.assertTrue(s.alarm)
        for r in tm.CAST:
            if r.home == -1:
                continue
            if r.defender:
                self.assertEqual(s.present[r.ref], tm.place(r, 9), r.name)
            else:
                self.assertIn(s.present[r.ref], set(tm.HOME.values()) | {tm.WATCH_BED}, r.name)

    def test_the_alarm_clears_after_an_hour(self):
        self.assertFalse(at(9, hostile_hours=1).alarm)

    def test_four_defenders(self):
        self.assertEqual(sorted(r.name for r in tm.CAST if r.defender),
                         ['Amos Pruitt', 'Hector Vane', 'Marisol', 'Wes Harlan'])


class Reactions(unittest.TestCase):
    def test_gunfight_won_brings_a_fourth_hand_and_greetings(self):
        s = at(8, gunfight=tm.GS_GUNFIGHT_WON)
        self.assertEqual(s.present['LIMGSTeaRef'], tm.FIELDS)
        self.assertTrue(s.greet_by_name)
        self.assertNotIn('LIMGSTeaRef', at(8).present)

    def test_gangers_win_the_families_leave_after_a_day(self):
        s = at(8, gunfight=tm.GS_GANGERS, gangers_since=10)
        self.assertEqual(s.present['LIMGSAmosRef'], tm.FIELDS)
        s = at(8, gunfight=tm.GS_GANGERS, gangers_since=24)
        self.assertEqual(s.present['LIMGSAmosRef'], tm.GONE)
        self.assertEqual(s.present['LIMGSDutchyRef'], tm.FIELDS)      # sided with the gangers
        self.assertLessEqual(tm.people_in_town(s), 3)

    def test_infamy_locks_doors_at_night_and_keeps_children_in(self):
        s = at(21, infamy=40, fame=5)
        self.assertTrue(s.doors_locked and s.children_inside and s.watch_shadows)
        self.assertEqual(at(9, infamy=40).present['LIMGSRuthRef'], tm.HOME[2])
        self.assertFalse(at(12, infamy=40).doors_locked)

    def test_fame_greets_by_name(self):
        self.assertTrue(at(9, fame=30).greet_by_name)
        self.assertFalse(at(9, fame=30, infamy=40).greet_by_name)

    def test_company_tier_2_makes_two_residents_hireable(self):
        self.assertEqual(at(9, company_tier=2).hireable, ('LIMGSWesRef', 'LIMGSMarisolRef'))
        self.assertEqual(at(9, company_tier=1).hireable, ())
        self.assertEqual(at(9, company_tier=2, gunfight=tm.GS_GANGERS, gangers_since=30).hireable, ())


if __name__ == '__main__':
    unittest.main()

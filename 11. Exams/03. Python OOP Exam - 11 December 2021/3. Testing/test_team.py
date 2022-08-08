from project.team import Team
import unittest

class TestTeam(unittest.TestCase):
    NAME = 'MyTeam'
    def setUp(self):
        self.tm = Team(self.NAME)

    def test__name_property(self):
        result = self.tm.name
        self.assertEqual(result, self.NAME)

    def test__name__when_try_set_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            self.tm.name = 'MyTeam1'
        self.assertIsNotNone(ex)
        self.assertEqual('Team Name can contain only letters!', str(ex.exception))

    def test__add_members__when_member_is_not_in_items(self):
        result = self.tm.add_member(**{'mitko': 39, 'kolio': 38})
        expected_result = 'Successfully added: mitko, kolio'
        self.assertEqual(result, expected_result)
        self.assertEqual(self.tm.members, {'mitko': 39, 'kolio': 38})

    def test__add_members__when_member_is_in_items(self):
        self.tm1 = Team(self.NAME)
        self.tm1.add_member(**{'mitko': 39})
        result = self.tm1.add_member(**{'mitko': 39})
        expected_result = 'Successfully added: '
        self.assertEqual(result, expected_result)
        self.assertEqual(self.tm1.members, {'mitko': 39})

    def test__remove_member__when_it_not_exist(self):
        result = self.tm.remove_member('Mitko')
        expected_result = 'Member with name Mitko does not exist'
        self.assertEqual(result, expected_result)

    def test__remove_member__when_it_exist(self):
        result = self.tm.add_member(**{'Mitko': 39})
        result = self.tm.remove_member('Mitko')
        expected_result = 'Member Mitko removed'
        self.assertEqual(result, expected_result)
        self.assertEqual(self.tm.members, {})

    def test__gt__when_first_is_great(self):
        self.tm.add_member(**{'Mitko': 39, 'Kolio': 40})
        tm2 = Team('YouTeam')
        tm2.add_member(**{'Mitko': 39})
        result = self.tm > tm2
        self.assertTrue(result)

    def test__gt__when_second_is_great(self):
        self.tm.add_member(**{'Mitko': 39})
        tm2 = Team('YouTeam')
        tm2.add_member(**{'Mitko': 39, 'Kolio': 40})
        result = self.tm > tm2
        self.assertFalse(result)

    def test__len(self):
        self.tm.add_member(**{'Mitko': 39})
        result = len(self.tm)
        self.assertEqual(result, 1)
        self.tm.add_member(**{'Mitko2': 40})
        result = len(self.tm)
        self.assertEqual(result, 2)

    def test_add__new_team_name(self):
        tm2 = Team('YourTeam')
        tm3 = self.tm + tm2
        result = tm3.name
        expected_result = 'MyTeamYourTeam'
        self.assertEqual(result, expected_result)

    def test_add__check_members(self):
        self.tm.add_member(**{'Mitko': 39})
        tm2 = Team('YouTeam')
        self.tm.add_member(**{'Kolio': 38})
        tm3 = self.tm + tm2
        result = tm3.members
        expected_result = {'Mitko': 39, 'Kolio': 38}
        self.assertEqual(result, expected_result)

    def test__str(self):
        self.tm.add_member(**{'Mitko': 12, 'Gosho': 12, 'Spas': 40, 'Binnaz': 4})
        result = str(self.tm)
        expected_result = 'Team name: MyTeam\nMember: Spas - 40-years old\nMember: Gosho - 12-years old\nMember: Mitko - 12-years old\nMember: Binnaz - 4-years old'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

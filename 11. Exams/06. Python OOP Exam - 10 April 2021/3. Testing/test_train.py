from project.train.train import Train
import unittest

class TestTrain(unittest.TestCase):

    def setUp(self):
        self.tr = Train('Vlak', 5)

    def test__init_name(self):
        result = self.tr.name
        expected_result = 'Vlak'
        self.assertEqual(result, expected_result)

    def test__init_capacity(self):
        result = self.tr.capacity
        expected_result = 100
        self.assertEqual(result, expected_result)

    def test__init_capacity(self):
        result = self.tr.passengers
        expected_result = []
        self.assertEqual(result, expected_result)

    def test__add__when_no_capacity(self):
        tr = Train('Vlak', 1)
        tr.add('Mitko')

        with self.assertRaises(ValueError) as ex:
            tr.add('Dalia')
        self.assertIsNotNone(ex)
        expected_mess = 'Train is full'
        self.assertEqual(str(ex.exception), expected_mess)

    def test__add__when_add_same_name(self):
        tr = Train('Vlak', 2)
        tr.add('Mitko')

        with self.assertRaises(ValueError) as ex:
            tr.add('Mitko')
        self.assertIsNotNone(ex)
        expected_mess = 'Passenger Mitko Exists'
        self.assertEqual(str(ex.exception), expected_mess)

    def test__add__when_add_normal(self):
        result = self.tr.add('Mitko')
        expected_mess = 'Added passenger Mitko'
        self.assertEqual(result, expected_mess)
        result = self.tr.passengers
        expected_mess = ['Mitko']
        self.assertEqual(result, expected_mess)

    def test__remove__when_name_not_in_passengers(self):
        self.tr.add('Mitko')

        with self.assertRaises(ValueError) as ex:
            self.tr.remove('Mirian')
        self.assertIsNotNone(ex)
        expected_mess = 'Passenger Not Found'
        self.assertEqual(str(ex.exception), expected_mess)

    def test__remove__when_name_not_in_passengers(self):
        self.tr.add('Mitko')
        self.tr.add('Dalia')
        self.tr.add('Mirian')

        result = self.tr.remove('Mitko')
        expected_mess = 'Removed Mitko'
        self.assertEqual(result, expected_mess)

        result = self.tr.passengers
        expected_mess = ['Dalia', 'Mirian']
        self.assertEqual(result, expected_mess)

if __name__ == '__main__':
    unittest.main()

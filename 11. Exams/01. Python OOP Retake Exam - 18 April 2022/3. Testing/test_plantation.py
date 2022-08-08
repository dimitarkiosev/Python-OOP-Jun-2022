from project.plantation import Plantation
import unittest

class TestPlantation(unittest.TestCase):
    PL_SIZE = 5

    def setUp(self):
        self.pl = Plantation(self.PL_SIZE)

    def test__init(self):
        result = self.pl.size
        self.assertEqual(result, self.PL_SIZE)

    def test__init_wrong_value(self):
        with self.assertRaises(ValueError) as ex:
            pl = Plantation(-1)
        self.assertEqual(str(ex.exception), 'Size must be positive number!')

    def test__size_property(self):
        result = self.pl.size
        self.assertEqual(result, self.PL_SIZE)

    def test__size__when_value_less_0(self):
        with self.assertRaises(ValueError) as ex:
            self.pl.size = -1
        self.assertEqual(str(ex.exception), 'Size must be positive number!')

    def test__size__when_value_is_correct(self):
        self.pl.size = 10
        result = self.pl.size
        self.assertEqual(result, 10)

    def test__hire_worker__when_worker_is_in_list(self):
        self.pl.hire_worker('Mitko Kiosev')
        with self.assertRaises(ValueError) as ex:
            self.pl.hire_worker('Mitko Kiosev')
        self.assertEqual(str(ex.exception), 'Worker already hired!')

    def test__hire_worker__when_worker_is_not_in_list(self):
        result_mess = self.pl.hire_worker('Mitko Kiosev')
        self.assertEqual(result_mess, 'Mitko Kiosev successfully hired.')
        result_mess = self.pl.hire_worker('Nikolay Kiosev')
        result = self.pl.workers

        self.assertEqual(len(self.pl.workers), 2)
        self.assertEqual(result, ['Mitko Kiosev','Nikolay Kiosev'])

    def test__len__(self):
        self.pl.hire_worker('Mitko Kiosev')
        self.pl.planting('Mitko Kiosev', 'niva_1')
        result = len(self.pl)
        self.assertEqual(result, 1)
        self.pl.hire_worker('Nikolay Kiosev')
        self.pl.planting('Nikolay Kiosev', 'niva_2')
        self.pl.planting('Mitko Kiosev', 'niva_3')
        result = len(self.pl)
        self.assertEqual(result, 3)

    def test__planting__when_worker_is_not_in_list(self):
        with self.assertRaises(ValueError) as ex:
            self.pl.planting('Mitko Kiosev', 'niva1')
        self.assertEqual(str(ex.exception), 'Worker with name Mitko Kiosev is not hired!')

    def test__planting__when_len_plants_great_size(self):
        self.pl.hire_worker('Mitko Kiosev')
        self.pl.planting('Mitko Kiosev', 'niva1')
        self.pl.planting('Mitko Kiosev', 'niva2')
        self.pl.planting('Mitko Kiosev', 'niva3')
        self.pl.planting('Mitko Kiosev', 'niva4')
        self.pl.planting('Mitko Kiosev', 'niva5')

        with self.assertRaises(ValueError) as ex:
            self.pl.planting('Mitko Kiosev', 'niva6')
        self.assertEqual(str(ex.exception), 'The plantation is full!')

    def test__planting__when_it_is_first_plant(self):
        self.pl.hire_worker('Mitko Kiosev')
        result = self.pl.planting('Mitko Kiosev', 'niva1')

        self.assertEqual(len(self.pl.plants['Mitko Kiosev']), 1)
        self.assertEqual(result, "Mitko Kiosev planted it's first niva1.")

    def test_planting_wrong_dict_assigment(self):
        self.pl.hire_worker('Mitko Kiosev')
        self.pl.planting('Mitko Kiosev', 'niva1')
        self.pl.planting('Mitko Kiosev', 'niva2')

        self.assertEqual(len(self.pl.plants['Mitko Kiosev']), 2)

    def test__planting__when_it_is_not_first_plant(self):
        self.pl.hire_worker('Mitko Kiosev')
        self.pl.planting('Mitko Kiosev', 'niva1')
        result = self.pl.planting('Mitko Kiosev', 'niva2')

        self.assertEqual(result, "Mitko Kiosev planted niva2.")

    def test__str__(self):
        self.pl.hire_worker('Mitko Kiosev')
        self.pl.hire_worker('Nikolay Kiosev')
        self.pl.planting('Mitko Kiosev', 'niva_1')
        self.pl.planting('Mitko Kiosev', 'niva_2')
        self.pl.planting('Nikolay Kiosev', 'niva_3')
        expected_result = [f'Plantation size: {self.PL_SIZE}']
        expected_result.append(f'{", ".join(self.pl.workers)}')
        for worker, plants in self.pl.plants.items():
            expected_result.append(f"{worker} planted: {', '.join(plants)}")
        expected_result = '\n'.join(expected_result)
        self.assertEqual(str(self.pl), expected_result)

    def test__repr__(self):
        self.pl.hire_worker('Mitko Kiosev')
        self.pl.hire_worker('Nikolay Kiosev')
        self.pl.planting('Mitko Kiosev', 'niva_1')
        self.pl.planting('Nikolay Kiosev', 'niva_1')
        result = self.pl.__repr__().strip()
        expected_result = f'Size: {self.PL_SIZE}\nWorkers: Mitko Kiosev, Nikolay Kiosev'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

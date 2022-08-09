from project.pet_shop import PetShop
import unittest


class TestPetShop(unittest.TestCase):

    def setUp(self):
        self.ps = PetShop('Kuche')

    def test__init_name(self):
        result = self.ps.name
        expected_result = 'Kuche'
        self.assertEqual(result, expected_result)

    def test__init_food(self):
        result = self.ps.food
        expected_result = {}
        self.assertEqual(result, expected_result)

    def test__init_pets(self):
        result = self.ps.pets
        expected_result = []
        self.assertEqual(result, expected_result)

    def test__add_food__when_quantiti_is_less_0(self):
        with self.assertRaises(ValueError) as ex:
            self.ps.add_food('Milk', -2)
        self.assertIsNotNone(ex)
        expected_mess = 'Quantity cannot be equal to or less than 0'
        self.assertEqual(str(ex.exception), expected_mess)

    def test__add_food__when_name_not_in_food(self):
        result = self.ps.food
        expected_result = {}
        self.assertEqual(result, expected_result)
        result = self.ps.add_food('Milk', 2.412)
        expected_result = 'Successfully added 2.41 grams of Milk.'
        self.assertEqual(result, expected_result)
        result = self.ps.food
        expected_result = {'Milk': 2.412}
        self.assertEqual(result, expected_result)

    def test__add_pet__when_name_is_not_in_pets(self):
        result = self.ps.add_pet('Pesho')
        expected_result = 'Successfully added Pesho.'
        self.assertEqual(result, expected_result)

    def test__add_pet__when_name_is_in_pets(self):
        self.ps.add_pet('Pesho')
        with self.assertRaises(Exception) as ex:
            self.ps.add_pet('Pesho')
        self.assertIsNotNone(ex)
        expected_mess = 'Cannot add a pet with the same name'
        self.assertEqual(str(ex.exception), expected_mess)

    def test__feed_pet__when_pet_name_is_not_in_pets(self):
        with self.assertRaises(Exception) as ex:
            self.ps.feed_pet('Milk','Pesho')
        self.assertIsNotNone(ex)
        expected_mess = 'Please insert a valid pet name'
        self.assertEqual(str(ex.exception), expected_mess)

    def test__feed_pet__when_food_name_is_not_in_foods(self):
        self.ps.add_pet('Pesho')
        result = self.ps.feed_pet('Milk','Pesho')
        expected_result = 'You do not have Milk'
        self.assertEqual(result, expected_result)

    def test__feed_pet__when_food_is_less_100_check_mess(self):
        self.ps.add_pet('Pesho')
        self.ps.add_food('Milk', 80)
        result = self.ps.feed_pet('Milk','Pesho')
        expected_result = 'Adding food...'
        self.assertEqual(result, expected_result)
        result = self.ps.food
        expected_result = {'Milk': 1080}
        self.assertEqual(result, expected_result)

    def test__feed_pet__when_food_is_less_100_check_value(self):
        self.ps.add_pet('Pesho')
        self.ps.add_food('Milk', 80.1)
        self.ps.feed_pet('Milk','Pesho')
        result = self.ps.food
        expected_result = {'Milk': 1080.1}
        self.assertEqual(result, expected_result)

    def test__feed_pet__when_food_is_great_100_check_value(self):
        self.ps.add_pet('Pesho')
        self.ps.add_food('Milk', 201.1)
        self.ps.feed_pet('Milk','Pesho')
        result = self.ps.food
        expected_result = {'Milk': 101.1}
        self.assertEqual(result, expected_result)

    def test__feed_pet__when_food_is_great_100_check_mess(self):
        self.ps.add_pet('Pesho')
        self.ps.add_food('Milk', 201.1)
        result = self.ps.feed_pet('Milk','Pesho')
        expected_result = 'Pesho was successfully fed'
        self.assertEqual(result, expected_result)

    def test__repr__(self):
        self.ps.add_pet('Pesho')
        self.ps.add_pet('Rex')
        result = str(self.ps)
        expected_result = 'Shop Kuche:\nPets: Pesho, Rex'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

from project.bookstore import Bookstore
import unittest

class TestBookstore(unittest.TestCase):

    def setUp(self):
        self.bs = Bookstore(20)

# = = = = = = = = = = = = = = = = = = =
# test for init
# = = = = = = = = = = = = = = = = = = =
    def test__init(self):
        self.assertEqual(self.bs.books_limit, 20)
        self.assertEqual(self.bs.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bs.total_sold_books, 0)

    def test__init__when_book_limit_is_less_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.bs.books_limit = -2
        expected_mess = 'Books limit of -2 is not valid'
        self.assertEqual(str(ex.exception), expected_mess)

    def test__init__when_book_limit_is_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.bs.books_limit = 0
        expected_mess = 'Books limit of 0 is not valid'
        self.assertEqual(str(ex.exception), expected_mess)


# = = = = = = = = = = = = = = = = = = =
# test for len
# = = = = = = = = = = = = = = = = = = =
    def test__len__zero(self):
        result = len(self.bs)
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test__len__great_than_zero(self):
        self.bs.receive_book('Pod Igoto', 5)
        self.bs.receive_book('Nemili, nedragi', 2)
        result = len(self.bs)
        expected_result = 7
        self.assertEqual(result, expected_result)


# = = = = = = = = = = = = = = = = = = =
# test for receive_book
# = = = = = = = = = = = = = = = = = = =
    def test__receive_book__when_not_have_enough_space_no_book_in_store(self):
        with self.assertRaises(Exception) as ex:
            self.bs.receive_book('Pod Igoto', 21)
        expected_mess = 'Books limit is reached. Cannot receive more books!'
        self.assertEqual(str(ex.exception), expected_mess)

    def test__receive_book__when_not_have_enough_space_some_book_in_store(self):
        self.bs.receive_book('Pod Igoto', 5)
        with self.assertRaises(Exception) as ex:
            self.bs.receive_book('Pod Igoto', 16)
        expected_mess = 'Books limit is reached. Cannot receive more books!'
        self.assertEqual(str(ex.exception), expected_mess)

    def test__receive_book__when_have_enough_space_check_availability(self):
        self.bs.receive_book('Pod Igoto', 1)
        result = self.bs.availability_in_store_by_book_titles['Pod Igoto']
        expected_result = 1
        self.assertEqual(result, expected_result)

        self.bs.receive_book('Pod Igoto', 5)
        result = self.bs.availability_in_store_by_book_titles['Pod Igoto']
        expected_result = 6
        self.assertEqual(result, expected_result)

        result = self.bs.availability_in_store_by_book_titles
        expected_result = {'Pod Igoto': 6}
        self.assertEqual(result, expected_result)

    def test__receive_book__when_have_enough_space_check_return_mess(self):
        self.bs.receive_book('Pod Igoto', 1)
        result = self.bs.receive_book('Pod Igoto', 5)
        expected_result = '6 copies of Pod Igoto are available in the bookstore.'
        self.assertEqual(result, expected_result)


# = = = = = = = = = = = = = = = = = = =
# test for sell_book
# = = = = = = = = = = = = = = = = = = =
    def test__sell_book__when_book_is_not_available_in_bookstore(self):
        with self.assertRaises(Exception) as ex:
            self.bs.sell_book('Pod Igoto', 1)
        expected_mess = "Book Pod Igoto doesn't exist!"
        self.assertEqual(str(ex.exception), expected_mess)

    def test__sell_book__when_book_is_available_and_not_enough_copies(self):
        self.bs.receive_book('Pod Igoto', 1)
        self.bs.sell_book('Pod Igoto', 1)
        with self.assertRaises(Exception) as ex:
            self.bs.sell_book('Pod Igoto', 2)
        expected_mess = "Pod Igoto has not enough copies to sell. Left: 0"
        self.assertEqual(str(ex.exception), expected_mess)

        result = self.bs.availability_in_store_by_book_titles['Pod Igoto']
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test__sell_book__when_book_is_available_and_not_enough_copies2(self):
        self.bs.receive_book('Pod Igoto', 1)
        with self.assertRaises(Exception) as ex:
            self.bs.sell_book('Pod Igoto', 2)
        expected_mess = "Pod Igoto has not enough copies to sell. Left: 1"
        self.assertEqual(str(ex.exception), expected_mess)

        result = self.bs.availability_in_store_by_book_titles['Pod Igoto']
        expected_result = 1
        self.assertEqual(result, expected_result)

    def test__sell_book__when_book_is_sell_successfully_check_availability(self):
        self.bs.receive_book('Pod Igoto', 5)
        self.bs.sell_book('Pod Igoto', 2)
        result = self.bs.availability_in_store_by_book_titles['Pod Igoto']
        expected_result = 3
        self.assertEqual(result, expected_result)

    def test__sell_book__when_book_is_sell_successfully_check_total_sold(self):
        self.bs.receive_book('Pod Igoto', 5)
        self.bs.sell_book('Pod Igoto', 1)
        self.bs.sell_book('Pod Igoto', 2)
        result = self.bs.total_sold_books
        expected_result = 3
        self.assertEqual(result, expected_result)

    def test__sell_book__when_book_is_sell_successfully_check_return_mess(self):
        self.bs.receive_book('Pod Igoto', 5)
        result = self.bs.sell_book('Pod Igoto', 2)
        expected_result = 'Sold 2 copies of Pod Igoto'
        self.assertEqual(result, expected_result)


# = = = = = = = = = = = = = = = = = = =
# test for str
# = = = = = = = = = = = = = = = = = = =
    def test__str__(self):
        self.bs.receive_book('Pod Igoto', 5)
        self.bs.receive_book('Bay Ganyo', 5)
        self.bs.sell_book('Pod Igoto', 2)
        result = f'{self.bs}'
        expected_result = 'Total sold books: 2\nCurrent availability: 8\n - Pod Igoto: 3 copies\n - Bay Ganyo: 5 copies'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

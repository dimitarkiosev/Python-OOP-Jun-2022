from project.library import Library
import unittest

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.lib = Library('MyLib')

    def test__name__when_is_empty(self):
        with self.assertRaises(ValueError) as ex:
            self.lib.name = ''
        self.assertIsNotNone(ex)
        self.assertEqual('Name cannot be empty string!', str(ex.exception))

    def test__name(self):
        result = self.lib.name
        expected_result = 'MyLib'
        self.assertEqual(result, expected_result)

    def test__add_book__when_author_is_not_in_books_by_authors(self):
        self.lib.add_book('Vazov', 'Pod igoto')
        result = self.lib.books_by_authors
        expected_result = {'Vazov': ['Pod igoto']}
        self.assertEqual(result, expected_result)

    def test__add_book__when_book_is_not_added_in_books_by_authors(self):
        self.lib.add_book('Vazov', 'Pod igoto')
        self.lib.add_book('Vazov', 'Nemili, nedragi')
        result = self.lib.books_by_authors
        expected_result = {'Vazov': ['Pod igoto', 'Nemili, nedragi']}
        self.assertEqual(result, expected_result)

    def test__add_book__when_book_is_in_books_by_authors(self):
        self.lib.add_book('Vazov', 'Nemili, nedragi')
        self.lib.add_book('Vazov', 'Pod igoto')
        self.lib.add_book('Vazov', 'Nemili, nedragi')
        result = self.lib.books_by_authors
        expected_result = {'Vazov': ['Nemili, nedragi', 'Pod igoto']}
        self.assertEqual(result, expected_result)

    def test__add_reader__when_name_is_not_in_readers(self):
        self.lib.add_reader('Mitko')
        result = self.lib.readers
        expected_result = {'Mitko': []}
        self.assertEqual(result, expected_result)

    def test__add_reader__when_name_is_in_readers(self):
        self.lib.add_reader('Mitko')
        result = self.lib.add_reader('Mitko')
        expected_result = f'Mitko is already registered in the {self.lib.name} library.'
        self.assertEqual(result, expected_result)

    def test__rent_book__when_reader_is_not_in_readers(self):
        result = self.lib.rent_book('Mitko', 'Vazov', 'Pod igoto')
        expected_result = 'Mitko is not registered in the MyLib Library.'
        self.assertEqual(result, expected_result)

    def test__rent_book__when_book_author_is_not_in_book_by_authors(self):
        self.lib.add_reader('Mitko')
        result = self.lib.rent_book('Mitko', 'Vazov', 'Pod igoto')
        expected_result = "MyLib Library does not have any Vazov's books."
        self.assertEqual(result, expected_result)

    def test__rent_book__when_book_title_is_not_in_books_by_authors(self):
        self.lib.add_reader('Mitko')
        self.lib.add_book('Vazov', 'Nemili, nedragi')
        result = self.lib.rent_book('Mitko', 'Vazov', 'Pod igoto')
        expected_result = """MyLib Library does not have Vazov's "Pod igoto"."""
        self.assertEqual(result, expected_result)

    def test__rent_book__when_everhing_is_on_line(self):
        self.lib.add_reader('Mitko')
        self.lib.add_book('Vazov', 'Nemili, nedragi')
        self.lib.add_book('Vazov', 'Pod igoto')
        self.lib.rent_book('Mitko', 'Vazov', 'Pod igoto')
        result = self.lib.readers['Mitko']
        expected_result = [{'Vazov': 'Pod igoto'}]
        self.assertEqual(result, expected_result)
        result = self.lib.books_by_authors
        expected_result = {'Vazov': ['Nemili, nedragi']}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

from project.movie import Movie
import unittest

class TestMovie(unittest.TestCase):
    NAME = 'Fast10'
    YEAR = 2022
    RATING = 5.8
    def setUp(self):
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test__name_property(self):
        result = self.movie.name
        self.assertEqual(result, self.NAME)

    def test__name__when_try_set_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ''
        self.assertIsNotNone(ex)
        self.assertEqual('Name cannot be an empty string!', str(ex.exception))

    def test__name__when_change_name(self):
        self.movie.name = 'test1'
        result = self.movie.name
        self.assertEqual(result, 'test1')

    def test__year_property(self):
        result = self.movie.year
        self.assertEqual(result, self.YEAR)

    def test__year__when_it_is_not_valid(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1885
        self.assertIsNotNone(ex)
        self.assertEqual('Year is not valid!', str(ex.exception))

    def test__year__when_change_year(self):
        self.movie.year = 1990
        result = self.movie.year
        self.assertEqual(result, 1990)

    def test__add_actor__when_it_is_possible(self):
        actor = 'Mitko Kiosev'
        self.movie.add_actor(actor)
        self.assertTrue(actor in self.movie.actors)

    def test__add_actor__when_it_is_already_added(self):
        actor = 'Mitko Kiosev'
        self.movie.add_actor(actor)
        result = self.movie.add_actor(actor)
        expected_result = f'{actor} is already added in the list of actors!'
        self.assertEqual(result, expected_result)


    def test__gt__when_first_is_great(self):
        movie2 = Movie('Fast09', 2000, self.RATING - 0.1)
        result = self.movie > movie2
        expected_result = f'"{self.movie.name}" is better than "{movie2.name}"'
        self.assertEqual(result, expected_result)

    def test__gt__when_second_is_great(self):
        movie2 = Movie('Fast09', 2000, self.RATING + 0.1)
        result = self.movie > movie2
        expected_result = f'"{movie2.name}" is better than "{self.movie.name}"'
        self.assertEqual(result, expected_result)

    def test__repr__(self):
        actor = 'Mitko Kiosev'
        self.movie.add_actor(actor)
        result = str(self.movie)
        expected_result = f"Name: {self.NAME}\nYear of Release: {self.YEAR}\nRating: {self.RATING:.2f}\nCast: Mitko Kiosev"
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

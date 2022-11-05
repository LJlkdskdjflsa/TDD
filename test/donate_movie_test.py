import unittest
from dataclasses import dataclass
from donate_movie import Movie, Library


class DonateMovieTest(unittest.TestCase):
    def setUp(self):
        self.movie = Movie()
        self.library = Library()
        self.library.donate(self.movie)

    def test_donated_movie_add_to_library(self):
        self.assertTrue(self.library.contains(self.movie))

    def test_copy_added(self):
        self.assertEqual(1, self.movie.get_copies())


if __name__ == "__main__":
    unittest.main()

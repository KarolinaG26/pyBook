import unittest

from book import Book


class TestBook2(unittest.TestCase):
    def setUp(self):
        self.book = Book("Wiedzmin", "Sapkowski", 2000)
    def test_get_info(self):
        text_correct = "Ksiazka: Wiedzmin Autor: Sapkowski Rok: 2000"
        text_result = self.book.get_info()
        self.assertEqual(text_result, text_correct)
    def test_change_title(self):
        self.book.change_title("Miecz przeznaczenia")
        self.assertEqual("Miecz przeznaczenia", self.book.title)
    def test_change_author(self):
        self.book.change_author("Karp")
        self.assertEqual("Karp", self.book.author)
    def test_change_year(self):
        self.book.change_year(2020)
        self.assertEqual(2020, self.book.year)

if __name__ == '__main__':
    unittest.main()
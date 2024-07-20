import os
import unittest
from library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Создаёт временный файл для тестов."""
        self.test_filename = 'test_library.json'
        self.library = Library(self.test_filename)

    def tearDown(self):
        """Удаляет временный файл после тестов."""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_add_book(self):
        """Тест добавления книги."""
        self.library.add_book("Убить пересмешника", "Харпер Ли", "1960")
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0]['title'], "Убить пересмешника")

    def test_remove_book(self):
        """Тест удаления книги."""
        self.library.add_book("Убить пересмешника", "Харпер Ли", "1960")
        self.library.remove_book(1)
        self.assertEqual(len(self.library.books), 0)

    def test_search_book(self):
        """Тест поиска книги."""
        self.library.add_book("Убить пересмешника", "Харпер Ли", "1960")
        self.library.add_book("Гордость и предубеждение", "Джейн Остин", "1813")
        results = self.library.search_book("Убить пересмешника")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], "Убить пересмешника")

    def test_change_status(self):
        """Тест изменения статуса книги."""
        self.library.add_book("Убить пересмешника", "Харпер Ли", "1960")
        self.library.change_status(1, "выдана")
        self.assertEqual(self.library.books[0]['status'], "выдана")

    def test_invalid_status_change(self):
        """Тест изменения статуса на неверный."""
        self.library.add_book("Убить пересмешника", "Харпер Ли", "1960")
        self.library.change_status(1, "недоступна")  # Неверный статус
        self.assertEqual(self.library.books[0]['status'], "в наличии")
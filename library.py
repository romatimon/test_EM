import os
import json
from typing import List, Dict, Optional

"""
Класс `Library` предназначен для управления библиотекой книг.
Он позволяет добавлять, удалять, искать книги и изменять их статус.
Данные хранятся в формате JSON в указанном файле.

"""


class Library:
    def __init__(self, filename: str = 'library.json') -> None:
        self.filename = filename
        self.books: List[Dict[str, str]] = self.load_books()

    def load_books(self) -> List[Dict[str, str]]:
        """Загружает книги из файла. Если файл не существует или повреждён, возвращает пустой список."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Ошибка загрузки данных. Файл поврежден.")
        return []

    def save_book(self) -> None:
        """Сохраняет текущий список книг в файл в формате JSON."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.books, file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: str) -> None:
        """Добавляет новую книгу в библиотеку."""
        new_id = len(self.books) + 1
        book: Optional[Dict[str, str]] = next((book for book in self.books if book['id'] == new_id), None)
        if book:
            new_id += 1
        new_book: Dict[str, str] = {
            'id': new_id,
            'title': title,
            'author': author,
            'year': year,
            'status': 'в наличии',
        }
        self.books.append(new_book)
        self.save_book()
        print(f'Книга {title} добавлена в библиотеку.')

    def remove_book(self, book_id: int) -> None:
        """Удаляет книгу из библиотеки по её идентификатору."""
        book: Optional[Dict[str, str]] = next((book for book in self.books if book['id'] == book_id), None)
        if book:
            self.books.remove(book)
            self.save_book()
            print(f"Книга {book_id} удалена")
        else:
            print(f"Книга не найдена")

    def search_book(self, search_obj: str) -> List[Dict[str, str]]:
        """Ищет книгу по названию, автору или году публикации."""
        result = [book for book in self.books if (search_obj.lower() in book['title'].lower() or
                                                  search_obj.lower() in book['author'].lower() or
                                                  search_obj == str(book['year']))]
        return result

    def get_all_books(self) -> None:
        """Выводит список всех книг в библиотеке на экран."""
        if not self.books:
            print("Библиотека пуста.")
        for book in self.books:
            print(
                f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")

    def change_status(self, book_id: int, new_status: str) -> None:
        """Изменяет статус книги (например, "в наличии" или "выдана")."""
        book: Optional[Dict[str, str]] = next((book for book in self.books if book['id'] == book_id), None)
        if book:
            if new_status in ['в наличии', 'выдана']:
                book['status'] = new_status
                self.save_book()
                print(f"Статус книги с ID {book_id} изменен на '{new_status}'.")
            else:
                print("Неверный статус. Используйте 'в наличии' или 'выдана'.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

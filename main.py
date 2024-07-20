from library import Library


def main():
    obj_library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            obj_library.add_book(title, author, year)
        elif choice == '2':
            book_id = int(input("Введите ID книги для удаления: "))
            obj_library.remove_book(book_id)
        elif choice == '3':
            search_obj = input("Введите название, автора или год для поиска: ")
            result = obj_library.search_book(search_obj)
            if result:
                for book in result:
                    print(
                        f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")
            else:
                print("Книга не найдена.")
        elif choice == '4':
            obj_library.get_all_books()
        elif choice == '5':
            book_id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            obj_library.change_status(book_id, new_status)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == '__main__':
    main()





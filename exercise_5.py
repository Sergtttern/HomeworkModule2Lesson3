"""
Модуль 2 Python Advanced, Урок 3 ООП Основні парадигми, Вправа 5

Розробіть клас Library для представлення бібліотеки. А також класс Book для представлення книги.
Класс Library повинен мати атрибут books зі списком книжок. Кожна книга в бібліотеці має атрибути,
такі як назва, автор і рік видання. Додайте метод add_book, який додає нову книгу до бібліотеки.
Реалізуйте метод __str__, який виводить список книг у бібліотеці.
Створіть об'єкт Library і додайте кілька книг. Виведіть список книг у бібліотеці.
"""

class Book:
    """ класс Book для представлення книги.
    Кожна книга в бібліотеці має атрибути, такі як назва, автор і рік видання."""

    def __init__(self, name, author, year_of_publication):
        """конструктор"""
        self.name = name
        self.author = author
        self.year_of_publication = year_of_publication

class Library:
    """ Призначений для зберігання назв книг у бібліотеці"""

    def __init__(self):
        """конструктор класу"""
        self.books = []

    def add_book(self, book):
        """метод для додавання книги до бібліотеки"""
        self.books.append(book)

    def __str__(self):
        """метод __str__, який виводить список книг у бібліотеці."""
        book_list = []
        for element in self.books:
            book_info = f"Назва: {element.name}, Автор: {element.author}, Рік видання: {element.year_of_publication}"
            book_list.append(book_info)

        return "\n".join(book_list)


book_1 = Book("Ромео і Джульєтта", "Вільям Шекспір", 1985)
book_2 = Book("Робінзон Крузо", "Даніель Дефо", 1990)
book_3 = Book("Мартин Іден", "Джек Лондон", 2000)
book_4 = Book("Лісова пісня", "Леся Українка", 1987)
book_5 = Book("Мауглі", "Редьярд Кіплінг", 2005)

library_school = Library()

library_school.add_book(book_1)

library_school.add_book(book_2)

library_school.add_book(book_3)

print(library_school)

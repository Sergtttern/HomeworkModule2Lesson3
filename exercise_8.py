"""
Модуль 2 Python Advanced, Урок 3 ООП Основні парадигми, Вправа 8
Створіть клас Book який має такі атрибути як рік видання, назву, автор та кількість сторінок. Створіть статік
метод який буде приймати список книжок та рік, та повертати кількість книжок з цього списку які були опубліковані
у цьому році.
"""

class Book:
    """клас Book має такі атрибути як рік видання, назву, автор та кількість сторінок"""
    def __init__(self, name, author, year_of_publication, number_of_pages):
        """конструктор"""
        self.name = name
        self.author = author
        self.year_of_publication = year_of_publication
        self.number_of_pages = number_of_pages

    @staticmethod
    def books_published_in_a_specific_year(books_list_prm:list, specific_year:int):
        """статік метод який буде приймати список книжок та рік, та повертати кількість книжок з цього списку
        які були опубліковані у цьому році."""
        counter = 0
        for element in books_list_prm:
            if element.year_of_publication == specific_year:
                counter += 1

        return counter

book_1 = Book("Ромео і Джульєтта", "Вільям Шекспір", 1985, 250)
book_2 = Book("Робінзон Крузо", "Даніель Дефо", 2005, 150)
book_3 = Book("Мартин Іден", "Джек Лондон", 2000, 320)
book_4 = Book("Лісова пісня", "Леся Українка", 1987, 170)
book_5 = Book("Мауглі", "Редьярд Кіплінг", 2005, 90)

book_list = [book_1, book_2, book_3, book_4, book_5]

print(Book.books_published_in_a_specific_year(book_list, 2005))

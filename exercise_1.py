"""
Модуль 2 Python Advanced, Урок 3 ООП Основні парадигми, Вправа 1
Створіть клас Rectangle для представлення прямокутника. Додайте методи для обчислення площі
та периметра прямокутника.  Створіть об'єкт Rectangle і викличте ці методи.
"""


class Rectangle:
    """
    клас Rectangle для представлення прямокутника. Містить методи для обчислення площі та периметра прямокутника.
    """
    def __init__(self, length, width):
        """конструктор"""
        self.length = length
        self.width = width

    def area(self):
        """метод для обчислення площі прямокутника """
        return self.length * self.width

    def perimeter(self):
        """метод для обчислення периметра прямокутника """
        return 2 * self.length + 2 * self.width


rectangle_1 = Rectangle(10, 5)

rectangle_2 = Rectangle(5, 5)

print(rectangle_1.area())

print(rectangle_1.perimeter())

print(rectangle_2.area())

print(rectangle_2.perimeter())

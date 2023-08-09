"""
Модуль 2 Python Advanced, Урок 3 ООП Основні парадигми, Вправа 6
Створіть клас Circle, який представляє коло.
Реалізуйте методи для обчислення площі та довжини кола. Використовуйте аттрибут класу для зберігання значення π (pi).
"""

import math

class Circle:
    """клас Circle, який представляє коло.Реалізовані методи для обчислення площі та довжини кола."""
    pi = math.pi
    def __init__(self, radius):
        """конструктор"""
        self.radius = radius

    def area(self):
        """метод для обчислення площі кола"""
        area = self.pi * self.radius *self.radius
        return area

    def circuit(self):
        """метод для обчислення довжини кола"""
        circuit = 2 * self.pi * self.radius
        return circuit


circle_1 = Circle(5)

print(circle_1.area())

print(circle_1.circuit())

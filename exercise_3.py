"""
Модуль 2 Python Advanced, Урок 3 ООП Основні парадигми, Вправа 3
Розробіть клас Vehicle для представлення транспортного засобу. Додайте атрибути, такі як назва, швидкість і вартість.
Реалізуйте метод __gt__, який порівнює два транспортних засоби за швидкістю.
Створіть список транспортних засобів і відсортуйте його за швидкістю.
"""

class Vehicle:
    """ клас Vehicle для представлення транспортного засобу. Містить атрибути, такі як назва, швидкість і вартість.
    Реалізований метод __gt__, який порівнює два транспортних засоби за швидкістю. """

    def __init__(self, name, speed, cost):
        """конструктор"""
        self.name = name
        self.speed = speed
        self.cost = cost

    def __gt__(self, other):
        """метод __gt__, який порівнює два транспортних засоби за швидкістю."""
        return self.speed > other.speed

    def __repr__(self):
        return f"[{self.name}, {self.speed}, {self.cost}]"

    def __str__(self):
        return f"Name: {self.name},\nSurname: {self.speed},\nIBAN: {self.cost},\n"




toyota_corolla = Vehicle("Toyota Corolla", 180, 22000)
honda_civic = Vehicle("Honda Civic", 170, 24000)
nissan_altima = Vehicle("Nissan Altima", 190, 28000)
ford_focus = Vehicle("Ford Focus", 160, 21000)
hyundai_elantra = Vehicle("Hyundai Elantra", 175, 23000)

car_list = [toyota_corolla, honda_civic, nissan_altima, ford_focus, hyundai_elantra]

print(car_list)

sorted_car_list_increase = sorted(car_list)

print(sorted_car_list_increase)

sorted_car_list_decrease = sorted(car_list, reverse=True)

print(sorted_car_list_decrease)

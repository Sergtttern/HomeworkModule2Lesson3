"""
Модуль 2 Python Advanced, Урок 3 ООП Основні парадигми, Вправа 4

Створіть клас Student для представлення студента. Додайте атрибути, такі як ім'я, прізвище і список оцінок.
Реалізуйте метод __len__, який повертає кількість оцінок студента. Створіть список студентів і відсортуйте його
за кількістю оцінок.
"""

class Student:
    """клас Student для представлення студента. Має атрибути, такі як ім'я, прізвище і список оцінок.
    Реалізований метод __len__, який повертає кількість оцінок студента."""

    def __init__(self, name, surname, list_of_grades ):
        """конструктор"""
        self.name = name
        self.surname = surname
        self.list_of_grades = list_of_grades

    def __len__(self):
        """метод __len__, який повертає кількість оцінок студента."""
        return len(self.list_of_grades)

    def __repr__(self):
        return f"(Object attributes:\nName: {self.name},\nSurname: {self.surname},\nList of grades: " \
               f"{self.list_of_grades})\n"

    def __gt__(self, other):
        """метод __gt__ для порівняння об'єктів по кількості оцінок"""
        if isinstance(other, Student):
            return self.__len__() > other.__len__()
        raise ValueError("Unsupported operand type for >")


stud_1 = Student("Ivan", "Ivanenko", [12, 11, 8, 7, 9])
stud_2 = Student("Petro", "Petrenko", [10, 5, 8, 6, 8, 8, 9,3])
stud_3 = Student("Vasyl", "Vasylenko", [9, 5, 4,])


students_list = [stud_1, stud_2, stud_3]

print("_" * 120)

print(f"Список студентів: {students_list}")

print("_" * 120)

sorted_students_list_increase_number_of_grades = sorted(students_list)

print(f"Список студентів від відсортований від меншої кількості оціцонк у студента до більшої:"
      f" {sorted_students_list_increase_number_of_grades}\n")

print("_" * 120)

sorted_students_list_decrease_number_of_grades = sorted(students_list, reverse=True)

print(f"Список студентів від відсортований від більшої кількості оціцонк у студента до меншої:"
      f" {sorted_students_list_decrease_number_of_grades}\n")

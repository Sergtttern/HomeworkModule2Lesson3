"""
Модуль 2 Python Advanced, Урок 3 ООП Основні парадигми, Вправа 7
Створіть клас Student, який представляє студента. Реалізуйте атрибут класу для відстеження кількості студентів.
Для цього змінюйте значення атрибуту класу у методі __init__ .
Та створіть клас метод для виведення загальної кількості студентів.
"""

class Student:
    """клас Student, який представляє студента."""
    students_number = 0

    def __init__(self, name, surname, age):
        """конструктор"""
        self.name = name
        self.surname = surname
        self.age = age
        Student.students_number += 1

    @classmethod
    def output_students_number(cls):
        """клас метод для виведення загальної кількості студентів"""
        print(cls.students_number)


student_1 = Student("Petro","Petrenko", 18)

print(Student.students_number)

student_2 = Student("Vasyl", "Vasulenko", 17)

print(Student.students_number)

Student.output_students_number()

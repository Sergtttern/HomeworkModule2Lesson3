"""
Модуль 2 Python Advanced, Урок 3 ООП Основні парадигми, Вправа 2
Розробіть клас BankAccount для представлення банківського рахунку. Додайте методи для зняття та
поповнення коштів на рахунку. Використовуйте магічний метод __str__ для виведення інформації про рахунок.
"""

class BankAccount:
    """ клас BankAccount для представлення банківського рахунку. Має методи для зняття та
    поповнення коштів на рахунку"""

    def __init__(self, name, surname, iban, amount):
        """конструктор"""
        self.name = name
        self.surname = surname
        self.iban = iban
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return BankAccount(self.name, self.surname, self.iban,self.amount + other.amount)
        raise ValueError("Unsupported operand type for +")

    def withdraw_funds_from_the_account(self, transaction):
        """метод для зняття коштів з рахунку"""
        if self.amount - transaction < 0:
            print("There are not enough funds in the account")
        else:
            self.amount = self.amount - transaction

    def top_up_the_account(self, transaction):
        """метод для поповнення рахунку"""
        self.amount = self.amount + transaction

    def __repr__(self):
        return f"{self.name}, {self.surname}, {self.iban}, {self.amount}"

    def __str__(self):
        return f"Name: {self.name},\nSurname: {self.surname},\nIBAN: {self.iban},\namount: {self.amount}\n"


user_1 = BankAccount('Petro', 'Petrenko', 'UA579403947234747234747', 100)
user_2 = BankAccount('Ivan', 'Ivanenko', 'UA475034859794734757545', 100)

transaction_1 = BankAccount('Petro', 'Petrenko', 'UA579403947234747234747', -20)
transaction_2 = BankAccount('Ivan', 'Ivanenko', 'UA475034859794734757545', 50)

result_1 = user_1 + transaction_1
result_2 = user_2 + transaction_2

print(user_1)
print(user_2)

print(result_1)
print(result_2)

transaction_3 = BankAccount('Petro', 'Petrenko', 'UA579403947234747234747', 10)
transaction_4 = BankAccount('Ivan', 'Ivanenko', 'UA475034859794734757545', 10)

result_3 = user_1 + transaction_3
result_4 = user_2 + transaction_4

print(result_3)
print(result_4)

user_1.top_up_the_account(1000)
print(user_1)

user_2.withdraw_funds_from_the_account(1000)
print(user_2)

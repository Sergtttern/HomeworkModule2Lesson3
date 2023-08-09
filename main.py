class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    def __eq__(self, other):
        print("self.age == other.age")
        return self.age == other.age

    def __lt__(self, other):
        #lower then
        print("self.age < other.age")
        return self.age < other.age

    def __gt__(self, other):
        #greater then
        print("self.age > other.age")
        return self.age > other.age

    def __add__(self, other):
        return Person(
            f"{self.name} and {other.name}",
            self.age + other.age
        )

    def __sub__(self, other):
        if self < other:
            raise Exception(f"Cannot substract {other} from {self}" )
        return Person(
            f"{self.name} and {other.name}",
            self.age - other.age
        )

    def __mul__(self, other):
        return Person(
            f"{self.name} and {other.name}",
            self.age * other.age
        )

    def __len__(self):
        return len(self.name)

person1 = Person("Vladislav", 24)
person2 = Person("Igor", 22)

print(person1 == person2)

print(person1 < person2)

print(person1 > person2)

print(person1 + person2)

print(person1 - person2)

print(person1 * person2)

print(len(person1))











class Animal:  # Parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):  # Child class
    def speak(self):
        return f"{self.name} barks."

class Cat(Animal):  # Another child class
    def speak(self):
        return f"{self.name} meows."

# Usage
dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Rex barks.
print(cat.speak())  # Output: Whiskers meows.


def animal_sound(animal):
    print(animal.speak())

# Polymorphic behavior
animal_sound(dog)  # Output: Rex barks.
animal_sound(cat)  # Output: Whiskers meows.



class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner       # Public attribute
        self._balance = balance  # Protected attribute

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):  # Public method to access protected attribute
        return self._balance

# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance())  # Output: 1200

# Attempting direct access
print(account._balance)  # Works but is discouraged (Protected attribute).



class Employee:
    def __init__(self, name, salary):
        self.name = name               # Public
        self.__salary = salary         # Private

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")

    def work(self):
        return f"{self.name} is working."

class Manager(Employee):
    def work(self):  # Polymorphism through overriding
        return f"{self.name} is managing the team."

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language  # Public

    def work(self):  # Polymorphism through overriding
        return f"{self.name} is writing code in {self.programming_language}."

# Usage
employees = [
    Manager("Alice", 120000),
    Developer("Bob", 80000, "Python"),
    Developer("Charlie", 85000, "Java")
]

for emp in employees:
    print(emp.work())  # Polymorphic behavior
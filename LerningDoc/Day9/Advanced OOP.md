Here’s an explanation of **inheritance**, **polymorphism**, and **encapsulation** in Python with examples for each:

---

### **1. Inheritance**
Inheritance enables one class (child or derived class) to inherit the attributes and methods of another class (parent or base class). This promotes code reuse and hierarchy.

#### Example:
```python
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
```

---

### **2. Polymorphism**
Polymorphism allows the same method name to behave differently based on the context, often in a class hierarchy. This is achieved through method overriding or using common interfaces.

#### Example:
```python
def animal_sound(animal):
    print(animal.speak())

# Polymorphic behavior
animal_sound(dog)  # Output: Rex barks.
animal_sound(cat)  # Output: Whiskers meows.
```

Here, the `speak` method is overridden in the `Dog` and `Cat` classes, but the interface (`speak`) remains consistent.

---

### **3. Encapsulation**
Encapsulation involves bundling data (attributes) and methods that operate on the data into a single unit (class) and restricting access to some of the object's components using access modifiers.

- **Public**: Accessible anywhere.
- **Protected**: Denoted by a single underscore (`_`), intended for internal use.
- **Private**: Denoted by double underscores (`__`), accessible only within the class.

#### Example:
```python
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
```

---

### **Combining All Three Concepts**
Here’s an advanced example combining **inheritance**, **polymorphism**, and **encapsulation**:

```python
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
```

#### Output:
```
Alice is managing the team.
Bob is writing code in Python.
Charlie is writing code in Java.
```
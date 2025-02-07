Writing **modular and reusable** code in Python involves structuring your code into well-defined, independent, and reusable components. Here’s how you can achieve that:

---

### 1. **Use Functions to Encapsulate Logic**
Functions allow you to break down your code into reusable blocks.

```python
def greet(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}!"

print(greet("Alice"))
```

✅ **Benefits:** Avoids repetition and makes updates easier.

---

### 2. **Organize Code into Modules**
A **module** is just a `.py` file containing functions, classes, and variables.

**Example**: Create a file `math_utils.py`:

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

Then, import and use it in another file:

```python
import math_utils

result = math_utils.add(5, 3)
print(result)  # 8
```

✅ **Benefits:** Separates concerns and improves maintainability.

---

### 3. **Use Classes for Reusable Components**
Encapsulate data and behavior using **OOP principles**.

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

alice = Person("Alice", 25)
print(alice.introduce())
```

✅ **Benefits:** Encourages encapsulation and code reuse.

---

### 4. **Leverage Inheritance & Polymorphism**
Avoid duplicating logic by using inheritance.

```python
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
```

✅ **Benefits:** Promotes code reuse and flexibility.

---

### 5. **Use Python Packages for Large-Scale Projects**
If your project grows, organize it into **packages** (folders with `__init__.py`).

```
my_project/
│── main.py
│── utils/
│   │── __init__.py
│   │── file_utils.py
│   │── db_utils.py
```

Then, import modules as:

```python
from utils.file_utils import read_file
```

✅ **Benefits:** Provides better structure for large applications.

---

### 6. **Use Decorators for Reusable Functionality**
Decorators allow you to modify functions dynamically.

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def say_hello():
    print("Hello!")

say_hello()
```

✅ **Benefits:** Improves modularity without modifying existing code.

---

### 7. **Use Dependency Injection for Flexibility**
Instead of hardcoding dependencies, pass them as parameters.

```python
class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")

class Notification:
    def __init__(self, service):
        self.service = service

    def notify(self, message):
        self.service.send_email(message)

email_service = EmailService()
notifier = Notification(email_service)
notifier.notify("Hello, World!")
```

✅ **Benefits:** Makes testing easier and promotes loose coupling.

---

### 8. **Write Generic Functions Using Generics**
Use **Type Hints** and **Generics** for reusable functions.

```python
from typing import TypeVar, List

T = TypeVar("T")  # Generic type

def reverse_list(items: List[T]) -> List[T]:
    return items[::-1]

print(reverse_list([1, 2, 3]))  # [3, 2, 1]
print(reverse_list(["a", "b", "c"]))  # ['c', 'b', 'a']
```

✅ **Benefits:** Increases code flexibility while maintaining type safety.

---

### 9. **Use Configuration Files Instead of Hardcoding Values**
Avoid hardcoding values; use `.json`, `.yaml`, or `.env` files.

Example using `config.json`:

```json
{
  "api_key": "123456",
  "timeout": 30
}
```

Load it in Python:

```python
import json

with open("config.json") as f:
    config = json.load(f)

print(config["api_key"])
```

✅ **Benefits:** Improves maintainability and reusability.

---

### 10. **Write Unit Tests for Reusable Components**
Use `pytest` or `unittest` to ensure your code is modular and works correctly.

Example:

```python
import unittest
from math_utils import add

class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

✅ **Benefits:** Prevents regressions and ensures reusability.

---

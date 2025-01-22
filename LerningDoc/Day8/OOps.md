Object-Oriented Programming (OOP) is a programming paradigm that revolves around the use of **classes**, **objects**, and **methods**. Python fully supports OOP, allowing you to create reusable and modular code.

### Key OOP Concepts in Python

1. **Class**: A blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.

2. **Object**: An instance of a class. It represents a specific entity created based on the class blueprint.

3. **Methods**: Functions defined inside a class that operate on objects of the class.

---

### Example of Classes, Objects, and Methods

```python
# Define a class
class Car:
    # Constructor method to initialize attributes
    def __init__(self, brand, model, year):
        self.brand = brand   # Instance attribute
        self.model = model
        self.year = year

    # Method to display car details
    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

    # Method to simulate starting the car
    def start_engine(self):
        return f"The {self.model} engine has started!"

# Create objects (instances of the Car class)
car1 = Car("Toyota", "Corolla", 2021)
car2 = Car("Honda", "Civic", 2022)

# Access object methods and attributes
print(car1.display_info())  # Output: 2021 Toyota Corolla
print(car2.start_engine())  # Output: The Civic engine has started!

# Modify object attributes
car1.year = 2023
print(car1.display_info())  # Output: 2023 Toyota Corolla
```

---

### Breakdown of the Example

1. **Class Definition**:  
   - `class Car:` defines the class.  
   - The `__init__` method is the constructor used to initialize object attributes.

2. **Attributes**:  
   - `self.brand`, `self.model`, and `self.year` are attributes specific to each object.

3. **Methods**:  
   - `display_info` and `start_engine` are methods defined within the class. They operate on the attributes of the object.

4. **Objects**:  
   - `car1` and `car2` are instances of the `Car` class, each with their own attributes.

---

### Key Points
- Use the keyword `class` to define a class.
- Use the `__init__` method to initialize object attributes.
- Use `self` to refer to the current instance of the class.
- Methods can be called using `object_name.method_name()`.

This is a simple introduction to OOP in Python. More advanced OOP concepts include **inheritance**, **polymorphism**, **encapsulation**, and **abstraction**. Let me know if you'd like to explore these further!
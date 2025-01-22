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

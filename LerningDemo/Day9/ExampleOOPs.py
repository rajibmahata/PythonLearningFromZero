#Scenario: Vehicle Management System


class Vehicle:
    def __init__(self, name, speed):
        self.name = name  # Public attribute
        self._speed = speed  # Protected attribute (speed in km/h)

    def move(self):
        return f"{self.name} is moving at {self._speed} km/h."

    def stop(self):
        return f"{self.name} has stopped."


class LandVehicle(Vehicle):
    def __init__(self, name, speed, wheels):
        super().__init__(name, speed)
        self.wheels = wheels  # Number of wheels

    def describe(self):
        return f"{self.name} is a land vehicle with {self.wheels} wheels."
    
class WaterVehicle(Vehicle):
    def __init__(self, name, speed, capacity):
        super().__init__(name, speed)
        self.capacity = capacity  # Number of passengers

    def describe(self):
        return f"{self.name} is a water vehicle with a capacity of {self.capacity} passengers."


class Car(LandVehicle):
    def __init__(self, name, speed, wheels, fuel_type):
        super().__init__(name, speed, wheels)
        self.fuel_type = fuel_type  # e.g., petrol, diesel, electric

    def honk(self):
        return f"{self.name} is honking: Beep Beep!"

class Boat(WaterVehicle):
    def __init__(self, name, speed, capacity, boat_type):
        super().__init__(name, speed, capacity)
        self.boat_type = boat_type  # e.g., sailboat, motorboat

    def anchor(self):
        return f"{self.name} has dropped anchor."


# Create instances
car = Car("Tesla Model S", 200, 4, "electric")
boat = Boat("Speedster 3000", 80, 6, "motorboat")

# Test methods
print(car.describe())  # Tesla Model S is a land vehicle with 4 wheels.
print(car.move())      # Tesla Model S is moving at 200 km/h.
print(car.honk())      # Tesla Model S is honking: Beep Beep!

print(boat.describe())  # Speedster 3000 is a water vehicle with a capacity of 6 passengers.
print(boat.move())      # Speedster 3000 is moving at 80 km/h.
print(boat.anchor())    # Speedster 3000 has dropped anchor.



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

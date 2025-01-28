import mymodule

print(mymodule.greet("Alice"))  # Output: Hello, Alice!
print(mymodule.PI)             # Output: 3.14159


from mymodule import greet, PI

print(greet("Bob"))  # Output: Hello, Bob!


import math

print(math.sqrt(16))         # Output: 4.0
print(math.pi)              # Output: 3.141592653589793
print(math.factorial(5))    # Output: 120
print(math.sin(math.radians(90)))  # Output: 1.0


import os

# Get the current working directory
print(os.getcwd())  

# List files and directories in a path
print(os.listdir('.'))

# Create a new directory
os.mkdir("new_folder")

# Remove a directory
os.rmdir("new_folder")

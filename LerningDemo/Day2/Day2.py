# Rules for Variable Names:
# Must start with a letter or an underscore (_), not a number.
# Can only contain alphanumeric characters and underscores (a-z, A-Z, 0-9, _).
# Case-sensitive (name and Name are different).
# Cannot use Python keywords (e.g., if, else, for, etc.)

from datetime import datetime

name="Rajib"
age=34
weight=69.20
is_valid = True
dateCreated= datetime.now()
dateEnd=datetime(2024,12,31)

print(f"Name:{name}, Age:{age}, Date created:{dateCreated}")

print(f"Type of Name Data Type :{type(name)}" )

print(f"Type of Age Data Type {type(age)}")

print(f"Type of Weight Data Type { type(weight)}")

print(f"Type of Date Created Data Type {type(dateCreated)}")

print(f"Type of Date End Data Type :{type(dateEnd)}")

print(f"Type of Date is_valid Data Type :{type(is_valid)}")

print(f"Name: {name}, Type:{type(name)}, Age:{age}, Type:{type(age)},  Date Created:{dateCreated}, Type:{type(dateCreated)}, is_valid:{is_valid}, Type:{type(is_valid)}")


print("Name:"+ name +" Age:"+ str(age))

str_Weight=str(weight)
Float_Age=float(age)

print("Weight:"+ str_Weight +" Age:"+ str(Float_Age))

name = input("Enter your name : ")

print("Name:"+name)

age= int(input("Enter your age : "))

print("Age:"+str(age))

str_dateCreated =input("Date Created (yyyy-mm-dd):")

print("Date Created :"+ str(str_dateCreated))
dateCreated_date=datetime.strptime(str_dateCreated,"%Y-%m-%d").date()
print(f"Date Created Date:{dateCreated_date}")

# Simple print
print("Hello, World!")

# Printing multiple values
print("Python", "is", "awesome", sep="-")  # Output: Python-is-awesome

# Custom ending
print("Hello", end="!")  # Output: Hello!
print("Welcome")         # Output: Hello!Welcome

price = 9.99
print("The price is ${:.2f}".format(price))  # Output: The price is $9.99

name = "Alice"
age = 25
print("Hello %s, you are %d years old." % (name, age))


a, b = map(int, input("Enter two numbers separated by space: ").split())
print(f"The sum of {a} and {b} is {a + b}")

# Input and output example
name = input("What is your name? ")
age = int(input("How old are you? "))
print(f"Hello {name}, you will be {age + 1} years old next year.")



print("Basic Arithmetic Operations in Python")
print("\nLet's practice some basic arithmetic operations:")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
addition = num1 + num2
print(f"Addition: {num1} + {num2} = {addition}")

# Subtraction
subtraction = num1 - num2
print(f"Subtraction: {num1} - {num2} = {subtraction}")

# Multiplication
multiplication = num1 * num2
print(f"Multiplication: {num1} * {num2} = {multiplication}")

# Division
if num2 != 0:
    division = num1 / num2
    print(f"Division: {num1} / {num2} = {division}")
else:
    print("Division by zero is not allowed.")

# Modulo
if num2 != 0:
    modulo = num1 % num2
    print(f"Modulo: {num1} % {num2} = {modulo}")
else:
    print("Modulo by zero is not allowed.")

# Exponentiation
exponentiation = num1 ** num2
print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")


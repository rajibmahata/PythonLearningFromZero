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

dateCreated =datetime(input("Date Created :"))

print("Date Created :"+ str(dateCreated))

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


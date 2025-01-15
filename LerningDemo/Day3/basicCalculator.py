# Basic Calculator Program
operator = input("Enter operator: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == '/':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Division by zero is not allowed.")
else:    
    print("Invalid operator")

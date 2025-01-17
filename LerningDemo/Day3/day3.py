age = 20
if age >= 18:
    print("You are an adult.")  # This line only executes if age >= 18 is True


num=12

if num>5:
    print("Number is greater than 5")
    if num>10:
        print("Number is greater than 10")
        if num> 12:
            print("Number is greater than 12")
        elif num==12:
            print("Number is 12")
        else:
            print("Number is less than 12")
    elif num==10:
       print("Number is 10")
    else:
       print("Number is less than 10")
elif num==5:
    print("Number is 5")
else:
    print("Number is less than 5")

    if num<=47:
        print("Number is between 5 and 47")
        if num==10:
            print("Number is 10")
        else:
            print("Number is not 10")
    else:
        print("Number is not between 5 and 47")

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


# Nested if-else statement


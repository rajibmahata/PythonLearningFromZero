

```python
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
```



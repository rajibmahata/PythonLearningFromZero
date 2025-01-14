### **Input and Output Functions in Python**  

Input and output functions are essential for interacting with users or displaying information. Here's how they work in Python:

---

### **1. Input Functions**  
The `input()` function is used to take input from the user.  

#### **Syntax**:  
```python
variable = input(prompt_message)
```

#### **Key Points**:  
- Always returns the input as a **string**, even if the user enters numbers.  
- You may need to **convert** the input to the desired data type (e.g., `int`, `float`).  

#### **Examples**:  
```python
# Taking a string input
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Taking a number input (convert string to integer)
age = int(input("Enter your age: "))
print("You are", age, "years old.")
```

---

### **2. Output Functions**  
The `print()` function is used to display output on the screen.  

#### **Syntax**:  
```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

#### **Key Parameters**:  
- **`*objects`**: One or more values to print.  
- **`sep`**: Separator between values (default is a space).  
- **`end`**: Specifies what to print at the end (default is a newline `\n`).  

#### **Examples**:  
```python
# Simple print
print("Hello, World!")

# Printing multiple values
print("Python", "is", "awesome", sep="-")  # Output: Python-is-awesome

# Custom ending
print("Hello", end="!")  # Output: Hello!
print("Welcome")         # Output: Hello!Welcome
```

---

### **3. Combining Input and Output**  
You can use both input and output functions together.  

#### **Example**:  
```python
name = input("What is your name? ")
print("Nice to meet you,", name)

# Calculate the square of a number entered by the user
num = int(input("Enter a number: "))
print("The square of", num, "is", num ** 2)
```

---

### **4. String Formatting in Outputs**  
You can format strings to make your outputs more readable.  

#### **Using f-strings** (Recommended in Python 3.6+):  
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")
```

#### **Using `format()` Method**:  
```python
price = 9.99
print("The price is ${:.2f}".format(price))  # Output: The price is $9.99
```

#### **Using `%` Formatting** (Older Style):  
```python
name = "Alice"
age = 25
print("Hello %s, you are %d years old." % (name, age))
```

---

### **5. Advanced Input Handling**  
You can process multiple inputs or use conditional logic based on user input.  

#### **Example**:  
```python
# Taking multiple inputs
a, b = map(int, input("Enter two numbers separated by space: ").split())
print(f"The sum of {a} and {b} is {a + b}")
```

---

### **Try It Yourself**  
```python
# Input and output example
name = input("What is your name? ")
age = int(input("How old are you? "))
print(f"Hello {name}, you will be {age + 1} years old next year.")
```
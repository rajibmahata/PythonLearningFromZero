### **Understanding Variables and Data Types in Python**  

---

### **1. Variables**  
A variable is a named container for storing data. In Python, variables are created when you assign a value to them.  

#### **Rules for Variable Names**:  
- Must start with a letter or an underscore (`_`), not a number.  
- Can only contain alphanumeric characters and underscores (`a-z`, `A-Z`, `0-9`, `_`).  
- Case-sensitive (`name` and `Name` are different).  
- Cannot use Python keywords (e.g., `if`, `else`, `for`, etc.).  

#### **Example**:  
```python
name = "Alice"  # A string variable
age = 30        # An integer variable
height = 5.6    # A float variable
is_student = True  # A boolean variable
```

---

### **2. Data Types**  
Python has several built-in data types. Let's focus on the most common ones:  

#### **(a) Integer (`int`)**  
Represents whole numbers, positive or negative.  
```python
age = 25
score = -10
```
Type checking:  
```python
print(type(age))  # Output: <class 'int'>
```

#### **(b) Float (`float`)**  
Represents decimal numbers.  
```python
pi = 3.14
temperature = -7.5
```
Type checking:  
```python
print(type(pi))  # Output: <class 'float'>
```

#### **(c) String (`str`)**  
Represents text or characters, enclosed in single or double quotes.  
```python
name = "Python"
greeting = 'Hello, World!'
```
Type checking:  
```python
print(type(name))  # Output: <class 'str'>
```
String operations:  
```python
full_name = "John" + " Doe"  # Concatenation
print(full_name)             # Output: John Doe
```

#### **(d) Boolean (`bool`)**  
Represents `True` or `False`.  
```python
is_valid = True
has_errors = False
```
Type checking:  
```python
print(type(is_valid))  # Output: <class 'bool'>
```

---

### **3. Type Conversion**  
You can convert between types using built-in functions.  

#### **Examples**:  
```python
# Integer to float
x = 10
y = float(x)  # Converts x to 10.0

# Float to integer
z = int(5.7)  # Converts z to 5 (truncated)

# Integer to string
age = 25
age_str = str(age)  # Converts 25 to "25"

# String to integer
num = int("100")  # Converts "100" to 100
```

---

### **4. Dynamic Typing**  
Python is dynamically typed, meaning you don’t need to declare the data type explicitly. It’s determined at runtime.  

Example:  
```python
x = 5           # Initially an integer
x = "Python"    # Now a string
```

---

### **Try It Yourself**  
Write this in your Python file and observe the output:  
```python
# Variables and their types
name = "Alice"
age = 30
height = 5.7
is_student = True

# Print values and types
print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}")
```
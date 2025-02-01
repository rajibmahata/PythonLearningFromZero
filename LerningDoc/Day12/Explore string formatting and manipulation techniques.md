String formatting and manipulation are essential in Python for handling and processing text. Here’s a comprehensive guide with examples:

---

## **1. String Formatting Methods**
### **a) f-strings (Python 3.6+)** ✅ (Best Practice)
```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```
#### **Formatting Inside f-strings**
```python
pi = 3.14159
print(f"Pi rounded to 2 decimal places: {pi:.2f}")  # Output: 3.14
```

---

### **b) `.format()` Method (Python 2.7+)**
```python
print("My name is {} and I am {} years old.".format(name, age))
print("Pi rounded to 2 decimal places: {:.2f}".format(pi))
```

---

### **c) `%` Formatting (Old Style, Python 2)**
```python
print("My name is %s and I am %d years old." % (name, age))
```
✅ **Use `f-strings` instead for modern Python**

---

## **2. String Manipulation Techniques**
### **a) Changing Case**
```python
text = "hello world"
print(text.upper())    # HELLO WORLD
print(text.lower())    # hello world
print(text.title())    # Hello World
print(text.capitalize())  # Hello world
print(text.swapcase())    # HELLO WORLD
```

---

### **b) Trimming Whitespace**
```python
text = "  hello world  "
print(text.strip())  # "hello world"
print(text.lstrip()) # "hello world  "
print(text.rstrip()) # "  hello world"
```

---

### **c) Replacing Substrings**
```python
text = "Hello, World!"
print(text.replace("World", "Python"))  # "Hello, Python!"
```

---

### **d) Splitting and Joining**
```python
text = "apple,banana,grape"
words = text.split(",")  # ['apple', 'banana', 'grape']
print(words)

joined = "-".join(words)  # "apple-banana-grape"
print(joined)
```

---

### **e) Checking Substrings**
```python
text = "Hello, Python!"
print("Python" in text)  # True
print(text.startswith("Hello"))  # True
print(text.endswith("!"))  # True
```

---

## **3. String Alignment and Padding**
```python
text = "Python"
print(text.center(20, "-"))  # "-------Python--------"
print(text.ljust(20, "*"))   # "Python**************"
print(text.rjust(20, "."))   # "..............Python"
```

---

## **4. Removing Unwanted Characters**
```python
text = "###Python###"
print(text.strip("#"))  # "Python"
print(text.lstrip("#"))  # "Python###"
print(text.rstrip("#"))  # "###Python"
```

---

## **5. Formatting Numbers in Strings**
```python
num = 12345.6789
print(f"Number: {num:,.2f}")  # "12,345.68"
print(f"Hex: {num:x}")        # "3039" (hexadecimal)
print(f"Binary: {num:b}")     # "11000000111001" (binary)
```

---

## **6. Multi-line Strings**
```python
multi_line = """This is
a multi-line
string."""
print(multi_line)
```

---


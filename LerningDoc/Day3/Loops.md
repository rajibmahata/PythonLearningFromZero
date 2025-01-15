Python offers two primary loop constructs: `for` loops and `while` loops.  They provide ways to repeatedly execute a block of code.  The choice between them depends on whether you know the number of iterations in advance.

**1. `for` Loops:**

`for` loops are ideal when you know the number of iterations or are iterating over a sequence (like a list, tuple, string, or range).

**Basic Syntax:**

```python
for item in sequence:
    # Code to be executed repeatedly
```

**Examples:**

* **Iterating over a list:**

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output: apple, banana, cherry (each on a new line)
```

* **Iterating over a string:**

```python
message = "Hello"
for character in message:
    print(character)  # Output: H, e, l, l, o (each on a new line)
```

* **Iterating over a range of numbers:**

```python
for i in range(5):  # range(5) generates numbers 0, 1, 2, 3, 4
    print(i)       # Output: 0, 1, 2, 3, 4 (each on a new line)

for i in range(2, 8): # range(2,8) generates numbers 2,3,4,5,6,7
    print(i)
```

* **Iterating with index:**

You can use `enumerate` to get both the index and value of each item in a sequence.

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Fruit at index {index}: {fruit}")
```


**2. `while` Loops:**

`while` loops repeat a block of code as long as a specified condition is `True`.  Use `while` loops when you don't know the exact number of iterations beforehand, or when the loop should continue until a specific condition is met.

**Basic Syntax:**

```python
while condition:
    # Code to be executed repeatedly
```

**Examples:**

* **Counting down from 10:**

```python
count = 10
while count > 0:
    print(count)
    count -= 1  # Decrement count in each iteration
```

* **Looping until user enters a specific input:**

```python
user_input = ""
while user_input != "quit":
    user_input = input("Enter 'quit' to exit: ")
    print(f"You entered: {user_input}")
```

* **Infinite Loop (Caution!):**

A `while True` loop runs indefinitely unless explicitly broken using a `break` statement.  Be careful with infinite loops, as they can crash your program.

```python
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")
```

**Loop Control Statements:**

* **`break`:**  Immediately terminates the loop.
* **`continue`:** Skips the rest of the current iteration and proceeds to the next.


**Example using `break` and `continue`:**

```python
for i in range(10):
    if i == 5:
        continue  # Skip the rest of this iteration if i is 5
    if i == 8:
        break     # Exit the loop if i is 8
    print(i)      # Output: 0 1 2 3 4 6 7
```

Choosing between `for` and `while` loops:

* Use `for` loops when you know the number of iterations or are iterating over a sequence.
* Use `while` loops when the number of iterations is unknown or depends on a condition.  Remember to avoid infinite loops.


These examples illustrate the core functionality of `for` and `while` loops in Python.  They are fundamental building blocks for creating programs with iterative behavior.  Mastering their use is crucial for writing effective Python code.

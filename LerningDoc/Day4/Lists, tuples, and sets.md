### **Lists, Tuples, and Sets in Python**

Python provides powerful built-in data structures like **lists**, **tuples**, and **sets** to store and manipulate collections of data. Here's a comprehensive guide to their creation, indexing, slicing, and methods.

---

## **1. Lists**
A **list** is an ordered, mutable (modifiable), and indexable collection of items.

### **Creation**
```python
# Creating a list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.5]
```

### **Indexing**
Lists use zero-based indexing.
```python
fruits = ["apple", "banana", "cherry"]

# Access elements
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry (negative indexing)
```

### **Slicing**
You can retrieve a portion of the list using slicing.
```python
numbers = [0, 1, 2, 3, 4, 5]

# Slicing
print(numbers[1:4])  # Output: [1, 2, 3]
print(numbers[:3])   # Output: [0, 1, 2]
print(numbers[3:])   # Output: [3, 4, 5]
print(numbers[::2])  # Output: [0, 2, 4] (step of 2)
```

### **Methods**
```python
fruits = ["apple", "banana", "cherry"]

# Add items
fruits.append("orange")  # Adds to the end
fruits.insert(1, "kiwi")  # Adds at index 1

# Remove items
fruits.remove("banana")  # Removes the first occurrence
popped = fruits.pop()  # Removes and returns the last item
del fruits[0]  # Deletes by index
fruits.clear()  # Removes all items

# Other methods
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Length of the list
fruits.sort()       # Sorts the list
fruits.reverse()    # Reverses the list
print(fruits.count("apple"))  # Count occurrences
```

---

## **2. Tuples**
A **tuple** is an ordered, immutable (cannot be changed after creation) collection of items.

### **Creation**
```python
# Creating a tuple
fruits = ("apple", "banana", "cherry")
singleton = (42,)  # Single element tuple requires a trailing comma
```

### **Indexing**
Similar to lists, tuples support indexing.
```python
fruits = ("apple", "banana", "cherry")
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry
```

### **Slicing**
Tuples support slicing just like lists.
```python
fruits = ("apple", "banana", "cherry", "date")
print(fruits[1:3])  # Output: ('banana', 'cherry')
```

### **Methods**
Tuples have fewer methods because they are immutable.
```python
fruits = ("apple", "banana", "cherry")
print(len(fruits))  # Length of the tuple
print(fruits.count("apple"))  # Count occurrences
print(fruits.index("banana"))  # Find index of an element
```

---

## **3. Sets**
A **set** is an unordered collection of unique items. Sets are mutable but do not allow duplicates.

### **Creation**
```python
# Creating a set
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 3, 4])  # Using the set() constructor
empty_set = set()  # Use set(), not {}, to create an empty set
```

### **Indexing and Slicing**
- **Sets do not support indexing or slicing** because they are unordered.
- You must iterate over a set to access elements.

### **Methods**
```python
fruits = {"apple", "banana", "cherry"}

# Add and remove items
fruits.add("orange")       # Adds an element
fruits.update(["kiwi", "mango"])  # Adds multiple elements
fruits.remove("banana")    # Removes an element (raises an error if not found)
fruits.discard("pear")     # Removes an element (does not raise an error if not found)
fruits.clear()             # Removes all elements

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))       # Union: {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # Intersection: {3}
print(set1.difference(set2))  # Difference: {1, 2}
print(set1.symmetric_difference(set2))  # Symmetric Difference: {1, 2, 4, 5}
```

---

### **Comparison of Lists, Tuples, and Sets**
| Feature            | List          | Tuple         | Set          |
|--------------------|---------------|---------------|--------------|
| Ordered            | Yes           | Yes           | No           |
| Mutable            | Yes           | No            | Yes          |
| Allows Duplicates  | Yes           | Yes           | No           |
| Indexable          | Yes           | Yes           | No           |
| Use Case           | General purpose, dynamic | Immutable collections | Unique elements, set operations |

---

### **Try It Yourself**
```python
# List example
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

# Tuple example
fruits_tuple = ("apple", "banana", "cherry")
print(fruits_tuple[1])

# Set example
fruits_set = {"apple", "banana", "cherry"}
fruits_set.add("orange")
print(fruits_set)
```
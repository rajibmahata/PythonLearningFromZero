Here’s a detailed look at the Python built-in functions `len()`, `sum()`, and `map()`:

---

### 1. **`len()`**
- **Purpose**: Returns the number of items in an object.
- **Supported Objects**: Strings, lists, tuples, dictionaries, sets, and other iterable objects.

#### Syntax:
```python
len(obj)
```

#### Examples:
```python
# String
print(len("Hello"))  # Output: 5

# List
print(len([1, 2, 3, 4]))  # Output: 4

# Dictionary
print(len({"a": 1, "b": 2}))  # Output: 2

# Tuple
print(len((10, 20, 30)))  # Output: 3
```

---

### 2. **`sum()`**
- **Purpose**: Adds the items in an iterable (e.g., list, tuple).
- **Optional Parameter**: A starting value can be specified.

#### Syntax:
```python
sum(iterable, start=0)
```

#### Examples:
```python
# List
print(sum([1, 2, 3, 4]))  # Output: 10

# Tuple
print(sum((10, 20, 30)))  # Output: 60

# Using a starting value
print(sum([1, 2, 3], 10))  # Output: 16

# Empty iterable with a starting value
print(sum([], 5))  # Output: 5
```

#### Notes:
- Works only for numeric data.
- For other data types (like strings), use `join()` for concatenation.

---

### 3. **`map()`**
- **Purpose**: Applies a given function to all items in an input iterable.
- **Returns**: A map object, which is an iterator (convert to a list, tuple, etc., if needed).

#### Syntax:
```python
map(function, iterable)
```

#### Examples:
```python
# Example 1: Doubling numbers
def double(x):
    return x * 2

nums = [1, 2, 3, 4]
result = map(double, nums)
print(list(result))  # Output: [2, 4, 6, 8]

# Example 2: Using lambda
nums = [1, 2, 3, 4]
result = map(lambda x: x ** 2, nums)
print(list(result))  # Output: [1, 4, 9, 16]

# Example 3: Mapping over multiple iterables
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
result = map(lambda x, y: x + y, nums1, nums2)
print(list(result))  # Output: [5, 7, 9]
```

#### Notes:
- The function provided to `map()` should take the same number of arguments as the number of iterables.
- Works well for transforming data.

---

### Key Differences:
| **Function** | **Purpose**                             | **Output**           |
|--------------|-----------------------------------------|----------------------|
| `len()`      | Counts items in an object.              | Integer              |
| `sum()`      | Adds items in an iterable.              | Number               |
| `map()`      | Applies a function to items in iterable.| Iterator (map object)|

Would you like a deeper dive into any of these, or examples combining them?
### **Introduction to NumPy in Python**
**NumPy (Numerical Python)** is a powerful library for numerical computing in Python. It provides support for **multi-dimensional arrays, mathematical functions, and efficient computations**.

#### **Installation**
If you haven't installed NumPy, install it using:
```sh
pip install numpy
```

---

## **1. Creating NumPy Arrays**
NumPy arrays (ndarrays) are **faster and more memory-efficient** than Python lists.

### **1.1 Creating an Array**
```python
import numpy as np

# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Creating a 2D array (Matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
```

### **1.2 Checking Array Properties**
```python
print(arr2.shape)  # (rows, columns)
print(arr2.size)   # Total number of elements
print(arr2.dtype)  # Data type of elements
print(arr2.ndim)   # Number of dimensions
```

### **1.3 Special Arrays**
```python
print(np.zeros((3, 3)))  # 3x3 matrix of zeros
print(np.ones((2, 2)))   # 2x2 matrix of ones
print(np.eye(4))         # 4x4 Identity matrix
print(np.random.rand(3, 3))  # Random numbers (0 to 1)
```

---

## **2. Indexing and Slicing**
NumPy arrays support advanced slicing and indexing.

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[1])      # Access element at index 1 (20)
print(arr[1:4])    # Slice from index 1 to 3 ([20, 30, 40])
print(arr[::-1])   # Reverse the array
```

### **Indexing in 2D Arrays**
```python
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr2[1, 2])    # Element at row index 1, column index 2 (6)
print(arr2[:, 1])    # All rows, column index 1 ([2, 5, 8])
print(arr2[0, :])    # Row index 0 ([1, 2, 3])
```

---

## **3. Basic Operations**
### **3.1 Arithmetic Operations**
NumPy allows element-wise operations.

```python
arr = np.array([1, 2, 3, 4])

print(arr + 10)  # Add 10 to each element
print(arr * 2)   # Multiply each element by 2
print(arr ** 2)  # Square each element
```

### **3.2 Mathematical Functions**
```python
print(np.sin(arr))   # Sine function
print(np.log(arr))   # Logarithm
print(np.sum(arr))   # Sum of all elements
print(np.mean(arr))  # Mean (average)
print(np.max(arr))   # Maximum value
print(np.min(arr))   # Minimum value
```

---

## **4. Reshaping and Transposing**
### **4.1 Reshape**
```python
arr = np.array([1, 2, 3, 4, 5, 6])
arr_reshaped = arr.reshape((2, 3))  # Reshape to 2 rows, 3 columns
print(arr_reshaped)
```

### **4.2 Transpose**
```python
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2.T)  # Transpose the matrix
```

---

## **5. Concatenation and Stacking**
### **5.1 Concatenation**
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate((a, b)))  # [1 2 3 4 5 6]
```

### **5.2 Stacking**
```python
print(np.vstack((a, b)))  # Vertical stack
print(np.hstack((a, b)))  # Horizontal stack
```

---

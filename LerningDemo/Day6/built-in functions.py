# len() function 

data="Hello World"

print(len(data))

numbers=[1,2,3,4,5,6,7,8,9,10]

print(len(numbers))

numbers=2
#print(len(numbers)) #TypeError: object of type 'int' has no len()

# max() function

numbers=[1,2,3,4,5,6,7,8,9,10]
print(max(numbers))

numbers=[1,2,3,4,5,6,7,8,9,10,100]
print(max(numbers))

names=["A","B","C","D","E","F","G","H","I","J"]
print(max(names))

names.reverse()
print(names)
print(max(names))

# min() function

numbers=[1,2,3,4,5,6,7,8,9,10]
print(min(numbers))

strings=["A","B","C","D","E","F","G","H","I","J"]
print(min(strings))

# sum() function

numbers=[1,2,3,4,5,6,7,8,9,10]
print(sum(numbers))

# round() function

print(round(10.5))

# abs() function

print(abs(-10))

# pow() function

print(pow(2,3))

# sorted() function

numbers=[1,2,3,4,5,6,7,8,9,10]
print(sorted(numbers))

# reversed() function

numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers.reverse())

# all() function

numbers=[1,2,3,4,5,6,7,8,9,10]
print(all(numbers))

#map() function 

numbers=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:x*x,numbers)))


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

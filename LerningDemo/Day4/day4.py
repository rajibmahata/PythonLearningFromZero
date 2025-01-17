
#List

list_Fruit=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(list_Fruit)

#Accessing Items
print(list_Fruit[1])

list_number=[1,2,3,4,5,6,7,8,9,10]

lst_numAndString=[1,2,3,4,5,6,7,8,9,10,"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(lst_numAndString)

print(lst_numAndString[10])
print(lst_numAndString[-5])

#Slicing

list1=[1,2,3,4,5,6,7,8,9,10]
slice_num=list1[1:3]
print(slice_num)

slice_num=list1[1:5]
print(slice_num)

slice_num=list1[:2]
print(slice_num)

slice_num=list1[2:]
print(slice_num)

slice_num=list1[-4:-1]
print(slice_num)

slice_num=list1[1:8:2]
print(slice_num)


fruits = ["apple", "banana", "cherry"]

# Add items
fruits.append("orange")  # Adds to the end
fruits.insert(1, "kiwi")  # Adds at index 1

print(fruits)

# Remove items
fruits.remove("banana")  # Removes the first occurrence
popped = fruits.pop()  # Removes and returns the last item
del fruits[0]  # Deletes by index
fruits.clear()  # Removes all items

print(fruits)

# Other methods
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Length of the list
fruits.sort()       # Sorts the list
fruits.reverse()    # Reverses the list
print(fruits.count("apple"))  # Count occurrences

print(fruits)

arrayNum=[1,2,3,4,5,6,7,8,9,10]

arrayNum.sort()
print(arrayNum)
arrayNum.append(11)
arrayNum.append(0)
arrayNum.sort()
print(arrayNum)

stringArray=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

stringArray.sort()
print(stringArray)
stringArray.reverse()

print(stringArray)
stringArray.remove("kiwi")
print(stringArray)
stringArray.pop()
print(stringArray)
del stringArray[0]

print(stringArray)


# Creating a tuple
fruits = ("apple", "banana", "cherry")
singleton = (42,)  # Single element tuple requires a trailing comma

print(fruits)
print(singleton)

fruits = ("apple", "banana", "cherry")
print(len(fruits))  # Length of the tuple
print(fruits.count("apple"))  # Count occurrences
print(fruits.index("banana"))  # Find index of an element


# Creating a set
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 3, 4,1])  # Using the set() constructor
empty_set = set()  # Use set(), not {}, to create an empty set

print(fruits)
print(numbers)
print(empty_set)


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
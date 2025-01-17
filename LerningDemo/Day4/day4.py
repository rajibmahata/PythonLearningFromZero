
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
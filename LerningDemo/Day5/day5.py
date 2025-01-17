

# create dictionary 

person={
    "name":"John",
    "age":36,
    "country":"Norway"
}

personDict= dict(name="John", age=36, country="Norway")

print(person)
print(personDict)

print(person["name"])
print(personDict["name"])
print(person.get("age"))
print(person.get("age2", "Not Found"))
print(person.keys())

person={ "name": "John", "age": 36, "country": "Norway" }
person["age"]=40
print(person)

person1 = {"name": "Alice", "age": 30, "city": "New York"}

# Remove a specific key
removed_value = person1.pop("age")  # Removes 'age' and returns its value
print(removed_value) 
 # Output: 30
print(person1)



# Remove the last inserted item (Python 3.7+)
last_item = person1.popitem()
print(last_item)  # Output: ('city', 'New York')

# Remove a key using del
del person1["name"]

# Clear all items
person1.clear()

print(person1)  # Output: {}


person = {"name": "Alice", "age": 30, "city": "New York"}

# Iterate through keys
for key in person:
    print(key)  # Output: name, age, city

# Iterate through values
for value in person.values():
    print(value)  # Output: Alice, 30, New York

# Iterate through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
    # Output: name: Alice, age: 30, city: New York


family = {
    "child1": {"name": "Alice", "age": 10},
    "child2": {"name": "Bob", "age": 8},
    "child3": {"name": "Charlie", "age": 5}
}

print(family["child1"]["name"])  # Output: Alice


# Example: Square of numbers
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

sentence = "apple banana apple cherry banana apple"
word_counts = {}

for word in sentence.split():
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)  # Output: {'apple': 3, 'banana': 2, 'cherry': 1}

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Using update()
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Using dictionary unpacking (Python 3.9+)
merged = {**dict1, **dict2}
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}

person = {"name": "Alice", "age": 30, "city": "New York"}

print(person.keys())    # Output: dict_keys(['name', 'age', 'city'])
print(person.values())  # Output: dict_values(['Alice', 30, 'New York'])
print(person.items())   # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
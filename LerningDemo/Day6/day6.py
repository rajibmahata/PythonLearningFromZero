# Recap of Day 5

#array 

array1=[1,2,3,4,5]
print(array1)

array1.append(6)
print(array1)
array1.pop()
print(array1)

array1.insert(2,7)
print(array1)
array1.remove(7)
print(array1)
array1.reverse()
print(array1)
array1.sort()
print(array1)

#tuple

tuple1=(1,2,3,4,5)
print(tuple1)
print(tuple1[2])

#dictionary

person={"name":"Rajib", "age":25, "city":"Kolkata"}
print(person)
person.pop("age")
print(person)
person.popitem()
print(person)
del person["name"]
print(person)

#set
set1={1,2,3,4,5}
print(set1)
set1.add(6)
print(set1)
set1.remove(6)
print(set1)




#functions :
print("Functions")

def add(a,b,c):
    return a+b+c

print(add(1,2,3))


def add(a,b,c=0):
    return a+b+c    

print(add(1,2))

def GetName(name):
    return name

print(GetName("Rajib"))

def GetAge(age=0):
    return age

print(GetAge(25))

function = lambda a,b,c : a+b+c

print(function(1,2,3))


def sum(*args):
    total=0
    for a in args:
        total+=a
    return total

print(sum(1,2,3,4,5))


#lambda function with *args

sum = lambda *args: sum(args)

print(sum(1,2,3,4,5))

squere= lambda x: x*x

print(squere(10))
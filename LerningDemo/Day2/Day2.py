# Rules for Variable Names:
# Must start with a letter or an underscore (_), not a number.
# Can only contain alphanumeric characters and underscores (a-z, A-Z, 0-9, _).
# Case-sensitive (name and Name are different).
# Cannot use Python keywords (e.g., if, else, for, etc.)

from datetime import datetime

name="Rajib"
age=34
weight=69.20
is_valid = True
dateCreated= datetime.now()
dateEnd=datetime(2024,12,31)

print(f"Name:{name}, Age:{age}, Date created:{dateCreated}")

print(f"Type of Name Data Type :{type(name)}" )

print(f"Type of Age Data Type {type(age)}")

print(f"Type of Weight Data Type { type(weight)}")

print(f"Type of Date Created Data Type {type(dateCreated)}")

print(f"Type of Date End Data Type :{type(dateEnd)}")

print(f"Type of Date is_valid Data Type :{type(is_valid)}")

print(f"Name: {name}, Type:{type(name)}, Age:{age}, Type:{type(age)},  Date Created:{dateCreated}, Type:{type(dateCreated)}, is_valid:{is_valid}, Type:{type(is_valid)}")
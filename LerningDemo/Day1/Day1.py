name = "Hello, Rajib "  # Assign a value to a variable
print(name)      # Print the value of the variable

# Correct indentation
if True:
    print("This is indented correctly.")

# Incorrect indentation
# if True:
# print("This will raise an IndentationError.")  # Not indented

# This is a single-line comment
print("Hello, World!")  # This prints a message

"""
This is a multi-line comment.
It can span multiple lines.
"""
print("Python is easy to learn!")

import sys

print(sys.version)

if 5>2 :
 print("five is greater then two")
if 5>2 :
 print("five is gretter then two")

 # nested if loop 

 if 2>1:
   if 3>2:
     print("three is greater then two and two is greater than one")

score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    if score >= 85:
        grade = 'B+'
    else:
        grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'

print(f"Your grade is: {grade}")

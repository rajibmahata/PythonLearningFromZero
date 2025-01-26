# Writing to a file
with open("example.txt", "w") as file:  # Open file in write mode
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
print("File written successfully.")

# Reading from a file
try:
    with open("example.txt", "r") as file:  # Open file in read mode
        content = file.read()
    print("\nFile content:")
    print(content)
except FileNotFoundError:
    print("File not found. Please ensure the file exists.")

# Appending to a file
with open("example.txt", "a") as file:  # Open file in append mode
    file.write("This is an appended line.\n")
print("\nData appended successfully.")

# Reading updated content
with open("example.txt", "r") as file:  # Open file in read mode
    updated_content = file.read()
print("\nUpdated file content:")
print(updated_content)

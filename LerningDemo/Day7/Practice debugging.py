numbers = [1, 2, 3]
index = 5

if index < len(numbers):
    print(numbers[index])
else:
    print(f"Error: Index {index} is out of range.")


try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist.")


def calculate_average(numbers):
    if not numbers:
        return "Error: No numbers provided!"
    total = sum(numbers)
    count = len(numbers)
    return total / count

user_input = input("Enter numbers separated by commas: ")
try:
    numbers = list(map(int, user_input.split(","))) if user_input else []
    print(f"The average is: {calculate_average(numbers)}")
except ValueError:
    print("Error: Please enter valid numbers!")

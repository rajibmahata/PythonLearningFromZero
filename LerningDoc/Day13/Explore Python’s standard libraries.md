Python’s standard libraries include powerful modules like `datetime` and `random`, which help with date/time manipulation and generating random numbers, respectively. Let's explore them in detail.

---

## **1. `datetime` Module (Date & Time Handling)**
The `datetime` module provides classes to manipulate dates and times easily.

### **Basic Usage**
```python
import datetime

# Get the current date and time
now = datetime.datetime.now()
print("Current Date & Time:", now)

# Get the current date
today = datetime.date.today()
print("Today's Date:", today)

# Create a custom date
custom_date = datetime.date(2023, 5, 17)
print("Custom Date:", custom_date)

# Time manipulation
custom_time = datetime.time(14, 30, 15)  # Hours, Minutes, Seconds
print("Custom Time:", custom_time)
```

### **Formatting Dates**
```python
# Format a datetime object as a string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)

# Convert a string to a datetime object
date_str = "2024-02-03 15:45:00"
parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed Date:", parsed_date)
```

### **Date Arithmetic**
```python
from datetime import timedelta

# Add 7 days to the current date
future_date = today + timedelta(days=7)
print("Future Date:", future_date)

# Subtract 3 days
past_date = today - timedelta(days=3)
print("Past Date:", past_date)
```

---

## **2. `random` Module (Random Number Generation)**
The `random` module provides functions to generate random numbers, shuffle sequences, and select random items.

### **Basic Random Numbers**
```python
import random

# Generate a random integer between 1 and 10
rand_int = random.randint(1, 10)
print("Random Integer:", rand_int)

# Generate a random floating-point number between 0 and 1
rand_float = random.random()
print("Random Float:", rand_float)

# Generate a random float in a range (e.g., 1.5 to 6.5)
rand_uniform = random.uniform(1.5, 6.5)
print("Random Uniform Float:", rand_uniform)
```

### **Random Choice & Shuffle**
```python
# Random choice from a list
colors = ["red", "blue", "green", "yellow"]
rand_color = random.choice(colors)
print("Random Color:", rand_color)

# Shuffle a list randomly
random.shuffle(colors)
print("Shuffled Colors:", colors)

# Get a random sample of 2 elements
rand_sample = random.sample(colors, 2)
print("Random Sample:", rand_sample)
```

### **Simulating Dice Rolls**
```python
def roll_dice():
    return random.randint(1, 6)

print("Dice Roll:", roll_dice())
```

---

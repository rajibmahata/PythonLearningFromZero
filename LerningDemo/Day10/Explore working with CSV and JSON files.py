import csv

# Read a CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list of strings

import csv

# Write data to a CSV file
data = [
    ["Name", "Age", "Country"],
    ["Alice", 30, "USA"],
    ["Bob", 25, "UK"],
    ["Charlie", 35, "Canada"],
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Write all rows at once
print("CSV file written successfully.")


import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # Each row is a dictionary


import csv

data = [
    {"Name": "Alice", "Age": 30, "Country": "USA"},
    {"Name": "Bob", "Age": 25, "Country": "UK"},
    {"Name": "Charlie", "Age": 35, "Country": "Canada"},
]

with open("output_dict.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "Country"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Write column headers
    writer.writerows(data)  # Write all rows
print("CSV file written successfully.")

import json

# Read a JSON file
with open("data.json", "r") as file:
    data = json.load(file)  # Load JSON into a Python dictionary or list
    print(data)


import json

data = [
    {"Name": "Alice", "Age": 30, "Country": "USA"},
    {"Name": "Bob", "Age": 25, "Country": "UK"},
    {"Name": "Charlie", "Age": 35, "Country": "Canada"},
]

# Write data to a JSON file
with open("output.json", "w") as file:
    json.dump(data, file, indent=4)  # Pretty print with indentation
print("JSON file written successfully.")

import csv

# Filter rows with Age > 30
with open("data.csv", "r") as infile, open("filtered_data.csv", "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()  # Write headers
    for row in reader:
        if int(row["Age"]) > 30:
            writer.writerow(row)  # Write only rows that match the condition

print("Filtered data written to 'filtered_data.csv'.")


import csv

# Add a new column based on Age
with open("data.csv", "r") as infile, open("transformed_data.csv", "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["Age Group"]  # Add new column
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in reader:
        age = int(row["Age"])
        row["Age Group"] = "Adult" if age >= 18 else "Minor"
        writer.writerow(row)

print("Transformed data written to 'transformed_data.csv'.")



import csv

# Combine two CSV files based on the 'Name' field
with open("data.csv", "r") as file1, open("extra_data.csv", "r") as file2, open("combined_data.csv", "w", newline="") as outfile:
    reader1 = csv.DictReader(file1)
    reader2 = csv.DictReader(file2)
    
    fieldnames = set(reader1.fieldnames + reader2.fieldnames)
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    extra_data = {row["Name"]: row for row in reader2}  # Build a lookup dictionary
    for row in reader1:
        if row["Name"] in extra_data:
            row.update(extra_data[row["Name"]])  # Merge data
        writer.writerow(row)

print("Combined data written to 'combined_data.csv'.")









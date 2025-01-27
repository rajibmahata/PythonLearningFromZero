### Working with CSV and JSON Files in Python

Python provides excellent support for handling **CSV** (Comma-Separated Values) and **JSON** (JavaScript Object Notation) files. These formats are commonly used for storing and exchanging structured data.

---

## 1. **Working with CSV Files**

The `csv` module in Python makes it easy to read, write, and process CSV files.

### Reading a CSV File
```python
import csv

# Read a CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list of strings
```

#### Example CSV (`data.csv`):
```
Name,Age,Country
Alice,30,USA
Bob,25,UK
Charlie,35,Canada
```

**Output:**
```
['Name', 'Age', 'Country']
['Alice', '30', 'USA']
['Bob', '25', 'UK']
['Charlie', '35', 'Canada']
```

---

### Writing to a CSV File
```python
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
```

**Output File (`output.csv`):**
```
Name,Age,Country
Alice,30,USA
Bob,25,UK
Charlie,35,Canada
```

---

### Reading a CSV as a Dictionary
```python
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # Each row is a dictionary
```

**Output:**
```
{'Name': 'Alice', 'Age': '30', 'Country': 'USA'}
{'Name': 'Bob', 'Age': '25', 'Country': 'UK'}
{'Name': 'Charlie', 'Age': '35', 'Country': 'Canada'}
```

---

### Writing a Dictionary to a CSV
```python
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
```

---

## 2. **Working with JSON Files**

The `json` module allows you to encode and decode JSON data.

---

### Reading a JSON File
```python
import json

# Read a JSON file
with open("data.json", "r") as file:
    data = json.load(file)  # Load JSON into a Python dictionary or list
    print(data)
```

#### Example JSON (`data.json`):
```json
[
    {"Name": "Alice", "Age": 30, "Country": "USA"},
    {"Name": "Bob", "Age": 25, "Country": "UK"},
    {"Name": "Charlie", "Age": 35, "Country": "Canada"}
]
```

**Output:**
```python
[{'Name': 'Alice', 'Age': 30, 'Country': 'USA'},
 {'Name': 'Bob', 'Age': 25, 'Country': 'UK'},
 {'Name': 'Charlie', 'Age': 35, 'Country': 'Canada'}]
```

---

### Writing to a JSON File
```python
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
```

**Output File (`output.json`):**
```json
[
    {
        "Name": "Alice",
        "Age": 30,
        "Country": "USA"
    },
    {
        "Name": "Bob",
        "Age": 25,
        "Country": "UK"
    },
    {
        "Name": "Charlie",
        "Age": 35,
        "Country": "Canada"
    }
]
```

---

### Converting JSON to Python Object and Vice Versa
1. **JSON to Python**:
   ```python
   json_string = '{"Name": "Alice", "Age": 30, "Country": "USA"}'
   python_dict = json.loads(json_string)  # Converts JSON string to Python dictionary
   print(python_dict)
   ```

2. **Python to JSON**:
   ```python
   python_dict = {"Name": "Alice", "Age": 30, "Country": "USA"}
   json_string = json.dumps(python_dict, indent=4)  # Converts Python dictionary to JSON string
   print(json_string)
   ```

---

### Key Differences Between CSV and JSON
| Feature       | CSV                              | JSON                            |
|---------------|----------------------------------|----------------------------------|
| **Format**    | Plain text (table-like structure)| Hierarchical (key-value pairs) |
| **Best For**  | Tabular data                     | Complex or nested data          |
| **Read/Write**| `csv.reader`, `csv.writer`       | `json.load`, `json.dump`        |
| **Flexibility**| Limited (fixed structure)        | Highly flexible (nested data)   |

---

Let’s explore **advanced operations** with CSV and JSON files, including filtering, transforming, and combining data. These examples demonstrate how to process real-world data efficiently.

---

### **Advanced CSV Operations**

#### **1. Filtering Rows from a CSV**
Suppose we want to filter rows where the `Age` is greater than 30.

```python
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
```

---

#### **2. Transforming CSV Data**
Add a new column, `Age Group`, based on the `Age` field.

```python
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
```

---

#### **3. Combining Two CSV Files**
Combine data from two CSV files by matching a common column (e.g., `Name`).

```python
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
```

---

### **Advanced JSON Operations**

#### **1. Filtering JSON Data**
Extract people from a JSON file whose age is greater than 30.

```python
import json

# Read JSON, filter data, and save to a new file
with open("data.json", "r") as infile:
    data = json.load(infile)

filtered_data = [person for person in data if person["Age"] > 30]

with open("filtered_data.json", "w") as outfile:
    json.dump(filtered_data, outfile, indent=4)

print("Filtered data written to 'filtered_data.json'.")
```

---

#### **2. Transforming JSON Data**
Add a derived field, such as `Age Group`, to each object.

```python
import json

# Read JSON, transform data, and save to a new file
with open("data.json", "r") as infile:
    data = json.load(infile)

for person in data:
    person["Age Group"] = "Adult" if person["Age"] >= 18 else "Minor"

with open("transformed_data.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

print("Transformed data written to 'transformed_data.json'.")
```

---

#### **3. Combining JSON Data**
Merge two JSON files based on a common key (e.g., `Name`).

```python
import json

# Read two JSON files and combine based on 'Name'
with open("data.json", "r") as file1, open("extra_data.json", "r") as file2:
    data1 = json.load(file1)
    data2 = {item["Name"]: item for item in json.load(file2)}  # Create lookup

combined_data = []
for person in data1:
    if person["Name"] in data2:
        person.update(data2[person["Name"]])  # Merge matching entries
    combined_data.append(person)

with open("combined_data.json", "w") as outfile:
    json.dump(combined_data, outfile, indent=4)

print("Combined data written to 'combined_data.json'.")
```

---

### Key Use Cases

1. **Data Cleaning**: Remove invalid entries or entries with missing fields in both CSV and JSON.
2. **Aggregation**: Group data by a key and calculate sums, averages, or counts.
3. **Data Conversion**: Convert between CSV and JSON formats for different use cases.

#### Example: Convert CSV to JSON
```python
import csv
import json

# Convert CSV to JSON
with open("data.csv", "r") as csvfile, open("output.json", "w") as jsonfile:
    reader = csv.DictReader(csvfile)
    json.dump(list(reader), jsonfile, indent=4)

print("CSV converted to JSON successfully.")
```

#### Example: Convert JSON to CSV
```python
import json
import csv

# Convert JSON to CSV
with open("data.json", "r") as jsonfile, open("output.csv", "w", newline="") as csvfile:
    data = json.load(jsonfile)
    fieldnames = data[0].keys()  # Use keys from the first object as headers
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)

print("JSON converted to CSV successfully.")
```

---

Let’s explore **advanced use cases** like working with **APIs**, **nested JSON**, and **large datasets** in Python.

---

## **1. Working with APIs and JSON**

Many APIs return data in JSON format. You can use the `requests` library to fetch, process, and save API data.

### Example: Fetching JSON from an API
```python
import requests
import json

# Fetch data from an API
url = "https://jsonplaceholder.typicode.com/users"  # Sample API
response = requests.get(url)

if response.status_code == 200:  # Check if the request was successful
    data = response.json()  # Convert JSON response to Python object
    print("Fetched data:", data[:2])  # Print the first two items for brevity

    # Save to a JSON file
    with open("api_data.json", "w") as file:
        json.dump(data, file, indent=4)
        print("Data saved to 'api_data.json'.")
else:
    print("Failed to fetch data. Status code:", response.status_code)
```

---

## **2. Handling Nested JSON**

### Example: Flatten Nested JSON
Consider the following JSON structure:
```json
{
    "Name": "Alice",
    "Details": {
        "Age": 30,
        "Country": "USA",
        "Hobbies": ["Reading", "Traveling"]
    }
}
```

#### Flatten Nested JSON:
```python
import json

# Sample nested JSON
data = {
    "Name": "Alice",
    "Details": {
        "Age": 30,
        "Country": "USA",
        "Hobbies": ["Reading", "Traveling"]
    }
}

# Flatten the nested structure
flattened_data = {
    "Name": data["Name"],
    "Age": data["Details"]["Age"],
    "Country": data["Details"]["Country"],
    "Hobbies": ", ".join(data["Details"]["Hobbies"])  # Combine list into a string
}

print("Flattened Data:", flattened_data)

# Save to a JSON file
with open("flattened_data.json", "w") as file:
    json.dump(flattened_data, file, indent=4)
```

---

### Example: Process Nested JSON from a File
Suppose you have a JSON file with nested data and want to extract specific fields.

```python
import json

# Read nested JSON from a file
with open("nested_data.json", "r") as file:
    data = json.load(file)

# Extract specific details
extracted_data = [{"Name": item["Name"], "Country": item["Details"]["Country"]} for item in data]

# Save the extracted data to a new JSON file
with open("extracted_data.json", "w") as file:
    json.dump(extracted_data, file, indent=4)

print("Extracted Data:", extracted_data)
```

---

## **3. Working with Large Datasets**

For large CSV/JSON files, use **chunking** or libraries like `pandas`.

### Processing Large CSV in Chunks
```python
import pandas as pd

# Read and process a large CSV in chunks
chunk_size = 1000
for chunk in pd.read_csv("large_data.csv", chunksize=chunk_size):
    # Perform operations on each chunk
    filtered_chunk = chunk[chunk["Age"] > 30]  # Example filter
    print(filtered_chunk.head())  # Preview the first few rows
```

---

### Streaming Large JSON Files
For large JSON files, process them line by line using `ijson`.

```bash
pip install ijson
```

```python
import ijson

# Stream large JSON file
with open("large_data.json", "r") as file:
    parser = ijson.items(file, "item")  # Process each item in the JSON array
    for obj in parser:
        if obj["Age"] > 30:  # Filter condition
            print(obj)
```

---

## **4. Combining CSV and JSON**

### Example: Convert CSV to Nested JSON
Convert a CSV file to nested JSON by grouping rows based on a key (e.g., `Country`).

#### Sample CSV (`data.csv`):
```
Name,Age,Country
Alice,30,USA
Bob,25,UK
Charlie,35,USA
David,28,UK
```

#### Code to Group Data:
```python
import csv
import json
from collections import defaultdict

# Read CSV and group by Country
grouped_data = defaultdict(list)
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        grouped_data[row["Country"]].append({"Name": row["Name"], "Age": row["Age"]})

# Save to JSON
with open("grouped_data.json", "w") as file:
    json.dump(grouped_data, file, indent=4)

print("Grouped Data:", json.dumps(grouped_data, indent=4))
```

---

### Example: Combine Data from JSON and CSV
Merge a JSON file (`data.json`) and a CSV file (`extra_data.csv`) based on the `Name` field.

```python
import csv
import json

# Read JSON file
with open("data.json", "r") as file:
    json_data = {item["Name"]: item for item in json.load(file)}  # Build a lookup

# Read CSV file and combine
combined_data = []
with open("extra_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["Name"]
        if name in json_data:
            combined = {**json_data[name], **row}  # Merge JSON and CSV data
            combined_data.append(combined)

# Save combined data to JSON
with open("combined_output.json", "w") as file:
    json.dump(combined_data, file, indent=4)

print("Combined Data:", combined_data)
```

---

### Key Tips for Large Datasets:
1. **Use Efficient Libraries**:
   - For CSV: Use `pandas` for speed and flexibility.
   - For JSON: Use `ijson` or `orjson` for large files.
2. **Chunk Processing**:
   - Process files in chunks to avoid memory overload.
3. **Parallel Processing**:
   - Use Python's `multiprocessing` module for faster processing of large files.


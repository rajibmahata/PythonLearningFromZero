Regular expressions (regex) in Python are handled using the `re` module. Here are some common regex operations to practice:

---

### 1. **Basic Match (`re.match`)**
Matches a pattern at the beginning of a string.

```python
import re

pattern = r"\d{4}"  # Matches exactly 4 digits
text = "2024 is a year"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
```

---

### 2. **Search (`re.search`)**
Finds the first occurrence of the pattern anywhere in the string.

```python
text = "Order number is 4567"
match = re.search(r"\d{4}", text)

if match:
    print("Found:", match.group())
```

---

### 3. **Find All (`re.findall`)**
Finds all occurrences of the pattern in the string.

```python
text = "My numbers are 1234, 5678, and 91011"
matches = re.findall(r"\d{4}", text)
print("All matches:", matches)
```

---

### 4. **Find Iter (`re.finditer`)**
Returns an iterator of all matches.

```python
text = "Find numbers like 123 and 456 in this text."
matches = re.finditer(r"\d+", text)

for match in matches:
    print(f"Match: {match.group()} at position {match.start()}")
```

---

### 5. **Substitution (`re.sub`)**
Replaces occurrences of a pattern with a replacement.

```python
text = "Replace 123 and 456 with 'XXX'"
result = re.sub(r"\d+", "XXX", text)
print("Replaced text:", result)
```

---

### 6. **Splitting (`re.split`)**
Splits a string based on a pattern.

```python
text = "apple,banana;grape orange"
parts = re.split(r"[,\s;]+", text)
print("Split parts:", parts)
```

---

### 7. **Using Groups (`re.groups`)**
Extracting specific parts of a match.

```python
text = "My email is example@email.com"
match = re.search(r"(\w+)@(\w+\.\w+)", text)

if match:
    print("Username:", match.group(1))
    print("Domain:", match.group(2))
```

---

### 8. **Using `re.compile` for Efficiency**
Compiling a regex pattern for reuse.

```python
pattern = re.compile(r"\b[A-Za-z]{5}\b")  # Words with exactly 5 letters
text = "Hello world, regex is fun"

matches = pattern.findall(text)
print("Words with 5 letters:", matches)
```

---


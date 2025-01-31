import re

pattern = r"\d{4}"  # Matches exactly 4 digits
text = "2024 is a year"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

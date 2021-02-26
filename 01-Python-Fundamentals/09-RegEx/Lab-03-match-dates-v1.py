import re


data = input()
pattern = r"\b(?P<day>\d{2})(?P<separator>[-./])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})\b"
matches = re.findall(pattern, data)
print(matches)
for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")

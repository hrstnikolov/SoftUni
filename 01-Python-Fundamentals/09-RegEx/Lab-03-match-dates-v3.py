# v3 използва компилиран re обект, наименовани групи, findall и match обекти
import re

data = input()
pattern = re.compile(r"\b(?P<day>\d{2})(?P<separator>[-./])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})\b")
matches = pattern.findall(data)
# findall returns list of tuples; each tuple contains groups
# print(matches)
for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")

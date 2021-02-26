import re


data = input()
pattern = r"\b(?P<day>\d{2})(?P<separator>[-./])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})\b"
# finditer returns iterator
# it contains match objects
# finditer finds ALL matches (not only the first one as seach does)
# this function is useful because it allows accessing capture groups
matches = re.finditer(pattern, data)
# print(matches)
for match in matches:
    day = match.group("day")
    month = match.group("month")
    year = match.group("year")
    print(f"Day: {day}, Month: {month}, Year: {year}")

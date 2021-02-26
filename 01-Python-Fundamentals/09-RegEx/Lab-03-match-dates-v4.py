# v4 използва компилиран РЕ обект, наименовани групи, finditer и match обекти
import re

data = input()
pattern = re.compile(r"\b(?P<day>\d{2})(?P<separator>[-./])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})\b")
matches = pattern.finditer(data)  # returns iterator of match objects
for match in matches:
    day = match.group("day")
    month = match.group("month")
    year = match.group("year")
    print(f"Day: {day}, Month: {month}, Year: {year}")

    # # група може да се достъпва чрез индексът (започва от 1, а не 0)
    #     # match.group(1)
    #     # # достъпване чрез име на група
    #     # match.group("year")
    #     # match.groups()  # връща вс групи събрани в тупъл

line = input()
occurrences = {}

for char in line:
    if not char == ' ':
        occurrences[char] = line.count(char)

for key, value in occurrences.items():
    print(f'{key} -> {value}')
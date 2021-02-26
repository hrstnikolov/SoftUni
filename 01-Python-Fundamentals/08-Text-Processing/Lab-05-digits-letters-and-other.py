text = input()

categorized_text = {
    'digits': '',
    'letters': '',
    'symbols': ''
}
for char in text:
    if char.isdigit():
        categorized_text['digits'] += char
    elif char.isalpha():
        categorized_text['letters'] += char
    else:
        categorized_text['symbols'] += char

for key, value in categorized_text.items():
    print(value)


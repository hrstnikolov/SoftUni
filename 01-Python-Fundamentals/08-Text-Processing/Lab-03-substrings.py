substring = input()
text = input()

modified_text = text
while substring in modified_text:
    modified_text = modified_text.replace(substring, "")

print(modified_text)

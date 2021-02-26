words = []

while True:
    word = input()
    if word == 'end':
        break
    words.append(word)

for word in words:
    print(f"{word} = {word[::-1]}")
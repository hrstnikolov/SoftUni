count = int(input())

synonyms = {}
for _ in range(count):
    word = input()
    synonym = input()
    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for key, value in synonyms.items():
    print(f'{key} - {", ".join(value)}')


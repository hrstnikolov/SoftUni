banned_words = input().split(", ")
text = input()

censored_text = text
for word in banned_words:
    censored_text = censored_text.replace(word, "*" * len(word))

print(censored_text)

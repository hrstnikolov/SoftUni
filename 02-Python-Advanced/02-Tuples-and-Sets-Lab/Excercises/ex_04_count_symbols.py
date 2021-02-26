def get_unique_chars(text):
    unique_chars = set()
    for ch in text:
        unique_chars.add(ch)

    return unique_chars


def print_unique_chars(text):
    unique_characters = get_unique_chars(text)
    for ch in sorted(unique_characters, key=ord):
        ch_count = text.count(ch)
        print(f'{ch}: {ch_count} time/s')


text = input()
# text = 'SoftUni rocks'
print_unique_chars(text)

def input_to_list():
    lst = ['Peter', 'George', 'Bill', 'Lilly', 'Katy']
    # lst = input().split(', ')
    return lst


def get_words_lengths(words):
    return [(word, len(word)) for word in words]


def print_result(result):
    couples = [f'{word} -> {length}' for word, length in result]
    print(', '.join(couples))


words = input_to_list()
result = get_words_lengths(words)
print_result(result)

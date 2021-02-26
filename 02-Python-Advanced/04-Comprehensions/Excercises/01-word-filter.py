def read_list():
    # lst = ['kiwi', 'orange', 'banana', 'apple']
    lst = input().split(' ')
    return lst


def is_word_even(word):
    return len(word) % 2 == 0


def get_even_length_words(words):
    return [w for w in words if is_word_even(w)]


def print_list(lst):
    for el in lst:
        print(el)


words = read_list()
result = get_even_length_words(words)
print_list(result)
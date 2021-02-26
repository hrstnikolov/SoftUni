def input_to_list():
    # lst = ['1 2 3 ',
    #        '4 5 6  ',
    #        '  7  8', ]
    lst = [x for x in input().split('|')]
    return lst


def get_reversed_flatten_list(lst):
    reversed_flatten_list = []
    for text in lst[::-1]:
        values = [int(x) for x in text.split()]
        reversed_flatten_list.extend(values)

    return reversed_flatten_list


def print_result(lst):
    print(' '.join(map(str, lst)))


lst = input_to_list()
reversed_flatten_list = get_reversed_flatten_list(lst)
print_result(reversed_flatten_list)

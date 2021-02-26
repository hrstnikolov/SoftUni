def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def print_sets(even: set, odd: set):
    even_sum = sum(even)
    odd_sum = sum(odd)

    result = set()
    if odd_sum == even_sum:
        result = odd.union(even)
    elif odd_sum > even_sum:
        result = odd - even
    else:
        result = odd.symmetric_difference(even)

    print(', '.join(map(str, result)))


def generate_quotient_set(names):
    odd = set()
    even = set()
    line_counter = 1
    for name in names:
        ascii_sum = sum(map(ord, name))
        line_len = line_counter
        quotient = ascii_sum // line_len
        if quotient % 2 == 0:
            even.add(quotient)
        else:
            odd.add(quotient)
        line_counter += 1
    return even, odd


n = int(input())
names = input_to_list(n)

# names = [
#     'Pesho',
#     'Stefan',
#     'Stamat',
#     'Gosho',
# ]

# names = [
# 'Preslav',
# 'Gosho',
# 'Ivan',
# 'Stamat',
# 'Pesho',
# 'Stefan',
# ]


even, odd = generate_quotient_set(names)
print_sets(even, odd)

def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def get_intersection(range_1, range_2):
    set1 = set(range(range_1[0], range_1[1] + 1))
    set2 = set(range(range_2[0], range_2[1] + 1))

    return set1 & set2


def print_set(s):
    print(f'Longest intersection is {sorted(list(s))} with length {len(s)}')


#
# lines = [
#     '0,3-1,2',
#     '2,10-3,5',
#     '6,15-3,10',
# ]
#
# lines = [
#     '0,10-2,5',
#     '3,8-1,7',
#     '1,8-2,4',
#     '4,7-2,5',
#     '1,10-2,11',
# ]

n = int(input())
lines = input_to_list(n)

longest_intersection = []
for line in lines:
    data_range_1, data_range_2 = line.split('-')
    range_1 = [int(x) for x in data_range_1.split(',')]
    range_2 = [int(x) for x in data_range_2.split(',')]

    intersection = get_intersection(range_1, range_2)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print_set(longest_intersection)

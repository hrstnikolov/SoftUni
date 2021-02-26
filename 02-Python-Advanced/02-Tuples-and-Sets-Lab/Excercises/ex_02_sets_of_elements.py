def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def print_collection(collection):
    for item in collection:
        print(item)


n, m = [int(num) for num in input().split(' ')]
set_1 = set(input_to_list(n))
set_2 = set(input_to_list(m))

# set_1 = {1,3,5,7}
# set_2 = {3, 4, 5}

intersection = set_1 & set_2

print_collection(intersection)
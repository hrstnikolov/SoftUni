def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def print_collection(collection):
    for item in collection:
        print(item)

n = int(input())
user_names = input_to_list(n)

# user_names = [
#     'George',
#     'George',
#     'George',
#     'Peter',
#     'George',
#     'NiceGuy1234',
# ]

unique_names = set(user_names)
print_collection(unique_names)

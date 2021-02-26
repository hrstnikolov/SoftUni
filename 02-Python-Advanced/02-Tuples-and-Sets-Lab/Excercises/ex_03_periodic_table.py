def input_to_elements(line_count):
    elements = []
    for _ in range(line_count):
        for element in input().split():
            elements.append(element)

    return elements


def print_collection(collection):
    for el in collection:
        print(el)


elements_count = int(input())
elements = input_to_elements(elements_count)

# elements = [
#     'Ce',
#     'O',
#     'Mo',
#     'O',
#     'Ce',
#     'Ee',
#     'Mo',
# ]

unique_elements = set(elements)
print_collection(unique_elements)

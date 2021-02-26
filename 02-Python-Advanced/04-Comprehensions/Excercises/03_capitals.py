def input_to_list():
    lst = input().split(', ')
    return lst


def create_dictionary(keys, values):
    # return {key: value for key, value in zip(keys, values)}
    return {keys[i]: values[i] for i in range(len(keys))}


def print_dict(result):
    for word, length in result.items():
        print(f'{word} -> {length}')


country_names = input_to_list()
capital_cities = input_to_list()
result = create_dictionary(country_names, capital_cities)
print_dict(result)
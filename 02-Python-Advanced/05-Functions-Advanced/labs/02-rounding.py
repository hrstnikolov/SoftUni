def get_iterable_round(*args):
    return [round(el) for el in args]


values = [float(x) for x in input().split()]
result = get_iterable_round(*values)
print(result)
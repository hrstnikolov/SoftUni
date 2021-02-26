# def get_iterable_absolute_values(*args):
#     return [abs(el) for el in args]
#
#
# values = [float(x) for x in input().split()]
# result = get_iterable_absolute_values(*values)
# print(result)

print([abs(float(s)) for s in input().split(' ')])


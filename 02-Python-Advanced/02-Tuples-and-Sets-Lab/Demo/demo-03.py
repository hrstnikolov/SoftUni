print(2 * n for n in (1, 4, 5))
# <generator object <genexpr> at 0x058F9728>

print([2 * n for n in (1, 4, 5)])
# [2, 8, 10]

# join може да приема за аргумент и генератор,
# не само лист или стринг
print('--'.join(f'{x:02.2f}' for x in [3, 5.5, 101]))
# 3.00--5.50--101.00

print('--'.join([f'{x:02.2f}' for x in [3, 5.5, 101]]))
# 3.00--5.50--101.00

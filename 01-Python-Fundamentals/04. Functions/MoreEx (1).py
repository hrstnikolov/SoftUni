def mod_int(n):
    print(2 * int(n))


def mod_float(n):
    print(f'{1.5 * float(n):.2f}')


def mod_str(n):
    print(f'${n}$')


def custom_func(type, value):
    switcher = {
        'int': mod_int,
        'real': mod_float,
        'string': mod_str
    }
    switcher.get(type)(value)


custom_func(input(), input())


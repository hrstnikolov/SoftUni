from math import log, e


def calc_log(argument, base):
    if base == 'natural':
        exponent = log(argument)
    else:
        exponent = log(argument, int(base))

    return exponent


number = int(input())
base = input()
print(f'{calc_log(number, base):.2f}')

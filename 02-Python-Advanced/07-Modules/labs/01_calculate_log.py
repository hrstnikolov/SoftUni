from math import log


def calculate_log(number, base):
    if base == 'natural':
        return log(number)
    return log(number, int(base))


number = int(input())
base = input()
print(format(calculate_log(number, base), '.2f'))


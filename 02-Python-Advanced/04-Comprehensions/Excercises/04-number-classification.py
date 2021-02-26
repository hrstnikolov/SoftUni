def filter_positive(nums):
    return [x for x in nums if x >= 0]


def filter_negative(nums):
    return [x for x in nums if x < 0]


def filter_even(nums):
    return [x for x in nums if x % 2 == 0]


def filter_odd(nums):
    return [x for x in nums if x % 2 == 1]


def input_to_list():
    lst = [int(x) for x in input().split(', ')]
    return lst


def print_result(nums):
    positive_nums = ", ".join(map(str, filter_positive(nums)))
    negative_nums = ", ".join(map(str, filter_negative(nums)))
    even_nums = ", ".join(map(str, filter_even(nums)))
    odd_nums = ", ".join(map(str, filter_odd(nums)))

    print(f'Positive: {positive_nums}')
    print(f'Negative: {negative_nums}')
    print(f'Even: {even_nums}')
    print(f'Odd: {odd_nums}')


numbers = input_to_list()
print_result(numbers)

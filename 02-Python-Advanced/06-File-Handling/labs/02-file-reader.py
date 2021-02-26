with open('numbers.txt', 'r') as f:
    # nums = [int(el[:-1]) for el in f.readlines()]
    print(f.readlines())
    nums = [int(el.strip()) for el in f.readlines()]
    nums_sum = sum(nums)

print(nums_sum)


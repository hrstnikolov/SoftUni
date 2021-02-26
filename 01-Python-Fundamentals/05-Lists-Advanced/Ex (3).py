nums = input().split()

result = ''.join([num for num in sorted(nums, reverse=True)])

print(result)

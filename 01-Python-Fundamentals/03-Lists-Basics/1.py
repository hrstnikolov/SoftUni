# # solution 1
#
# str_of_nums = input()  # '1 2 -3'
#
# list_of_nums = str_of_nums.split(' ')  # ['1', '2', '-3']
# for index in range(len(list_of_nums)):
#     list_of_nums[index] = int(list_of_nums[index]) * -1
#
# print(list_of_nums)


# solution 2
list_of_nums = [-1 * int(num) for num in input().split(' ')]

print(list_of_nums)
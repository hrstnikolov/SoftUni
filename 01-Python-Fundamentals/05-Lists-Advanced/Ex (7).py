nums = [int(el) for el in input().split(', ')]

group_of_tens = []
boundary = 10
while nums:
    group = [el for el in nums if el < boundary]
    group_of_tens.append(group)

    nums = [el for el in nums if el not in group]

    boundary += 10

for ind, grp in enumerate(group_of_tens):
    print(f"Group of {10 * (ind + 1)}'s: {grp}")


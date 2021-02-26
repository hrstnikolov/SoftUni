offerings = list(map(int, input().split(', ')))
beggars_count = int(input())
sums = [0] * beggars_count

index = 0
while offerings:
    sums[index] += offerings.pop(0)
    index += 1
    if index == beggars_count:
        index = 0

print(sums)

for ind, amount in enumerate(offerings):

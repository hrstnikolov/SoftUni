values = map(float, input().split(' '))

values_counts = {}

# Вариант 2 - по-бърз
# сложност O(n)
for v in values:
    if v not in values_counts:
        values_counts[v] = 0
    values_counts[v] += 1

for (value, count) in values_counts.items():
    print(f'{value} - {count} times')
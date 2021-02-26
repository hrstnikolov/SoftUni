values = tuple(map(float, input().split(' ')))

values_counts = {}

# Вариант 1 - по-лош, по-бавен
# сложност O(n ** 2)
# квадратна сложност
for v in values:
    if v not in values_counts:
        values_counts[v] = 0
    values_counts[v] = values.count(v)

for (value, count) in values_counts.items():
    print(f'{value} - {count} times')


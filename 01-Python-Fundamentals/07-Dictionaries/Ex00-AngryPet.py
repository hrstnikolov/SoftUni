price_ratings = list(map(int, input().split(' ')))
entry_pos = int(input())
items_type = input()
prices_type = input()

type_conditions = {
    'cheap': lambda x: x < price_ratings[entry_pos],
    'expensive': lambda x: x >= price_ratings[entry_pos]
}
price_conditions = {
    'positive': lambda x: x > 0,
    'negative': lambda x: x < 0,
    'all': True
}

cond_1 = type_conditions[items_type]
cond_2 = price_conditions[prices_type]
left_portion = filter(cond_1 and cond_2, price_ratings[:entry_pos])
right_portion = filter(cond_1 and cond_2, price_ratings[entry_pos + 1:])

damage_left = sum(left_portion)
damage_right = sum(right_portion)

if damage_left < damage_right:
    print(f'Right - {damage_right}')
else:
    print(f'Left - {damage_left}')

"""
in:
1 5 1
1
cheap
all

out:
Left - 1

in:
-2 2 1 5 9 3 2 -2 1 -1 -3 3
7
expensive
positive

out:
Left - 22
"""

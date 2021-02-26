force_sides = {}

while True:
    line = input()
    if line == 'Lumpawaroo':
        break

    data = line.split(' ')
    action = data[1]

    if action == '|':
        side, user = data[0], data[2]
        if user not in force_sides:
            force_sides[user] = side

    elif action == '->':
        user, side = data[0], data[2]
        force_sides[user] = side
        print(f'{user} joins the {side} side!')

sides_occurrence = {}
for side in set(force_sides.values()):
    sides_occurrence[side] = list(force_sides.values()).count(side)
sorted_sides_occurrence = dict(sorted(sides_occurrence.items(), key=lambda x: x[1], reverse=True))

for side, occ in sorted_sides_occurrence.items():
    if occ:
        print(f'Side: {side}, Members: {occ}')
        for user, s in force_sides.items()):



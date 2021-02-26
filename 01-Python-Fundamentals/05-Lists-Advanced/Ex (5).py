rooms_qty = int(input())

free_chairs = 0
needed_chairs = []
for room in range(1, rooms_qty + 1):
    line = input().split()
    chairs = line[0].count('X')
    taken_seats = int(line[1])

    diff = chairs - taken_seats
    if diff >= 0:
        free_chairs += diff
    else:
        needed_chairs.append([abs(diff), room])

if needed_chairs:
    for el in needed_chairs:
        print(f'{el[0]} more chairs needed in room {el[1]}')
else:
    print(f'Game On, {free_chairs} free chairs left')

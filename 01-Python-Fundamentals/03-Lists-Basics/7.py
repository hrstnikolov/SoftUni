gifts = input().split(' ')
orders = ('OutOfStock', 'Required', 'JustInCase')

has_finished = False
while True:

    line = input()
    if line == 'No Money':
        has_finished = True
    else:
        line = line.split(' ')

    if has_finished:
        break

    if line[0] == orders[0]:  # OutOfStock
        gifts = [None if gift == line[1] else gift for gift in gifts]

    if line[0] == orders[1] and int(line[2]) < len(gifts):  # Required
        gifts[int(line[2])] = line[1]

    if line[0] == orders[2]:
        gifts[-1] = line[1]
1
print(' '.join([gift for gift in gifts if gift is not None]))

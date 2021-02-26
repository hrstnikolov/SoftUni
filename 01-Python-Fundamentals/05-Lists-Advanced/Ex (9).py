targets = [int(tar) for tar in input().split()]

while True:
    command = input().split()
    action = command[0]

    if action == 'End':
        break

    index = int(command[1])

    if action == 'Shoot':
        power = int(command[2])
        try:
            if power >= targets[index]:
                targets.pop(index)
            else:
                targets[index] -= power
        except IndexError:
            pass

    elif action == 'Add':
        value = int(command[2])

        if index < len(targets):
            targets.insert(index, value)
        else:
            print('Invalid placement!')

    elif action == 'Strike':
        radius = int(command[2])
        strike_range = range(index - radius, index + radius + 1)
        is_in_range = (0 <= index - radius) and (index + radius < len(targets))
        if is_in_range:
            targets = [targets[i] for i in range(0,len(targets)) if not i in strike_range]
        else:
            print('Strike missed!')

print('|'.join(map(str, targets)))

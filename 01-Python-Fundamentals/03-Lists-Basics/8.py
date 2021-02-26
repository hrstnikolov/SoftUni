
fire_range = {
    'high': range(81, 126),
    'medium': range(51,80),
    'low': range(1, 50)
}

fires = []
for i in input().split('#'):
    fires.append(i.split(' = '))

water = int(input())
extinguished_cells = []
effort = 0

for fire in fires:

    fire[1] = int(fire[1])
    if fire[1] not in fire_range[fire[0].lower()] or water < fire[1]:
        continue

    water -= fire[1]
    extinguished_cells.append(fire[1])

effort = 0.25 * sum(extinguished_cells)

print("Cells:\n")
for cell in extinguished_cells:
    print(f' - {cell}')

print(f'Effort: {effort:.2f}')

print(f'Total fire: {sum(extinguished_cells)}')

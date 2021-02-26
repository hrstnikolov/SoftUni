def legendary_item(key_materials):
        if key_materials['shards'] >= 250:
            return 'Shadowmourne'

        elif key_materials['fragments'] >= 250:
            return 'Valanyr'

        elif key_materials['motes'] >= 250:
            return 'Deagonwrath'


key_material_quantities = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
    }
junk_material_quantities = {}

legendary_item = ''
while not legendary_item:
    line = input().split(' ')

    for index in range(1, len(line), 2):
        resource = line[index].lower()
        quantity = int(line[index - 1])

        if resource in key_material_quantities:
            key_material_quantities[resource] += quantity
            legendary_item = legendary_item(key_material_quantities)

        elif resource in junk_material_quantities:
            junk_material_quantities[resource] += quantity
        else:
            junk_material_quantities[resource] = quantity


print(f'{legendary_item} obtained!')

for material, qty in key_material_quantities.items():
    print(f'{material}: {qty}')

for material, qty in junk_material_quantities.items():
    print(f'{material}: {qty}')

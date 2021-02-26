resources = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = float(input())
    if resource not in resources:
        resources[resource] = quantity
    else:
        resources[resource] += quantity

for res, qty in resources.items():
    print(f'{res} -> {int(qty)}')

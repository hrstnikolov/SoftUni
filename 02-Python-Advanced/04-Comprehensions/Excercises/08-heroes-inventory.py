def read_input():
    # inventories = {
    #     'Peter': {
    #         'Sword': 20,
    #         'Shield': 10,
    #     },
    #     'George': {
    #         'Gem': 100,
    #         'Sword': 20,
    #     }
    # }
    heros_names = input().split(', ')
    inventories = {name: {} for name in heros_names}

    while True:
        line = input()
        if line == 'End':
            break
        params = line.split('-')
        name = params[0]
        item = params[1]
        cost = int(params[2])
        if item not in inventories[name]:
            inventories[name][item] = cost

    return inventories


def get_items_summary(inventories):
    # summary = {
    #     'Peter': {
    #         'items_count': 2,
    #         'total_cost': 30,
    #     },
    #     'George': {
    #         'items_count': 2,
    #         'total_cost': 120,
    #     },
    # }
    summary = {}
    for hero_name, inventory in inventories.items():
        items_count = len(inventory)
        total_cost = sum(inventory.values())
        summary[hero_name] = {}
        summary[hero_name]['items_count'] = items_count
        summary[hero_name]['total_cost'] = total_cost

    return summary


def print_result(summary):
    for hero_name, inventory in summary.items():
        items_count = inventory['items_count']
        total_cost = inventory['total_cost']
        print(f'{hero_name} -> Items: {items_count}, Cost: {total_cost}')


inventories = read_input()
items_summary = get_items_summary(inventories)
print_result(items_summary)

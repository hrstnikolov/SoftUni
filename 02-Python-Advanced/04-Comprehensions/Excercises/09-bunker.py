def read_input():
    # bunker = {
    #     'food': {
    #         'pizza': {
    #             'quantity': 10,
    #             'quality': 5,
    #         },
    #         'burgers': {
    #             'quantity': 5,
    #             'quality': 2,
    #         },
    #     },
    #     'water': {
    #         'mineral': {
    #             'quantity': 5,
    #             'quality': 10,
    #         },
    #     },
    #     'materials': {
    #         'wood': {
    #             'quantity': 2,
    #             'quality': 5,
    #         },
    #     },
    #     'metal': {
    #         'copper': {
    #             'quantity': 3,
    #             'quality': 10,
    #         },
    #     },
    # }

    categories = input().split(', ')
    bunker = {cat: {} for cat in categories}
    # bunker = {}
    # [bunker.update(cat={}) for cat in categories]

    number_of_lines = int(input())
    for _ in range(number_of_lines):
        cat, item, stats = input().split(' - ')
        quantity, quality = [int(el.split(':')[1]) for el in stats.split(';')]
        if cat in bunker:
            # bunker[cat][item].update(quantity=quantity, quality=quality)
            # bunker[cat][item].update({'quantity': quantity, 'quality': quality})
            if item not in bunker[cat]:
                bunker[cat][item] = {
                    'quantity': quantity,
                    'quality': quality,
                }

    return bunker

def get_total_qty(bunker):
    total_qty = 0
    for category, items in bunker.items():
        for item, statistics in items.items():
            total_qty += statistics['quantity']

    for items in bunker.values():
        for params in items.values():
            total_qty += params['quantity']

    return total_qty


def get_quality_sum(bunker):
    items_quality = 0
    for category, items in bunker.items():
        for item, statistics in items.items():
            items_quality += statistics['quality']

    return items_quality


def print_result(bunker):
    items_quantity = get_total_qty(bunker)
    quality_sum = get_quality_sum(bunker)
    categories_count = len(bunker)
    avg_quality = quality_sum / categories_count

    print(f'Count of items: {items_quantity}')
    print(f'Average quality: {avg_quality:.2f}')

    for category, items in bunker.items():
        items_list = ', '.join(items)
        print(f'{category} -> {items_list}')


bunker = read_input()
print_result(bunker)

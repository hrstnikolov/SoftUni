def collect(item_list, i):
    if i not in item_list:
        item_list.append(i)
    return item_list


def drop(item_list, i):
    if i in item_list:
        item_list.remove(i)
    return item_list


def combine(item_list, old_i, new_i):
    if old_i in item_list:
        index = item_list.index(old_i) + 1
        item_list.insert(index, new_item)
    return item_list


def renew(item_list, i):
    if i in item_list:
        item_list.remove(i)
        item_list.append(i)
    return item_list


items = input().split(', ')

data = input()
while not data == 'Craft!':
    command, item = data.split(' - ')

    if command == 'Collect':
        items = collect(items, item)
    elif command == 'Drop':
        items = drop(items, item)
    elif command == 'Combine Items':
        old_item, new_item = item.split(':')
        items = combine(items, old_item, new_item)
    elif command == 'Renew':
        items = renew(items, item)

    data = input()

print(', '.join(items))
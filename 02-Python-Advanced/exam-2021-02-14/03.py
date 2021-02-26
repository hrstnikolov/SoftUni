from collections import deque


def stock_availability(inventory, operation, *args):
    if operation == 'delivery':
        inventory.extend(args)
    elif operation == 'sell':
        inventory = deque(inventory)
        if args:
            if isinstance(args[0], int):
                boxes_to_remove = int(args[0])
                for _ in range(boxes_to_remove):
                    inventory.popleft()
            else:
                for flavour in args:
                    while flavour in inventory:
                        inventory.remove(flavour)
        else:
            inventory.popleft()

    return list(inventory)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))


'''
['choco', 'vanilla', 'banana', 'caramel', 'berry']
['chocolate', 'vanilla', 'banana', 'cookie', 'banana']
['vanilla', 'banana']
[]
['banana']
['cookie', 'banana']
['chocolate', 'vanilla', 'banana']
'''
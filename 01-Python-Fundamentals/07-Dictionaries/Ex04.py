# orders = {}
#
# while True:
#     line = input()
#     if line == 'buy':
#         break
#
#     product, price, qty = line.split(' ')
#     price = float(price)
#     qty = int(qty)
#
#     if product in orders:
#         orders[product][0] = price
#         orders[product][1] += qty
#     else:
#         orders[product] = [price, qty]
#
# for product, value in orders.items():
#     price = value[0]
#     qty = value[1]
#     total = price * qty
#     print(f'{product} -> {total:.2f}')
#

class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

products = []

while True:
    line = input()
    if line == "buy":
        break

    name, price, quantity = line.split()
    price = float(price)
    quantity = int(quantity)


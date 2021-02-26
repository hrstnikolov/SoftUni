prices = {}
quantities = {}

while True:
    data = input()
    if data == 'buy':
        break

    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if name in prices:
        prices[name] = price
        quantities[name] += quantity
    else:
        prices[name] = price
        quantities[name] = quantity

for product, price in prices.items():
    total = price * quantities[product]
    print(f'{product} -> {total:.2f}')
products = {}

while True:
    data = input()
    if data == 'statistics':
        break
    product, qty = data.split(': ')
    if product in products:
        products[product] += int(qty)
    else:
        products[product] = int(qty)


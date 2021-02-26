# max prices
MAX_PRICE_CLOTHES = 50
MAX_PRICE_SHOES = 35
MAX_PRICE_ACCESSORIES = 20

# get input
items_list = input().split('|')
budget = float(input())

profit = 0
new_prices = []

# looping all items
for item in items_list:
    # splitting item
    item_type, price = item.split('->')
    price = float(price)

    # checking if price is below allowable max
    is_valid = (
        (item_type == 'Clothes' and price <= MAX_PRICE_CLOTHES) or
        (item_type == 'Shoes' and price <= MAX_PRICE_SHOES) or
        (item_type == 'Accessories' and price <= MAX_PRICE_ACCESSORIES)
    )

    # if valid and enough money - buy
    if is_valid and price <= budget:
        # adding new price to list and increasing profit
        new_prices.append(price * 1.4)
        profit += price * 0.4

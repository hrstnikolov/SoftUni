orders = int(input())

total_all = 0
for order in range(orders):
    price_capsule = float(input())
    days = int(input())
    capsule_count = int(input())
    total_price = days * capsule_count * price_capsule
    total_all += total_price
    print(f'The price for the coffee is: ${total_price:.2f}')

print(f'Total: ${total_all:.2f}')

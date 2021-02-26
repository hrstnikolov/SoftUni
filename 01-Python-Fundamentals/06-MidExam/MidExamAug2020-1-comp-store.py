price_before_taxes = 0
taxes = 0

while True:
    line = input()
    if line in ('special', 'regular'):
        taxes = 0.2 * price_before_taxes
        price_after_taxes = price_before_taxes + taxes

        if line == 'special':
            price_after_taxes *= 0.9

        break

    price = float(line)
    if price < 0:
        print("Invalid price!")
    else:
        price_before_taxes += price

if price_before_taxes:
    print(f"Congratulations you've just bought a new computer!\n"
      f"Price without taxes: {price_before_taxes:.2f}$\n"
      f"Taxes: {taxes:.2f}$\n"
      f"-----------\n"
      f"Total price: {price_after_taxes:.2f}$")
else:
    print("Invalid order!")

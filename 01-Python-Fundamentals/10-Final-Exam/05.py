import re

n = int(input())
pattern = r'(@#+)(?P<barcode>[A-Z][A-Za-z0-9]{4,}[A-Z])\1'

for _ in range(n):
    data = input()
    match = re.search(pattern, data)
    if match:
        barcode = match.group('barcode')
        digits = [d for d in barcode if d.isdigit()]
        if digits:
            product_group = ''.join(digits)
        else:
            product_group = '00'
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")

def is_product_positive(n1, n2, n3):
    is_positive = True
    for n in (n1, n2, n3):
        if n < 0:
            is_positive = not is_positive
    return is_positive


num1, num2, num3 = [float(input()) for i in range(3)]

if is_product_positive(num1, num2, num3):
    print('positive')
else:
    print('negative')
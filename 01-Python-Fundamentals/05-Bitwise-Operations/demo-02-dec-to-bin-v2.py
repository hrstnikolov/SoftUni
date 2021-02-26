def dec_to_bin(d):
    if d > 1:
        dec_to_bin(d // 2)
    print(d % 2, end='')


d = 11
dec_to_bin(d)

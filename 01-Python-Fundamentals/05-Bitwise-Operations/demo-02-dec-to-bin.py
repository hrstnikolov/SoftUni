def dec_to_bin(d):
    b = ''
    while d > 0:
        r = d % 2
        b = str(r) + b
        d = d // 2
    return b


d = int(input())
print(dec_to_bin(d))

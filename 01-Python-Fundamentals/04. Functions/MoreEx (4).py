def tribon(n):
    li = [1, 1, 2]
    for i in range(2, n - 1):
        li.append(li[i - 2] + li[i - 1] + li[i])
    return li


seq = tribon(int(input()))
while seq:
    print(seq.pop(0))

c = 0
while c <= 3:
    c += 1
    if c == 2:
        break
else:
    print('This will NOT be printed')

c = 0
while c <= 3:
    c += 1
else:
    print('You should see only this')
a = {2, 4}
b = a
b.add('s')
print(id(a))
print(id(b))
print(a)
print(b)



c = (12, ['s', '1'])
d = c
c[1].append('djalsdkalskd')
print(id(c))
print(id(d))
print(c)
print(d)
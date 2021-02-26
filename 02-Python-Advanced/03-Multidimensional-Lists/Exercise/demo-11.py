ll = [
    'word',
    'This is a sentence',
    [1, 2, 3],
    {1: 'banana', 'or': 'and'}
]

for el in ll:
    print(*el)

s = 'this is another senstence'.split(' ')
print(*s)

'''
w o r d
T h i s   i s   a   s e n t e n c e
1 2 3
1 or
this is another senstence
'''
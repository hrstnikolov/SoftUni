# разделяне на текс на букви
print(list('sloth'))  # ['s', 'l', 'o', 't', 'h']

# joining lists
print(' '.join([1, 2]))  # TypeError: sequence item 0: expected str instance, int found

# joining list of integers
print(' '.join(str([1, 2])))  # [ 1 ,   2 ]

# joining strings
print(' '.join('asd'))  # a s d

# joining tuples
print(' '.join(('sd', 'qd')))  # sd qd

# joining list of strings
print(' '.join(['2', '3']))  # 2 3
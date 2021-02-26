# множество = set

# конструктурът на set = ф-ята set()
a = set([129, 4, 5])
b = {2, 5, 0}
c = {0, 2}

# обединение
print(a | b)

# сечение
print(a & b)

# подмножество
print(a < b)  # False
print(c < b)  # True

# difference
print(b - c)

# union,intersection,subset
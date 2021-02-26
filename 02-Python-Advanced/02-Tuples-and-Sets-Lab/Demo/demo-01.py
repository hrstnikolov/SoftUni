# tuple от 1 елемент
tt = (1)  # връща числото 1
tt1 = (1,)  # това вече е tuple

# празен tuple
tt3 = ()

# Колко пъти има стойност в tuple-а
(1, 2, 1).count(1)  # 2

# на кой индекс е елемент
(1, 'a', 'b', 'a').index('a')  # 1
(1, 'a', 'b', 'a').index('a', 2)  # 3
# (1, 'a', 'b', 'a').index('a', 10)  # ValueError: tuple.index(x): x not in tuple
# [1, 'a', 'b', 'a'].index('a', 10)  # ValueError: 'a' is not in list
# [1, 'a', 'b', 'a'][7]  # IndexError: list index out of range



t1 = 'deleteAll'
t2 = 'copy x'
t3 = 'sum x y z'

command, *args = t1.split(' ')
print(command, *args)
print(*args)
command, *args = t2.split(' ')
print(command, *args)
print(*args)
command, *args = t3.split(' ')
print(command, *args)
print(*args)

'''
deleteAll

copy x
x
sum x y z
x y z
'''
# linked list In python
# свързани списъци


from collections import deque

llist = deque('House')
llist.append(' is old!')
print(llist)  # deque(['H', 'o', 'u', 's', 'e', ' is old!'])

llist.pop()
llist.pop()
print(llist)  # deque(['H', 'o', 'u', 's'])

llist.appendleft('asdas')
print(llist)  # deque(['asdas', 'H', 'o', 'u', 's'])
llist.popleft()
print(llist)  # deque(['H', 'o', 'u', 's'])

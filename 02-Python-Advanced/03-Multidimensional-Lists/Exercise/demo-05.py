from collections import deque

queue = deque()
queue.append('Ivan')
queue.append('Pesho')
queue.append('Maria')
print(queue)  # deque(['Ivan', 'Pesho', 'Maria'])
queue.popleft()
queue.popleft()
print(queue)  # deque(['Maria'])





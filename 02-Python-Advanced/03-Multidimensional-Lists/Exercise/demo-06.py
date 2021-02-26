from collections import deque

q = deque()

q.append('Sofia')
q.append('Varna')
q.append('Burgas')
q.append('Plovdiv')

while q:
    print(q.popleft())
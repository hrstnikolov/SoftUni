from collections import deque


def shift(q):
    q.append(q.popleft())
    return q


queue = deque(['a', 2, 4])
queue2 = shift(queue)
queue3 = queue
queue4 = queue.copy()

print(queue)
print(queue2)

print(id(queue))
print(id(queue2))
print(id(queue3))
print(id(queue4))

'''
deque([2, 4, 'a'])
deque([2, 4, 'a'])
86007304
86007304
'''

from collections import deque

children = input().split(' ')
children_queue = deque(children)

step = int(input())

count = 1
while len(children_queue) > 1:
    if count == step:
        print(f'Removed {children_queue.popleft()}')
        count = 1
    else:
        children_queue.append(children_queue.popleft())
        count += 1

print(f'Last is {children_queue.popleft()}')

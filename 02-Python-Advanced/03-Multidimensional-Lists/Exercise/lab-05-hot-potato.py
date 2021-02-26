from collections import deque


people = input().split(' ')
people_queue = deque(people)

repetitions = int(input())

while len(people_queue) > 1:
    for _ in range(repetitions - 1):
        people_queue.append(people_queue.popleft())
    print(f'Removed {people_queue.popleft()}')
print(f'Last is {people_queue.popleft()}')
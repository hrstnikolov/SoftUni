from collections import deque


def shift_queue(queue, steps):
    for _ in range(steps):
        queue.append(queue.popleft())


KM_PER_LITER = 1  # km/liter

petrol_queue = deque()
distances_queue = deque()
tank_capacity = 0
next_distance = 0

stations_count = int(input())
for _ in range(stations_count):
    petrol, distance = [int(x) for x in input().split(' ')]
    petrol_queue.append(petrol)
    distances_queue.append(distance)

for index in range(stations_count):
    petrol_queue_copied = petrol_queue.copy()
    distances_queue_copied = distances_queue.copy()

    shift_queue(petrol_queue_copied, index)
    shift_queue(distances_queue_copied, index)

    while distances_queue_copied:
        tank_capacity += petrol_queue_copied.popleft()
        reachable_distance = tank_capacity * KM_PER_LITER
        next_distance = distances_queue_copied.popleft()

        if next_distance <= reachable_distance:
            spent_petrol = next_distance / KM_PER_LITER
            tank_capacity -= spent_petrol
        else:
            tank_capacity = 0
            break

    else:
        print(index)
        break




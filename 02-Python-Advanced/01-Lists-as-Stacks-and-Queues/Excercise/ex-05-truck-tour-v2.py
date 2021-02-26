from collections import deque

KM_PER_LITER = 1

pump_count = int(input())
pumps = deque()
for _ in range(pump_count):
    petrol, distance_to_next = [int(el) for el in input().split(' ')]
    pumps.append([petrol, distance_to_next])

for _ in range(pump_count):


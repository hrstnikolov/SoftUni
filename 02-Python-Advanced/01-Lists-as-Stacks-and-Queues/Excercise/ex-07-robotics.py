from collections import deque

END_COMMAND = 'End'


class Timer:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def increase(self):
        if self.s == 59:
            if self.m == 59:
                if self.h == 23:
                    self.h = 0
                    self.m = 0
                    self.s = 0
                else:
                    self.h += 1
                    self.m = 0
                    self.s = 0
            else:
                self.m += 1
                self.s = 0
        else:
            self.s += 1

    def __repr__(self):
        return f'{self.h:02d}:{self.m:02d}:{self.s:02d}'


class Robot:
    def __init__(self, name, productivity, time_left=0):
        self.name = name
        self.productivity = productivity
        self.time_left = time_left


robots_queue = deque([])
robot_specs = input()
for el in robot_specs.split(';'):
    name, productivity = el.split('-')
    robots_queue.append(Robot(name, int(productivity)))

time_input = input().split(':')
h, m, s = [int(x) for x in time_input]
timer = Timer(h, m, s)
timer.increase()

assembly_line = deque()
while True:
    product = input()
    if product == END_COMMAND:
        break
    assembly_line.append(product)

while assembly_line:

    for r in robots_queue:
        if r.time_left == 0:
            r.time_left = r.productivity
            product = assembly_line.popleft()
            print(f'{r.first_name} - {product} [{timer}]')
            break
    else:
        assembly_line.append(assembly_line.popleft())

    for r in robots_queue:
        if r.time_left > 0:
            r.time_left -= 1

    timer.increase()

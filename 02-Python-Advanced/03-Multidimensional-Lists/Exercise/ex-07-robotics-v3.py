from collections import deque
from datetime import datetime, timedelta

END_COMMAND = 'End'

# read the robots spec
data = input().split(';')
robot = {}
robots = []
initial_order = 0
for entry in data:
    name, work_rate = entry.split('-')
    robot['name'] = name
    robot['work_rate'] = timedelta(seconds=int(work_rate))
    robot['initial_order'] = initial_order
    initial_order += 1
    robots.append(robot.copy())

# read starting time
starting_time = datetime.strptime(input(), '%H:%M:%S')
for r in robots:
    r['available_at'] = starting_time

# populate the line
assembly_line = deque()
curr_time = starting_time
while True:
    product = input()
    if product == END_COMMAND:
        break
    assembly_line.append(product)

# while there are products on the line
while assembly_line:
    curr_time += timedelta(seconds=1)

    # check if the there is available robot
    sorted_robots = sorted(robots, key=lambda x: x(['available_at'], - [initial_order]))
    first_robot_in_queue = sorted_robots[-1]
    if first_robot_in_queue['available_at'] <= curr_time:
        n = first_robot_in_queue['name']
        p = assembly_line.popleft()
        t = curr_time.strftime("[%H:%M:%S]")
        print(f"{n} - {p} {t}")
        first_robot_in_queue['available_at'] = curr_time + first_robot_in_queue['work_rate']
    else:
        # if no avail robots -> send the product to the end of line
        assembly_line.append(assembly_line.popleft())




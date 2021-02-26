from collections import deque
from datetime import datetime, timedelta

END_COMMAND = 'End'

# read the robots spec
data = input().split(';')
robot = {}
robots = []
for entry in data:
    name, work_rate = entry.split('-')
    robot['name'] = name
    robot['work_rate'] = timedelta(seconds=int(work_rate))
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

    # check if there is available robot
    for r in robots:
        if r['available_at'] <= curr_time:
            n = r['name']
            p = assembly_line.popleft()
            t = curr_time.strftime("[%H:%M:%S]")
            print(f"{n} - {p} {t}")
            r['available_at'] = curr_time + r['work_rate']
            break
    else:
        # if no avail robots -> send the product to the end of line
        assembly_line.append(assembly_line.popleft())




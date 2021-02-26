from math import sqrt, floor


def get_dist(x1, y1, x2=0, y2=0):  # returns distance between two points
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_longer_line(*coord):  # returns the coord of longer line
    line1 = coord[:4]
    line2 = coord[4:]
    len1 = get_dist(*line1)
    len2 = get_dist(*line2)

    if len1 >= len2:
        return line1
    return line2


# input from console
lines_coord = []
for point in range(2):  # 2 points
    for coord in range(4):  # 4 coord for each point
        lines_coord.append(float(input()))

# data manipulation
result = get_longer_line(*lines_coord)  # getting longer line coordinates
p1 = [floor(el) for el in result[:2]]  # point 1
p2 = [floor(el) for el in result[2:]]  # point 2
is_p1_closer = get_dist(*result[:2]) <= get_dist(*result[2:])  # is point 1 closer to origen

# output to console
if is_p1_closer:
    print('({0}, {1})({2}, {3})'.format(*p1, *p2))
else:
    print('({0}, {1})({2}, {3})'.format(*p2, *p1))

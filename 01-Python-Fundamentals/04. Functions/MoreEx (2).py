from math import sqrt


def dist(point):  # returns distance to origin for cartesian point
    x = point[0]
    y = point[1]
    return sqrt(x ** 2 + y ** 2)


def compare_points(p1, p2):  # returns closer point to origin
    if dist(p1) <= dist(p2):
        return p1
    return p2


# input
points = []
for ind in range(2):
    x = int(input())
    y = int(input())
    points.append([x, y])

res = compare_points(points[0], points[1])

# output
print(f'({res[0]},{res[1]})')
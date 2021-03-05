from math import sqrt


class Point:
    def __init__(sel, x, y):
        sel.x = x
        sel.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        x_distance = abs(self.x - x)
        y_distance = abs(self.y - y)
        distance = sqrt(x_distance ** 2 + y_distance ** 2)

        return distance


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))

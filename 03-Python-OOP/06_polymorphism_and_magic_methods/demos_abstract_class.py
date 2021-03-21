class Shape:
    def __init__(self):
        if type(self) == Shape:
            raise TypeError('Shape is abstract')

    def area(self):
        raise TypeError('Abstract method, please create method in the child class')


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


print(Circle(2))
print(Shape())

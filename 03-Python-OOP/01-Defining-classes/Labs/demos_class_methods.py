# class Circle:
#     max_radius = 100
#
#     def __init__(self, radius=None, diameter=None):
#         self.radius = radius if radius else diameter / 2
#
#     def __repr__(self):
#         return f'radius = {self.radius}'
#
#
# circle = Circle(radius=4)
# circle2 = Circle(diameter=20)
# print(circle)
# print(circle2)
import json


class Circle:
    max_radius = 100

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f'radius = {self.radius}'

    @staticmethod
    def is_radius_valid(radius):
        return 0 <= radius <= Circle.max_radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @classmethod
    def from_json(cls, circle_json):
        attrs = json.loads(circle_json)
        if 'radius' in attrs:
            r = int(attrs['radius'])
            return cls(r)
        elif 'diameter' in attrs:
            d = int(attrs['diameter'])
            return cls.from_diameter(d)
        return None


# circle = Circle(4)
# circle2 = Circle.from_diameter(20)
# print(circle)
# print(circle2)

circle3 = Circle.from_json('''
{
    "radius": "10"
}
''')
print(circle3)

circle4 = Circle.from_json('''
{
    "diameter": "30"
}
''')
print(circle4)

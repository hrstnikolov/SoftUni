from time import sleep


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '; '.join([f'{key} = {value}'
                          for key, value
                          in self.__dict__.items()])

    def get_attributes_with_prefix(self, prefix):
        return [key for key in self.__dict__ if key.startswith(prefix)]

    def add_to_dict(self):
        self.__dict__['ajskdja'] = 123
        # bad practice, never do


def get_values(obj, attr_names):
    return [getattr(obj, attr_name, None) for attr_name in attr_names]


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def __repr__(self):
        return f'r = {self.radius}, A = {self.area()}'


emil = Person('Emil', 18)
circle = Circle(4)
print(get_values(emil, ['name', 'age', 'asssss']))
print(get_values(circle, ['radius', 'asdnaks', 'area']))

# the same:
print(getattr(circle, 'diam', None))
print(getattr(circle, 'diam') if hasattr(circle, 'diam') else None)

# setattr за дейта атрибути
print(emil)
setattr(emil, 'city', 'Sofia')
print(emil)
setattr(emil, 'city', 'Varna')
print(emil)

delattr(emil, 'city')
print(emil)
# delattr(emil, 'amxcm')

# setattr за методи
# setattr(emil, 'is_adult', lambda self: True if self.age >= 18 else False)
# print(emil.is_adult(emil))

print(getattr(Person, "add_to_dict"))


class Tracker:
    def __init__(self):
        self.last_id = 0
        self.objects = []

    def add_object(self, obj):
        self.last_id += 1
        setattr(obj, 'track_id', self.last_id)
        self.objects.append(obj)

    def track(self):
        while True:
            for obj in self.objects:
                print(obj, getattr(obj, 'track_id', None))
            sleep(2)


tracker = Tracker()
tracker.add_object(emil)
tracker.add_object(circle)
tracker.track()

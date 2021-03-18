# class Person:
#     min_adult_age = 18
#     def __init__(self, name, age, nationality = None):
#         self.name = name
#         self.age = age
#         self.nationality = nationality
#         if self.nationality == 'Japanese':
#             self.min_adult_age = 20
#             Person.min_adult_age = 21
#
#     def __repr__(self):
#         return f'{self.name} - {self.min_adult_age}'
#
#
# jan = Person('Jan', 24, 'dutch')
# hiroshi = Person('hiroshi', 23, 'Japanese')
# pesho = Person('Pesho', 24, 'German')
#
# print(jan)
# print(hiroshi)
# print(pesho)
# print(Person.min_adult_age)
# print(pesho.min_adult_age)
# print(hiroshi.min_adult_age)


# class Dog:
#     tricks = []
#
#     def __init__(self, name):
#         self.name = name
#         if name == 'murdjo':
#             self.tricks = []
#
#     def __repr__(self):
#         return f'{self.tricks}'
#
#
# sharo = Dog('Sharo')
# murdjo = Dog('murdjo')
#
# sharo.tricks.append('asndkansm')
# murdjo.tricks.append('nkznckq')
#
# print(sharo)
# print(murdjo)
# del murdjo.tricks
# print(murdjo)

class Person:
    def __init__(self, name):
        self.name = name


p1 = Person()
p2 = Person('asd')
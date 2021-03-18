class Person:
    MIN_AGE = 18

    def __init__(self, first_name, last_name, age, city):
        self.last_name = last_name
        self.first_name = first_name  # питонски начин с @prop И @name.setter
        self.set_age(age)  # не питонско
        self.__city = city
        self._gender = 'male'

    # private static method
    # скрит статичен метод
    @staticmethod
    def __validate_age(age):
        if age < Person.MIN_AGE:
            raise ValueError('Under-aged')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    # getter - the pythonic way
    # не е нужно да се променя както при age:
    # 1) инит: от self.__age = age
    # 2) да се достъпва вместо с pesho.age
    #    с pesho.get_age() или pesho._Person__age
    @property
    def first_name(self):
        return self.__first_name[:1]

    # setter - the pythonic way
    @first_name.setter
    def first_name(self, new_first_name):
        self.__first_name = new_first_name

    # getter - bad implementation
    def get_age(self):
        return self.__age

    # setter - bad implementation
    def set_age(self, new_age):
        self.__validate_age(new_age)
        self.__age = new_age


pesho = Person('Pesho', 'Nikolov', 30, 'Sofia')


# print(pesho.__validate_age)  # AttributeError: 'Person' object has no attribute '__validate_age'
# print(pesho._Person__validate_age)  # <bound method Person.__validate_age of <__main__.Person object at 0x032E1D90>>



# print(pesho.full_name)
# print(type(pesho.full_name))
# print(pesho.first_name)

# print(pesho.__dict__)
#
# pesho.__age = 22
# print(pesho.__dict__)
#
# pesho._Person__age = 29
# print(pesho.__dict__)
#
# pesho._gender = 'female'
# print(pesho.__dict__)
#
# print(pesho.set_age(20))
# print(pesho.get_age())
#

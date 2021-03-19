# class Person:
#     min_age = 0
#     max_age = 150
#
#     def __init__(self, age):
#         self.age = age
#
#     @staticmethod
#     def __validate_age(age):
#         if age < Person.min_age or Person.max_age < age:
#             raise ValueError(f'Age mush be between {Person.min_age} and {Person.max_age}')
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, new_age):
#         self.__validate_age(new_age)
#         self.__age = new_age

# V1

# ако имаме дефинирани пропъертите или други методи
# с дублиращи се имена в родителя и наследника,
# при достъпване self.age ще се извика
# пропъртито на наследника;
# т.е. метода на наследника е с по-висок приоритет
# и замества метода на родителя

# class Employee(Person):
#     # min_age = 18
#     # max_age = 65
#     __MIN_EMPLOYEE_AGE = 18
#     __MAX_EMPLOYEE_AGE = 65
#
#     def __init__(self, age, company):
#         super().__init__(age)
#         self.company = company
#
#     @staticmethod
#     def __validate_employee_age(age):
#         if age < Employee.__MIN_EMPLOYEE_AGE or Employee.__MAX_EMPLOYEE_AGE < age:
#             raise ValueError(f'Age mush be between {Employee.__MIN_EMPLOYEE_AGE} and {Employee.__MAX_EMPLOYEE_AGE}')
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, new_age):
#         self.__validate_employee_age(new_age)
#         self.__age = new_age


# V2 - неработещ вариант

# тук дублираме само метода __validate_age
# НО той НЯМА да се извика от setter-а на пропъртито age в Person
# защото __validate_age извикано в Person го превръща в _Person__validate_age
# няма как да извикаме _Employee__validate_age

# class Employee(Person):
#     # min_age = 18
#     # max_age = 65
#     __MIN_EMPLOYEE_AGE = 18
#     __MAX_EMPLOYEE_AGE = 65
#
#     def __init__(self, age, company):
#         super().__init__(age)
#         self.company = company
#
#     @staticmethod
#     def __validate_age(age):
#         if age < Employee.__MIN_EMPLOYEE_AGE or Employee.__MAX_EMPLOYEE_AGE < age:
#             raise ValueError(f'Age mush be between {Employee.__MIN_EMPLOYEE_AGE} and {Employee.__MAX_EMPLOYEE_AGE}')

# V3 - правилен начин - с клас метод
# тъй като Hristo e от клас Employee, тогава в
# __validate_age аргумент ще е cls = Employee
# и ще се вземе cls.min_age и cls.max_age от Employee
# Важно е клас атрибутите min_age, max_age да не са скрити:
# т.е. да не са __min_age, защото в такъв случай не можем
# да ги достъпваме извън класа;
# също, ще са прекръстни автоматично на _Person__min_age и _Employee_min_age

class Person:
    min_age = 0
    max_age = 150

    def __init__(self, age):
        self.age = age

    @classmethod
    def __validate_age(cls, age):
        if age < cls.min_age or cls.max_age < age:
            raise ValueError(f'Age mush be between {cls.min_age} and {cls.max_age}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__validate_age(new_age)
        self.__age = new_age


class Employee(Person):
    min_age = 18
    max_age = 65

    # __MIN_EMPLOYEE_AGE = 18
    # __MAX_EMPLOYEE_AGE = 65

    def __init__(self, age, company):
        super().__init__(age)
        self.company = company


pesho = Person(90)
hristo = Employee(60, 'ZMM')
print(hristo.age)

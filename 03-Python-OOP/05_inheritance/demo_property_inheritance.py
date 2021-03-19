class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def __validate_age(age):
        if age < 1:
            raise ValueError("Age must be positive number")

    def say_hello(self):
        print(f'I am {self.name}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if self.__validate_age(value):
            self.__age = value


class Student(Person):
    def __init__(self, name, age, grade):
        # before py 3.5
        # super(Student, self).__init__(name, age)

        # after py 3.5
        super().__init__(name, age)

        self.grade = grade

    def get_student_info(self):
        print(f'studen age is {self.age}')

    @staticmethod
    def __validate_age(age):
        if age < 18:
            raise ValueError("Employee must be over 18")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if self.__validate_age(value):
            self.__age = value


gosho = Student('Georgi', 122, 5)
# pesho = Student('Petar', -23, 's')
gosho.get_student_info()
gosho.say_hello()

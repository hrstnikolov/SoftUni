class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'I am {self.name}')


class Student(Person):
    def __init__(self, name, age, grade):
        # before py 3.5
        # super(Student, self).__init__(name, age)

        # after py 3.5
        super().__init__(name, age)

        self.grade = grade

    def get_student_info(self):
        print(f'studen age is {self.age}')


gosho = Student('Georgi', 12, 5)
gosho.get_student_info()
gosho.say_hello()

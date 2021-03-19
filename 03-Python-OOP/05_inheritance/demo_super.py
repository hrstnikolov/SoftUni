class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'{self.name} is {self.age} years old.'

class Student(Person):
    def __init__(self, name, age, student_id):
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.student_id = student_id

    def get_id(self):
        return self.student_id

    def print_super(self):
        print('1:', super)
        print('2:', super())
        print('3:', id(super()))
        print('4:', id(Person))
        print('5:', id(Student))

# Create an object of the superclass
john = Person("John", 25)
print(john.get_info())
# returns 'John is 25 years old.'

# Create an object of the subclass
leo = Student("Leo", 20, 10035464)
print(leo.get_info())  # returns 'Leo is 20 years old.'
print(leo.get_id())  # returns 10035464
leo.print_super()

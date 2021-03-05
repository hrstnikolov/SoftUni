class Person:
    MAX_AGE = 150

    def __init__(self, name, age):
        self.validate_age(age)
        self.name = name
        self.age = age

    @staticmethod
    def validate_age(age):
        if age < 0 or Person.MAX_AGE < age:
            raise ValueError('Age is invalid')

pesho = Person('Pesho', 12)
# gosho = Person('Gosho', 233)

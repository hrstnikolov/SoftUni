class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, key, value):
        if key == 'age' and value < 18:
            raise ValueError("Under-aged")
        return super().__setattr__(key, value)

    def __getattr__(self, item):
        return super().__getattribute__(item)


pesho = Person('Petar', 26)
pesho.age = 33
print(pesho.age)

pesho.age = 5
print(pesho.age)

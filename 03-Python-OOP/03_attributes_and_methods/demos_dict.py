class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '; '.join([f'{key} = {value}'
                          for key, value
                          in self.__dict__.items()])

    def get_attributes_with_prefix(self, prefix):
        return [key for key in self.__dict__ if key.startswith(prefix)]

    def add_to_dict(self):
        self.__dict__['ajskdja'] = 123
        # bad practice, never do


emil = Person('Emil')
print(emil.__dict__)
print(Person.__dict__)
emil.age = 5
print(emil.__dict__)

print(emil)
print(Person)

emil.name_of_mother = 'Maria'
emil.name_of_father = 'Tosho'
emil.car = "Mazda"
emil.age_of_cat = 2
print(emil.get_attributes_with_prefix('name'))
emil.add_to_dict()
print(emil)



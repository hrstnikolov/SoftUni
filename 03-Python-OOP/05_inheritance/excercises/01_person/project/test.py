from project.child import Child
from project.person import Person

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
child.p()
# print(person.name)
# print(person.age)
# print(child.__class__.__bases__[0].__name__)
# print(child.__class__.mro()[1].__name__)

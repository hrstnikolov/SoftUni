class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal):
        if Vet.space <= len(Vet.animals):
            return "Not enough space"

        Vet.animals.append(animal)
        self.animals.append(animal)

        return f"{animal} registered in the clinic"

    def unregister_animal(self, animal):
        if animal not in self.animals:
            return f"{animal} not in the clinic"

        Vet.animals.remove(animal)
        self.animals.remove(animal)

        return f"{animal} unregistered successfully"

    def info(self):
        amount = len(self.animals)
        space_left = Vet.space - len(Vet.animals)
        return f"{self.name} has {amount} animals." \
               f" {space_left} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())

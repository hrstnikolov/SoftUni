from abc import ABC, abstractmethod, abstractproperty


class Animal(ABC):
    DIET = []
    WEIGHT_INCREASE = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0


    @abstractmethod
    def feed(self, food):
        if food not in self.DIET:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity

    @staticmethod
    @abstractmethod
    def make_sound():
        pass


class Bird(Animal):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def feed(self, food):
        super

    def __repr__(self):
        animal_type = self.__class__.__name__
        return f"{animal_type} [{self.name}, {self.wing_size}," \
               f" {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        animal_type = self.__class__.__name__
        return f"{animal_type} [{self.name}, {self.weight}," \
               f" {self.living_region}, {self.food_eaten}]"

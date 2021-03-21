from project.animals.animal import Mammal
from project.food import Meat, Vegetable


class Mouse(Mammal):
    DIET = [Vegetable, Meat]
    WEIGHT_INCREASE = 0.10

    def make_sound(self):
        return 'Squeak'

    def feed(self, food):
        if food_type not in Mouse.DIET:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += Mouse.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    DIET = ['Meat']
    WEIGHT_INCREASE = 0.40

    @staticmethod
    def make_sound():
        return 'Woof!'

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in Dog.DIET:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += Dog.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    DIET = ['Vegetable', 'Meat']
    WEIGHT_INCREASE = 0.30

    @staticmethod
    def make_sound():
        return 'Meow'

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in Cat.DIET:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += Cat.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    DIET = ['Meat']
    WEIGHT_INCREASE = 1.00

    @staticmethod
    def make_sound():
        return 'ROAR!!!'

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in Tiger.DIET:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += Tiger.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity

from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit


class Owl(Bird):
    DIET = ['Meat']
    WEIGHT_INCREASE = 0.25

    @staticmethod
    def make_sound():
        return 'Hoot Hoot'

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in Owl.DIET:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += Owl.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    DIET = ['Vegetable', 'Fruit', 'Meat', 'Seed']
    WEIGHT_INCREASE = 0.35

    @staticmethod
    def make_sound():
        return 'Cluck'

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type not in Hen.DIET:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += Hen.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


#
# owl = Owl("Pip", 10, 10)
# print(owl)
# meat = Meat(4)
# print(owl.make_sound())
# owl.feed(meat)
# veg = Vegetable(1)
# print(owl.feed(veg))
# print(owl)
#
# hen = Hen("Harry", 10, 10)
# veg = Vegetable(3)
# fruit = Fruit(5)
# meat = Meat(1)
# print(hen)
# print(hen.make_sound())
# hen.feed(veg)
# hen.feed(fruit)
# hen.feed(meat)
# print(hen)

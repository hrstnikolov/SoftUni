class Dough:
    def __init__(self, flour_type, baking_technique, weight):
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight

    @property
    def flour(self):
        return self.__flour_type

    @flour.setter
    def flour(self, value):
        self.__flour_type = value

    @property
    def baking_technique(self):
        return self.__baking_technique

    @baking_technique.setter
    def baking_technique(self, new_technique):
        self.__baking_technique = new_technique

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

# dough_for_mid_size_pizza = Dough(
#     'тип 500',
#     '10 min at 300 degrees C',
#     300
# )
#
# dough_for_mid_size_pizza.flour = 'пълнозърнесто'
# print(dough_for_mid_size_pizza.flour)

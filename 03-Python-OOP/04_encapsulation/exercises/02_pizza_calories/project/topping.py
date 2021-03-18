class Topping:
    def __init__(self, topping_type, weight):
        self.__topping_type = topping_type
        self.__weight = weight

    # v2 - incorrect, non-pythonic
    # def get_topping_type(self):
    #     return self.__topping_type
    #
    # def set_topping_type(self, new_topping):
    #     self.__topping_type = new_topping

    # v1 - pythonic, correct way
    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, new_topping):
        self.__topping_type = new_topping

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

# mozzarella = Topping('mozzarella', 50)

# v1 - pythonic, correct way
# print(mozzarella.topping_type)
# mozzarella.topping_type = 'pecorino'
# print(mozzarella.topping_type)

# v2 - incorrect, non-pythonic
# print(mozzarella.get_topping_type())
# mozzarella.set_topping_type('pecorino')
# print(mozzarella.get_topping_type())

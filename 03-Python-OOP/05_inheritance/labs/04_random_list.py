from random import randrange


class RandomList(list):
    def get_random_element(self):
        element_index = randrange(0, len(self))
        return self.pop(element_index)


random_list = RandomList([1, 2, 1, 6, -4])
while random_list:
    print(random_list.get_random_element())

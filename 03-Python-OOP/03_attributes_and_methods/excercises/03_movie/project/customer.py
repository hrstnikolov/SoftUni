# from typing import List
#
# from dvd import DVD


class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        count_rented_dvds = len(self.rented_dvds)
        dvd_names = ', '.join([dvd.first_name for dvd in self.rented_dvds])

        return f"{self.id}: {self.name} of age {self.age}" \
               f" has {count_rented_dvds} rented DVD's ({dvd_names})"


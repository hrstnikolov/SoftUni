WAGGON_SEAT_CAPACITY = 4

class Lift:

    def __init__(self, passengers):
        self.passengers = passengers

    def get_free_seats(self):
        return WAGGON_SEAT_CAPACITY * len(self.passengers)\
               - sum(self.passengers)


    def board_passengers(self, boarding_passengers):
        if self.get_free_seats() >= boarding_passengers:
            for index, waggon in enumerate(self.passengers):
                if waggon < WAGGON_SEAT_CAPACITY:

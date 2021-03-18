class Subscription:
    last_id = 0

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return all([self.__dict__[key] == other.__dict__[key]
                    for key in self.__dict__
                    if not key == 'id'])

    @staticmethod
    def get_next_id():
        Subscription.last_id += 1
        return Subscription.last_id


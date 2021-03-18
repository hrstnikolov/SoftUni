class ExercisePlan:
    last_id = 0

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Plan <{self.id}> " \
               f"with duration {self.duration} minutes"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return all([self.__dict__[key] == other.__dict__[key]
                    for key in self.__dict__
                    if not key == 'id'])

    @staticmethod
    def get_next_id():
        ExercisePlan.last_id += 1
        return ExercisePlan.last_id

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        duration = hours * 60
        return cls(trainer_id, equipment_id, duration)

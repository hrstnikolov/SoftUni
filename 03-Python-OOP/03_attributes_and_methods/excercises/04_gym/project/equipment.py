class Equipment:
    last_id = 0

    def __init__(self, name):
        self.name = name
        self.id = Equipment.get_next_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return all([self.__dict__[key] == other.__dict__[key]
                    for key in self.__dict__
                    if not key == 'id'])

    @staticmethod
    def get_next_id():
        Equipment.last_id += 1
        return Equipment.last_id




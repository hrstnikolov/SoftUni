class Lion:
    MONEY_TO_TEND = 50

    def __init__(self, name, gender, age):
        self.age = age
        self.gender = gender
        self.name = name

    @staticmethod
    def get_needs():
        return Lion.MONEY_TO_TEND

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


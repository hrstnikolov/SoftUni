class Hero:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __repr__(self):
        return f"{self.username} " \
               f"of type {self.__class__.__name__} " \
               f"has level {self.level}"

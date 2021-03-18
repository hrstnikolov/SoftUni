class Customer:
    last_id = 0

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; " \
               f"Address: {self.address}; " \
               f"Email: {self.email}"

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return all([self.__dict__[key] == other.__dict__[key]
                    for key in self.__dict__ if not key == 'id'])

    # V1 - correct way
    @staticmethod
    def get_next_id():
        Customer.last_id += 1
        return Customer.last_id

    # V2 - Maybe not correct?
    # @classmethod
    # def get_next_id(cls):
    #     cls.last_id += 1
    #     return cls.last_id

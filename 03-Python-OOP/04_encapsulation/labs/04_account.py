class Account:
    def __init__(self, id, balance, pin):
        self.set_id(id)
        # self.id = id
        self.balance = balance
        self.pin = pin

    @property
    def id(self, new_id):
        self.__id = new_id

    def get_id(self):
        return self.__id

    def change_pin(self, old_pin, new_pin):
        pass



account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))

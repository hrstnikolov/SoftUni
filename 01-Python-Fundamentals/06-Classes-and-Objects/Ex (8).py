class Vehicle:
    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money, owner):
        if money >= self.price and not self.owner:
            self.owner = owner
            change = money - self.price
            print(f'Successfully  bought a {self.type}. Change: {change:.2f}')
        else:
            if self.owner:
                print('Car already sold')
            else:
                print('Sorry, not enough money.')

    def sell(self):
        if self.owner:
            self.owner = None
        else:
            print('Vehicle has no owner')

    def __repr__(self):
        if self.owner:
            return f'{self.model} {self.type} is owned by: {self.owner}'
        else:
            return f'{self.model} {self.type} is on sale: {self.price}'


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type,
model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)
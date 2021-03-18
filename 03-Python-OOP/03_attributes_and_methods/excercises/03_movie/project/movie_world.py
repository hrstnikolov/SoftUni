# from project.dvd import DVD
# from project.customer import Customer
#

class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        return '\n'.join([str(c) for c in self.customers]) + \
               '\n' + \
               '\n'.join([str(d) for d in self.dvds])

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    @staticmethod
    def get_from_id(id, collection):
        return [obj for obj in collection if obj.id == id][0]

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.get_from_id(customer_id, self.customers)
        dvd = self.get_from_id(dvd_id, self.dvds)

        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.first_name} has already rented {dvd.first_name}"
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.first_name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.first_name} has successfully rented {dvd.first_name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.get_from_id(customer_id, self.customers)
        dvd = self.get_from_id(dvd_id, self.dvds)
        if dvd not in customer.rented_dvds:
            return f"{customer.first_name} does not have that DVD"
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.first_name} has successfully returned {dvd.first_name}"

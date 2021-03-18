class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def get_from_id(id_num, objects):
        return [obj
                for obj in objects
                if id_num == getattr(obj, 'id')][0]

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.get_from_id(subscription_id, self.subscriptions)
        customer = self.get_from_id(subscription.customer_id, self.customers)
        trainer = self.get_from_id(subscription.trainer_id, self.trainers)
        plan = self.get_from_id(subscription.exercise_id, self.plans)
        equipment = self.get_from_id(plan.equipment_id, self.equipment)

        result = [str(el) for el in [subscription, customer, trainer, equipment, plan]]
        return '\n'.join(result)

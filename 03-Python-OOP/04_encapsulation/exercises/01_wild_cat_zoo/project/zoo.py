class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.workers = []
        self.animals = []
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

    @staticmethod
    def get_objects_from_attr(obj_list, **kwargs):
        result = []
        for obj in obj_list:
            is_valid = True
            for key, value in kwargs.items():
                if not hasattr(obj, key) or getattr(obj, key, None) != value:
                    is_valid = False
                    break
            if is_valid:
                result.append(obj)

        return result

    @staticmethod
    def divide_in_groups(objects_list):
        objects_dict = {}
        for obj in objects_list:
            key = obj.__class__.__name__
            if key not in objects_dict:
                objects_dict[key] = []
            objects_dict[key].append(obj)

        return objects_dict

    def add_animal(self, animal, price):
        if not self.is_enough_capacity():
            return "Not enough space for animal"
        if not self.is_enough_budget(price):
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price

        return f"{getattr(animal, 'name')} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if not self.is_vacant_position():
            return "Not enough space for worker"
        self.workers.append(worker)

        return f"{getattr(worker, 'name', None)} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker_to_fire = self.get_objects_from_attr(self.workers, name=worker_name)[0]
            self.workers.remove(worker_to_fire)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        amount_to_pay = self.get_total_salaries()
        if not amount_to_pay <= self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= amount_to_pay

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        amount_to_pay = self.get_total_tend()
        if not amount_to_pay <= self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= amount_to_pay

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animals_count = len(self.animals)
        result = f'You have {total_animals_count} animals\n'
        animals_dict = self.divide_in_groups(self.animals)
        animal_order = ['Lion', 'Tiger', 'Cheetah']
        index_mapper = {key: index for index, key in enumerate(animal_order)}
        sorted_animals_dict = dict(sorted(animals_dict.items(), key=lambda x: index_mapper[x[0]]))
        for group, animals in sorted_animals_dict.items():
            result += f'----- {len(animals)} {group}s:\n'
            for animal in animals:
                result += repr(animal) + '\n'
        result = result[:-1]   # removing the last new line

        return result

    def workers_status(self):
        total_workers_count = len(self.workers)
        result = f'You have {total_workers_count} workers\n'
        workers_dict = self.divide_in_groups(self.workers)
        workers_order = ['Keeper', 'Caretaker', 'Vet']
        index_mapper = {key: index for index, key in enumerate(workers_order)}
        sorted_workers_dict = dict(sorted(workers_dict.items(), key=lambda x: index_mapper[x[0]]))
        for group, workers in sorted_workers_dict.items():
            result += f'----- {len(workers)} {group}s:\n'
            for worker in workers:
                result += repr(worker) + '\n'
        result = result[:-1]   # removing the last new line

        return result

    def is_enough_budget(self, price):
        return price <= self.__budget

    def is_enough_capacity(self):
        return len(self.animals) < self.__animal_capacity

    def is_vacant_position(self):
        return len(self.workers) < self.__workers_capacity

    def get_total_salaries(self):
        total = 0
        for worker in self.workers:
            total += getattr(worker, 'salary', 0)

        return total

    def get_total_tend(self):
        total = 0
        for animal in self.animals:
            total += animal.get_needs()

        return total

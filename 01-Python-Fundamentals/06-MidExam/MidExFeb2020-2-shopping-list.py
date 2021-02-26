class ShoppingList:
    def __init__(self, groceries):
        self.groceries = groceries

    def add_urgent(self, item):
        if item not in self.groceries:
            self.groceries.insert(0, item)

    def remove_unnecessary(self, item):
        if item in self.groceries:
            self.groceries.remove(item)

    def correct_item(self, old_item, new_item):
        for index, item in enumerate(self.groceries):
            if item == old_item:
                self.groceries[index] = new_item

    def rearrange_item(self, item):
        if item in self.groceries:
            self.groceries.remove(item)
            self.groceries.append(item)

    def __repr__(self):
        return ', '.join(self.groceries)


line = input().split('!')
li = ShoppingList(line)
while True:
    command = input()
    if command == 'Go Shopping!':
        break

    action, item = command.split(' ', maxsplit=1)
    if action == 'Urgent':
        li.add_urgent(item)
    elif action == 'Unnecessary':
        li.remove_unnecessary(item)
    elif action == 'Correct':
        li.correct_item(*item.split(' '))
    elif action == 'Rearrange':
        li.rearrange_item(item)

print(li)
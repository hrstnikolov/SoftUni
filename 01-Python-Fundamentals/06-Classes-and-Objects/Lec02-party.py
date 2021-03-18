class Person:
    def __init__(self, name):
        self.name = name


class Party:
    def __init__(self):
        self.attendees = []

    def invite(self, person):
        self.attendees.append(person)

    def names_of_attendees(self):
        return ', '.join([person.first_name for person in self.attendees])

    def number_of_guests(self):
        return len(self.attendees)


party = Party()

while True:
    command = input()
    if command == 'End':
        break
    name = command
    person = Person(name)
    party.invite(person)

print(f'Going: {party.names_of_attendees()}')
print(f'Total: {party.number_of_guests()}')

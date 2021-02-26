class SugarCubes:
    def __init__(self, sequence):
        self.sequence = sequence

    def add(self, value):
        self.sequence.append(value)

    def remove(self, value):
        self.sequence.remove(value)

    def replace(self, val, rep):
        for ind, cube in enumerate(self.sequence):
            if cube == val:
                self.sequence[ind] = rep
                break

    def collapse(self, val):
        self.sequence = [el for el in self.sequence if el >= val]

    def __repr__(self):
        return ' '.join(map(str, self.sequence))


line = list(map(int, input().split(' ')))
sugar_cubes = SugarCubes(line)

while True:
    command = input()
    if command == 'Mort':
        break

    command = command.split(' ')
    action = command[0]

    if action == 'Add':
        value = int(command[1])
        sugar_cubes.add(value)
    if action == 'Remove':
        value = int(command[1])
        sugar_cubes.remove(value)
    if action == 'Replace':
        value = int(command[1])
        replacement = int(command[2])
        sugar_cubes.replace(value, replacement)
    if action == 'Collapse':
        value = int(command[1])
        sugar_cubes.collapse(value)

print(sugar_cubes)


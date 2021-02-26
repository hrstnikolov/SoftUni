class Score:
    def __init__(self, title, composer, key):
        self.title = title
        self.composer = composer
        self.key = key

    def change_key(self, new_key):
        self.key = new_key


class Scores:
    def __init__(self):
        self.sheets = []

    def is_stored(self, title):
        for s in self.sheets:
            if s.title == title:
                return True
        return False

    def get_index(self, title):
        for index, s in enumerate(self.sheets):
            if s.title == title:
                return index
        return None

    def add_sheet(self, title, composer, key):
        index = self.get_index(title)
        if index is None:
            new_score = Score(title, composer, key)
            self.sheets.append(new_score)
            print(f"{title} by {composer} in {key} added to the collection!")
            return
        print(f"{title} is already in the collection!")

    def remove_piece(self, title):
        index = self.get_index(title)
        if index is not None:
            self.sheets.pop(index)
            print(f"Successfully removed {title}!")
            return
        print(f"Invalid operation! {title} does not exist in the collection.")

    def change_key(self, title, new_key):
        index = self.get_index(title)
        if index is not None:
            self.sheets[index].key = new_key
            print(f"Changed the key of {title} to {new_key}!")
            return
        print(f"Invalid operation! {title} does not exist in the collection.")


initial_sheets = int(input())
my_scores = Scores()

# recording initial sheet music
for _ in range(initial_sheets):
    title, composer, key = input().split('|')
    new_score = Score(title, composer, key)
    my_scores.sheets.append(new_score)

# receiving commands
while True:
    data = input().split('|')
    command = data[0]
    parameters = data[1:]

    if command == 'Stop':
        break
    elif command == 'Add':
        my_scores.add_sheet(*parameters)
    elif command == 'Remove':
        my_scores.remove_piece(*parameters)
    elif command == 'ChangeKey':
        my_scores.change_key(*parameters)

for sheet in sorted(my_scores.sheets, key=lambda x: (x.title, x.composer)):
    t, c, k = sheet.title, sheet.composer, sheet.key
    print(f"{t} -> Composer: {c}, Key: {k}")


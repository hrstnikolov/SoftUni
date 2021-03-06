class PhotoAlbum:

    def __init__(self, pages, slots=4):
        self.pages = pages
        self.slots = slots
        self.photos = [[] for _ in range(pages)]
        self.current_page = 0
        self.current_slot = 0
        self.is_full = False

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4 + 1)

    def add_photo(self, label):
        if self.is_full:
            return "No more free spots"

        self.photos[self.current_page].append(label)
        result = f"{label} photo added successfully" \
                 f" on page {self.current_page + 1}" \
                 f" slot {self.current_slot + 1}"
        self.move_to_next_slot()
        return result

    def display(self):
        result = '-----------\n'
        for _ in range(self.current_page):
            result += '[] ' * (self.slots - 1) + '[]\n'
            result += '-----------\n'
        result += '[] ' * (self.current_slot - 1) + '[]\n'
        result += '-----------\n'
        return result

    def move_to_next_slot(self):
        if self.current_slot == self.slots - 1:
            if self.current_page == self.pages - 1:
                self.is_full = True
                return
            self.current_slot = 0
            self.current_page += 1
            return
        self.current_slot += 1
        return



album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

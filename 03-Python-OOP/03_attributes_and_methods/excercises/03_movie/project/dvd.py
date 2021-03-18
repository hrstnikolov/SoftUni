from datetime import datetime


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        status = 'rented' if self.is_rented else 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {status}"

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        date_obj = datetime.strptime(date, '%d.%m.%Y')
        creation_year = int(date_obj.strftime('%Y'))
        creation_month = date_obj.strftime('%B')
        return cls(name, id, creation_year, creation_month, age_restriction)


#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
#
# print(d1)
# print(d2)
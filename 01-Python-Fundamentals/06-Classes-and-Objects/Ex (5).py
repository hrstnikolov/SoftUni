from statistics import mean


class Class:
    __students_count = 22

    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        return round(mean(self.grades), 2)

    def __repr__(self):
        return f"The students in {self.class_name}: " \
               f"{', '.join(self.students)}. " \
               f"Average#$ас grade: {self.get_average_grade()}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
print(ascii(a_class))

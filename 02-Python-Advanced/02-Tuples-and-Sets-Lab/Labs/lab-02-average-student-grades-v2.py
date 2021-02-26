def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def avg(values):
    return sum(values) / len(values)


number_of_students = int(input())
student_grades_input = input_to_list(number_of_students)
student_grades = {}
for el in student_grades_input:
    student, grade = el.split(' ')
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(float(grade))

for (student, grades) in student_grades.items():
    avg_grade = avg(grades)
    grades_string = ' '.join(map(lambda g: f'{g:.2f}', grades))
    print(f"{student} -> {grades_string} (avg: {avg_grade:.2f})")

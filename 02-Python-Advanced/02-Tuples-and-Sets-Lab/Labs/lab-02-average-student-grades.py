from statistics import mean

number_of_students = int(input())


# custom функция за средна ст-т
# предпочитано е пред statistics.mean защото е по-бързо
def avg(values):
    return sum(values) / len(values)


grades_of = {}
for _ in range(number_of_students):
    student, grade = input().split(' ')
    if student not in grades_of:
        grades_of[student] = []
    grades_of[student].append(float(grade))

for (student, grades) in grades_of.items():
    avg_grade = avg(grades)
    grs = ' '.join(map(str, grades))
    print(f"{student} -> {grs} (avg: {avg_grade:.2f})")

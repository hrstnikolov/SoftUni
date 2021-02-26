# from statistics import mean


n = int(input())

grades = {}
for _ in range(n):
    name = input()
    grade = float(input())

    if name in grades:
        grades[name].append(grade)
    else:
        grades[name] = [grade]

good_students = grades.copy()
for student, scores in good_students.items():
    avg_grade = sum(scores) / len(scores)
    if avg_grade < 4.5:
        good_students.pop(student)
    else:
        good_students[student] = avg_grade

good_students = dict(sorted(good_students.items(), key=lambda x:x[1], reverse=True))

for name, avg_grade in good_students.items():
    print(f'{name} -> {avg_grade:.2f}')


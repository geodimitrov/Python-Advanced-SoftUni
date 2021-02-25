n = int(input())

students_grades = {}

for _ in range(n):
    student, grade = input().split()

    if student not in students_grades:
        students_grades[student] = []

    students_grades[student].append(float(grade))

for student, grades in students_grades.items():
    all_grades = " ".join(map(lambda x: f"{x:.2f}", grades))
    grade_avg = sum(grades) / len(grades)
    print(f"{student} -> {all_grades} (avg: {grade_avg:.2f})")
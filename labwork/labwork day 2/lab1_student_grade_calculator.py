"""
Lab: Functions in Python
Problem Statement 1: Student Grade Calculator
"""


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    if marks >= 75:
        return "A"
    if marks >= 60:
        return "B"
    if marks >= 40:
        return "C"
    return "Fail"


student_results = []

for i in range(1, 6):
    marks = float(input(f"Enter marks for student {i} (0-100): "))
    grade = calculate_grade(marks)
    student_results.append((marks, grade))

print("\nMarks and Grades:")
for index, (marks, grade) in enumerate(student_results, start=1):
    print(f"Student {index}: Marks = {marks}, Grade = {grade}")

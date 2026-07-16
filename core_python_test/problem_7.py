# Problem 7: Student Result Management
students = {}

for i in range(10):
    roll = int(input("Enter Roll No: "))
    marks = int(input("Enter Marks: "))
    students[roll] = marks

topper = max(students, key=students.get)

print("Topper Roll No:", topper)
print("Marks:", students[topper])

average = sum(students.values()) / len(students)

print("Average Marks:", average)

print("Students Above Average:")
for roll, marks in students.items():
    if marks > average:
        print(roll, marks)

failed = 0

for marks in students.values():
    if marks < 35:
        failed += 1

print("Failed Students:", failed)

print("\nGrades:")

for roll, marks in students.items():

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 35:
        grade = "D"
    else:
        grade = "Fail"

    print("Roll:", roll, "Marks:", marks, "Grade:", grade)

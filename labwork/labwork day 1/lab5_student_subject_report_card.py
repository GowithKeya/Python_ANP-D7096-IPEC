# Python Lab: 6th July 2026
# Lab 5: Student Subject Report Card

students = {
    "Rahul": {"Math": 85, "Science": 90, "English": 88},
    "Priya": {"Math": 78, "Science": 95, "English": 82},
    "Ankit": {"Math": 91, "Science": 89, "English": 94}
}

totals = {}
averages = {}

print("Total and average marks of each student:")
for name, marks in students.items():
    total = sum(marks.values())
    average = total / len(marks)
    totals[name] = total
    averages[name] = average
    print(name, "-> Total:", total, "| Average:", round(average, 2))

topper = max(totals, key=totals.get)
print("\nTopper based on total marks:", topper, "-", totals[topper])

print("\nSubject-wise highest marks:")
subjects = ["Math", "Science", "English"]
for subject in subjects:
    highest_student = None
    highest_marks = -1
    for name, marks in students.items():
        if marks[subject] > highest_marks:
            highest_marks = marks[subject]
            highest_student = name
    print(subject + ":", highest_marks, "by", highest_student)

print("\nStudents with average marks >= 85:")
found = False
for name, average in averages.items():
    if average >= 85:
        print(name, ":", round(average, 2))
        found = True

if not found:
    print("No student has average >= 85.")

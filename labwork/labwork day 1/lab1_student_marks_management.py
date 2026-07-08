# Python Lab: 6th July 2026
# Lab 1: Student Marks Management

students = {
    "Aarav": 78,
    "Diya": 85,
    "Kunal": 91,
    "Meera": 88,
    "Rohan": 73
}

print("All student names and marks:")
for name, marks in students.items():
    print(name, ":", marks)

new_name = input("\nEnter new student name to add: ")
new_marks = int(input("Enter marks: "))
students[new_name] = new_marks

update_name = input("\nEnter existing student name to update marks: ")
if update_name in students:
    updated_marks = int(input("Enter new marks: "))
    students[update_name] = updated_marks
else:
    print("Student not found.")

delete_name = input("\nEnter student name to delete: ")
if delete_name in students:
    del students[delete_name]
else:
    print("Student not found.")

topper = max(students, key=students.get)
print("\nStudent with highest marks:", topper, "-", students[topper])

print("\nFinal student data:")
for name, marks in students.items():
    print(name, ":", marks)

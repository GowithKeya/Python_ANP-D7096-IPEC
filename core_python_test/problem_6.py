# Problem 6: Tuple Operations
students = (
    "Aman", "Rahul", "Priya", "Neha", "Rohan",
    "Amit", "Karan", "Anjali", "Pooja", "Vikas",
    "Aman", "Simran", "Ritika", "Arjun", "Nikita"
)

print("Total Students:", len(students))

print("First Five Students:")
print(students[:5])

print("Last Five Students:")
print(students[-5:])

name = input("Enter student name to search: ")

if name in students:
    print("Student Found")
else:
    print("Student Not Found")

print("Occurrences:", students.count(name))

student_list = list(students)
student_list.sort()

print("Sorted List:")
print(student_list)

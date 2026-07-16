# Problem 10: Student Record Management System
students = []

def add_student():
    roll = int(input("Enter Roll No: "))

    for student in students:
        if student["roll"] == roll:
            print("Duplicate Roll Number!")
            return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    students.append({
        "roll": roll,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    })

    print("Student Added Successfully")

def display_students():
    for student in students:
        print(student)

def search_student():
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["roll"] == roll:
            print(student)
            return

    print("Student Not Found")

def update_marks():
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["roll"] == roll:
            student["marks"] = float(input("Enter New Marks: "))
            print("Marks Updated")
            return

    print("Student Not Found")

def delete_student():
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student Deleted")
            return

    print("Student Not Found")

def display_topper():
    if not students:
        print("No Records")
        return

    topper = max(students, key=lambda x: x["marks"])
    print("Topper:", topper)

def average_marks():
    if not students:
        print("No Records")
        return

    avg = sum(student["marks"] for student in students) / len(students)
    print("Average Marks:", avg)

def above_average():
    if not students:
        print("No Records")
        return

    avg = sum(student["marks"] for student in students) / len(students)

    print("Students Above Average:")

    for student in students:
        if student["marks"] > avg:
            print(student)

while True:

    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Display Topper")
    print("7. Display Average Marks")
    print("8. Display Students Above Average")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        display_topper()

    elif choice == "7":
        average_marks()

    elif choice == "8":
        above_average()

    elif choice == "9":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")

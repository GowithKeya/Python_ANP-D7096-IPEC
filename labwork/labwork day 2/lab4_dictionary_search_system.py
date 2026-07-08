"""
Lab: Functions in Python
Problem Statement 4: Dictionary Search System
"""


def search_student(student_dict, roll_no):
    return student_dict.get(roll_no, "Student Not Found")


students = {
    "101": "Aarav",
    "102": "Diya",
    "103": "Kunal",
    "104": "Meera",
    "105": "Rohan",
}

roll_number = input("Enter roll number to search: ")
result = search_student(students, roll_number)
print("Search Result:", result)

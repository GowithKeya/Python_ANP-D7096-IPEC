# Question 3: Student Grade Calculator
# Scenario:
# A school assigns grades based on the marks obtained by students.

# Problem Statement:
# Write a Python program to accept marks from the user and display
# the corresponding grade.

# Grade Criteria:
# Marks 90 and above -> Grade A
# Marks 75 to 89 -> Grade B
# Marks 50 to 74 -> Grade C
# Below 50 -> Grade F

# Input:
# Marks

# Output:
# Grade

marks = float(input("Enter Marks: "))

if marks >= 90:
    print("Grade A")
else:
    if marks >= 75:
        print("Grade B")
    else:
        if marks >= 50:
            print("Grade C")
        else:
            print("Grade F")

# Question 5: Classroom Seating Arrangement
# Scenario:
# A school wants to arrange students into equal rows.
#
# Problem Statement:
# Write a Python program to determine how many complete rows can be formed.
#
# Input:
# Total Students
# Students per Row
#
# Output:
# Number of Complete Rows

total_students = int(input("Enter total students: "))
students_per_row = int(input("Enter students per row: "))

complete_rows = total_students // students_per_row

print("Number of Complete Rows:", complete_rows)

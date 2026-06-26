# Question 6: Loan Eligibility Check
# Scenario:
# A bank considers an applicant eligible for a personal loan only if their
# monthly salary is Rs. 30,000 or more.

# Problem Statement:
# Write a Python program to accept the applicant's monthly salary and display
# whether they are eligible to apply for the loan.

# Input:
# Monthly Salary

# Output:
# Loan eligibility message

monthly_salary = float(input("Enter your monthly salary: "))

if monthly_salary >= 30000:
    print("Congratulations! You are eligible to apply for the loan.")
else:
    print("Sorry! You are not eligible to apply for the loan.")

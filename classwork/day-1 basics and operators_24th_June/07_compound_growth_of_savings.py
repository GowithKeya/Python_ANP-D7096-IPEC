# Question 7: Compound Growth of Savings
# Scenario:
# A person invests money and wants to see how the amount grows over years.
#
# Problem Statement:
# Write a Python program to calculate the value of money after a certain number
# of years assuming it doubles every year.
#
# Input:
# Initial Amount
# Number of Years
#
# Output:
# Final Amount

initial_amount = float(input("Enter initial amount: "))
number_of_years = int(input("Enter number of years: "))

final_amount = initial_amount * (2 ** number_of_years)

print("Final Amount:", final_amount)

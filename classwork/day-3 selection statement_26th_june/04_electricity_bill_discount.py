# Question 4: Electricity Bill Discount
# Scenario:
# An electricity provider offers a 10% discount on the total bill amount
# if the customer's bill is Rs. 5,000 or more.

# Problem Statement:
# Write a Python program to accept the total bill amount from the user
# and display the final amount to be paid.

# Input:
# Electricity Bill Amount

# Output:
# Discount status and final bill amount

import sys

sys.stdout.reconfigure(encoding="utf-8")

bill_amount = float(input("Enter the electricity bill amount: "))

if bill_amount >= 5000:
    discount = bill_amount * 10 / 100
    final_amount = bill_amount - discount
    print("Discount Applied!")
else:
    final_amount = int(bill_amount)
    print("No Discount Applied!")

print("Final Bill Amount: ₹" + str(final_amount))

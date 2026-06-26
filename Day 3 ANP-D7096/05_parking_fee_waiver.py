# Question 5: Parking Fee Waiver
# Scenario:
# A shopping mall waives the parking fee if a customer has made purchases
# worth Rs. 2,000 or more.

# Problem Statement:
# Write a Python program to accept the purchase amount and display whether
# the parking fee is waived or payable.

# Input:
# Purchase Amount

# Output:
# Parking fee status and parking fee

import sys

sys.stdout.reconfigure(encoding="utf-8")

purchase_amount = float(input("Enter the purchase amount: "))

if purchase_amount >= 2000:
    parking_fee = 0
    print("Parking Fee Waived!")
else:
    parking_fee = 100
    print("Parking Fee Applicable!")

print("Parking Fee: ₹" + str(parking_fee))

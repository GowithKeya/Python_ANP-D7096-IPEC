# Question 1: ATM Minimum Balance Check
# Scenario:
# A bank requires customers to maintain a minimum balance of Rs. 5,000
# in their savings account.

# Problem Statement:
# Write a Python program that accepts the current account balance from the user.
# If the balance is less than Rs. 5,000, display a warning message indicating
# that the minimum balance requirement is not maintained.

# Input:
# Account Balance

# Output:
# Warning message if balance is below the minimum required balance

import sys

sys.stdout.reconfigure(encoding="utf-8")

account_balance = float(input("Enter Account Balance: "))

if account_balance < 5000:
    print("Warning! Your account balance is below the minimum required balance of ₹5000.")
else:
    pass

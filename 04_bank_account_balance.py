# Question 4: Bank Account Balance
# Scenario:
# A customer withdraws money from their bank account.
#
# Problem Statement:
# Write a Python program to calculate the remaining balance after withdrawal.
#
# Input:
# Current Balance
# Withdrawal Amount
#
# Output:
# Remaining Balance

current_balance = float(input("Enter current balance: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))

remaining_balance = current_balance - withdrawal_amount

print("Remaining Balance:", remaining_balance)

'''
Lab Work 2: Loan Approval System

A bank evaluates loan applications using:
• Credit Score ≥ 750
• Annual Income ≥ Rs.8,00,000
• Existing Loan Amount ≤ Rs.2,00,000

Conditions:
• All conditions satisfied → Approved
• Only one condition fails → Manual Review
• More than one condition fails → Rejected
'''

credit_score = int(input("Enter Credit Score: "))
annual_income = float(input("Enter Annual Income: "))
existing_loan = float(input("Enter Existing Loan Amount: "))

# Check each condition
failed_conditions = 0
reasons = []

if credit_score < 750:
    failed_conditions += 1
    reasons.append("Credit Score criteria not satisfied.")

if annual_income < 800000:
    failed_conditions += 1
    reasons.append("Income criteria not satisfied.")

if existing_loan > 200000:
    failed_conditions += 1
    reasons.append("Existing loan amount too high.")

# Determine loan status
if failed_conditions == 0:
    print("Loan Status: Approved")
elif failed_conditions == 1:
    print("Loan Status: Manual Review")
    print(f"Reason: {reasons[0]}")
else:
    print("Loan Status: Rejected")
    for reason in reasons:
        print(f"Reason: {reason}")

'''
Lab Work 1: Smart Income Tax Calculator

A government tax portal calculates tax based on:
• Income up to Rs.5,00,000 → No tax
• Rs.5,00,001 to Rs.10,00,000 → 10%
• Rs.10,00,001 to Rs.20,00,000 → 20%
• Above Rs.20,00,000 → 30%

Additional Benefits:
• Senior citizens (Age ≥ 60) receive a 5% rebate on tax.
• Women taxpayers receive an additional 2% rebate on tax.
'''

income = float(input("Enter Annual Income: "))
age = int(input("Enter Age: "))
gender = input("Enter Gender (M/F): ").upper()

# Calculate tax based on income slabs
if income <= 500000:
    tax = 0
elif income <= 1000000:
    tax = income * 0.10
elif income <= 2000000:
    tax = income * 0.20
else:
    tax = income * 0.30

print(f"Tax before rebate: Rs.{tax}")

# Apply senior citizen rebate
senior_rebate = 0
if age >= 60:
    senior_rebate = tax * 0.05
    print(f"Senior Citizen Rebate: Rs.{senior_rebate}")

# Apply women rebate
women_rebate = 0
if gender == "F":
    women_rebate = tax * 0.02
    print(f"Women Rebate: Rs.{women_rebate}")

final_tax = tax - senior_rebate - women_rebate
print(f"Final Tax Payable: Rs.{final_tax}")

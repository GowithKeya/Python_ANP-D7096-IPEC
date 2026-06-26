'''
Lab Work 10: Multi-Level Access Control System

Assign access levels based on:
Roles: Admin, Manager, Employee, Guest

Conditions:
• Admin + Security Clearance ≥ 5 → Full Access
• Manager + Experience > 5 Years → Department Access
• Employee + Experience > 2 Years → Limited Access
• Guest → Read-Only Access
• Inactive Account → No Access
'''

role = input("Role: ").capitalize()
account_status = input("Account Status: ").capitalize()

if account_status != "Active":
    print("Access Level: NO ACCESS")
    print("Reason: Account is inactive.")
elif role == "Admin":
    security_clearance = int(input("Security Clearance: "))
    if security_clearance >= 5:
        print("Access Level: FULL ACCESS")
    else:
        print("Access Level: LIMITED ACCESS")
        print("Reason: Security clearance below 5.")
elif role == "Manager":
    experience = int(input("Years of Experience: "))
    if experience > 5:
        print("Access Level: DEPARTMENT ACCESS")
    else:
        print("Access Level: LIMITED ACCESS")
        print("Reason: Experience is 5 years or less.")
elif role == "Employee":
    experience = int(input("Years of Experience: "))
    if experience > 2:
        print("Access Level: LIMITED ACCESS")
    else:
        print("Access Level: READ-ONLY ACCESS")
        print("Reason: Experience is 2 years or less.")
elif role == "Guest":
    print("Access Level: READ-ONLY ACCESS")
else:
    print("Access Level: NO ACCESS")
    print("Reason: Invalid role.")

'''
Bonus Challenge: Hospital Emergency Triage System

A hospital prioritizes patients based on:
• Critical Condition
• Age
• Oxygen Level

Rules:
• Critical condition → Immediate Treatment
• Oxygen below 90 → High Priority
• Age above 65 → Medium Priority
• Others → Normal Priority
'''

critical = input("Critical Condition (Y/N): ").upper()
age = int(input("Age: "))
oxygen_level = int(input("Oxygen Level: "))

if critical == "Y":
    print("Patient Priority: Immediate Treatment")
    print("Reason: Critical Condition")
elif oxygen_level < 90:
    print("Patient Priority: High Priority")
    print("Reason: Oxygen level below 90")
elif age > 65:
    print("Patient Priority: Medium Priority")
    print("Reason: Senior Citizen")
else:
    print("Patient Priority: Normal Priority")

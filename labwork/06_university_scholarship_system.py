'''
Lab Work 6: University Scholarship System

Scholarship is awarded based on percentage:
• 95+       → 100%
• 90-94     → 75%
• 85-89     → 50%
• 80-84     → 25%
• Below 80  → No Scholarship

Conditions:
• Family income must be below Rs.8,00,000.
• Students with disciplinary actions receive no scholarship.
'''

percentage = float(input("Percentage: "))
family_income = float(input("Family Income: "))
disciplinary = input("Disciplinary Action (Y/N): ").upper()

# Check disqualifying conditions first
if disciplinary == "Y":
    print("Scholarship Awarded: None")
    print("Reason: Disciplinary action on record.")
elif family_income >= 800000:
    print("Scholarship Awarded: None")
    print("Reason: Family income exceeds Rs.800000.")
else:
    # Determine scholarship percentage
    if percentage >= 95:
        scholarship = "100%"
    elif percentage >= 90:
        scholarship = "75%"
    elif percentage >= 85:
        scholarship = "50%"
    elif percentage >= 80:
        scholarship = "25%"
    else:
        scholarship = "No Scholarship"

    print(f"Scholarship Awarded: {scholarship}")

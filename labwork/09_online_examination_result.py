'''
Lab Work 9: Online Examination Result Analyzer

A student appears in 5 subjects.
Rules:
• Minimum 40 marks in every subject to pass.
• Distinction    → Average ≥ 75
• First Division → Average ≥ 60
• Second Division→ Average ≥ 50
• Pass           → Average ≥ 40
• Fail if any subject score < 40
'''

hindi = int(input("Hindi : "))
english = int(input("English : "))
mathematics = int(input("Mathematics : "))
science = int(input("Science : "))
computer = int(input("Computer : "))

total = hindi + english + mathematics + science + computer
average = total / 5

print(f"Average Marks: {average}")

# Check if failed in any subject
if hindi < 40 or english < 40 or mathematics < 40 or science < 40 or computer < 40:
    print("Result: FAIL")
    failed_subjects = []
    if hindi < 40:
        failed_subjects.append("Hindi")
    if english < 40:
        failed_subjects.append("English")
    if mathematics < 40:
        failed_subjects.append("Mathematics")
    if science < 40:
        failed_subjects.append("Science")
    if computer < 40:
        failed_subjects.append("Computer")
    print(f"Failed in: {', '.join(failed_subjects)}")
else:
    print("Result: PASS")
    if average >= 75:
        print("Classification: Distinction")
    elif average >= 60:
        print("Classification: First Division")
    elif average >= 50:
        print("Classification: Second Division")
    else:
        print("Classification: Pass")

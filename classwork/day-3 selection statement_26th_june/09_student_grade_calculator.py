'''
Problem Statement 3 : Student Grade Calculator
A school assigns grades based on the marks obtained by students:
* Marks 90 and above → Grade A
* Marks 75 to 89 → Grade B
* Marks 50 to 74 → Grade C
* Below 50 → Grade F
'''

marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade F")

# Question 4 (Inbuilt): Write a program to ask the user for their full name and display the first name.
# Condition: Both first name and last name are mandatory.
# Input: Enter full name (for example: "John Smith")
# Expected Output: First name: John

while True:
    full_name = input("Enter your full name (first and last): ").strip()
    parts = full_name.split()

    if len(parts) >= 2:
        print("First name:", parts[0])
        break

    print("Please enter both first name and last name.")

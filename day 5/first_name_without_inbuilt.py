# Question 4 (Without Inbuilt): Write a program to ask the user for their full name and display the first name.
# Condition: Both first name and last name are mandatory.
# Input: Enter full name (for example: "John Smith")
# Expected Output: First name: John

while True:
    full_name = input("Enter your full name (first and last): ")

    n = len(full_name)
    i = 0

    while i < n and full_name[i] == ' ':
        i += 1

    first_name = ""
    while i < n and full_name[i] != ' ':
        first_name += full_name[i]
        i += 1

    while i < n and full_name[i] == ' ':
        i += 1

    has_last_name = False
    while i < n:
        if full_name[i] != ' ':
            has_last_name = True
            break
        i += 1

    if first_name != "" and has_last_name:
        print("First name:", first_name)
        break

    print("Please enter both first name and last name.")

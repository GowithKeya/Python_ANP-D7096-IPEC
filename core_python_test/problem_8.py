# Problem 8: Password Strength Checker
password = input("Enter Password: ")

missing = []

if len(password) < 8:
    missing.append("Minimum 8 characters")

if not any(ch.isupper() for ch in password):
    missing.append("One uppercase letter")

if not any(ch.islower() for ch in password):
    missing.append("One lowercase letter")

if not any(ch.isdigit() for ch in password):
    missing.append("One digit")

if not any(not ch.isalnum() for ch in password):
    missing.append("One special character")

if len(missing) == 0:
    print("Strong Password")
else:
    print("Weak Password")
    print("Missing Conditions:")
    for item in missing:
        print("-", item)

"""
Lab: Functions in Python
Problem Statement 3: Password Strength Checker
"""


def check_password(password):
    has_min_length = len(password) >= 8
    has_uppercase = any(ch.isupper() for ch in password)
    has_lowercase = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)

    if has_min_length and has_uppercase and has_lowercase and has_digit:
        return "Strong Password"
    return "Weak Password"


password = input("Enter password: ")
print(check_password(password))

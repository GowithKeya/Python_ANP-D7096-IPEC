'''
Lab Work 7: Cybersecurity Login Validation

A login system validates:
• Username
• Password
• OTP

Conditions:
• All correct → Login Successful
• Incorrect OTP → Re-enter OTP
• Incorrect Password after 3 attempts → Account Locked
• Incorrect Username → User Not Found
'''

# Stored credentials
correct_username = "admin"
correct_password = "admin123"
correct_otp = "4567"

username = input("Username: ")

if username != correct_username:
    print("User Not Found")
else:
    # Password validation with 3 attempts
    attempts = 0
    max_attempts = 3
    password_correct = False

    while attempts < max_attempts:
        password = input("Password: ")
        if password == correct_password:
            password_correct = True
            break
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Incorrect Password. {remaining} attempt(s) remaining.")
            else:
                print("Account Locked")

    if password_correct:
        # OTP validation
        otp = input("OTP: ")
        if otp == correct_otp:
            print("Login Successful")
            print("Welcome Admin")
        else:
            print("Incorrect OTP. Please re-enter OTP.")
            otp = input("OTP: ")
            if otp == correct_otp:
                print("Login Successful")
                print("Welcome Admin")
            else:
                print("Login Failed. Too many incorrect OTP attempts.")

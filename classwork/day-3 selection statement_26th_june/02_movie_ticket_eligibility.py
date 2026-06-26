# Question 2: Movie Ticket Eligibility
# Scenario:
# A multiplex allows entry to a movie only if the customer is 18 years
# of age or older.

# Problem Statement:
# Write a Python program that accepts the age of a customer and determines
# whether they are eligible to watch the movie.

# Input:
# Age

# Output:
# Eligibility message

age = int(input("Enter Your Age: "))

if age >= 18:
    print("You are eligible to watch the movie.")
else:
    print("You are not eligible to watch the movie.")

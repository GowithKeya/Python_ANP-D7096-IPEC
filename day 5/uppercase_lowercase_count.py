# Question 2: Write a program to find the number of uppercase and lowercase characters in a sentence without using inbuilt functions.
# Input: Enter a sentence (for example: "Hello World")
# Expected Output:
# Number of uppercase letters: 2
# Number of lowercase letters: 8

sentence = input("Enter a sentence: ")

upper_count = 0
lower_count = 0

for ch in sentence:
    if 'A' <= ch <= 'Z':
        upper_count += 1
    elif 'a' <= ch <= 'z':
        lower_count += 1

print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)

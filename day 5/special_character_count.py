# Question 3: Write a program to count the number of special characters in a sentence.
# Input: Enter a sentence (for example: "Hello@123!")
# Expected Output: Number of special characters: 2

sentence = input("Enter a sentence: ")

special_count = 0

for ch in sentence:
    if ch.isalnum() or ch.isspace():
        continue
    else:
        special_count += 1

print("Number of special characters:", special_count)

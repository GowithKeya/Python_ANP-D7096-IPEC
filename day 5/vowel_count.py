# Question: Write a program to input a sentence and count the number of vowels.
# Input: Enter a sentence (for example: "Hello World")
# Expected Output: Number of vowels: 3

sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
count = 0

for ch in sentence:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)

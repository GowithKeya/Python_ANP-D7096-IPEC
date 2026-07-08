"""
Lab: Functions in Python
Problem Statement 5: Vowel Counter using Function
"""


def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count


sentence = input("Enter a sentence: ")
total_vowels = count_vowels(sentence)
print("\nTotal Vowels:", total_vowels)

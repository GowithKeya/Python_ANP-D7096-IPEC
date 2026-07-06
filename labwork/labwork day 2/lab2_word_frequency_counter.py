# Python Lab: 6th July 2026
# Lab 2: Word Frequency Counter

sentence = input("Enter a sentence: ").strip().lower()
words = sentence.split()

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord frequency dictionary:")
print(frequency)

if frequency:
    most_frequent_word = max(frequency, key=frequency.get)
    print("Most frequently occurring word:", most_frequent_word, "-", frequency[most_frequent_word], "times")

print("\nWords in alphabetical order:")
for word in sorted(frequency):
    print(word, ":", frequency[word])

# Problem 9: Word Frequency Counter
import string

def word_frequency(sentence):

    for p in string.punctuation:
        sentence = sentence.replace(p, "")

    sentence = sentence.lower()

    words = sentence.split()

    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    print("Word Frequencies:")

    for word in sorted(freq):
        print(word, ":", freq[word])

    most_repeated = max(freq, key=freq.get)

    print("\nMost Repeated Word:")
    print(most_repeated)

sentence = input("Enter Sentence: ")
word_frequency(sentence)

'''Problem 2: Character Frequency Analyzer 
Accept a string from the user and perform the following: 
• Count uppercase letters  
• Count lowercase letters  
• Count digits  
• Count special characters  
• Print the most frequently occurring character  
Example: 
Input: 
Python@2026 
Output: 
Uppercase : 1 
Lowercase : 5 
Digits : 4 
Special Characters : 1 
Most Frequent Character : 2 '''

def char_frq_analyzer():
    text = input("Enter a string: ")

    uppercase = 0
    lowercase = 0
    digits = 0
    special = 0

    frq = {}

    for ch in text:
        if ch.isupper():
            uppercase += 1
        elif ch.islower():
            lowercase += 1
        elif ch.isdigit():
            digits += 1
        else:
            special += 1

        frq[ch] = frq.get(ch, 0) + 1

    most_frequent = max(frq, key=frq.get)

    print("Uppercase :", uppercase)
    print("Lowercase :", lowercase)
    print("Digits :", digits)
    print("Special Characters :", special)
    print("Most Frequent Character :", most_frequent)

# Example
char_frq_analyzer()
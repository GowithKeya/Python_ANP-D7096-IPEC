"""
Question 3:
Write a program to find the frequency of a given number in a list.
Take the list input from the user.
"""


# Accept a list of numbers from the user
user_input = input("Enter numbers separated by commas (e.g., 1, 2, 3, 2, 4): ")
numbers = [int(item.strip()) for item in user_input.split(",") if item.strip() != ""]

if len(numbers) == 0:
        print("The list is empty.")
else:
        # Ask for the number whose frequency is to be found
        target = int(input("Enter the number to find its frequency: "))
        frequency = numbers.count(target)

        print("Your list:", numbers)
        print(f"Frequency of {target}: {frequency}")
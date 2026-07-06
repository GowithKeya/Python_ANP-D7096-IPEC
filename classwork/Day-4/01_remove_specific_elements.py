# Question 1: Remove Any List Element by Specific Index
# Scenario:
# You want to create a generic program that allows a user to input their own list of elements
# and remove any element at a specified index.

# Problem Statement:
# Write a Python program that:
# 1. Accepts a list of elements from the user (e.g., comma-separated).
# 2. Prompts the user to enter the index of the element to remove.
# 3. Removes the element from the list at that index.
# 4. Handles invalid inputs (non-integer indices) and out-of-range errors.
# 5. Displays the removed element and the updated list.

try:
    # Accept the list from the user
    user_input = input("Enter list elements separated by commas (e.g., apple, banana, cherry): ")
    # Split the input string and strip whitespace around each item
    my_list = [item.strip() for item in user_input.split(",") if item.strip() != ""]

    if len(my_list) == 0:
        print("The list is empty. Nothing to remove.")
    else:
        print("\nYour list:", my_list)
        
        # Ask for the index to remove
        index_input = input(f"Enter the index (0 to {len(my_list) - 1}) of the element to remove: ")
        index = int(index_input)
        
        # Validate if index is within the valid range
        if index < -len(my_list) or index >= len(my_list):
            print(f"Error: Index {index} is out of range. Valid range is 0 to {len(my_list) - 1}.")
        else:
            # Remove and retrieve the item using pop()
            removed_item = my_list.pop(index)
            print(f"Successfully removed '{removed_item}' from index {index}.")
            print("Updated list:", my_list)

except ValueError:
    print("Error: Please enter a valid integer for the index.")

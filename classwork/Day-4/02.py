#a list given by user of 20 ites, and if number some numbers are alrady there remove dublicates


# Accept a list of elements from the user
user_input = input("Enter a list of elements separated by commas (e.g., apple, banana, cherry): ")
my_list = [item.strip() for item in user_input.split(",")]  
my_list = list(set(my_list))  # Remove duplicates
print("List after removing duplicates:", my_list)

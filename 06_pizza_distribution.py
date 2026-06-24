# Question 6: Pizza Distribution
# Scenario:
# A party organizer wants to distribute pizza slices equally among children.
#
# Problem Statement:
# Write a Python program to find how many slices remain after equal distribution.
#
# Input:
# Total Pizza Slices
# Number of Children
#
# Output:
# Remaining Slices

total_slices = int(input("Enter total pizza slices: "))
number_of_children = int(input("Enter number of children: "))

remaining_slices = total_slices % number_of_children

print("Remaining Slices:", remaining_slices)

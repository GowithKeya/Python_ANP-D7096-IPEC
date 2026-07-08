"""
Lab: Functions in Python
Problem Statement 2: List Analysis using Functions
"""


def find_max(numbers):
    return max(numbers)


def find_min(numbers):
    return min(numbers)


def find_average(numbers):
    return sum(numbers) / len(numbers)


numbers = []
for i in range(1, 11):
    value = int(input(f"Enter integer {i}: "))
    numbers.append(value)

print("\nList Analysis Result:")
print("Maximum value:", find_max(numbers))
print("Minimum value:", find_min(numbers))
print("Average value:", find_average(numbers))

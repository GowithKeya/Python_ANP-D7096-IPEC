# Problem 5: List Processing
numbers = []

for i in range(20):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Largest Number:", max(numbers))

unique_sorted = sorted(set(numbers))
print("Second Largest Number:", unique_sorted[-2])

print("Smallest Number:", min(numbers))

print("List Without Duplicates:", list(set(numbers)))

print("Even Numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")

print("\nNumbers Divisible by 3 and 5:")
for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print(num, end=" ")

reversed_list = numbers[::-1]
print("\nReversed List:", reversed_list)

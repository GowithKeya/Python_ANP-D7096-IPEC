# Question 8: Online Shopping Discount
# Scenario:
# An e-commerce website offers a fixed discount on products.
#
# Problem Statement:
# Write a Python program to calculate the final payable amount after applying
# the discount.
#
# Input:
# Product Price
# Discount Amount
#
# Output:
# Final Price

product_price = float(input("Enter product price: "))
discount_amount = float(input("Enter discount amount: "))

final_price = product_price - discount_amount

print("Final Price:", final_price)

# Question 11: Food Delivery Business Profit Analysis
# Scenario:
# A food delivery startup wants to calculate its daily profit and package
# distribution details.
#
# Problem Statement:
# Write a Python program that:
# 1. Calculates total revenue generated.
# 2. Calculates profit after deducting expenses.
# 3. Determines how many complete delivery boxes can be prepared.
# 4. Finds remaining food packets.
# 5. Predicts revenue after a certain number of days assuming revenue doubles
#    daily.
#
# Input:
# Number of orders
# Price per order
# Daily expenses
# Total food packets
# Packets per box
# Number of days
#
# Output:
# Total Revenue
# Profit
# Complete Boxes
# Remaining Packets
# Future Revenue

number_of_orders = int(input("Enter number of orders: "))
price_per_order = float(input("Enter price per order: "))
daily_expenses = float(input("Enter daily expenses: "))
total_food_packets = int(input("Enter total food packets: "))
packets_per_box = int(input("Enter packets per box: "))
number_of_days = int(input("Enter number of days: "))

total_revenue = number_of_orders * price_per_order
profit = total_revenue - daily_expenses
complete_boxes = total_food_packets // packets_per_box
remaining_packets = total_food_packets % packets_per_box
future_revenue = total_revenue * (2 ** number_of_days)

print("Total Revenue:", total_revenue)
print("Profit:", profit)
print("Complete Boxes:", complete_boxes)
print("Remaining Packets:", remaining_packets)
print("Future Revenue:", future_revenue)

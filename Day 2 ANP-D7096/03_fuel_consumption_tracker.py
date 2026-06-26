# Question 3: Fuel Consumption Tracker
# Scenario:
# A person wants to calculate the average fuel consumption of a car.

# Problem Statement:
# Write a Python program to find the average mileage of a car.

# Input:
# Total distance traveled (km)
# Fuel consumed (liters)

# Output:
# Mileage (km/l)

distance = float(input("Enter total distance traveled in km: "))
fuel_consumed = float(input("Enter fuel consumed in liters: "))

mileage = distance / fuel_consumed

print("Mileage:", mileage, "km/l")

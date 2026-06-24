# Question 2: Grocery Store Bill
# Scenario:
# A customer purchases multiple packets of rice from a grocery store.
#
# Problem Statement:
# Write a Python program to calculate the total cost of rice packets purchased.
#
# Input:
# Price per packet
# Number of packets
#
# Output:
# Total Bill Amount

price_per_packet = float(input("Enter price per rice packet: "))
number_of_packets = int(input("Enter number of packets: "))

total_bill = price_per_packet * number_of_packets

print("Total Bill Amount:", total_bill)

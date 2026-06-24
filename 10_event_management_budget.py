# Question 10: Event Management Budget
# Scenario:
# An event manager wants to calculate the cost contribution per participant.
#
# Problem Statement:
# Write a Python program to calculate how much each participant should pay.
#
# Input:
# Total Event Cost
# Number of Participants
#
# Output:
# Amount per Participant

total_event_cost = float(input("Enter total event cost: "))
number_of_participants = int(input("Enter number of participants: "))

amount_per_participant = total_event_cost / number_of_participants

print("Amount per Participant:", amount_per_participant)

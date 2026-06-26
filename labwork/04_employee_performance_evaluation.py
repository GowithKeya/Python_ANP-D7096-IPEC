'''
Lab Work 4: Employee Performance Evaluation

An employee is evaluated using:
• Project Score
• Attendance Percentage
• Client Feedback Score

Rules:
• Excellent → All scores above 90
• Good → Scores above 75
• Average → Scores above 60
• Poor → Otherwise

Additional Rule:
• Attendance below 70% cannot receive more than Average rating.
'''

project_score = int(input("Project Score: "))
attendance = int(input("Attendance: "))
client_feedback = int(input("Client Feedback: "))

# Determine rating based on scores
if project_score > 90 and attendance > 90 and client_feedback > 90:
    rating = "Excellent"
elif project_score > 75 and attendance > 75 and client_feedback > 75:
    rating = "Good"
elif project_score > 60 and attendance > 60 and client_feedback > 60:
    rating = "Average"
else:
    rating = "Poor"

# Apply attendance rule
reason = ""
if attendance < 70 and rating in ["Excellent", "Good"]:
    rating = "Average"
    reason = "Attendance below 70%"

print(f"Performance Rating: {rating}")
if reason:
    print(f"Reason: {reason}")

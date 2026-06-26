'''
Lab Work 5: E-Commerce Premium Membership Eligibility

A customer becomes Premium Member if:
• Total Purchases > Rs.50,000
• Orders Completed ≥ 20
• Customer Rating ≥ 4.5

Special Case:
• Purchases above Rs.1,00,000 automatically qualify.
'''

total_purchases = float(input("Total Purchases: "))
orders_completed = int(input("Orders Completed: "))
customer_rating = float(input("Customer Rating: "))

# Special case: automatic qualification
if total_purchases > 100000:
    print("Premium Membership Status: Eligible")
    print("Reason: Purchase amount exceeded Rs.100000.")
elif total_purchases > 50000 and orders_completed >= 20 and customer_rating >= 4.5:
    print("Premium Membership Status: Eligible")
    print("Reason: All criteria satisfied.")
else:
    print("Premium Membership Status: Not Eligible")
    reasons = []
    if total_purchases <= 50000:
        reasons.append("Total purchases below Rs.50000")
    if orders_completed < 20:
        reasons.append("Orders completed less than 20")
    if customer_rating < 4.5:
        reasons.append("Customer rating below 4.5")
    for reason in reasons:
        print(f"Reason: {reason}")

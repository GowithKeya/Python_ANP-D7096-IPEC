'''
Lab Work 8: Smart Electricity Billing System

Calculate electricity bill using:
• 0-100 units     → Rs.5/unit
• 101-300 units   → Rs.7/unit
• Above 300 units → Rs.10/unit

Additional Rules:
• Commercial consumers pay 20% extra.
• Bills above Rs.5000 attract 5% surcharge.
• Senior citizens receive 10% discount.
'''

units = int(input("Units Consumed: "))
consumer_type = input("Consumer Type (Residential/Commercial): ").capitalize()
senior_citizen = input("Senior Citizen (Y/N): ").upper()

# Calculate base bill using slab rates
if units <= 100:
    base_bill = units * 5
elif units <= 300:
    base_bill = (100 * 5) + (units - 100) * 7
else:
    base_bill = (100 * 5) + (200 * 7) + (units - 300) * 10

print(f"Base Bill: Rs.{base_bill}")

total = base_bill

# Commercial charge
commercial_charge = 0
if consumer_type == "Commercial":
    commercial_charge = base_bill * 0.20
    total += commercial_charge
    print(f"Commercial Charge: Rs.{commercial_charge}")

# Surcharge on bills above Rs.5000
surcharge = 0
if total > 5000:
    surcharge = total * 0.05
    total += surcharge
    print(f"Surcharge: Rs.{surcharge}")

# Senior citizen discount
senior_discount = 0
if senior_citizen == "Y":
    senior_discount = total * 0.10
    total -= senior_discount
    print(f"Senior Citizen Discount: Rs.{senior_discount}")

print(f"Final Bill Amount: Rs.{total}")

'''
Lab Work 3: Airline Ticket Pricing Engine

Base Fare = Rs.5000
Additional Charges:
• Business Class → +Rs.3000
• Window Seat → +Rs.500
• Weekend Travel → +Rs.1000

Discounts:
• Age below 12 → 50%
• Age above 60 → 20%
'''

age = int(input("Enter Passenger Age: "))
business_class = input("Business Class (Y/N): ").upper()
window_seat = input("Window Seat (Y/N): ").upper()
weekend_travel = input("Weekend Travel (Y/N): ").upper()

base_fare = 5000
additional_charges = 0

if business_class == "Y":
    additional_charges += 3000

if window_seat == "Y":
    additional_charges += 500

if weekend_travel == "Y":
    additional_charges += 1000

print(f"Base Fare: Rs.{base_fare}")
print(f"Additional Charges: Rs.{additional_charges}")

total = base_fare + additional_charges

# Apply age-based discount
if age < 12:
    discount = 50
    print(f"Child Discount: {discount}%")
    total = total * (1 - discount / 100)
elif age > 60:
    discount = 20
    print(f"Senior Citizen Discount: {discount}%")
    total = total * (1 - discount / 100)

print(f"Final Ticket Fare: Rs.{total}")

'''Problem 1: Electricity Bill Calculator 
Write a Python program that calculates the electricity bill based on the following conditions: 
unit	rate per unit
first 100	5rs
Next 100	7rs
Above 200	10rs

Additional Charges:
• If the bill exceeds ₹2000, apply a 5% surcharge.  
• If the total bill is below ₹500, the minimum bill should be ₹500.  
Display: 
• Total Units  
• Bill Amount  
• Final Payable Amount '''

def Electric_bill_cal(units):
    if units < 0:
        print("Units cannot be negative.")
        return 0, 0
        
    if units <= 100:
        bill_amount = units * 5
    elif units <= 200:
        bill_amount = (100 * 5) + ((units - 100) * 7)
    else:
        bill_amount = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    
    # surcharge
    surcharge = 0
    if bill_amount > 2000:
        surcharge = bill_amount * 0.05
    Final_payable_amount = bill_amount + surcharge
    
    # minimum bill
    if Final_payable_amount < 500:
        Final_payable_amount = 500.0
        
    print("Total Units:", units)
    print("Bill Amount:", bill_amount)
    print("Final Payable Amount:", Final_payable_amount)
    
    return bill_amount, Final_payable_amount

units = float(input("Enter total units: "))
Electric_bill_cal(units)

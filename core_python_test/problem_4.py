# Problem 4: Employee Salary Calculator
def calculate_hra(basic):
    return basic * 0.20

def calculate_da(basic):
    return basic * 0.10

def calculate_tax(gross_salary):
    return gross_salary * 0.08

def calculate_net_salary(basic):
    hra = calculate_hra(basic)
    da = calculate_da(basic)

    gross_salary = basic + hra + da
    tax = calculate_tax(gross_salary)

    net_salary = gross_salary - tax

    return hra, da, gross_salary, tax, net_salary


basic = float(input("Enter Basic Salary: "))

hra, da, gross, tax, net = calculate_net_salary(basic)

print("Basic Salary :", basic)
print("HRA :", hra)
print("DA :", da)
print("Gross Salary :", gross)
print("Tax :", tax)
print("Net Salary :", net)

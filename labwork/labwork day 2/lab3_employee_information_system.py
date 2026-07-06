# Python Lab: 6th July 2026
# Lab 3: Employee Information System

employees = {
    "E101": {"Name": "Amit", "Department": "HR", "Salary": 40000},
    "E102": {"Name": "Neha", "Department": "IT", "Salary": 55000},
    "E103": {"Name": "Ravi", "Department": "Finance", "Salary": 50000},
    "E104": {"Name": "Sneha", "Department": "IT", "Salary": 60000}
}

print("All employee details:")
for emp_id, details in employees.items():
    print(emp_id, ":", details)

search_id = input("\nEnter Employee ID to search: ")
if search_id in employees:
    print("Employee found:", employees[search_id])
else:
    print("Employee not found.")

for emp_id in employees:
    employees[emp_id]["Salary"] = employees[emp_id]["Salary"] * 1.10

print("\nEmployee details after 10% salary increase:")
for emp_id, details in employees.items():
    print(emp_id, ":", details)

dept_name = input("\nEnter department name to filter employees: ").strip().lower()
print("Employees in department", dept_name + ":")
found = False
for emp_id, details in employees.items():
    if details["Department"].lower() == dept_name:
        print(emp_id, ":", details)
        found = True

if not found:
    print("No employees found in this department.")

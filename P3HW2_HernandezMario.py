#Mario Hernandez
#4/23/2025
#P3HW2
#decision structures

# Input Employee information
name = input("Enter the employee's name: ")
hours_worked = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the employee's pay rate: "))

# Determine regular and overtime hours
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

# Calculate Regular pay
regular_pay = regular_hours * pay_rate

# Determine if there is Overtime pay
if overtime_hours > 0:
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    overtime_pay = 0

# Calculate Gross pay
gross_pay = regular_pay + overtime_pay

# Assign Output variables 
var1 = hours_worked
var2 = pay_rate
var3 = overtime_hours
var4 = overtime_pay
var5 = regular_pay
var6 = gross_pay
print("---------------------------------------")
# Display results
print("Employees Name:      " + name)
print("\nHours Worked   Pay Rate  Overtime   Overtime Pay  RegHour Pay  Gross Pay")
print("--------------------------------------------------------------------------------")
print(f'{var1:<15.2f}{var2:<10.2f}{var3:<10.2f}{var4:<15.2f}{var5:<15.2f}{var6:<15.2f}')



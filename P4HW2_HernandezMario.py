#Mario Hernandez
#4/28/2025
#P4HW2
#Decision structures updated with loops

# Initialize totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Prompt outside the loop
name = input("Enter the employee's name or 'Done' to terminate: ")

while name.lower() != "done":
    hours_worked = float(input(f"How many hours did {name} work?: "))
    pay_rate = float(input(f"What is {name}'s pay rate?: "))

# Determine regular and overtime hours
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

# Calculate pay
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)

    gross_pay = regular_pay + overtime_pay


    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

# Display individual employee summary
    print("---------------------------------------")
    print("Employee's Name:      " + name)
    print("\nHours Worked   Pay Rate  Overtime   Overtime Pay  RegHour Pay  Gross Pay")
    print("--------------------------------------------------------------------------------")
    print(f'{hours_worked:<15.2f}{pay_rate:<10.2f}{overtime_hours:<10.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}')
    print("")

# Ask again at the end of the loop
    name = input("Enter the employee's name or 'Done' to terminate: ")

# Final totals display

print(f"Total number of employees entered:       {employee_count}")
print(f"Total amount paid for overtime:          ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours:     ${total_regular_pay:.2f}")
print(f"Total amount paid in gross:              ${total_gross_pay:.2f}")


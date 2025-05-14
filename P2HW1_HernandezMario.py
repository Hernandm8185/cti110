#Mario Hernandez
#4/9/2025
#P2HW1
#Edit and enhance existing programs

print("This program calculates and displays travel expenses\n")


#Add float to make sure whatever user enters is converted to float.
budget = float(input("Enter budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas_expense = float(input("How much do you think you will spend on gas? "))
print()
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))
print()
food_expense = float(input("Last, how much will you need for food? "))

remaining_budget = budget - (gas_expense + accommodation_expense + food_expense)
#format so output is converted to float, has ($) with two decimal places, and specify width of column.
print("\n-------------Travel Expenses-------------")
width = 20
print(f"{'Location:':{width}} {destination}")
print(f"{'Initial Budget:':{width}} ${budget:.2f}")
print(f"{'Fuel:':{width}} ${gas_expense:.2f}")
print(f"{'Accommodation:':{width}} ${accommodation_expense:.2f}")
print(f"{'Food:':{width}} ${food_expense:.2f}")
print("-----------------------------------------\n")
print(f"{'Remaining Balance:':{width}} ${remaining_budget:.2f}")


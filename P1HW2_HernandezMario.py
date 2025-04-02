# Mario Hernandez
# 3/31/2005
# P1HW2
# A program to calculate travel expenses.

print("This program calculates and displays travel expenses\n")


budget = int(input("Enter budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas_expense = int(input("How much do you think you will spend on gas? "))
print()
accommodation_expense = int(input("Approximately, how much will you need for accommodation/hotel? "))
print()
food_expense = int(input("Last, how much will you need for food? "))

remaining_budget = budget - (gas_expense + accommodation_expense + food_expense)

print("\n-------Travel Expenses-------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas_expense)
print("Accommodation:", accommodation_expense)
print("Food:", food_expense)
print()
print("Remaining Balance:", remaining_budget)

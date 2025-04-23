# Mario Hernandez
# 4/17/2025
# P3_Lab
# Converting money into change

user_input = input("Enter the amount as a float: ")
user_input = float(user_input)

if user_input <= 0:
    print("No Change.")
else:
    cents = int(round(user_input * 100))
# Dollar output
    dollars = cents // 100
    cents = cents - (dollars * 100)
    if dollars > 0:
        print(f"{dollars} Dollar" if dollars == 1 else f"{dollars} Dollars")
# Quarter output
    quarters = cents // 25
    cents = cents - (quarters * 25)
    if quarters > 0:
        print(f"{quarters} Quarter" if quarters == 1 else f"{quarters} Quarters")
# Dime output
    dimes = cents // 10
    cents = cents - (dimes * 10)
    if dimes > 0:
        print(f"{dimes} Dime" if dimes == 1 else f"{dimes} Dimes")
# Nickle output
    nickels = cents // 5
    cents = cents - (nickels * 5)
    if nickels > 0:
        print(f"{nickels} Nickel" if nickels == 1 else f"{nickels} Nickels")
# Penny output
    pennies = cents // 1
    cents = cents - (pennies * 1)
    if pennies > 0:
        print(f"{pennies} Penny" if pennies == 1 else f"{pennies} Pennies")

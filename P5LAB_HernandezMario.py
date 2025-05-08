# Mario Hernandez
# 5/4/2025
# P5_Lab
# Dispurse_change

import random

def disperse_change(change):
    if change <= 0:
        print("No Change.")
    else:
        cents = int(round(change * 100))
        
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
        
        # Nickel output
        nickels = cents // 5
        cents = cents - (nickels * 5)
        if nickels > 0:
            print(f"{nickels} Nickel" if nickels == 1 else f"{nickels} Nickels")
        
        # Penny output
        pennies = cents // 1
        cents = cents - (pennies * 1)
        if pennies > 0:
            print(f"{pennies} Penny" if pennies == 1 else f"{pennies} Pennies")

def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"you owe ${total_owed}")
    
    user_input = input("How much cash will you put in the self-checkout: ")
    cash_given = float(user_input)

    if cash_given < total_owed:
        print("Add more money.")
    else:
        change = round(cash_given - total_owed, 2)
        print(f"Change is: ${change}")
        disperse_change(change)

# Call the main function to run the program
main()
main()

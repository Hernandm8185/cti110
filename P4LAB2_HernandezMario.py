# Mario Hernandez
# 4/27/2025
# P4HW1
# display information with loops.

repeat_list = ["yes"]  

for repeat in repeat_list:  
    user_input = input("Enter an integer: ")

    if user_input.lstrip('-').isdigit():
        number = int(user_input)

        if number < 0:
            print("This program does not handle negative values.")
        else:
            print(f"Multiplication table for {number}:")
            i = 1
            while i <= 12: 
                print(f"{number} * {i} = {number * i}")
                i += 1
    else:
        print("Invalid input. Please enter a valid integer.")

    repeat = input("Would you like to run the program again? ").strip().lower()
    
    if repeat == "yes":
        repeat_list.append("yes")
    else:
        print("Exiting program...")

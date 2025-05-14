# Mario Hernandez
# 5/10/2025
# P5LAB
# Avendture game

import random

# Create variables for the dictionary
def create_jumper(jumper):
    print("\nCliff Jump Adventure\n")

    name = input("Name your Jumper: ")
    health_points = 100
    jump_ability = 0
    inventory = []
# Loop to keep getting items from the user
    item = input("Should " + name + " have any items to begin? (y/n): ")
    if item.lower() == "y":
        keep_adding = 1
    else:
        keep_adding = 0

    while keep_adding:
        obj = input("Enter an item to add to inventory (Rocket Boots, Spring Shoes): ")
        if obj == "Rocket Boots":
            inventory.append(obj)
        elif obj == "Spring Shoes":
            inventory.append(obj)
        else:
            print("That item won't help you jump.")

        item = input("Add another item? (y/n): ")
        if item.lower() == "y":
            keep_adding = 1
        else:
            keep_adding = 0

    print("\nYou successfully created " + name + "'s inventory")
    print("Inventory:", inventory)
# Create the dictionary that represents the character
    jumper["name"] = name
    jumper["hp"] = health_points
    jumper["jump_ability"] = jump_ability
    jumper["inventory"] = inventory
    jumper["jump_success"] = 0


# Function to simulate a jump and return success or fail
def jump_cliff(jumper, cliff_height):
    base_jump = 1
    bonus = 0

    index = 0
    while index < len(jumper["inventory"]):
        item = jumper["inventory"][index]
        if item == "Rocket Boots":
            bonus = bonus + 10
        elif item == "Spring Shoes":
            bonus = bonus + 5
        index = index + 1

    total_jump = base_jump + bonus

    print(jumper["name"] + " tries to jump a " + str(cliff_height) + " ft cliff...")
    print("Jump Power:", total_jump, "ft")

    if total_jump >= cliff_height:
        print("Success! You cleared the cliff!\n")
        jumper["jump_success"] = 1
    else:
        damage = random.randint(2, 11)
        jumper["hp"] = jumper["hp"] - damage
        print("Missed! You hit the edge and lost HP.")
        print("Remaining HP:", jumper["hp"], "\n")
        jumper["jump_success"] = 0

        direction = input("Take the path to the right or to the left: ").lower()
        if direction == "left":
            print("Continue down the path....")
        elif direction == "right":
            print("You moved right into another cliff!\n")

# Allow input for path choices 
def choose_path(jumper):
    direction = input("Take the path to the right or to the left: ").lower()

    if direction == "left":
        print("A rockslide! You barely escaped. No damage.\n")
    elif direction == "right":
        print("Found a healing spring! +5 HP!\n")
        jumper["hp"] = jumper["hp"] + 5
    else:
        print("You wandered in a circle. Nothing happens.\n")

# Main game loop
def play_game(jumper):
    cliffs = [10, 15, 20, 12, 18]
    level = 0
    total = len(cliffs)
    hp_exhausted = 0  

    while level < total:
        if hp_exhausted == 0:
            print("Level " + str(level + 1) + " - Cliff Ahead!")
            jump_cliff(jumper, cliffs[level])

            if jumper["hp"] <= 0:
                print("Game Over! You ran out of HP.")
                hp_exhausted = 1
            else:
                choose_path(jumper)
                level = level + 1

    if jumper["hp"] > 0:
        print("Well done " + jumper["name"] + "! You survived the cliffs and finished the game!")


def main():
    jumper = {}
    create_jumper(jumper)
    play_game(jumper)


if __name__ == "__main__":
    main()

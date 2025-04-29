# Mario Hernandez
# 4/29/2025
# P4HW1
# Understanding lists updated with loops.



# Ask how many scores to enter
num_scores = input("How many scores would you like to enter? ")

while num_scores.isdigit() == 0:
    print("Input must be a number.")
    num_scores = input("How many scores would you like to enter? ")

num_scores = int(num_scores)


module_grades = []
i = 0

# Loop to collect scores
while i < num_scores:
    score_input = input(f"Enter grade for Module #{i + 1}: ")

    score_numeric = score_input.replace('.', '', 1).isdigit()
    if score_numeric:
        score = float(score_input)

        score_in_range_low = 0 <= score
        score_in_range_high = score <= 100

        if score_in_range_low:
            if score_in_range_high:
                module_grades.append(score)
                i = i + 1
            else:
                print("Invalid input. Score must be 100 or less.")
        else:
            print("Invalid input. Score must be 0 or more.")
    else:
        print("INVALID Score endered!!!")
        print("Score Should be between 0 and 100")

# Processing results
lowest = min(module_grades)
module_grades.remove(lowest)
total = sum(module_grades)
count = len(module_grades)
average = total / count

# Determine letter grade
if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display results
print("\n----------- Results -----------")
print("Lowest Score:", lowest)
print("Modified List:    ", module_grades)
print("Scores Average:       ", format(average, ".2f"))
print("Grade:        ", letter_grade)
print("--------------------------------")

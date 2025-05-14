# Mario Hernandez
# 4/09/2025
# P2HW2
# Understanding lists


#User inputs grades for each module.
module_grades = []
module_grades.append(float(input("Enter grade for Module 1: ")))
module_grades.append(float(input("Enter grade for Module 2: ")))
module_grades.append(float(input("Enter grade for Module 3: ")))
module_grades.append(float(input("Enter grade for Module 4: ")))
module_grades.append(float(input("Enter grade for Module 5: ")))
module_grades.append(float(input("Enter grade for Module 6: ")))

#Perform calculations
lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

#Display results
print("\n-----------Results-----------")
print(f"Lowest Grade:     {lowest}")
print(f"Highest Grade:    {highest}")
print(f"Sum of Grades:    {total}")
print(f"Average:          {average:.2f}")
print("--------------------------------------")

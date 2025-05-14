# Mario Hernandez
# 4/06/2025
# P2LAB1
# Using Math expressions

import math

# Get radius from user
radius = float(input("What is the radius of the circle: "))
print()
# Calculate circumference, diameter, and area
cir = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius ** 2)

# Display results
print(f"The diameter of the circle is {diam:.1f}")
print()
print(f"The circumference of the circle is {cir:.2f}")
print()
print(f"The area of the circle is {area:.3f}")


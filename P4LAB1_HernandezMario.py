# Mario Hernandez
# 4/30/2025
# P4Lab1 (a)
# Draw a triangle and a square using loops.

import turtle 


wn = turtle.Screen()

t1 = turtle.Turtle()
t2= turtle.Turtle()

# Assign turtle 1
t1.pensize(5)          
t1.pencolor("purple")     
t1.shape("turtle")

# Assign turtle 2
t2.pensize(3)          
t2.pencolor("green")     
t2.shape("turtle")


# Draw a triangle using a while loop
sides = 0
while sides < 3:
    t1.forward(80)
    t1.left(120)
    sides += 1           

# Draw a square using a while loop

sides = 0
while sides < 4:
    t2.forward(50)
    t2.left(90)
    sides += 1


wn.mainloop()

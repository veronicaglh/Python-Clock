# This program will build a working clock using python.

# Import statements
import turtle
import time

# Creating the screen
window = turtle.Screen()
window.bgcolor('violet')
window.setup(width=500, height=500)
window.tracer(0)

# Creating turtle pen named pennie to draw the clock
pennie = turtle.Turtle()

# Creating separate turtle pen named title to place the title on the screen
title = turtle.Turtle()
title.penup()
title.goto(-75,160)
title.pendown()
title.write("Python Clock",font=("Calibri",22, "bold"))
title.hideturtle()
title.penup()
title.goto(-30,150)
title.pendown()
title.write("A working clock",font=("Calibri",13, "italic"))
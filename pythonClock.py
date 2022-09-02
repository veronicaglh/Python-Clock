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

# Function to draw the clock
def draw_clock(hour, minute, second):
    pennie.penup()
    pennie.goto(0, 120)
    pennie.setheading(180)
    pennie.pendown()
    pennie.pensize(3)
    pennie.circle(120)
    pennie.penup()
    pennie.goto(0, 0)
    pennie.setheading(90)

    for _ in range(0, 13):
        pennie.forward(90)
        pennie.pendown()
        pennie.write(_, font=('Ravie', '10'), align='center')
        pennie.penup()
        pennie.forward(5)
        pennie.pendown()
        pennie.forward(5)
        pennie.penup()
        pennie.goto(0, 0)
        pennie.right(30)

    # Drawing the hands of the clock
    pennie.penup()  # to draw the hour hand
    pennie.goto(0, 0)
    pennie.color('blue')
    pennie.setheading(90)
    angle = (hour / 12) * 360
    pennie.right(angle)
    pennie.pendown()
    pennie.forward(38)

    pennie.penup()  # to draw the minute hand
    pennie.goto(0, 0)
    pennie.color('purple')
    pennie.setheading(90)
    angle = (minute / 60) * 360
    pennie.right(angle)
    pennie.pendown()
    pennie.forward(56)

    pennie.penup()  # to draw the second hand
    pennie.goto(0, 0)
    pennie.pensize(1)
    pennie.color('black')
    pennie.setheading(90)
    angle = (second / 60) * 360
    pennie.right(angle)
    pennie.pendown()
    pennie.forward(30)

while True:
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M"))
    second = int(time.strftime("%S"))

    draw_clock(hour, minute, second)
    window.update()
    pennie.clear()
    time.sleep(1)
turtle.done()



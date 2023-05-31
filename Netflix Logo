
import turtle

def draw_rectangle(color, width, height):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_netflix_logo():
    turtle.speed(2)
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.pensize(3)

    # Drawing the red rectangle
    draw_rectangle("#E50914", 200, 100)

    # Moving to draw the 'N'
    turtle.penup()
    turtle.goto(-60, 0)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.speed(3)

    # Drawing the 'N'
    turtle.circle(120, 120)
    turtle.left(120)
    turtle.circle(120, 120)

    # Moving to draw the 'E'
    turtle.penup()
    turtle.goto(40, 0)
    turtle.setheading(0)
    turtle.pendown()

    # Drawing the 'E'
    draw_rectangle("#221F1F", 40, 100)
    turtle.penup()
    turtle.goto(40, 0)
    turtle.pendown()
    draw_rectangle("#E50914", 40, 50)
    turtle.penup()
    turtle.goto(40, -50)
    turtle.pendown()
    draw_rectangle("#E50914", 40, 50)

    # Moving to draw the 'T'
    turtle.penup()
    turtle.goto(100, 0)
    turtle.setheading(0)
    turtle.pendown()

    # Drawing the 'T'
    draw_rectangle("#221F1F", 40, 100)
    turtle.penup()
    turtle.goto(80, 0)
    turtle.pendown()
    draw_rectangle("#E50914", 80, 20)

    # Hiding the turtle
    turtle.hideturtle()

    # Ending the turtle graphics
    turtle.done()

# Calling the function to draw the Netflix logo
draw_netflix_logo()
  

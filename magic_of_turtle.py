import turtle

_ = 1
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)

while True:
    t.forward(_)
    t.color("yellow")
    t.left(120+23)
    t.left(1)
    _ += 1
    t.forward(_)
    t.color("greenyellow")
    t.right(350)

turtle.done()

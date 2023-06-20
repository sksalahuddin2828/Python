from turtle import *
from time import sleep
bgcolor("black")
t = [Turtle(), Turtle()]
x = 6
colors = ["red", "yellow", "blue", "lime"]
for index, i in enumerate(t):
    i.speed(0)
    i.color("white")
    i.shape("circle")
    i.shapesize(0.3)
    i.width(3)
    i.pu()
    i.seth(90)
    i.fd(350)
    i.seth(-180)
    i.pd()
t[0].pu()
delay(0)
speed(0)
ht()
for i in colors:
    color(i)
    for i in range(360):
        t[0].fd(x)
        t[0].lt(1)
        pu()
        goto(t[0].pos())
        pd()
        t[1].fd(2*x)
        t[1].ld(2)
        goto(t[1].pos())
done()

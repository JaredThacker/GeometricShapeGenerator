import turtle
import random


wn = turtle.Screen()
turtle = turtle.Turtle()

turtle.hideturtle()
turtle.speed(0)

r = random.randrange(-360,361)

for i in range(9999):
    turtle.left(r)
    turtle.forward(i) 
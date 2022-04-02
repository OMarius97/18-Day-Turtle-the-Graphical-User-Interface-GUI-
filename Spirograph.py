from turtle import Turtle,Screen, colormode
import random

colormode(255)
valy = Turtle()
valy.shape("turtle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b

valy.speed('fastest')


for i in range(0, 365, 5):
    valy.circle(100)
    valy.color(random_color())
    valy.setheading(i)

screen = Screen()
screen.exitonclick()

from turtle import Turtle, colormode,Screen
import random

colormode(255)
valy = Turtle()
valy.shape("turtle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b

valy.speed(10)
valy.pensize(10)

angle = [0,90,180,270]

while True:
    move = random.choice(angle)
    valy.seth(move)
    valy.forward(30)
    valy.color(random_color())


screen = Screen()
screen.exitonclick()

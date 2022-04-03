import colorgram
from turtle import Turtle, Screen, colormode
import random

# set color mode to 255
colormode(255)

# extracting colors
def extracting_colors(name_image, nr_colors):
    colors_extracted = colorgram.extract(f"{name_image}", nr_colors)
    for i in colors_extracted:
        image_colors.append(i.rgb)

image_colors = []

extracting_colors("image.jpg", 1000)

# setup turtle
valy = Turtle()
valy.penup()
valy.hideturtle()
valy.setpos(-250, -250)

# start drawing
for i in range(-5, 5):
    valy.setpos(-250, (50 * i))
    for _ in range(10):
        valy.dot(20, random.choice(image_colors))
        valy.forward(50)

# screen
screen = Screen()
screen.exitonclick()

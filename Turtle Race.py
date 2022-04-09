from turtle import Turtle,Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500,height=400)
bet = screen.textinput(title="BET", prompt="Which turtle will win? chose a color:")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = -125
racer = []

for i in color:
    new_racer = Turtle("turtle")
    new_racer.color(i)
    new_racer.penup()
    new_racer.setposition(x=-230, y=y_position)
    y_position += 50
    racer.append(new_racer)

if bet:
    race_on = True

while race_on:
    for turtle in racer:
        turtle.forward(random.randint(0,10))

        if turtle.xcor() >= 250:
            race_on = False

            if bet.lower() == turtle.color()[0]:
                print(f"Congratulation you win the winner was {turtle.color()[0]}")
            else:
                print(f"You lose the winner was {turtle.color()[0]}")
            
screen.exitonclick()

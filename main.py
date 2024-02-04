from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=800)
user_bet = screen.textinput(title="Make your bet?", prompt="Which turtle will win the race? Enter Color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
all_turtles = []

"""Set The Turtles To The Position"""
y_axis = [150, 100, 50, 0, -50, -100]
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-380, y=y_axis[turtle_index])
    all_turtles.append(new_turtle)

"""After the user input start the game"""
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 380:
            if user_bet == turtle.color():
                print(f"You win! The '{user_bet}' turtle is the winner.")
                is_race_on = False
            else:
                print(f"You've lost. The '{turtle.pencolor()}' turtle is the winner")
                is_race_on = False


screen.exitonclick()
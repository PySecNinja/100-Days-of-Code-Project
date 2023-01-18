from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-80, -30, 20, 70, 120, 180]
all_turtles = []


for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    new_turtle.goto
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner.")    
            else:
                print(f"You've lost! The {winning_color} is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick() 
    
# See how a for loop saves me all this code

# drew = Turtle(shape="turtle")
# drew.penup()
# drew.goto(x=-240, y=-80)
# drew.color(colors[1])

# anna = Turtle(shape="turtle")
# anna.penup()
# anna.goto(x=-240, y=-30)
# anna.color(colors[2])

# tom = Turtle(shape="turtle")
# tom.penup()
# tom.goto(x=-240, y=20)
# tom.color(colors[3])

# bill = Turtle(shape="turtle")
# bill.penup()
# bill.goto(x=-240, y=70)
# bill.color(colors[4])

# bill = Turtle(shape="turtle")
# bill.penup()
# bill.goto(x=-240, y=120)
# bill.color(colors[5])

# ben = Turtle(shape="turtle")
# ben.penup()
# ben.goto(x=-240, y=120)
# ben.color(colors[5])



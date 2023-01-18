from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
screen = Screen()

directions = [0, 90, 100, 270]
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# Colors list came from 'turle name' in https://trinket.io/docs/colors

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

draw_shape()

screen.exitonclick()
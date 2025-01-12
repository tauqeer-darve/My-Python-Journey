import random
from color import color_generator
from turtle import *

screen = Screen()
screen.colormode(255)
screen.title("Spots Art")

colors = color_generator()

tim = Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.teleport(-250,-250)
tim.penup()
dot_amount = 101

def spot_art_maker():
    for dot_count in range(1, dot_amount):
        tim.dot(20,random.choice(colors))
        tim.forward(50)
        if dot_count % 10 == 0:
            tim.setheading(180)
            tim.fd(500)
            tim.setheading(90)
            tim.fd(50)
            tim.setheading(0)

screen.onkey(spot_art_maker,"space")
screen.listen()
screen.exitonclick()


from turtle import Turtle, Screen
from random import randint

tim = Turtle()
screen = Screen()
screen.colormode(255)
sides = [3,4,5,6,7,8,9]

for i in range(len(sides)):
    screen.colormode(255)
    tim.pencolor(randint(0,255),randint(0,255),randint(0,255))
 
    for _ in range(sides[i]):
        tim.speed("fast")
        tim.pensize(10)
        tim.forward(150)
        tim.right(360/sides[i])

screen.exitonclick()

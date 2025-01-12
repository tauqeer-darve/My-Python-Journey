from turtle import Turtle, Screen
import random
dir = [0,90,180,270]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(0)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour = (r,g,b)
    return colour
    
for _ in range(200):
    tim.pencolor(random_color())
    tim.pensize(20)
    tim.forward(30)
    tim.setheading(random.choice(dir))

screen.exitonclick()
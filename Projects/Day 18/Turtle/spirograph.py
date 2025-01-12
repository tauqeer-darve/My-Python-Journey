from turtle import Turtle, Screen
from random import choice, randint

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed("fastest")

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colour = (r,g,b)
    return colour
    
def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.pencolor(random_color())
        tim.pensize(8)
        tim.circle(200)
        tim.left(gap_size)
        
draw_spirograph(5)
screen.exitonclick()
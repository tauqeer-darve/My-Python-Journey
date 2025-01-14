from turtle import *

tim = Turtle()

screen = Screen()
screen.listen()
screen.title("Etch-A-Sketch")
screen.setup(600,600)

def forward():
    tim.fd(10)

def backward():
    tim.fd(-10)

def up():
    tim.right(10)

def down():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(forward,"w")
screen.onkey(backward,"s")
screen.onkey(up,"a")
screen.onkey(down,"d")
screen.onkey(clear,"c")
screen.exitonclick()

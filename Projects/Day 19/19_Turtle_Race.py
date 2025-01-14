from tkinter import messagebox
from turtle import *
from random import randint
screen = Screen()
screen.setup(width=1500,height=320)
screen.title("Turtle Race")

def finish_line():
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.setheading(90)
    finish_line.penup()
    finish_line.teleport(700,-140)
    finish_line.pd()
    for _ in range(15):
        finish_line.forward(10)
        finish_line.penup()
        finish_line.forward(10)
        finish_line.pd()
finish_line()

user_bet = textinput("Let's bet!","Which turtle do you think will win? Enter a color: ")
colors_list = ["red","blue","green","yellow","purple","pink"]
y = [-100,-60,-20,20,60,100]
all_turtles = []

for index in range(len(colors_list)):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors_list[index])
    turtle.teleport(-680, y[index])
    all_turtles.append(turtle)

start = ""
if user_bet:
    start = True

while start:
    for turtle in all_turtles:
        if turtle.xcor() > 680:
            winner = turtle.pencolor()
            if winner == user_bet:
                messagebox.showinfo("Betting results", f"Congratulations! You won the bet. Winner is {winner} turtle!")
                start = False
            else:
                messagebox.showinfo("Betting results", f"Sorry. You lost the bet. Winner is {winner} turtle.")
                start = False
        forward_dist = randint(0,10)
        turtle.forward(forward_dist)
screen.listen()
screen.exitonclick()
from turtle import Turtle, Screen
tawy = Turtle()
print(tawy)
tawy.shape("turtle")
tawy.color("red")
tawy.fd(100)
tawy.right(90)
tawy.fd(100)
tawy.right(90)
tawy.fd(100)
tawy.right(90)
tawy.fd(100)
my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon",["Pikachu", "Bulbasaur", "Charmander", "Squirtle"])
table.add_column("Type",["Electric", "Grass", "Fire", "Water"])
table.align = "l" # left = l, right = r, center = c
print(table)
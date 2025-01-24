from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        """Create the food for the snake game."""
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()  # Ensure the food does not draw a trail
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Set the size of the food
        self.speed("fastest")  # Make the food movement instantaneous
        self.refresh()

    def refresh(self):
        """Reposition the food to a random location on the screen."""
        x = random.randint(-280, 280)  # Random x-coordinate within screen bounds
        y = random.randint(-280, 280)  # Random y-coordinate within screen bounds
        self.goto(x, y)  # Move the food to the new position

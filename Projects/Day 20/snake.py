from turtle import Turtle

# Constants for initial snake setup and movement
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions for the snake segments
MOVE_DISTANCE = 20  # Distance the snake moves per step
UP = 90             # Angle for upward movement
DOWN = 270          # Angle for downward movement
LEFT = 180          # Angle for leftward movement
RIGHT = 0           # Angle for rightward movement

class Snake:
    def __init__(self):
        """Initialize the snake with its segments and head."""
        self.segment = []  # List to hold all segments of the snake
        self.create_snake()  # Create the initial snake
        self.head = self.segment[0]  # Set the first segment as the head

    def create_snake(self):
        """Create the initial snake using the starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake at the specified position."""
        turtle = Turtle("square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)
        self.segment.append(turtle)

    def extend(self):
        """Extend the snake by adding a new segment at the tail's position."""
        self.add_segment(self.segment[-1].position())

    def move(self):
        """Move the snake forward by shifting each segment to the position of the one in front."""
        for move_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[move_num - 1].xcor()
            new_y = self.segment[move_num - 1].ycor()
            self.segment[move_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)  # Move the head forward

    def up(self):
        """Change the direction of the snake to up if not already moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the direction of the snake to down if not already moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the direction of the snake to left if not already moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the direction of the snake to right if not already moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

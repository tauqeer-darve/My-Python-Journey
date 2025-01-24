from turtle import Turtle

# Constants for scoreboard styling
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        """Initialize the scoreboard."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()  # Hide the turtle cursor
        self.goto(0, 265)  # Position the scoreboard at the top of the screen
        self.score = 0     # Initialize the score
        self.text = f"Score: {self.score}"
        self.write_text()

    def write_text(self):
        """Write the current score on the screen."""
        self.write(align=ALIGNMENT, arg=self.text, font=FONT)

    def game_over(self):
        """Display a game over message."""
        self.goto(0, 0)
        self.write(align=ALIGNMENT, arg="GAME OVER", font=FONT)
        self.goto(0, -30)
        self.write(align=ALIGNMENT, arg="Press 'Esc' to exit", font=("Courier", 12, "normal"))

    def update_score(self):
        """Update the score and refresh the scoreboard display."""
        self.clear()  # Clear the previous score
        self.score += 1  # Increment the score
        self.text = f"Score: {self.score}"
        self.write_text()

from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

# Initialize the screen for the game
screen = Screen()
screen.setup(height=600, width=600)  # Set up the screen dimensions
screen.title("Snake Xenzia")  # Title for the game window
screen.bgcolor("black")  # Background color of the game
screen.tracer(0)  # Turn off animation for smooth game updates

# Initialize the game components
snake = Snake()
food = Food()
score = ScoreBoard()

# Listen for user input to control the snake
screen.listen()
screen.onkey(snake.up, "Up")       # Move up when the "Up" arrow key is pressed
screen.onkey(snake.down, "Down")   # Move down when the "Down" arrow key is pressed
screen.onkey(snake.left, "Left")   # Move left when the "Left" arrow key is pressed
screen.onkey(snake.right, "Right") # Move right when the "Right" arrow key is pressed

def exit_game():
    """Exit the game by closing the screen."""
    screen.bye()

game_on = True

while game_on:
    screen.update()  # Update the screen for smooth animation
    time.sleep(0.10)  # Delay to control the speed of the game
    snake.move()      # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()          # Reposition the food to a new random location
        snake.extend()          # Add a new segment to the snake
        score.update_score()    # Update the score

    # Detect collision with walls
    if (
            snake.head.xcor() > 295 or
            snake.head.xcor() < -295 or
            snake.head.ycor() > 295 or
            snake.head.ycor() < -295
    ):
        score.game_over()       # Display the game over message
        game_on = False         # End the game loop

    # Detect collision with the tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()   # Display the game over message
            game_on = False     # End the game loop

# Exit the game with the "Escape" key
screen.onkey(exit_game, "Escape")
screen.mainloop()

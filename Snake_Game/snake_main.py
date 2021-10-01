# from tkinter.constants import OFF
from turtle import Turtle, Screen, forward, xcor
from snake_behaviour import Snake
from food import Food
from scoreboard import Scoreboard
import time

# main.py controls how the screen should behave and 
# how the snake should behave.

screen = Screen()


#setup my screen for the game
screen.bgcolor("black")
screen.title("PySnake Game")
screen.setup(width=600, height=600)
screen.tracer(0)
#create snake body


snake = Snake()
food = Food()
score = Scoreboard()
# on key listeners for moving the snake

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
   
    snake.snake_move()
    #segments --> === --> 3 segments
    #for seg_num in range(2, 0, -1)
    # so the idea is the coordinates of 2 will be from 1 and 1 from 0.
    

    # collision with food and generate new random food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_scoreboard()


    # Detect collision with wall
    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        score.game_over()
        game_is_on = False


    # Detect collision with tail
    # if the head collodes with any segment in the tail
    # then trigegr game over function.

    for segment in snake.segments[1:]:
        # to avoid the beginning when we start the game and
        #  head is the first segment
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False














screen.exitonclick()
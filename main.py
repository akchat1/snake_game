from turtle import Screen, Turtle
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -287 or snake.head.ycor() > 287:
        scoreboard.game_over()
        game_is_on = False
    if food.distance(snake.head) < 15:
        food.refresh()
        snake.extend_segment()
        scoreboard.increase_score()
    # Detect collision with tail
    # for segments in snake.snake:
        # if snake.head != segments and snake.head.distance(segments) < 10:
    for segments in snake.snake[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()

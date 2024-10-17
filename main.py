from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(key="Right", fun=snake.move_right)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)

game_on = True
while game_on is True:
    time.sleep(.1)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 16:
        food.refresh_food()
        snake.extend_snake()
        scoreboard.increase_score()
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

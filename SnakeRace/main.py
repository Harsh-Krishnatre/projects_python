import turtle
import random
import time
from snake import Snake
from food import Food
from score_board import Score


win = turtle.Screen()
win.bgcolor("black")
win.tracer(0)
win.screensize(600, 600)
game_is_on = True


snake = Snake()
food = Food()
score = Score()
win.listen()
win.onkey(snake.move_up, "Up")
win.onkey(snake.move_down, "Down")
win.onkey(snake.move_left, "Left")
win.onkey(snake.move_right, "Right")


while game_is_on:

    win.update()
    time.sleep(0.1)
    snake.snake_move()
    snake_x = snake.snake_head.xcor()
    snake_y = snake.snake_head.ycor()
    if snake.snake_head.distance(food) < 15:
        snake.extend()
        score.update()
        food.refresh()

    if (snake.snake_head.xcor() > 300 or snake.snake_head.ycor() > 300 or snake.snake_head.xcor() < -300
            or snake.snake_head.ycor() < -300):
        game_is_on = False
        score.game_over()

    for segment in snake.snake_body:
        if segment == snake.snake_head:
            continue
        elif snake.snake_head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


win.exitonclick()

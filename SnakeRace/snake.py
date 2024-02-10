import turtle
import time


START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_body = []
        self.snake_create()
        self.snake_head = self.snake_body[0]

    def snake_create(self):
        for snake_index in START_POS:
            self.add_segment(snake_index)

    def snake_move(self):
        for seg in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[seg-1].xcor()
            new_y = self.snake_body[seg-1].ycor()
            self.snake_body[seg].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.seth(LEFT)

    def move_right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.seth(RIGHT)

    def move_up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.seth(UP)

    def move_down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.seth(DOWN)

    def add_segment(self, snake_index):
        snake_part = turtle.Turtle(shape="square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.setpos(snake_index)
        self.snake_body.append(snake_part)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())


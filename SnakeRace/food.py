from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('blue')
        self.speed('fastest')
        rand_x = random.randrange(-210, 210, 10)
        rand_y = random.randrange(-210, 210, 10)
        self.goto(rand_x, rand_y)
        self.refresh()

    def refresh(self):
        new_x = random.randrange(-210, 210)
        new_y = random.randrange(-210, 210)
        self.goto(new_x, new_y)



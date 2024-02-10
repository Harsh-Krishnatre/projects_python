import turtle
from turtle import Turtle, Screen
from random import choice

l1 = [(235, 234, 232), (235, 232, 234), (184, 147, 94), (151, 104, 46), (228, 229, 231), (178, 150, 22), (83, 34, 27),
      (12, 57, 73), (31, 100, 120), (101, 41, 47)]

turtle.colormode(255)
nt = Turtle()
nt.pensize(15)
nt.setpos(-300,-300)
for i in range(10):
    for j in range(10):
        nt.penup()
        nt.setposition(j*30, i*30)
        nt.dot(10,choice(l1))
        nt.pendown()


main_screen = Screen()
main_screen.exitonclick()

"""008 - Turtle"""
import random as r
from turtle import Screen, Turtle


def reset_pos(x_pos=-150, y_pos=150):
    """Pen position reset"""
    timmy.penup()
    timmy.setposition(x_pos, y_pos)
    timmy.pendown()


timmy = Turtle()
screen = Screen()
reset_pos()


def dash_line():
    """Draw a Dash line"""
    # status = 1
    # def draw(status):
    #     if status == -1:
    #         timmy.pendown()
    #     else:
    #         timmy.penup()
    # for n in range(40):
    #     status = status * -1
    #     draw(status)
    #     timmy.forward(10)

    # Actually not over-engineered dash line loop...
    for _ in range(20):
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)


reset_pos()
dash_line()


def draw_shapes():
    """Draw a Triangle, square, pentagon, hex, hep, oct, mono and deca"""
    for shape in range(3, 11):
        timmy.pencolor(r.random(), r.random(), r.random())
        timmy.pensize(3)
        for _ in range(shape):
            timmy.forward(100)
            timmy.right(360 / shape)


reset_pos()
draw_shapes()


def random_walk():
    """Draw a Random Walk"""
    turn = [270, 0, 90]
    timmy.pensize(10)
    timmy.pencolor(r.random(), r.random(), r.random())
    timmy.right(r.choice(turn))
    timmy.forward(25)


reset_pos(0, 0)
for _ in range(100):
    random_walk()

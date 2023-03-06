"""008 - Turtle"""
from turtle import Screen, Turtle


def resetPos():
    timmy.penup()
    timmy.setposition(-150, 150)
    timmy.pendown()


timmy = Turtle()
screen = Screen()
resetPos()


"""Dash line"""
# status = 1
# def draw(status):
#     if status == -1:
#         timmy.pendown()
#     else:
#         timmy.penup()
# for n in range(20):
#     status = status * -1
#     draw(status)
#     timmy.forward(10)

# Actually not over-engineered dash line loop...
for _ in range(20):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

resetPos()

""" Triangle, square, pentagon, hex, hep, oct, mono and deca"""
for n in range(3, 11):
    for _ in range(n):
        v = float(n)
        timmy.pencolor(v / 15, v / 10, v / 12)
        timmy.forward(100)
        timmy.right(360 / n)

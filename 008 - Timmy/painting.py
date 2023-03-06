"""Painting, 6x6, dot size 20, 50 space"""
import random as r
from turtle import Screen, Turtle

RGB = [
    (29, 21, 60),
    (196, 129, 174),
    (61, 20, 58),
    (137, 69, 106),
    (178, 97, 136),
    (104, 39, 80),
    (78, 79, 114),
    (58, 49, 93),
    (236, 157, 191),
    (139, 148, 175),
    (111, 116, 159),
    (238, 202, 224),
]

draw = Turtle()
screen = Screen()
screen.colormode(255)
draw.penup()
draw.setpos(-100, -150)

for n in range(6):
    draw.setpos(-100, -150 + (50 * n))
    for _ in range(6):
        draw.dot(20, r.choice(RGB))
        draw.fd(50)

from turtle import Screen, Turtle

timmy = Turtle()

screen = Screen()

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

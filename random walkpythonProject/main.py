import turtle
from turtle import Turtle, Screen, colormode
import random
# color = ['#37AB65', '#3DF735', '#AD6D70', '#EC2504', '#8C0B90', '#C0E4FF', '#27B502', '#7C60A8', '#CF95D7']

turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


move = [90, 180, 270, 360]
ouss = Turtle()
ouss.hideturtle()
ouss.pensize(10)
ouss.speed(10)


for _ in range(100):

    ra = random.choice(move)
    ouss.color(random_color())
    ouss.right(ra)
    ouss.forward(20)




screen = Screen()
screen.exitonclick()


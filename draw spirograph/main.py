import turtle
from random import randint
from turtle import Turtle, Screen, colormode
turtle.colormode(255)
t = Turtle()
t.hideturtle()

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


t.speed("fastest")
def draw_spiro(gap):
    for _ in range(int(360/gap)):
        r = 100
        t.circle(r)
        # t.right(10)
        t.color(random_color())
        current_heading = t.heading()
        t.setheading(current_heading+gap)
draw_spiro(10)



screen = Screen()
screen.exitonclick()
from turtle import Turtle, Screen, colormode
from random import randint
turtle = colormode(255)

pen_s = 1
size = 1
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


pen = Turtle()
pen.pensize(1)
pen.turtlesize(1 )
def move_forwards():
    pen.forward(10)


def move_backwards():
    pen.backward(10)


def move_left():
    pen.left(45)


def move_right():
    pen.right(45)


def start_over():
    pen.reset()


def change_color():
    pen.color(random_color())


def size_plus():
    pen.pensize(size+1)


def size_mines():
    pen.pensize(size-1)

screen = Screen()
screen.listen()
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="c", fun=start_over)
screen.onkey(key="g", fun=change_color)
screen.onkey(key="=", fun=size_plus)
screen.onkey(key="-", fun=size_mines)

screen.exitonclick()
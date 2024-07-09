from turtle import Turtle, Screen
tim = Turtle()
color = ['#37AB65', '#3DF735', '#AD6D70', '#EC2504', '#8C0B90', '#C0E4FF', '#27B502', '#7C60A8', '#CF95D7', '#145JKH']
tim.shape("triangle")
tim.color("red")
# for _ in range (0,100):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)

# for _ in range(3):
#     tim.forward(40)
#     tim.left(360/3)
#
# for _ in range(4):
#     tim.color("green")
#     tim.forward(40)
#     tim.left(360/4)
#
# for _ in range(5):
#     tim.color("blue")
#     tim.forward(40)
#     tim.left(360/5)
#
# for _ in range(6):
#     tim.color("purple")
#     tim.forward(40)
#     tim.left(360/6)
#
# for _ in range(7):
#     tim.color("black")
#     tim.forward(40)
#     tim.left(360/7)
#
# for _ in range(8):
#     tim.color("yellow")
#     tim.forward(40)
#     tim.left(360/8)
#
# for _ in range(9):
#     tim.color("brown")
#     tim.forward(40)
#     tim.left(360/9)
n = 0
count = 3
while n <= 8:
    for _ in range(count):
        tim.color(color[n])
        tim.forward(100)
        tim.left(360 / count)
    n += 1
    count += 1

screen = Screen()
screen.exitonclick()


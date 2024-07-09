from turtle import Turtle, Screen, colormode
import random
# import colorgram
# color = colorgram.extract('hirst.jpg', 20)
# color_list = []
# for col in color:
#     r = col.rgb.r
#     g = col.rgb.g
#     b = col.rgb.b
#     color_list.append((r, g, b))
#     print(color_list)
turtle = colormode(255)
full_color = [(229, 222, 217), (230, 223, 228), (223, 221, 228), (218, 172, 126), (159, 180, 190), (132, 74, 55), (52, 102, 152), (117, 82, 93), (180, 143, 153), (160, 105, 150), (44, 48, 67), (128, 173, 115), (83, 95, 182), (66, 10, 29), (82, 133, 107), (227, 189, 144), (52, 63, 78), (192, 92, 74), (216, 225, 216), (114, 45, 59)]

dot = Turtle()
dot.penup()
dot.hideturtle()
dot.speed("fastest")
dot.setposition(-200.00, -200)
# dot.pensize(10)
i = 1
x_pos = 0
while i <= 10:
    for _ in range(10):
        # dot.color(random.choice(full_color))
        dot.dot(20,random.choice(full_color))
        dot.forward(50)
    x_pos += 50
    dot.setposition(-200.00, -200 + x_pos)
    i += 1






print(dot.position())
screen = Screen()
screen.exitonclick()


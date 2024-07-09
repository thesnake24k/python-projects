from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
snake = Turtle()
class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.snakes.append(snake)

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def reset(self):
        for seg in self.snakes:
            seg.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def extend(self):
        self.add_segment(self.snakes[-1].position())




    def move(self):
        for sn in range(len(self.snakes) - 1, 0, -1):
            newx = self.snakes[sn - 1].xcor()
            newy = self.snakes[sn - 1].ycor()
            self.snakes[sn].goto(newx, newy)
        self.snakes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)





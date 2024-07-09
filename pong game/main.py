from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import  Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong Game")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True
speed = 0.1
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.ball_move()
    # detect collusion with the ball
    if ball.ycor() > 280 or ball.ycor() < (-280):
        ball.y_bounce()
    # detect collusion with the paddle
    if (ball.distance(r_paddle.paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle.paddle) < 50 and
                                                                       ball.xcor() < -320):
        ball.x_bounce()
        speed *= 0.9
    # detect if the ball missed the right paddle
    if ball.xcor() > 380:
        speed = 0.1
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -380:
        speed = 0.1
        ball.reset_position()
        score.r_point()



screen.exitonclick()

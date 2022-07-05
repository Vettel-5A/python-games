from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
net = Turtle()
scoreboard = Scoreboard()
net.hideturtle()
net.pencolor("white")
net.penup()
net.goto(0, 300)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
net.setheading(270)
for x in range(12):
    net.pendown()
    net.forward(25)
    net.penup()
    net.forward(25)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
sleep = 0.1

while game_is_on:
    time.sleep(sleep)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) <= 50 and ball.xcor() >= 320 or ball.distance(l_paddle) <= 50 and ball.xcor() <= -320:
        ball.bounce_x()
        sleep = sleep * 0.9

    #Detect R paddle misses
    if ball.xcor() == 400:
        scoreboard.l_point()
        ball.center()
        sleep = 0.1

    #Detect L paddle misses:
    if ball.xcor() == -400:
        scoreboard.r_point()
        ball.center()
        sleep = 0.1


screen.exitonclick()
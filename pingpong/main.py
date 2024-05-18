from turtle import Turtle,Screen
from bat import Bat
from ball import Ball
import time
from scoreboard import Scoreboard
screen=Screen()
screen.setup(800,500)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Ping Pong")
# bat1=Turtle()
# bat1.shape("square")
# bat1.color("white")
# bat1.shapesize(5,1)
# bat1.penup()
# bat1.goto(350,0)
# def b1_moveup():
#     y=bat1.ycor()
#     y+=20
#     bat1.sety(y)
# def b1_movedown():
#     y=bat1.ycor()
#     y-=20
#     bat1.sety(y)
# bat2=Turtle()
# bat2.shape("square")
# bat2.color("white")
# bat2.shapesize(5,1)
# bat2.penup()
# bat2.goto(-350,0)
# def b2_moveup():
#     y=bat2.ycor()
#     y+=20
#     bat2.sety(y)
# def b2_movedown():
#     y=bat2.ycor()
#     y-=20
#     bat2.sety(y)
# screen.update()
l_bat=Bat(-350,0)
r_bat=Bat(350,0)

ball=Ball()
score=Scoreboard()
screen.update()
game_is_on=True
while game_is_on:
    ball.move()
    time.sleep(0.05)
    screen.listen()
    screen.onkey(r_bat.moveup,"Up")
    screen.onkey(r_bat.movedown,"Down")
    screen.onkey(l_bat.moveup,"w")
    screen.onkey(l_bat.movedown,"s")
    if ((ball.xcor()<-330) and(l_bat.distance(ball)<=50)) or ((ball.xcor()>330) and(r_bat.distance(ball)<=50)):
        ball.bat_bounce()
    if ball.xcor()<-350:
        # print("left miss")
        ball.reset()
        l_bat.reset()
        r_bat.reset()
        time.sleep(1.5)
        score.update_r_score()
    if ball.xcor()>350:
        # print("right miss")
        ball.reset()
        l_bat.reset()
        r_bat.reset()
        time.sleep(1.5)
        score.update_l_score()
        # print("point to left") 
    if score.l_score==10:
        score.game_over_A()
        game_is_on=False
    elif score.r_score==10:
        score.game_over_B()
        game_is_on=False












    screen.update()



screen.exitonclick()

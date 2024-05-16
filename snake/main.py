from turtle import Turtle,Screen
from snake import Snake
from food import Food
import time
import math
from scoreboard import Score
from wall import Wall


screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake=Snake()
food=Food()
# wall=Wall()
score=Score()
gameison=True
pause=False

while gameison:
    time.sleep(0.1)
    screen.update()
    snake.move()
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.extend,"e")
    x=(int(snake.bodies[0].xcor())-food.x_pos)
    y=(int(snake.bodies[0].ycor())-food.y_pos)
    distance=pow((pow(x,2)+pow(y,2)),1/2)
    if distance <15:
         snake.extend()
         food.update()
         score.update()
    if((snake.bodies[0].xcor()>=300) or (snake.bodies[0].xcor()<-300) or (snake.bodies[0].ycor()>=300) or (snake.bodies[0].ycor()<-300) ):
        score.game_over()
        # time.sleep(60)
        gameison=False
    for body in snake.bodies:
        if body.distance(snake.bodies[0])<10 and body is not snake.bodies[0]:
            score.game_over()
            gameison=False

    
    





screen.exitonclick()
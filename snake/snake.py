from turtle import Turtle
import time


class Snake:
    def __init__(self):
       self.bodies=[]
       self.create()
       self.head=self.bodies[0]
    def create(self):
        for i in range(3):
            body=Turtle()
            body.shape("square")
            body.color("white")
            body.penup()
            body.goto(-i*20,0)
            self.bodies.append(body)
    def move(self):
        for body_num in range(len(self.bodies)-1,0,-1):
            x=self.bodies[body_num-1].xcor()
            y=self.bodies[body_num-1].ycor()
            self.bodies[body_num].goto(x,y)
        self.bodies[0].forward(20)
    def extend(self):
        body=Turtle()
        body.shape("square")
        body.color("white")
        body.penup()
        body.goto(self.bodies[-1].xcor(),self.bodies[-1].ycor())
        self.bodies.append(body)
    def up(self):
        if self.bodies[0].heading()!=270:
            self.bodies[0].setheading(90)
    def down(self):
        if self.bodies[0].heading()!=90:
            self.bodies[0].setheading(270)
    def left(self):
        if self.bodies[0].heading()!=0:
            self.bodies[0].setheading(180)
    def right(self):
        if self.bodies[0].heading()!=180:
            self.bodies[0].setheading(0)
            
    def pause(self):
        self.bodies[0].forward(0)
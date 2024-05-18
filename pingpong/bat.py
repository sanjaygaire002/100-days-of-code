from turtle import Turtle
class Bat(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.initialposition=(x,y)
        self.goto(x,y)
    def moveup(self):
        y=self.ycor()
        if y<200:
            y+=40
            self.sety(y)
    def movedown(self):
        y=self.ycor()
        if y>-200:
            y-=40
            self.sety(y)
    def reset(self):
        self.goto(self.initialposition)
    
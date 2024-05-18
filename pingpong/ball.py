from turtle import Turtle
import random
A=[1,-1]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x=random.randint(6,18)
        self.y=random.randint(6,14)
        
    def move(self):
        if int(self.ycor())>=240 or int(self.ycor())<=-240:
           self.wall_bounce()
        x_cor=self.xcor()
        y_cor=self.ycor()
        self.goto(x_cor+self.x,y_cor+self.y)
        return self.x,self.y
    def wall_bounce(self):
        self.y=-self.y
    def bat_bounce(self):
        self.x=-self.x
    def reset(self):

        self.goto(0,0)
        self.x=random.randint(6,18)
        self.y=random.randint(6,14)
        C=random.choice(A)
        self.x=C*(self.x)
        self.y=C*self.y
        # print(C)
    
            
            
        
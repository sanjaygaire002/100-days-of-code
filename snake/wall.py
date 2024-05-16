from turtle import Turtle
class Wall:
    
    def __init__(self):
        self.width=600
        self.height=600
        self.wall=Turtle()
        self.draw()
        self.wall.color("red")
    def draw(self):
        self.wall.penup()
        self.wall.goto(-295,295)
        self.wall.pendown()
        self.wall.goto(295,295)
        self.wall.goto(295,-295)
        self.wall.goto(-295,-295)
        self.wall.penup()
        self.wall.goto(-293,293)
        self.wall.pendown()
        self.wall.goto(293,293)
        self.wall.goto(293,-293)
        self.wall.goto(-293,-293)
        
        
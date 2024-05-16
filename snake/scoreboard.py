from turtle import Turtle
SCORE=0
class Score:
    def __init__(self):
        self.score=Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.color("white")
        self.score.goto(0,270)
        self.score.write(f"Score:{SCORE}",align="center",font=("Arial",15,"normal"))
    def update(self):
        global SCORE
        SCORE+=1
        self.score.clear()
        self.score.write(f"Score:{SCORE}",align="center",font=("Arial",15,"normal"))
    def game_over(self):
        self.score.clear()
        self.score.goto(0,0)
        self.score.write(f"GAME OVER",align="center",font=("Arial",15,"normal"))
        self.score.goto(0,-40)
        self.score.write(f"Score:{SCORE}",align="center",font=("Arial",15,"normal"))
        
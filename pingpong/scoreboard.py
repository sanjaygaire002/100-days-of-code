


from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.goto(-300,180)
        self.write("Player: A ",font=("Courier",20,"normal"))
        self.goto(-300,160)
        self.write(f"Score: {self.l_score}",font=("Courier",20,"normal"))
        self.goto(100,180)
        self.write("Player: B",font=("Courier",20,"normal"))
        self.goto(100,160)
        self.write(f"Score: {self.r_score}",font=("Courier",20,"normal"))
    def update_l_score(self):
        self.clear()
        self.l_score+=1
        self.goto(-300,180)
        self.write("Player: A ",font=("Courier",20,"normal"))
        self.goto(-300,160)
        self.write(f"Score: {self.l_score}",font=("Courier",20,"normal"))
        self.goto(100,180)
        self.write("Player: B",font=("Courier",20,"normal"))
        self.goto(100,160)
        self.write(f"Score: {self.r_score}",font=("Courier",20,"normal"))
    def update_r_score(self):
        self.clear()
        self.r_score+=1
        self.goto(-300,180)
        self.write("Player: A ",font=("Courier",20,"normal"))
        self.goto(-300,160)
        self.write(f"Score: {self.l_score}",font=("Courier",20,"normal"))
        self.goto(100,180)
        self.write("Player: B",font=("Courier",20,"normal"))
        self.goto(100,160)
        self.write(f"Score: {self.r_score}",font=("Courier",20,"normal"))
    def game_over_A(self):
        self.clear()
        self.goto(-100,0)
        self.write("GAME OVER",font=("Courier",40,"normal"))
        self.goto(-100,-100)
        self.write("Winner is Player: A ",font=("Courier",20,"normal"))
    def game_over_B(self):
        self.clear()
        self.goto(-100,0)
        self.write("GAME OVER",font=("Courier",40,"normal"))
        self.goto(-100,-100)
        self.write("Winner is Player: B",font=("Courier",20,"normal"))
from turtle import Turtle
import random
food_pos=[-280,-240,-220,-200,-180,-160,-140,-120,-100,-80,-60,-40,-20,0,280,240,220,200,180,160,140,120,100,80,60,40,20]
# class Food:
#     def __init__(self):
#         self.create()
        
    
#     def create(self):
#         self.food=turtle.Turtle()
#         self.food.shape("circle")
#         self.food.color("red")
#         self.food.penup()
#         self.food.speed("fastest")
#         self.food.goto(random.choice(food_pos),random.choice(food_pos))
#     def update(self):
#         self.food.clear()
#         self.create()
#     # def positionx(self):
#     #     return self.food.xcor()
#     # def positiony(self):
#     #     return self.food.ycor()
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.x_pos=random.choice(food_pos)
        self.y_pos=random.choice(food_pos)
        self.goto(self.x_pos,self.y_pos)
         
    
    def update(self):
        self.x_pos=random.choice(food_pos)
        self.y_pos=random.choice(food_pos)
        self.goto(self.x_pos,self.y_pos)
        
        
    

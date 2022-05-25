from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        
        self.shapesize(stretch_wid= 0.5, stretch_len=0.5)
        self.speed(11)
        self.color('blue')
        self.penup()
        self.change()
    def change(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        
        self.goto(x,y)

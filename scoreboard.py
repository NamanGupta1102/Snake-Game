import turtle

class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0,290)
    def update(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}",align='center',font=("Arial",20,"normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.penup()
        self.color("red")
        self.write(f"GAME OVER",align='center',font=("Arial",20,"normal"))
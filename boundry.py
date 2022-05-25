import turtle
ln = 290
class Boundry(turtle.Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("White")
        self.penup()
        self.speed(10)
        self.goto(-ln,-ln)
        self.pendown()
        self.goto(ln,-ln)
        self.goto(ln,ln)
        self.goto(-ln,ln)
        self.goto(-ln,-ln)
        self.hideturtle()
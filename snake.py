import turtle
screen = turtle.Screen()
class Snake():
    def __init__(self) -> None:
        self.li = [turtle.Turtle(shape = 'square') for _ in range(3)]
        c =0
        for i in self.li:
            i.color('white')
            i.penup()
            i.goto(c,0)
            c-=20
        self.head = self.li[0]
        self.head.color("red")
    def move_fd(self):
        if self.li[0].heading() != 270:
            self.li[0].seth(90)
    def move_down(self):
        if self.li[0].heading() != 90:
            self.li[0].seth(270)
    def move_right(self):
        if self.li[0].heading() != 180:
            self.li[0].seth(0)
    def move_left(self):
        if self.li[0].heading() != 0:
            self.li[0].seth(180)
    def move(self):
    # screen.update()
    # time.sleep(0.2
        
        for i in range(len(self.li)-1,0,-1):
            x = self.li[i-1].position()
            self.li[i].goto(x)
            
        screen.onkey(key = 'w', fun = self.move_fd )
        screen.onkey(key = 'a', fun = self.move_left )
        screen.onkey(key = 'd', fun = self.move_right )
        screen.onkey(key = 's', fun = self.move_down )
        screen.onkey(key = 'Up', fun = self.move_fd )
        screen.onkey(key = 'Left', fun = self.move_left )
        screen.onkey(key = 'Right', fun = self.move_right )
        screen.onkey(key = 'Down', fun = self.move_down )
        self.li[0].fd(20)
    
    def add(self):
        t = turtle.Turtle(shape="square")
        t.penup()
        t.goto(self.li[-1].pos())
        t.color("White")
        
        self.li.append(t)
    
    def collide(self):
        for i in range(1,len(self.li)):
            if self.head.distance(self.li[i])<10:
                return True
        return False
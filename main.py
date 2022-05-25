import turtle
import scoreboard
import time
import boundry
import snake
import food
screen = turtle.Screen()
screen.setup(height=600,width=600)
screen.title('Snake Game')
screen.bgcolor('Black')
screen.tracer(0)
c=0
bound = boundry.Boundry()
obj = snake.Snake()
foo = food.Food()
screen.listen() 
game_on = True
score_game = scoreboard.ScoreBoard()

score_game.update()
while game_on:
    screen.update()
    time.sleep(0.1)
    obj.move()
    # turtle.write(f"Score: {score}",align="center")
    #collision
    
    if foo.distance(obj.li[0]) <15:
        score_game.update()
        foo.change()
        obj.add()
        screen.update()
    
    if obj.head.xcor()>280 or obj.head.xcor()<-280 or obj.head.ycor()>280 or obj.head.ycor()<-280:
        screen.update()
        score_game.game_over()
        game_on = False
    
    if obj.collide():
        screen.update()
        score_game.game_over()
        game_on = False

turtle.done()
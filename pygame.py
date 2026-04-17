import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0

#Paddle A and it's attributes
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1,stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350,0)
#Paddle B and it's attributes
paddle_b = turtle.Turtle()
paddle_a.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1,stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350,0)
#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=4
ball.dy=-4

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Function
def MoveUpA():
    y=paddle_a.ycor()
    y+=30
    paddle_a.sety(y)
def MoveDownA():
    y=paddle_a.ycor()
    y-=30
    paddle_a.sety(y)
def MoveUpB():
    y=paddle_b.ycor()
    y+=30
    paddle_b.sety(y)
def MoveDownB():
    y=paddle_b.ycor()
    y-=30
    paddle_b.sety(y)
def Stop():
    return True

#To make it move
wn.listen()
wn.onkeypress(MoveUpA,"w")
wn.onkeypress(MoveDownA,"s")
wn.onkeypress(MoveUpB,"Up")
wn.onkeypress(MoveDownB,"Down")


while True:
    

    wn.update()
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)

    if ball.ycor() > 290:
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        
    if (ball.xcor() > 340 and ball.xcor() < 360) and (ball.ycor() > paddle_b.ycor()-40 and ball.ycor()<paddle_b.ycor()+40):
        ball.setx(340)
        ball.dx *= -1 
    if (ball.xcor() < -340 and ball.xcor() > -360) and (ball.ycor() > paddle_a.ycor()-40 and ball.ycor()<paddle_a.ycor()+40):
        ball.setx(-340)
        ball.dx *= -1 
        
            

        

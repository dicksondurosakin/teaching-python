import turtle
import random

screen = turtle.Screen()
width = 500
height = 400
screen.setup(width, height)
paddles = []
bricks = []

x_position = -50
##for creating the paddle
for i in range(5):
    screen.tracer(0)
    paddle = turtle.Turtle("square")
    paddle.penup()
    paddle.color("black")
    paddle.goto(x_position, -180)
    x_position += 20
    paddles.append(paddle)
    screen.tracer(1)


## Function that moves the paddle to the right
def move_paddle_right():
    if paddles[0].xcor() <= 140:
        screen.tracer(0)
        for paddle in paddles:
            paddle.forward(20)
        screen.tracer(1)


## Function that moves the paddle to the left
def move_paddle_left():
    if paddles[2].xcor() >= -200:
        screen.tracer(0)
        for paddle in paddles:
            paddle.backward(20)
        screen.tracer(1)


## creating the bricks
x_position = -200
y_position = 160
screen.tracer(0)
for i in range(27):
    if i == 9:
        x_position = -200
        y_position = 120
    if i == 18:
        x_position = -200
        y_position = 80
    new_brick = turtle.Turtle("square")
    new_brick.penup()
    new_brick.shapesize(1, 2)
    new_brick.goto(x_position, y_position)
    x_position += 50
    bricks.append(new_brick)
screen.tracer(1)

## defining the ball
ball = turtle.Turtle()
ball.penup()
ball.color("cyan")
ball.shape("circle")
ball.shapesize(0.8)
ball.goto(-40,-160)
ball.left(90)
print(ball.heading())
    
screen.onkey(move_paddle_right, "Right")
screen.onkey(move_paddle_left, "Left")
screen.listen()

yplus = 1
xplus = 1
distance = 3
close = 20
game_on = True
random_number = random.randint(40,120)
while 100 - random_number > 0 and 100 - random_number < 16:
    random_number = random.randint(40,120)
##ball.setheading(45)

## Writing Turtle
turtle.hideturtle()
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()

## Game Starts 
while game_on:
    # If the ball hits bottom end the code
    if ball.ycor() <= -180:
        turtle.write("Game over",font=("Arial", 15, "normal"))
        break
    
    # If the ball hits the top bounce the ball back
    if ball.ycor() > 190 :
        yplus *= -1
        
    # If the ball hits the side bounce the ball back     
    if ball.xcor() >= 240 or ball.xcor() <= -240:
        xplus *= -1

    # If the ball hit the brick i want you to take the brick away 
    for i in bricks:
        if -close < ball.ycor() - i.ycor() < close and -close< ball.xcor() - i.xcor() < close:
            screen.tracer(0)
            i.goto(1000,1000)
            print(ball.heading())
            bricks.remove(i)
            screen.tracer(1)
            
    # If the ball touches the paddle I want it to bounce back
    for i in paddles:
        if i.distance(ball) <18:
            print("yes")
            yplus*= -1
            
    # Print game over when there is no more brick
    if len(bricks) == 0:
        turtle.write("Congratulations You win",font=("Arial", 15, "normal"))
        break
    ball.goto(ball.xcor()+xplus,ball.ycor()+yplus)
        
##screen.exitonclick()

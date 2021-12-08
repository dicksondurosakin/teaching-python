import turtle
import time

screen = turtle.Screen()
screen.setup(500, 400)
bricks = []


##for creating the paddle

screen.tracer(0)
paddle = turtle.Turtle("square")
paddle.penup()
paddle.color("black")
paddle.shapesize(1,3)
paddle.goto(0, -180)
screen.tracer(1)


## Function that moves the paddle to the right
def move_paddle_right():
    if paddle.xcor() <= 200:
        screen.tracer(0)
        paddle.forward(20)
        screen.tracer(1)


## Function that moves the paddle to the left
def move_paddle_left():
    if paddle.xcor() >= -200:
            paddle.backward(20)


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
ball.shapesize(0.7)
ball.goto(-10,-160)
ball.left(90)
print(ball.heading())
    
screen.onkey(move_paddle_right, "Right")
screen.onkey(move_paddle_left, "Left")
screen.listen()

count = 0
distance = 3
close = 20
game_on = True
ball.setheading(135)
while game_on:
    if ball.xcor()<=-240 or ball.xcor()>= 240:
        screen.tracer(0)
        heading = ball.heading()
        ball.setheading(180 - heading)
        screen.tracer(1)
    if ball.ycor()>=200:
        screen.tracer(0)
        heading = ball.heading()
        ball.setheading(-heading)
        screen.tracer(1)
    for i in bricks:
        if -close < ball.ycor() - i.ycor() < close and -close< ball.xcor() - i.xcor() < close:
            screen.tracer(0)
            i.goto(1000,1000)
            screen.tracer(1)
            heading = ball.heading()
            ball.setheading(-heading)
        if paddle.distance(ball) <= 25 and count > 10:
            screen.tracer(0)
            heading = ball.heading()
            ball.setheading(- heading)
            ball.forward(30)
            screen.tracer(1)

    if ball.ycor() <= -190:
        break
    count += 1
    ball.forward(distance)
        

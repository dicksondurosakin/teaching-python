import turtle
import random
import time

#constants
DISTANCE = 10
STARTING_X = 0
STARTING_Y = -280
SLEEP = 0.1
level = 1

# screen
screen = turtle.Screen()
screen.setup(700,600)

#crossing turtle
crossing_turtle = turtle.Turtle("turtle")
crossing_turtle.penup()
crossing_turtle.setheading(90)
##crossing_turtle.shapesize(stretch_wid=1, stretch_len=0.9, outline=1)
crossing_turtle.goto(STARTING_X,STARTING_Y)

#controling the turtle
def move_up():
    crossing_turtle.forward(10)
screen.onkey(move_up,"Up")
screen.listen()

#creating the cars
cars_list = []
y_positions = [*range(-243, 283,60)]
turtle.colormode(255)

# writing turtle
writing_turtle = turtle.Turtle()
writing_turtle.penup()
writing_turtle.hideturtle()
writing_turtle.goto(-300,260)
writing_turtle.write(f"Level {level}",font=("Yu Gothic",20,'normal'))

game_on  = True
while game_on:    
    screen.tracer(0)
    random_y = random.choice(y_positions)
    car_turtle = turtle.Turtle('square')
    car_turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    car_turtle.penup()
    car_turtle.shapesize(stretch_wid=1, stretch_len=2)
    car_turtle.setheading(180)
    car_turtle.goto(350,random_y)
    cars_list.append(car_turtle)
    for i in cars_list:        
        i.forward(DISTANCE)
        if i.xcor()<= -400:
            cars_list.remove(i)
        if crossing_turtle.distance(i) <= 20:
            game_on = False
    if crossing_turtle.ycor() >= 300:
        crossing_turtle.goto(STARTING_X,STARTING_Y)
        SLEEP *= 0.5
        level += 1
        writing_turtle.undo()
        writing_turtle.write(f"Level {level}",font=("Yu Gothic",20,'normal'))
        
        
    screen.tracer(1)
    time.sleep(SLEEP)



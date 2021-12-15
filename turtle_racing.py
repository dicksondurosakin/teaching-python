import turtle
import random

screen = turtle.Screen()
screen.setup(700, 500)
screen.bgcolor("cyan")
# list of colors for the turtle and list of turtles
colors = ["red","blue","black","orange","purple"]
turtles = []

#ask the use for his prediction

guess = turtle.textinput('PREDICTION','predict which color will win')

#set some global variables
winner = ''
x_axis = -300
y_axis = 130
track_x= -330
track_y=150

#draw the turtle tracks
screen.tracer(0)
for track in range(6):
    turtle.penup()
    turtle.goto(track_x,track_y)
    turtle.pendown()
    for lines in range(24):
        turtle.forward(20)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
    track_y -=48

## draw the finish line
turtle.penup()
turtle.goto(290,-90)
turtle.left(90)
turtle.pendown()
for i in range(6):
    turtle.forward(30)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
turtle.hideturtle()
screen.tracer(1)

#create the different turtles
for i in range(5):
    new_turtle = turtle.Turtle()
    new_turtle.shape('turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x_axis,y_axis)
    turtles.append(new_turtle)
    y_axis -= 50

#start the game
game_on = True
while game_on:
    for i in turtles:
        i.forward(random.randint(1,10))
        if i.xcor() >=270:
            winner = i.color()[1]
            game_on = False
            

#check if the user's guess is correct
turtle.hideturtle()
turtle.penup()
turtle.goto(-200,200)

if guess == winner:
    turtle.write(f"{winner} won, You are fit for a magician",font=("Arial", 15, "normal"))
else:
    turtle.write(f"{winner} is the winner, better luck next time",font=("Arial", 15, "normal"))


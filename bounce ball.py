import turtle

window = turtle.Screen()

# Starting parameters
MAX_X = 20
MAX_Y = 20
initial_angle = 5
speed = 1

# Create a turtle and name it Bob.
Bob = turtle.Turtle()
window.reset()
window.setworldcoordinates(-MAX_X,-MAX_Y,MAX_X,MAX_Y)
Bob.left(initial_angle)
#Bob.fd(51) No need for this
##Bob.speed(speed)
while True:
    xBob = Bob.xcor()
    yBob = Bob.ycor()
##    print(xBob,yBob)
    if abs(xBob) >= MAX_X: # Use abs() to capture both walls
        heading = Bob.heading()
##        print(heading)
        Bob.setheading(180 - heading)
    if abs(yBob) >= MAX_Y:
        heading = Bob.heading()
        print(-heading)
        Bob.setheading(-heading)
    Bob.fd(10)
window.exitonclick()

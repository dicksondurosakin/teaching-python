import random
import turtle


bg = turtle.Screen()
words = 'ant bat bear camel cat clam cobra \
                    crow deer dog duck eagle fox frog goat goose hawk\
                    lion mole moose mouse mule owl panda\
                    ram rat raven rhino seal shark sheep\
                    snake swan tiger toad \
                    whale wolf zebra'.split()
chosen_word = random.choice(words)
display='?'*len(chosen_word)
lives = 9
x_pos = -220

bg.tracer(0)
testing= turtle.Turtle()
testing.ht()
testing.penup()
bg.tracer(1)
def write_word(x_pos,chosen_word):
    for i in range(len(chosen_word)):
        testing.goto(x_pos,-150)
        testing.write(f"{display[i]}",font=("Yu Gothic",50,"bold"))
        x_pos+=100

def game_graphics(chosen_word,lives,x_pos,display):
    #draws the board
    def boards():
        bg.tracer(0)
        board = turtle.Turtle()
        board.st()
        board.fillcolor("Orange")
        board.begin_fill()
        board.pencolor("Orange")
        board.pu()
        board.goto(0, -100)
        board.shape("square")
        board.shapesize(stretch_len = 30, stretch_wid = 10)

        board_legsleft = turtle.Turtle()
        board_legsleft.fillcolor("Orange")
        board_legsleft.begin_fill()
        board_legsleft.pencolor("Orange")
        board_legsleft.pu()
        board_legsleft.goto(200, -250)
        board_legsleft.shape("square")
        board_legsleft.shapesize(stretch_len = 3, stretch_wid = 5)

        board_legsright = turtle.Turtle()
        board_legsright.fillcolor("Orange")
        board_legsright.begin_fill()
        board_legsright.pencolor("Orange")
        board_legsright.pu()
        board_legsright.goto(-200, -250)
        board_legsright.shape("square")
        board_legsright.shapesize(stretch_len = 3, stretch_wid = 5)

        question_board = turtle.Turtle()
        question_board.fillcolor("Aqua")
        question_board.begin_fill()
        question_board.pencolor("Aqua")
        question_board.pu()
        question_board.goto(0, -100)
        question_board.shape("square")
        question_board.shapesize(stretch_len = 29, stretch_wid = 9)
        bg.tracer(1)
    boards()


    # draws white square
    posx = -200
    posy = -100
    bg.tracer(0)
    for i in range(len(chosen_word)):
        question_box = turtle.Turtle()
        question_box.shape("square")
        question_box.color("White")
        question_box.pu()
        question_box.goto(posx ,posy)
        question_box.shapesize(stretch_len = 4, stretch_wid = 4)
        posx += 100
    bg.tracer(1)


    # writes the live
    bg.tracer(0)
    life = turtle.Turtle()
    life.pensize(4)
    life.color("White","red")
    life.begin_fill()
    life.lt(150)
    life.fd(180)
    life.circle(-90, 180)
    life.setheading(60)
    life.circle(-90, 180)
    life.fd(180)
    life.end_fill()
    life.hideturtle()
##    write 9
    text = turtle.Turtle()
    text.pu()
    text.ht()
    text.goto(-80, 70)
    text.write(lives, False, font = ("Arail", 100, "normal"))
    bg.tracer(1)
        
    # text on the board
    write_word(x_pos,chosen_word)

# Keep asking the user to input the word
while '?' in display:
    game_graphics(chosen_word,lives,x_pos,display)
    guess = turtle.textinput("LETTER", "Guess a letter or type exit to stop playing").lower()
    if guess == 'exit':
        break
    if guess not in chosen_word:
        lives -= 1
    for i in  range(len(chosen_word)):
        if chosen_word[i] == guess:
            display = display[:i]+guess+display[i+1:]
            bg.clear()
    if lives == 0:
        game_over = turtle.Turtle()
        game_over.ht()
        game_over.penup()
        game_over.goto(-200,0)
        game_over.write("GAME OVER", font=('Yu Gothic',18,'bold'))
        break
if '?' not in display:
        win_turtle = turtle.Turtle()
        win_turtle.ht()
        win_turtle.penup()
        win_turtle.goto(-200,0)
        win_turtle.write("YOU WIN", font=('Yu Gothic',18,'bold'))
game_graphics(chosen_word,lives,x_pos,display)


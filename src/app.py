import random as rd
import time
import turtle as t
from body import body
from tkinter import *

# --- screen ---
sc = t.Screen()
sc.title('Snake Game')
sc.bgcolor('blue')
sc.setup(width=600, height=600)
sc.tracer(0)
canvas = sc.getcanvas()

# --- head ---
head = body(shape='square', color='black')
head.goto(0, 0)
head.direction = 'stop'


# --- food ---
food = body(shape='circle', color='orange')
food.goto(0, 100)
food.speed(0)

# --- scoreboard ---
high_score = 0
score_board = body(shape='square', color='white')
score_board.speed(0)
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 250)
score_board.write(arg=f"Score: 0 High score {high_score}", align= "center", font=('Arial', 24, 'normal'))


# --- Set controls for moving snake ---
def up():
    if head.direction != 'down':
        head.direction = 'up'


def down():
    if head.direction != 'up':
        head.direction = 'down'


def left():
    if head.direction != 'right':
        head.direction = 'left'


def right():
    if head.direction != 'left':
        head.direction = 'right'


def move(direction):
    match direction:
        case 'up':
            head.sety(head.ycor() + 20)
        case 'down':
            head.sety(head.ycor() - 20)
        case 'left':
            head.setx(head.xcor() - 20)
        case 'right':
            head.setx(head.xcor() + 20)


sc.listen()
sc.onkeypress(up, 'w')
sc.onkeypress(down, 's')
sc.onkeypress(left, 'a')
sc.onkeypress(right, 'd')
# --- Main game ---
body_parts = [head]
continue_game = True
reset_game = True
score = 0
while continue_game:
    while reset_game:
        sc.update()
        time.sleep(0.2)

        # --- check if snake eat food ---

        if head.distance(food) < 20:
            food_xcor = rd.randint(-270, 270)
            food_ycor = rd.randint(-270, 270)
            food.goto(food_xcor, food_ycor)

            new_body = body(shape='square', color='white')
            new_body.speed(0)
            new_body.penup()
            body_parts.append(new_body)

            score += 10
            score_board.clear()
            score_board.write(arg=f"Score: {score} High score {high_score}", align="center", font=('Arial', 24, 'normal'))

        for index in range(len(body_parts) -1, 0, -1):
            xcor = body_parts[index -1].xcor()
            ycor = body_parts[index -1].ycor()
            body_parts[index].goto(xcor, ycor)

        # --- check if snake hit wall ---

        if head.ycor() > 270 or head.ycor() < -270 or head.xcor() > 270 or head.xcor() < -270:
            game_over = body(shape='square', color= 'white')
            game_over.speed(0)
            game_over.penup()
            game_over.goto(0, 0)
            game_over.hideturtle()
            game_over.write(arg="GAME OVER!!!", align="center", font=('Arial', 24, 'bold'))

            rest_game = False

        move(head.direction)

    yes_button = body(shape='square', color='red')
    yes_button.fillcolor('red')
    yes_button.penup()
    yes_button.write('No', align= "center", font=('Arial', 24, 'normal'))
    yes_button.goto(0, -50)



sc.exitonclick()
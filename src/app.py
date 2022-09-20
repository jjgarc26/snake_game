import random as rd
import time
import turtle as t
from body import body

# --- screen ---
sc = t.Screen()
sc.title('Snake Game')
sc.bgcolor('blue')
sc.setup(width=600, height=600)
sc.tracer(0)

# --- head ---
head = body(shape='square', color='black')
head.goto(0, 0)
head.direction = 'stop'


# --- food ---
food = body(shape='circle', color='orange')
food.goto(0, 100)
food.speed(0)


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
# ----------------------------------- Main game ---------------------------------
body_parts = [head]
continue_game = True
while continue_game:
    sc.update()
    time.sleep(0.2)
    # head.forward(20)

    # --- check if snake eat food ---

    if head.distance(food) < 20:
        food_xcor = rd.randint(-270, 270)
        food_ycor = rd.randint(-270, 270)
        food.goto(food_xcor, food_ycor)

        new_body = body(shape='square', color='white')
        new_body.speed(0)
        new_body.penup()
        body_parts.append(new_body)

    for index in range(len(body_parts) -1, 0, -1):
        xcor = body_parts[index -1].xcor()
        ycor = body_parts[index -1].ycor()
        body_parts[index].goto(xcor, ycor)



    move(head.direction)



    # --- check if snake hit wall ---


# expend snake body

sc.exitonclick()
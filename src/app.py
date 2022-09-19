import time
import turtle as t
from body import body
from moves import go_up, go_down, go_left, go_right


# --------------------------- Set screen and snake body ---------------------------
# --- screen ---
sc = t.Screen()
sc.title('Snake Game')
sc.bgcolor('blue')
sc.setup(width=600, height=600)
# sc.tracer(0)

# --- head ---
head = body(shape='square', color='black')
head.goto(0, 0)
head.direction = 'stop'


# --- food ---
food = body(shape='circle', color='orange')
food.goto(0, 100)
food.speed(0)


# --- Set controls for moving snake ---
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
sc.onkeypress(go_up, 'w')
sc.onkeypress(go_down, 's')
sc.onkeypress(go_left, 'a')
sc.onkeypress(go_right, 'd')
# ----------------------------------- Main game ---------------------------------

# expend snake body

sc.exitonclick()
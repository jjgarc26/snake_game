import time
import turtle as t
from snake_head import snake_head
from food import food

# --------------------------- Set screen and snake body ---------------------------
# --- screen ---
sc = t.Screen()
sc.title('Snake Game')
sc.bgcolor('blue')
sc.setup(width=600,height=600)

# --- head ---
head = snake_head(shape='square', color='black')
head.goto(0, 0)


# --- food ---
food = food(shape='circle', color='orange')
food.goto(0, 100)
food.speed(0)


# ------------------------- Set controls for moving snake -----------------------


# ----------------------------------- Main game ---------------------------------

# expend snake body

sc.exitonclick()
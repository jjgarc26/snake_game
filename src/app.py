import turtle as t
from food import create_food

from src.snake import Snake
from src.screen import Screen

# --------------------------- Set screen and snake body ---------------------------
screen = Screen()

head = Snake()
body = Snake()

# ------------------------- Set controls for moving snake -----------------------
screen.left_key(head)
screen.right_key(head)

head.body(0)
body.body(-10)

# ----------------------------------- Main game ---------------------------------
body_coo = [[30, 30], [20, 20]]
food = create_food(body_coo)
print(food)

for i in range(1000):
    head.move(15)
    position = head.position()
    body.follow(position[0], position[1])
continue_game = 'yes'

# while continue_game == 'yes':
#
#     pass

screen.exit_screen()
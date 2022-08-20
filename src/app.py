import turtle as t

from src.snake import Snake
from src.screen import Screen

# --------------------------- Set screen and snake body ---------------------------
screen = Screen()

head = Snake()
body = Snake()

# ------------------------- Set controls for moving snake -----------------------
screen.left(head)
screen.right(head)

head.body(0)
body.body(-10)

# ----------------------------------- Main game ---------------------------------
for i in range(1000):
    head.move(15)
    position = head.position()
    body.follow(position[0], position[1])
continue_game = 'yes'

# while continue_game == 'yes':
#
#     pass

screen.exit_screen()
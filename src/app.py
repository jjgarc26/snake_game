import turtle as t

from src.snake import Snake
from src.screen import Screen

screen = Screen()

head = Snake()
body = Snake()

head.body(0)
body.body(-20)
screen.left(head)

for i in range(100):
    head.move(1)
    position = head.position()
    body.follow(position[0] - 1, position[1] -1)
continue_game = 'yes'

# while continue_game == 'yes':
#
#     pass

screen.exit_screen()
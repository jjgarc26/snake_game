
def go_up(head):
    if head.direction != 'down':
        head.direction = 'down'


def go_down(head):
    if head.direction != 'up':
        head.direction = 'down'


def go_left(head):
    if head.direction != 'right':
        head.direction = 'left'


def go_right(head):
    if head.direction != 'left':
        head.direction = 'right'

import turtle
import turtle as t


class Screen:
    def __init__(self):
        self.screen = t.Screen()
        self.screen.setup(width=500, height=500)
        self.screen.bgcolor('black')
        self.screen.title('Snake Game')

    def left(self, turtle_moved):
        def move_left():
            turtle_moved.left(90)
        self.screen.onkey(move_left, 'a')
        self.screen.listen()

    def right(self, turtle_moved):
        def move_right():
            turtle_moved.right(90)
        self.screen.onkey(move_right, 'd')
        self.screen.listen()

    def exit_screen(self):
        self.screen.exitonclick()

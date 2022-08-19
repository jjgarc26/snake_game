import turtle as t


class Screen:
    def __init__(self):
        self.screen = t.Screen()
        self.screen.setup(width=500, height=500)
        self.screen.bgcolor('black')
        self.screen.title('Snake Game')

    def left(self, turtle):
        def move_left():
            turtle.left(90)
        self.screen.onkey(move_left, 'a')
        self.screen.listen()

    def exit_screen(self):
        self.screen.exitonclick()

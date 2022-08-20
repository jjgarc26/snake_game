import turtle as t


class Snake:
    def __init__(self):
        self.snake = t.Turtle()
        self.screen = t.Screen()

    def move(self, steps):
        self.snake.forward(steps)

    def body(self, position):
        self.snake.penup()
        self.snake.shape('square')
        self.snake.color('white')
        self.snake.goto(position, 0)
        self.snake.speed('fast')

    def follow(self, x,y):
        self.snake.setheading(self.snake.towards(x,y))
        self.snake.speed('fast')
        self.snake.forward(15)

    def position(self):
        x_pos = self.snake.xcor()
        y_pos = self.snake.ycor()
        return [x_pos, y_pos]

    def left(self, degrees):
        self.snake.left(degrees)

    def right(self, degrees):
        self.snake.right(degrees)


# we can use clone to add more blocks
# wall checker to check the boundries
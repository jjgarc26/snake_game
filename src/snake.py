import turtle as t


class Snake:
    def __init__(self):
        self.snake_head = t.Turtle()
        self.snake_body = t.Turtle()

    def move(self):
        pass

    def head(self, postion):
        self.snake_head.penup()
        self.snake_head.shape('square')
        self.snake_head.color('white')
        self.snake_head.setpos(postion, 0)

    def body(self, position):
        self.snake_head.penup()
        self.snake_body.shape('square')
        self.snake_body.color('white')
        self.snake_body.setpos(position, 0)

    def grow(self):
        pass

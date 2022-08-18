import turtle as t

from src.snake import Snake

screen = t.Screen()
screen.setup(width=500, height=500)
screen.bgcolor('black')
screen.title('Snake Game')

snake = Snake()
tail = Snake()

snake.head(0)
snake.body(-20)
tail.body(-40)


screen.exitonclick()
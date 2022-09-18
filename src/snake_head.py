import turtle as t


def snake_head(shape, color):
    head = t.Turtle()
    head.shape(shape)
    head.color(color)
    head.penup()
    return head

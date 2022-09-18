import turtle as t


def food(shape, color):
    fd = t.Turtle()
    fd.shape(shape)
    fd.color(color)
    fd.penup()
    return fd

import turtle as t


def body(shape, color):
    bd = t.Turtle()
    bd.shape(shape)
    bd.color(color)
    bd.penup()
    return bd

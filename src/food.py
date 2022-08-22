import random as rd
import turtle as t


def create_food(coordinates):
    position_x = 0
    position_y = 0

    create_new_coordinates = 'yes'

    while create_new_coordinates == 'yes':
        num_of_similar_coordinates = 0
        position_x = rd.randint(-100, 100)
        position_y = rd.randint(-100, 100)
        for coordinate in coordinates:
            if coordinate == [position_x, position_y]:
                num_of_similar_coordinates += 1
            else:
                continue

        if num_of_similar_coordinates > 0:
            continue
        else:
            create_new_coordinates = 'no'

    food = t.Turtle()
    food.hideturtle()
    food.penup()
    food.shape("circle")
    food.color("blue")
    food.setpos(position_x, position_y)
    food.showturtle()

    return [position_x, position_y]

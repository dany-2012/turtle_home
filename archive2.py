import turtle

t = turtle.Turtle()


def draw_square():

    for x in range(3):
        t.forward(100)
        t.left(90)

    t.forward(100)

def draw_circle():

    t.forward(50)

    for x in range(360):
        t.left(1)
        t.forward(1)


def draw_triangle():
    t.right(45)
    t.forward(73)
    t.right(90)
    t.forward(73)
    t.right(135)
    t.forward(100)


#draw_square()
#draw_triangle()

def draw_hexagon():
    t.left(45)
    t.forward(125)
    t.left(45)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(45)
    t.forward(50)
    t.left(45)
    t.forward(50)
    t.left(90)
    t.forward(50)

#draw_hexagon()

#draw_circle()


while True:# это цикл повторять всегда из scratch
    input_figure = input('введите фигуру, которую хотите чтобы нарисовала черепашка: ')
    if input_figure == "квадрат":
        draw_square()

    elif input_figure == "круг":
        draw_circle()

    elif input_figure == "треугольник":
        draw_triangle()

    elif input_figure == "шестиугольник":
        draw_hexagon()

    else:
        print("этой фигуры нет в прашрамме")




















































turtle.done()




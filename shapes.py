def draw_sun(pen, x, y, size):
    pen.setheading(0)  # повернуться в направлении
    pen.fillcolor("yellow")  # установить цвет заливки
    pen.penup()  # поднять черепашку
    pen.goto(x, y)  # перейти в х у
    pen.pendown()  # опускаем ручку
    pen.begin_fill()  # начинаем заливку
    pen.circle(size)  # нарисуй круг
    pen.end_fill()  # закончить заливку


def draw_bush(pen, x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor("green")
    pen.color('green')
    for x in range(10):
        pen.begin_fill()
        pen.circle(size)
        pen.end_fill()
        pen.left(45)


def draw_cloud(pen, x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor("white")
    pen.color('blue')
    for x in range(10):
        pen.begin_fill()
        pen.circle(size)
        pen.end_fill()
        pen.left(45)


def draw_trapezoid(pen, x, y, size):
    pen.setheading(90)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color('black')
    pen.fillcolor("brown")
    pen.begin_fill()
    pen.right(15)
    pen.forward(200)
    pen.right(75)
    pen.forward(50)
    pen.right(75)
    pen.forward(200)
    pen.right(105)
    pen.forward(150)
    pen.end_fill()


def draw_house_foundation(pen, x, y, size):
    pen.setheading(90)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color('black')
    pen.fillcolor("#9E6868")
    pen.begin_fill()

    for x in range(3):
        pen.forward(size)
        pen.left(90)

    pen.forward(size)
    pen.left(90)
    pen.forward(size)
    pen.end_fill()


def draw_roof(pen, x, y, size):
    pen.color('black')
    pen.fillcolor("#FF002B")
    pen.begin_fill()
    pen.left(45)
    pen.forward(size)
    pen.left(90)
    pen.forward(size)
    pen.end_fill()


def draw_earth(pen, x, y, size):
    pen.setheading(90)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color('black')
    pen.fillcolor("#4E2D2D")
    pen.begin_fill()
    pen.right(90)
    pen.forward(1000)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(1000)
    pen.right(90)
    pen.forward(100)
    pen.end_fill()


def draw_window_circle(pen, x, y, size):
    pen.setheading(90)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color('black')
    pen.fillcolor("#6F7C2D")
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()


def draw_window_square(pen, x, y, size):
    pen.setheading(90)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color('black')
    pen.fillcolor("#3F899B")
    pen.begin_fill()
    pen.forward(size)
    pen.right(90)
    pen.forward(size)
    pen.right(90)
    pen.forward(size)
    pen.right(90)
    pen.forward(size)
    pen.end_fill()
    pen.penup()



def draw_board(pen):
    pen.setheading(90)
    pen.penup()
    pen.pendown()
    pen.color('black')
    pen.fillcolor("#8E6943")
    pen.begin_fill()
    pen.forward(100)
    pen.right(45)
    pen.forward(20)
    pen.right(90)
    pen.forward(20)
    pen.right(45)
    pen.forward(100)
    pen.right(90)
    pen.forward(30)
    pen.end_fill()
    pen.penup()


def draw_fence(pen, x, y):
    pen.goto(x, y)
    pen.pendown()
    for i in range(30):
        draw_board(pen)
        pen.right(180)
        pen.forward(30)

def draw_door(pen, x, y):
    pen.setheading(90)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color('black')
    pen.fillcolor("#9A6565")
    pen.begin_fill()
    pen.forward(50)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(35)


import turtle

from shapes import *

t = turtle.Turtle()
t.speed(1000000000000000000000)

draw_sun(t, -300, 220, 50)
draw_bush(t, -148, -22, 20)
draw_cloud(t, 137, 220, 35)
draw_trapezoid(t, -80, -315, 20)
draw_house_foundation(t, 65, -125, 150)
draw_roof(t,0, 70, 108)
draw_earth(t, -400, -240, 100)
draw_window_circle(t, 0, 60, 15)
draw_window_square(t, 0,  -15, 32)
#draw_board(t, 150, 200)
draw_fence(t, -400, -240)
draw_door(t, -20, -125)

turtle.done()


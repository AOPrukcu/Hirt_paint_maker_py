import turtle
import random

rgb =[(246, 244, 243), (234, 239, 246), (240, 245, 243), (246, 239, 242), (132, 166, 204), (220, 148, 108), (197, 135, 148), (32, 41, 61), (163, 59, 49), (41, 106, 155), (141, 183, 162), (237, 211, 92), (148, 61, 68), (214, 83, 72), (35, 61, 56), (52, 111, 91), (170, 29, 33), (158, 33, 30), (234, 167, 158), (17, 97, 71), (52, 44, 48), (230, 161, 165), (171, 188, 220), (58, 52, 49), (184, 103, 113), (32, 60, 108), (107, 127, 159), (175, 200, 188), (35, 150, 209), (66, 66, 56)]
turtle.colormode(255)

tim = turtle.Turtle()
tim.shape("arrow")

tim.pensize(20)
tim.setheading(225)
tim.color("white")
tim.forward(250)
tim.setheading(0)

def painting(width):
    for i in range(width):
        for i in range(width):
            tim.color(random.choice(rgb))
            tim.forward(0)
            tim.penup()
            tim.forward(50)
            tim.pendown()
        tim.penup()
        tim.back(500)
        tim.left(90)
        tim.forward(50)
        tim.right(90)
        tim.pendown()


painting(10)



screen =turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
screen.exitonclick()

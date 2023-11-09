from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
screen.bgcolor("black")

tim = Turtle()
tim.shape("turtle")
tim.pensize(1)
tim.speed("fastest")

color_list = [
    (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
    (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85),
    (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36),
    (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79),
    (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186),
    (172, 153, 159), (212, 183, 177), (176, 198, 203)
]

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.pendown()

circle_radius = 20
number_of_dots = 25

# Hide the turtle and set pen color to white
tim.hideturtle()
tim.pencolor("white")

for dot_count in range(number_of_dots):
    tim.fillcolor(random.choice(color_list))
    tim.begin_fill()
    tim.circle(circle_radius)
    tim.end_fill()
    tim.penup()
    tim.forward(50)
    tim.pendown()
    if (dot_count + 1) % 5 == 0:
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(250)
        tim.setheading(0)
        tim.pendown()

screen.exitonclick()

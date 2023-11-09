from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.penup()
tim.goto(0, -100)
tim.pendown()

screen = Screen()
screen.bgcolor("black")
screen.colormode(255)

tim.pensize(1)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen.exitonclick()

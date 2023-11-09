from turtle import Turtle , Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.home()

Screen = Screen()
Screen.bgcolor("black")

colors = ["Green","Blue","Yellow","Cyan","Orange","Red","White"]

tim.pensize(1)
tim.speed("fastest")

def draw_s(sg):
    for _ in range(int(360 / sg)):
        tim.color(random.choice(colors))
        tim.circle(100)
        tim.fd(sg)
        tim.rt(5)

draw_s(5)
    
Screen.exitonclick()

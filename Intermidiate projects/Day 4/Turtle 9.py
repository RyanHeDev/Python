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
tim.color(random.choice(colors))


for _ in range(360):
    tim.position()
    tim.circle(100)
    tim.fd(5)
    tim.rt(5)

    
    
Screen.exitonclick()

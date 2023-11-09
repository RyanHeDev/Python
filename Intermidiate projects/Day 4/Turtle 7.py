from turtle import Turtle , Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.home()

Screen = Screen()
Screen.bgcolor("black")

colors = ["Green","Blue","Yellow","Cyan","Orange","Red","White"]

tim.pensize("15")
tim.speed("fastest")
directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random.choice(colors))
    tim.fd(30)
    tim.setheading(random.choice(directions))


    
    
Screen.exitonclick()

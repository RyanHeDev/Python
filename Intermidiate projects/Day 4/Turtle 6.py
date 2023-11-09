from turtle import Turtle , Screen
import random

tim = Turtle()
tim.shape("turtle")

Screen = Screen()
Screen.bgcolor("black")

colors = ["Green","Blue","Yellow","Cyan","Orange"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
        
for shape_side_n in range(3, 10):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
    
    
    
    
Screen.exitonclick()

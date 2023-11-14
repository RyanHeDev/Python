import turtle 
import random

turtle.shape("turtle")
turtle.color("cyan")
turtle.speed(0)
turtle.bgcolor("black")

colors = ["blue","cyan","lime","green","orange","red"]
for i in range(0, 8):
    turtle.fd(100)
    turtle.color(random.choice(colors))
    turtle.rt(45)

turtle.exitonclick()

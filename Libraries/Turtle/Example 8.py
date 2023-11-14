import turtle 
import random

lines = random.randint(5, 20)

turtle.shape("turtle")
turtle.color("cyan")
turtle.speed(0)
turtle.bgcolor("black")

for i in range(0, lines):
    lenght = random.randint(25, 100)
    rotate = random.randint(1, 365)
    turtle.fd(lenght)
    turtle.rt(rotate)

turtle.exitonclick()

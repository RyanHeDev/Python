from turtle import Turtle , Screen

tim = Turtle()
tim.shape("turtle")

Screen = Screen()
Screen.bgcolor("black")

for _ in range(4):
    tim.color("cyan")
    tim.fd(100)
    tim.rt(90)

for _ in range(5):
    tim.color("green")
    tim.fd(100)
    tim.rt(72)










Screen.exitonclick()

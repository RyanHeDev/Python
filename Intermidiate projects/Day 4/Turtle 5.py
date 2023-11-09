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


for _ in range(6):
    tim.color("yellow")
    tim.fd(100)
    tim.rt(60)


for _ in range(8):
    tim.color("orange")
    tim.fd(100)
    tim.rt(45)
    
for _ in range(9):
    tim.color("red")
    tim.fd(100)
    tim.rt(40)
    





Screen.exitonclick()

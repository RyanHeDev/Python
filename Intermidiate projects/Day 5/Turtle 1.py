from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("black", "cyan")
screen = Screen()
screen.bgcolor("black")

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()

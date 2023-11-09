from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("black", "cyan")
screen = Screen()
screen.bgcolor("black")

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.forward(-10)


def turn_right():
    tim.rt(10)
    

def turn_left():
    tim.lt(10)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_right)
screen.onkey(key="d", fun=turn_left)
Screen.onkey(key="c",fun=clear())



screen.exitonclick()

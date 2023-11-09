from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.bgcolor("black")
tim.color("cyan")

def move_forwards(x, y):
    tim.setheading(tim.towards(x, y))
    tim.forward(10)

def move_backwards(x, y):
    tim.setheading(tim.towards(x, y) + 180)
    tim.forward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def clear():
    tim.clear()

screen.onclick(move_forwards)
screen.onclick(move_backwards, btn=2)
#screen.onkey(turn_right, "a")
#screen.onkey(turn_left, "d")
#screen.onkey(clear, "c")

screen.listen()
screen.mainloop()

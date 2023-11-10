from turtle import Screen, Turtle

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# creating a Snake body

x_positions = [-20, -40]
for square_index in range(0, 2):
  snake = Turtle()
  snake.penup()
  snake.color("white")
  snake.shape("square")
  snake.clone()
  snake.goto(x=x_positions[square_index],y=0)








screen.exitonclick()


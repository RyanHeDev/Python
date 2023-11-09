# Turtle race

from turtle import Turtle, Screen
import random


is_race_on = False


screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your choice",prompt="Which turtle win the race? Enter a color: ")

colors = ["red","lime","cyan","yellow"]
y_positions = [-40, -10, 20, 50]
all_turtles = []


for turtle_index in range(0, 4):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
    
    

if user_choice:
    is_race_on = True


while is_race_on:
   for turtle in all_turtles:
       if turtle.xcor() > 230:
           is_race_on = False
           winning_color = turtle.pencolor()
           if winning_color == user_choice:
               print(f"You've won! The {winning_color} turtle is the winner!")
           else:
              print(f"You've lost! The {winning_color} turtle is the winner!")
       random_distance = random.randint(0,10)
       turtle.forward(random_distance)

screen.exitonclick()

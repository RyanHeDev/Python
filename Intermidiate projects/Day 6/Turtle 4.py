from turtle import Screen, Turtle
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# creating a Snake body
starting_positions = [(0,0), (-20,0), (-40,0)]  # Starting positions for the snake segments

segments = []  # List to store the turtle segments

# Create turtle segments for each starting position
for position in starting_positions:
    new_segment = Turtle("square")  # Create a new turtle segment with a square shape
    new_segment.color("white")  # Set the color of the segment to white
    new_segment.penup()  # Lift the pen up, so it doesn't draw while moving
    new_segment.goto(position)  # Move the turtle segment to the specified position
    segments.append(new_segment)  # Add the turtle segment to the segments list

game_is_on = True  # Variable to control the game loop

while game_is_on:
    screen.update()  # Update the screen to show any changes
    time.sleep(0.1)  # Introduce a 0.1-second delay between each iteration of the game loop

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()  # Get the x-coordinate of the previous segment
        new_y = segments[seg_num - 1].ycor()  # Get the y-coordinate of the previous segment
        segments[seg_num].goto(new_x, new_y)  # Move the current segment to the new position

    # Move the first segment forward by 20 units
    segments[0].forward(20)

screen.exitonclick()  # Exit the program when the user clicks on the screen

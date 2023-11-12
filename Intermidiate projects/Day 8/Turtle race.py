import turtle
import time
import random

# constant values
WIDTH, HEIGHT = 500, 500
COLORS = ["red", "orange", "yellow", "cyan", "blue", "pink", "white", "brown", "purple", "green"]

# function for number of racers
def get_number_of_racers():
    racers = 0
    while True:
        racers = turtle.textinput("Number of Racers", "Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try again!")
            # continue goes back to the start of the while loop.
            continue
            
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number is not in range 2-10 ... Try again!")


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    # enumerate gives the index and value 
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        # set position
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2  + 20)
        racer.pendown()
        turtles.append(racer)
       
    return turtles
    

def race(colors):
    turtles = create_turtles(colors)

    # Countdown
    countdown = 3
    countdown_turtle = turtle.Turtle()
    countdown_turtle.color("white")
    countdown_turtle.penup()
    countdown_turtle.goto(0, 0)
    countdown_turtle.hideturtle()
    countdown_turtle.write("Get Ready!", align="center", font=("Arial", 16, "bold"))
    time.sleep(2)
    countdown_turtle.clear()

    while countdown > 0:
        countdown_turtle.write(str(countdown), align="center", font=("Arial", 32, "bold"))
        countdown -= 1
        time.sleep(1)
        countdown_turtle.clear()

    countdown_turtle.write("Go!", align="center", font=("Arial", 32, "bold"))
    time.sleep(1)
    countdown_turtle.clear()

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.fd(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
                


def init_turtle():
    # turtle screen setup
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race Game")
    screen.bgcolor("black")


# Call the function to get the number of racers
racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)

# make this print as a GUI printing the winner
turtle.penup()
turtle.goto(0, 0)
turtle.color("white")
turtle.write(f"The winner is: {winner}", align="center", font=("Arial", 16, "bold"))
turtle.done()

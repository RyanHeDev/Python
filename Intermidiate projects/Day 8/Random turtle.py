import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.color("cyan")
turtle.shape("turtle")
turtle.speed(0)


    
for i in range(12):
    for colors in ["red","orange","yellow","green","cyan","blue"]:
        turtle.color(colors)
        turtle.circle(150)
        turtle.lt(5)
    

turtle.exitonclick()

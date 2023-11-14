import turtle 

turtle.shape("turtle")
turtle.color("cyan")
turtle.speed(0)
turtle.bgcolor("black")

for i in range(0, 10):
    for y in range(0, 8):
        
        turtle.fd(50)
        turtle.rt(45)
    turtle.rt(36)
turtle.exitonclick()

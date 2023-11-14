import turtle 

turtle.shape("turtle")
turtle.color("cyan")
turtle.speed(0)
turtle.bgcolor("black")

for i in range(1):
    turtle.rt(90)
    turtle.fd(200)

turtle.penup()
for i in range(1):
    turtle.lt(90)
    turtle.fd(100)
    turtle.pendown()
    turtle.fd(100)
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    turtle.lt(90)
    turtle.fd(100)
    turtle.rt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(100)
    turtle.lt(90)
    turtle.fd(100)
    
turtle.exitonclick()    

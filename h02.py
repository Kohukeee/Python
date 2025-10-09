import turtle

#kilpkonna seaded
turtle.speed(0)
ekraan = turtle.Screen()
ekraan.title("Olümpiarõngad - Henry")
ekraan.setup(500,400)


#olümpiarõngad
turtle.penup()
turtle.goto(-110,0)
turtle.pendown()
turtle.pencolor("blue")
turtle.pensize(6)
turtle.circle(50)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.pencolor("black")
turtle.circle(50)

turtle.penup()
turtle.goto(110,0)
turtle.pendown()
turtle.pencolor("red")
turtle.circle(50)

turtle.penup()
turtle.goto(-55,-45)
turtle.pendown()
turtle.pencolor("yellow")
turtle.circle(50)

turtle.penup()
turtle.goto(55,-45)
turtle.pendown()
turtle.pencolor("green")
turtle.circle(50)


turtle.done()

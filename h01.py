import turtle

#see on ruut
for i in range(4): #tsükkel 4x
    turtle.fd(150)
    turtle.left(90)

turtle.penup() #tõstab pliiatsi üles
turtle.goto(-400,200) #muudab positsiooni
turtle.pendown() #laseb pliiatsi alla

#see on kolmnurk
for i in range(3):
    turtle.fd(150)
    turtle.left(120)
    
turtle.penup()
turtle.goto(-400,-100)
turtle.pendown()

turtle.rt(90)
turtle.fd(100)
turtle.bk(50)
turtle.lt(90)
turtle.fd(50)
turtle.rt(90)
turtle.fd(50)
turtle.bk(100)
turtle.lt(90)
turtle.penup()
turtle.fd(30)
turtle.pendown()
turtle.rt(90)
turtle.fd(100)
turtle.bk(50)
turtle.lt(135)
turtle.goto(-270,-100)
turtle.rt(135)
turtle.penup()
turtle.fd(100)
turtle.pendown()
turtle.goto(-320,-150)





    




turtle.done()
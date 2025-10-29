import turtle as t #Jah, see tuli gpt abist, aga nii tundub lihtsam ja mõistlikum kui kirjutada t=turtle.turtle

print("Kujundi joonistamine.")

kulg = 100
alguspunkt = 0, 0

t.penup()
t.goto(alguspunkt)
t.pendown()                 #Alguspunkt kirja, et pärast tippusid lihtsam joonsitada oleks.

tipud = []                  #Et koguks tippude koordinaadid.

for i in range(6):
    t.forward(kulg)
    tipud.append(t.pos())   #Et salvestaks tippude koordinaadid.
    t.left(60)              #Kuusnurk joonistatud.

t.penup()
t.goto(alguspunkt)
t.left(60)
t.forward(kulg)
keskpunkt = t.pos()
t.pendown()                 #Liigutame turtle keskele.

for a in tipud:
    t.goto(a)
    t.goto(keskpunkt)       #Joonistame jooned keskelt tippu.

t.done

                            #AI on täitsa lollakas, pidi ikka ise mõtlema. :D

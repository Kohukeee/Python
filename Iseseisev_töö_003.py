import turtle as t
import random   

# Kilpkonn
# Kirjutada programm, mis lubab kasutajal valida kujundite tüübi 
# (viisnurk, ring, ruut või suvaline) ja arvu. 
# Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, 
# kui valik on “suvaline”, valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.

# Kõik kujundite joonistamise käsud peavad olema kirjutatud eraldi funktsioonidesse. 
# Näiteks funktsioon joonista_ruut() või joonista_viisnurk(). 
# Pärast joonistamist peab programm pakkuma võimalust sisestada uued väärtused või väljuda programmist, jättes sisendi tühjaks.

# Näiteks:
# Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5
# [Joonistab 5 kujundit, igaüks juhuslikult valitud tüübiga suvalistesse kohtadesse]
# Soovid jätkata?

def ruut(): 
    for i in range(4):
        t.forward(100)
        t.right(90)

def viisnurk():
    for i in range(5):
        t.forward(100)
        t.left(72)

def ring():
    t.circle(50)

def suvaline():
        random.choice([ruut, viisnurk, ring])()

def joonista_kujund(valik):
    if valik == "ruut":
        ruut()
    elif valik == "viisnurk":
        viisnurk()
    elif valik == "ring":
        ring()
    elif valik == "suvaline":
        random.choice([ruut, viisnurk, ring])()

while True:
    valik = input("Mida soovid joonistada?\n1. Ruut\n2. Viisnurk\n3. Ring\n4. Suvaline\nVastus tekstina, lõpetamiseks jäta tühjaks: ")
    if valik == "":
        print("Lõpetame programmi!")
        break 

    kogus = int(input("Mitu kujundit soovid joonistada:"))

    for a in range(kogus):
        t.penup()
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        t.goto(x, y)
        t.pendown()
        
        joonista_kujund(valik)

    edasi = input("Soovid joonistada järgmise kujundi?\nJah\nEi\nVastus: ")
    if edasi == "ei":
        print("Lõpetame programmi!")
        break

t.done()
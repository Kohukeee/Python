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



def joonista_ruut(): 
    for i in range(4):
        t.forward(75)
        t.right(90)

def joonista_viisnurk():
    for i in range(5):
        t.forward(75)
        t.right(72)

def joonista_ring():
    t.circle(75)

def joonista_kujund(valik):
    if valik == "ruut":
        joonista_ruut()
    elif valik == "viisnurk":
        joonista_viisnurk()
    elif valik == "ring":
        joonista_ring()
    elif valik == "suvaline":
        random.choice([joonista_ruut, joonista_viisnurk, joonista_ring])()
    else:
        print("Midagi on mäda!")

kujund = input("Mida soovid joonistada?\n1. Ruut\n2. Viisnurk\n3. Ring\n4. Suvaline kujund")
kogus = int(input("Mitu kujundit soovid joonistada:"))

for e in range(kogus):
    if joonista_kujund == "suvaline":
        valik = random.choice([joonista_ruut, joonista_viisnurk, joonista_ring])
    else:
        joonista_kujund(kujund)





t.done

        



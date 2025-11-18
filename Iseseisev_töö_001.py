import random

# Iseseisev töö 001
# 
#  1. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
# 	kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# 	eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
# 	kood mis teavitab paaris või paaritust arvust - 1p
# 	kuvatakse programmi pealkiri - 1p
# 	kood kommenteeritud - 1p

# HARJUTUS 1 ALGUS

# küsimus = print("Kas see on paaris või paaritu arv?")
# kasutaja_arv = (input("Sisesta arv: "))

# try:
#     kasutaja_arv = int(kasutaja_arv)
#     print("Vaatame, kas paaris või paaritu arv.")
#     if kasutaja_arv <= 0:
#         print("Palun sisesta korrektne arv, mis oleks positiivne täisarv.")
#     elif kasutaja_arv % 2 == 0:
#         print("Arv on paaris!")
#     else:
#         print("Arv on paaritu!")
# except:
#     print("Sisestus peab olema number!")

# HARJUTUS 1 LÕPP


	
# 2. Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või EEK->EUR.
# 	kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# 	kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
# 	küsitakse valuuta kogust ja tehakse arvutused - 2p
# 	kood kommenteeritud - 1p



# Harjutus 2 algus

print("Eurokalkulaator")
kurss = 15.6466
try:

    valik = int(input("Millist valuutat soovite konverteerida?\n1. EUR -> EEK\n2. EEK -> EUR\nSisesta vastus: \n"))
    summa = int(input("Vali summa: "))

    if valik == 1:
        summa = int(summa) * kurss
        print(summa, "EEK")
    elif valik == 2:
        summa = int(summa) // kurss
        print(summa, "EUR")
    else:
        print("Valik peab olema 1 või 2, muudel juhtudel pole hetkel midagi arvutada. :)")
except:
    print("Programm läks katki!")
        
# # Harjutus 2 lõpp            

# 3. Täringud
# 	kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
# 	kasutaja võistleb kahe täringuga arvuti vastu - 1p
# 	kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
# 	kood kommenteeritud - 1p



# print("Täringud!")


# try:
#     panus = float(input("Sisesta panus: €"))
#     kasutaja = random.randint(1,12)
#     arvuti = random.randint(1,12)

#     for i in range(1,2):
#             print(arvuti,"Arvuti", kasutaja, "Kasutaja")

#     if kasutaja == arvuti:
#         print("Viik,",panus, "€, tagastatakse!")
#     elif kasutaja > arvuti:
#         voitja = kasutaja
#         print("Palju õnne, sa võitsid", panus * 2, "€!")
#     elif kasutaja < arvuti:
#         voitja = arvuti
#         print("Kahjuks kaotasid", panus, "€, proovi uuesti!")
#     else:
#         print("Palun sisesta korrektne panus!")

# except:
#     print("Sa oled mängust bannitud!")



	
# 4. Emaili kontroll
# 	kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
# 	programm kontrollib kas email on sisestatud õigesti - vähemalt @-märgi kontroll - 1p
# 	programm tükeldab selle ja väljastab lause: ‘Tere enimi, sinu email on server serveris ja domeeniks on sul com’ - 1p
# 	kasutajalt küsitud küsimused on selgelt üheselt mõistetavad - 1p
# 	kood kommenteeritud - 1p
	
# 5. Kaugushüpe
# 	kasutaja sisestab 3 kaugushüppe tulemust - 1p
# 	sinu programm leiab ning väljastab parima ja keskmise tulemuse - 2p
# 	programmi dialoog kasutajaga on arusaadav ja üheselt mõistetav - 1p
# 	kood kommenteeritud - 1p
	
# 6. Salakeel
# 	sinu programm küsib kasutajalt, kas ta soovib salakeelt luua või tõlkida - 1p
# 	kasutaja sisestab tavalise sõna, mis muudetakse salakeeleks - 1p
# 	kasutaja sisestab salakeeles sõna, mis teisendatakse jälle normaalseks - 1p
# 	kood kommenteeritud - 1p
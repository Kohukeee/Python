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

EUR = 1
EEK = 15,6466


print("Eurokalkulaator")

valik = input("1. EUR -> EEK\n2. EEK -> EUR\n")

if valik == "1":
    print("EUR -> EEK")
elif valik == "2":
    print("EEK -> EUR")
else: 
    print("Palun vali 1 või 2")

if valik == "1":
    summa = input("Sisesta summa: ")
    try:
        summa = int(summa)
        if summa > 0:
            vastus = summa * EEK
            print(f"(summa) EUR = {vastus: 2f} EEK")
        else:
            print("Sisesta positiivne arv!")
    except:
        print("Sisesta ainult täisarv!")
                

# 3. Täringud
# 	kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
# 	kasutaja võistleb kahe täringuga arvuti vastu - 1p
# 	kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
# 	kood kommenteeritud - 1p
	
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
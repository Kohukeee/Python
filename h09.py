# Harjutus 09

ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]

print(ev_data)

lugeja = 0
r_kokku = 0
p_kokku = 0

for i in ev_data:
    print(f"{i[0]:30} {i[1]:10} {i[2]:10}") #Vormindan tulpadena :30 on laius
    if (i[1]).isnumeric()==True:            #Liidab kõik sõiduulatused
        r_kokku+=int(i[1])
        p_kokku+=int(i[2])
        lugeja+=1


print(f"Keskmine sõidu ulatus: {r_kokku/lugeja}")   #sõiduulatus jagatud sõidukitega, et keskmine saada
print((f"Keskmine hind: {p_kokku/lugeja}"))         #Sõiduki keskmine hind

print("Autod, mis sõidavad 300+")
for i in ev_data:                                   #Toob esile sõidukid, mis sõidavad kaugemale kui 300km
    if (i[1]).isnumeric()==True: 
        if int(i[1]) >= 300:
            print(i[0])

parim_hinnasuhe = 1000000000000
parim_auto = ""

for i in ev_data:                                  #arvutab välja millise auto km ja hinnasuhe on parim
    if (i[1]).isnumeric()==True: 
        km_tasu = float(i[2]) / float(i[1])
        if km_tasu<parim_hinnasuhe:
            parim_hinnasuhe = km_tasu
            parim_auto = i[0]

print(f"Parim elektriauto: {parim_auto}")




# for i in range(1,21):
#     if i%15 == 0:    
#         print(i,"TIK-TAK", end=" ")
#     elif i%3 == 0:
#         print(i, "TIK", end=" ")
#     elif i%5 == 0:
#         print(i,"TAK", end=" ")
    
#     else:
#         print(i)
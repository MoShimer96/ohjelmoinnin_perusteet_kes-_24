print("Tämä ohjelma laskee tuotteen hinnan keskiarvon neljän kaupan hinnoista.")
hintaKauppaYksi = float(input("Anna hinta ensimmäisessä kaupassa: "))
hintaKauppaKaksi = float(input("Anna hinta toisessa kaupassa: "))
hintaKauppaKolme = float(input("Anna hinta kolmannessa kaupassa: "))
hintaKauppaViimeinen = float(input("Anna hinta viimeisessä kaupassa: \n"))

summa = hintaKauppaYksi + hintaKauppaKaksi + hintaKauppaKolme + hintaKauppaViimeinen
hintojenSumma = round(summa, 1)
hintojenKeskiArvo = round(summa/4, 1)


print(f"Antamiesi hintojen summa on {hintojenSumma}.")
print(f"Antamiesi hintojen keskiarvo on {hintojenKeskiArvo}.")
print(f"Keskiarvo on kokonaislukuna {int(hintojenKeskiArvo)}.")
print("Kiitos ohjelman käytöstä.")
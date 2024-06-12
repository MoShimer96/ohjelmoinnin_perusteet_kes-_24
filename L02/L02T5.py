print("Tämä ohjelma laskee pituuksien yksikkömuunnoksia.")
annettuPituusTuumina = float(input("Anna pituus tuumina: "))
pituusCM = annettuPituusTuumina * 2.54
print(f"Pituus on {annettuPituusTuumina} tuumaa eli {round(pituusCM,1)} senttimetriä.")


annettuPituusMaileina = float(input("Anna pituus maileina: "))
pituusKM = annettuPituusMaileina * 1.609344
print(f"Pituus on {annettuPituusMaileina} mailia eli {round(pituusKM,2)} kilometriä.")

print("Kiitos ohjelman käytöstä.")


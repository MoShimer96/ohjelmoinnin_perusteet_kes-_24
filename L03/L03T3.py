print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
valikko = input("Valitse haluamasi toiminto:\n1) Tulosta merkkijonon ensimmäinen puolikas\n2) Tulosta merkkijonon toinen puolikas\n3) Tulosta merkkijonon pituus\n0) Lopeta\nAnna valintasi: ")
merkkijono = input("Anna merkkijono: ")
merkkijononPituus = len(merkkijono)
merkkijononPituusJaettunaKahdella = int(merkkijononPituus/2)

if int(valikko) == 1:
    ensimmainenPuolikas = merkkijono[:merkkijononPituusJaettunaKahdella]
    print(f"Merkkijonon ensimmäinen puolikas on '{ensimmainenPuolikas}'.")
    print("Kiitos ohjelman käytöstä.")
elif int(valikko) == 2:
    toinenPuolikas = merkkijono[merkkijononPituusJaettunaKahdella:]
    print(f"Merkkijono toinen puolikas on '{toinenPuolikas}'.")
    print("Kiitos ohjelman käytöstä.")
elif int(valikko) == 3:
    print(f"Merkkijonon pituus on {merkkijononPituus}.")
    print("Kiitos ohjelman käytöstä.")
elif int(valikko) == 0:
    print("Lopetetaan.")
    print("Kiitos ohjelman käytöstä.")
else:
    print("Tuntematon valinta.")
    print("Kiitos ohjelman käytöstä.")
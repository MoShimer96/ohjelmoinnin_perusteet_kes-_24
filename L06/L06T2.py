def tiedostoLue(luettavanTiedostonNimi):
    lukujenMaara = 0
    keskiarvo = 0
    summa = 0
    luettuTiedosto = open(luettavanTiedostonNimi, "r")
    for i in luettuTiedosto:
        summa += float(i)
        lukujenMaara +=1
    luettuTiedosto.close()
    keskiarvo = round(summa/lukujenMaara, 2)
    print(f"Tiedostossa '{luettavanTiedostonNimi}' oli {lukujenMaara} lukua.")
    print(f"Lukujen keskiarvo oli {keskiarvo} ja summa {summa}.")
    return None



def paaohjelma():
    luettavanTiedostonNimiSyote = input("Anna luettavan tiedoston nimi: ")
    tiedostoLue(luettavanTiedostonNimiSyote)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
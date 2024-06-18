def tiedostoKirjoita(tiedostoNimi):
    kirjoitaTiedostoon  = open(tiedostoNimi, "w")
    while True:
        syote = input("Anna tiedostoon tallennettava desimaaliluku (enter lopettaa): ")
        if syote != "":
            kirjoitaTiedostoon.write(syote + "\n")
            continue
        else:
            break
    kirjoitaTiedostoon.close()
    return None

def paaohjelma():
    uudenTiedostonNimi = input("Anna tallennettavan tiedoston nimi: ")
    tiedostoKirjoita(uudenTiedostonNimi)
    print(f"Tiedosto '{uudenTiedostonNimi}' kirjoitettu.")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
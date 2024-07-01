######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Opiskelijanumero: 000524560
# Päivämäärä: 1.7.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T5.py

# eof
import L08T5Kirjasto as kirjasto

def valikko():

    print("Valitse haluamasi toiminto:", end="\n")
    print("1) Lue tiedosto", end="\n")
    print("2) Analysoi tiedot",end="\n")
    print("3) Tallenna tulokset", end="\n")
    print("0) Lopeta", end="\n")
    valinta = int(input("Anna valintasi: "))

    return valinta


def paaohjelma():

    olioLista = []

    while True:
        valinta = valikko()

        if valinta == 0:
            print("Lopetetaan.\n", end="\n")
            break
        elif valinta == 1:
            olioLista = kirjasto.lueTiedosto()
            continue
        elif valinta == 2:
            kirjasto.analysoi(olioLista)
            continue
        elif valinta == 3:
            kirjasto.tallennaTulokset(olioLista)
            continue
        else:
            print("Tuntematon valinta, yritä uudestaan.", end="\n")
            continue
    
    olioLista.clear()
    print("Kiitos ohjelman käytöstä.", end="\n")
    return None

paaohjelma()
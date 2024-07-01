######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 1.7.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L09T1.py
import datetime
import math
import sys

def LueTiedosto():

    lista = []
    LuettavanTiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    try:
        LuettavaTiedostoAvattu = open(LuettavanTiedostonNimi, "r")
        print(f"Tiedosto '{LuettavanTiedostonNimi}' luettu.", end="\n")
        for rivi in LuettavaTiedostoAvattu:
            lista.append(rivi)
        LuettavaTiedostoAvattu.close()
    except OSError:
        print(f"Tiedoston '{LuettavanTiedostonNimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit()
    return lista

def kirjoitaTiedosto(lista):

    KirjoitettavaTiedostoNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    try:
        KirjoitettavaTiedostoAvattu = open(KirjoitettavaTiedostoNimi, "w")
        for item in lista:
            KirjoitettavaTiedostoAvattu.write(item)
        print(f"Tiedoston '{KirjoitettavaTiedostoNimi}' kirjoittaminen onnistui.", end="\n")
        KirjoitettavaTiedostoAvattu.close()
    except OSError:
        print(f"Tiedoston '{KirjoitettavaTiedostoNimi}' käsittelyssä virhe, lopetetaan.\n", end="\n")
        sys.exit()
    
    return None


def paaohjelma():

    lista = []

    lista = LueTiedosto()

    kirjoitaTiedosto(lista)

    lista.clear()

    print("Kiitos ohjelman käytöstä.")
    return None


paaohjelma()


# eof ##############################################
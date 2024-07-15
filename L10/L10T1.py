######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 14.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L10T1.py

# eof

import os
import sys

def lueTiedosto():
    Nimi = annaNimi("Anna luettavan tiedoston nimi: ")

    SyytLista = []
    # Luetaan tiedosto ensin
    try:
        TiedostoAvattu = open(Nimi, "r", encoding="UTF-8")
        next(TiedostoAvattu)
        # Sessio;Hahmo;Heiton syy;Noppien määrä;Noppa;Heitot

        # Me halutaan syyt ja kuinka monta heittoa per syy

        for Rivi in TiedostoAvattu:
            RiviStripped = Rivi.strip()
            RiviStrippedSplit = RiviStripped.split(";")
            if len(RiviStrippedSplit) > 2:
                SyytLista.append(RiviStrippedSplit[2])
        
        TiedostoAvattu.close()
    except OSError:
        print(f"Tiedoston '{Nimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)


    return SyytLista




def analyysi(Lista) -> list:
    PalautettavaLista = []
    Syyt = 0
    Heittoa = 0
    AnalyysiDict = {}

    for Heitto in Lista:
        if Heitto in AnalyysiDict:
            AnalyysiDict[Heitto] += 1
            Heittoa += 1
        else:
            AnalyysiDict[Heitto] = 1
            Syyt += 1
            Heittoa += 1
    
    # Sanakirjan lajittelu
    AnalyysiDictSorted = dict(sorted(AnalyysiDict.items()))
    PalautettavaLista.append(Syyt)
    PalautettavaLista.append(Heittoa)
    PalautettavaLista.append(AnalyysiDictSorted)

    kirjoitaTiedosto(PalautettavaLista)

    print(f"Tunnistettiin {Syyt} erilaista syytä ja {Heittoa} heittoa:")

    for key, value in AnalyysiDictSorted.items():
        if value > 1:
            print(f"{key}: {value} heittoa")
        else:
            print(f"{key}: {value} heitto")

    
    return PalautettavaLista


def kirjoitaTiedosto( Lista):
    Nimi = annaNimi("Anna kirjoitettavan tiedoston nimi: ")

    try:
        TiedostoAvattu = open(Nimi, "w", encoding="UTF-8")

        TiedostoAvattu.write(f"Tunnistettiin {Lista[0]} erilaista syytä ja {Lista[1]} heittoa:\n")

        for key, value in Lista[2].items():
            if value > 1:
                TiedostoAvattu.write(f"{key}: {value} heittoa\n")
            else:
                TiedostoAvattu.write(f"{key}: {value} heitto\n")
        TiedostoAvattu.close()
    except OSError:
        print(f"Tiedoston '{Nimi}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    return None


def annaNimi(Syote):
    Nimi = input(Syote)
    return Nimi


def paaohjelma():
    
    ListaAnalyysiaVarten = lueTiedosto()
    ListaTiedostonKirjoittamiseen = analyysi(ListaAnalyysiaVarten)
    

    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
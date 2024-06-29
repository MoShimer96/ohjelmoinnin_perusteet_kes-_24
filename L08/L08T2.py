######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 29.6.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T2.py

# eof

import L08T2Kirjasto as kirjasto


def valikko():

    print("Valitse haluamasi toiminto:", end="\n")
    print("1) Muunna eurot Ruotsin kruunuiksi", end="\n")
    print("2) Muunna eurot Yhdysvaltain dollareiksi", end="\n")
    print("3) Muunna Yhdysvaltain dollarit euroiksi", end="\n")
    print("4) Muunna Ruotsin kruunut euroiksi", end="\n")
    print("5) Muunna Yhdysvaltain dollarit Ruotsin kruunuiksi", end="\n")
    print("6) Muunna Ruotsin kruunut Yhdysvaltain dollareiksi", end="\n")
    print("0) Lopeta", end="\n")
    valinta = int(input("Anna valintasi: "))

    return valinta

def paaohjelma():

    while True:
        valinta_paaohjelma = valikko()
        if valinta_paaohjelma == 0:
            print("Lopetetaan.\n", end="\n")
            break
        elif valinta_paaohjelma == 1:
            kirjasto.EURtoSEK()
            continue
        elif valinta_paaohjelma == 2:
            kirjasto.EURtoUSD()
            continue
        elif valinta_paaohjelma == 3:
            kirjasto.USDtoEUR()
            continue
        elif valinta_paaohjelma == 4:
            kirjasto.SEKtoEUR()
            continue
        elif valinta_paaohjelma == 5:
            kirjasto.USDtoSEK()
            continue
        elif valinta_paaohjelma == 6:
            kirjasto.SEKtoUSD()
            continue
        else:
            print("Tuntematon valinta, yritä uudestaan.\n", end="\n")
            continue
    
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

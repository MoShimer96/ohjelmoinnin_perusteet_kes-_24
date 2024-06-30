######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 30.6.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T3.py

# eof
import L08T3Kirjasto as kirjasto
def valikko():
    print("Valitse haluamasi toiminto:", end="\n")
    print("1) Lue tiedosto", end="\n")
    print("2) Analysoi", end="\n")
    print("3) Kirjoita tiedosto", end="\n")
    print("4) Analysoi vuosittaiset keskiarvot", end="\n")
    print("0) Lopeta", end="\n")
    valinta = int(input("Anna valintasi: "))

    return valinta


def paaohjelma():
    print("Tällä ohjelmalla voit analysoida eurosetelien tietoja.", end="\n")
    data_lista = []
    olio_lista = []
    setelin_arvo = None
    setelin_sijainti = None
    while True:
        valikko_valinta = valikko()

        if valikko_valinta == 0:
            print("Lopetetaan.\n", end="\n")
            break
        elif valikko_valinta == 1:
            #data_lista, setelinSijainti, setelinArvo
            data_lista, setelin_sijainti, setelin_arvo = kirjasto.lueTiedosto()
            continue
        elif valikko_valinta == 2:
            olio_lista = kirjasto.analyysi(data_lista, setelin_sijainti, setelin_arvo)
            continue
        elif valikko_valinta == 3:
            kirjasto.kirjoitaTiedosto(olio_lista, setelin_arvo)
            continue
        elif valikko_valinta == 4:
            kirjasto.analyysi_vuosittainen(olio_lista)
            continue
        else:
            print("Tuntematon valinta, yritä uudestaan.\n", end="\n")
            continue
    
    data_lista.clear()
    olio_lista.clear()
    print("Kiitos ohjelman käytöstä.")
    return None



paaohjelma()
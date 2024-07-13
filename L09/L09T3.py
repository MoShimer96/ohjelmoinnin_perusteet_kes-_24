######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 13.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L09T3.py


import L09T3Kirjasto as Kirjasto

def valikko():
    
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("0) Lopeta")
    
    Valinta = int(input("Anna valintasi: "))

    return Valinta

            

def annaNimi(Syote):
    Nimi = input(Syote)
    return Nimi

def paaohjelma():
    DataLista = []
    while True:
        Valinta = valikko()

        if Valinta == 1:

            DataLista.clear()
            Nimi = annaNimi("Anna luettavan tiedoston nimi: ")
            DataLista = Kirjasto.lueTiedosto(Nimi)

        elif Valinta == 2:
            if len(DataLista) != 0:
             Kirjasto.analysoi(DataLista)
            else:
                print("Ei analysoitavia tietoja, lue tiedot ensin.\n")
   
        
        elif Valinta == 0:
            print("Lopetetaan.\n")
            break

        else:
            print("Tuntemaon valinta, yritä uudestaan.\n")
    
    print("Kiitos ohjelman käytöstä.")

    DataLista.clear()
    return None

paaohjelma()

# eof
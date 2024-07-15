######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 15.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L10T2.py

# eof

class HENKILO:
    Nimi = None
    Puhelinnumero = None
    Osoite = None
    

def lisaaOsoitekirjaan(Lista) -> list:
    print("Anna lisättävän henkilön tiedot.")
    UusiHenkilo = HENKILO()
    UusiHenkilo.Nimi = input("Nimi: ") 
    UusiHenkilo.Puhelinnumero = input("Puhelinnumero: ")
    UusiHenkilo.Osoite = input("Osoite: ") 
    print(f"Henkilö '{UusiHenkilo.Nimi}' lisätty osoitekirjaan.\n")

    Lista.append(UusiHenkilo)

    return Lista

def poistaOsoitekirjasta(Lista) -> list:
    PoistettavanHenkilonNimi = input("Anna poistettavan henkilön nimi: ")

    for Henkilo in Lista:
        if Henkilo.Nimi == PoistettavanHenkilonNimi:
            print(f"Henkilö '{Henkilo.Nimi}' poistettu osoitekirjasta.\n")
            Lista.remove(Henkilo)
            
    return Lista

def tulostaOsoitekirja(Lista):
    HenkilonNimi = input("Anna tulostettavan henkilön nimi tai jätä tyhjäksi: ")

    if HenkilonNimi != "":
        found = False
        for Henkilo in Lista:
            if Henkilo.Nimi == HenkilonNimi:
                found = True
                print(f"Nimi: {Henkilo.Nimi}")
                print(f"Puhelinnumero: {Henkilo.Puhelinnumero}")
                print(f"Osoite: {Henkilo.Osoite}\n")
        if not found:
            print(f"Henkilöä '{HenkilonNimi}' ei löydy osoitekirjasta.\n")
    else:
        print("Osoitekirjassa on seuraavat henkilöt:")
        for Henkilo in Lista:
            print(f"Nimi: {Henkilo.Nimi}")
            print(f"Puhelinnumero: {Henkilo.Puhelinnumero}")
            print(f"Osoite: {Henkilo.Osoite}\n", end="\n")
        print("",end="\n")


    return None


def valikko() -> int:
    
    print("Valitse haluamasi toiminto:")
    print("1) Lisää osoitekirjaan")
    print("2) Poista osoitekirjasta")
    print("3) Tulosta osoitekirja")
    print("0) Lopeta")
    
    Valinta = int(input("Anna valintasi: "))


    return Valinta




def paaohjelma():
    OlioLista = []

    while True:
        Valinta = valikko()

        if Valinta == 1:
            OlioLista = lisaaOsoitekirjaan(OlioLista)
        elif Valinta == 2:
            if len(OlioLista) != 0:
                OlioLista = poistaOsoitekirjasta(OlioLista)
            else:
                print("Osoitekirja on tyhjä.\n")
        elif Valinta == 3:
            if len(OlioLista) != 0:
                tulostaOsoitekirja(OlioLista)
            else:
                print("Osoitekirja on tyhjä.\n")
            
        elif Valinta == 0:
            print("Lopetetaan.\n")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")
    
    OlioLista.clear()
    print("Kiitos ohjelman käytöstä.")
    return None


paaohjelma()


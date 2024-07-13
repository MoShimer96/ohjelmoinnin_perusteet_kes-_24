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
# Tehtävä L09T4.py

import sys

try:
    import L09T4Kirjasto as Kirjasto
except ImportError:
    print("Virhe, kirjastoja ei voitu tuoda, lopetetaan.\n")
    sys.exit(0)

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Testaa testaaPienempi")
    print("2) Testaa jaaLuku")
    print("3) Testaa arvoListalta")
    print("4) Testaa listanSatunnainenArvo")
    print("0) Lopeta")
    
    Valinta = int(input("Anna valintasi: "))

    return Valinta


def paaohjelma():

    
    while True:
        
        Valinta = valikko()

        if Valinta ==  1:
            try:
                TestattavaLuku = int(input("Anna testattava luku: "))
                Tulos = Kirjasto.testaaPienempi(TestattavaLuku)
                if Tulos == True:
                    print(f"Antamasi luku on pienempi kuin 10.\n")
                else:
                    print(f"Antamasi luku on suurempi kuin 10.\n")
            except AssertionError:
                if type(TestattavaLuku) == float:
                    print("Virhe, valinta ei ollut kokonaisluku.\n")
                elif TestattavaLuku < 0:
                    print("Virhe, annoit negatiivisen luvun.\n")
        
        elif Valinta == 2:
            try:
                TestattavaLuku = int(input("Anna jakaja: "))
                Tulos = Kirjasto.jaaLuku(TestattavaLuku)
                print(f"{10}/{TestattavaLuku} on {Tulos}.\n")
            except ZeroDivisionError:
                print("Virhe, nollalla ei voi jakaa.\n")

        elif Valinta == 3:
            try:
                TestattavaIndeksi = int(input("Anna haettava indeksi: "))
                Tulos = Kirjasto.arvoListalta(TestattavaIndeksi)
                print(f"Listan indeksillä {TestattavaIndeksi} löytyi arvo '{Tulos}'.\n")
            except IndexError:
                print("Virhe, listalla ei ollut annettua indeksiä.\n")
        
        elif Valinta == 4:
            try:
                Tulost = Kirjasto.listanSatunnainenArvo()
                print(f"Listalta löytyi arvo '{Tulost}'.\n")
            except TypeError:
                print("Virhe, listan indeksi oli merkkijono.\n")
        elif Valinta == 0:
            print("Lopetetaan.\n")
            print("Kiitos ohjelman käytöstä.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")
    

paaohjelma()


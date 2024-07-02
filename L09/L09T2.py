######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 2.7.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L09T2.py

# eof


def valikko():

    valinta = None
    print("Mitä haluat tehdä:", end="\n")
    print("1) Testaa ValueError", end="\n")
    print("2) Testaa IndexError", end="\n")
    print("3) Testaa ZeroDivisionError", end="\n")
    print("4) Testaa TypeError", end="\n")
    print("0) Lopeta", end="\n")
    
    while True:
        try:
            valinta = int(input("Valintasi: "))
            break
        except ValueError:
            print("Virhe, valinta ei ollut kokonaisluku.", end="\n")
            continue

    return valinta

def testaaIndexError():

    lista = [11, 22, 33, 44, 55] 

    AnnaIndeksi = int(input("Anna indeksi 0-4: "))
    try:
        print(f"Listan arvo on {lista[AnnaIndeksi]} indeksillä {AnnaIndeksi}.\n", end="\n")
    except IndexError:
        print(f"Tuli IndexError, indeksi oli {AnnaIndeksi}.\n", end="\n")

    return None

def testaaZeroDivisionError():

    AnnaJakaja = int(input("Anna jakaja: "))

    try:
        print(f"12/{AnnaJakaja} on {12/AnnaJakaja}.\n",end="\n")
    except ZeroDivisionError:
        print("Tuli ZeroDivisionError, jakaja oli 0.\n", end="\n")

    return None

def testaaTypeError():
    AnnaNumero = input("Anna numero: ")

    try:
        print(AnnaNumero*AnnaNumero)
    except TypeError:
        print(f"Tuli TypeError, {AnnaNumero}*{AnnaNumero} merkkijonoilla ei onnistunut.\n", end="\n")
    
    return None


def paaohjelma():

    

    while True:

        valinta = valikko()

        if valinta == 0:
            print("Lopetetaan\n", end="\n")
            break
        elif valinta == 1:
            print("Valikko-ohjelma testaa ValueError'n.\n", end="\n")
            continue
        elif valinta == 2:
            testaaIndexError()
            continue
        elif valinta == 3:
            testaaZeroDivisionError()
            continue
        elif valinta == 4:
            testaaTypeError()
            continue
        else:
            print("Tuntematon valinta, yritä uudestaan.\n", end="\n")
            continue

    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
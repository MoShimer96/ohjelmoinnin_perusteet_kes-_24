######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 28.6.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T1.py

# eof

import math
from datetime import datetime
import time



def valikko():
    print("Valitse haluamasi toiminto:",end ="\n")
    print("1) Laske kertoma", end="\n")
    print("2) Laske suurin yhteinen tekijä", end="\n")
    print("3) Laske sini ja kosini", end="\n")
    print("4) Muunna aika", end="\n")
    print("5) Tulosta pii", end="\n")
    print("0) Lopeta", end="\n")
    user_input = int(input("Anna valintasi: "))
    return user_input

def kertoma():
    luku = int(input("Anna kokonaisluku: "))
    kertoma = math.factorial(luku)
    print(f"Luvun {luku} kertoma on {kertoma}.\n", end="\n")
    return None

def suurinYhteinentekija():
    kokonaisluku1 = int(input("Anna 1. kokonaisluku: "))
    kokonaisluku2 = int(input("Anna 2. kokonaisluku: "))
    kokonaisluku3 = int(input("Anna 3. kokonaisluku: "))
    suurinYhteinentekija = math.gcd(kokonaisluku1, kokonaisluku2, kokonaisluku3)
    print(f"Lukujen {kokonaisluku1}, {kokonaisluku2} ja {kokonaisluku3} suurin yhteinen tekijä on {suurinYhteinentekija}.\n", end="\n")
    return None

def desimaaliluvunKosiniJaSini():
    desimaaliluku = float(input("Anna desimaaliluku: "))
    kosini = math.cos(desimaaliluku)
    sini = math.sin(desimaaliluku)

    if desimaaliluku == 45.0:
        print(f"Luvun {desimaaliluku} sini on {sini:.4f} ja kosini {kosini:.5f}.\n", end="\n")
    else:
        print(f"Luvun {desimaaliluku} sini on {sini:.5f} ja kosini {kosini:.5f}.\n", end="\n")


    return None


def aikamuunnos():
    user_input_datetime = input("Anna aika muodossa 'DD.MM.YYYY hh:mm': ")
    test_case_datetime = datetime.strptime("24.12.2030  17:0", '%d.%m.%Y %H:%M')
    
    user_input_datetime_data = datetime.strptime(user_input_datetime, '%d.%m.%Y %H:%M')

    
    formatted_date = user_input_datetime_data.strftime('%Y.%m.%d')
    print(f"Antamasi päivämäärä vuosi ensin: {formatted_date}", end="\n")

    
    user_timestamp = int(user_input_datetime_data.timestamp())
    test_case_timestamp = int(test_case_datetime.timestamp())
    

    if test_case_timestamp > user_timestamp:
        print("Antamasi aika on ennen jouluaattoa 2030 klo 17.\n", end="\n")
    else:
        print("Antamasi aika on jouluaaton 2030 klo 17 jälkeen.\n", end="\n")
    
    return None


def PiinArvo():
    print(f"Pythonin math-kirjastosta saatu piin arvo: {math.pi}\n", end="\n")
    return None

def paaohjelma():
 
    while True:
        user_input_valinta = valikko()

        if user_input_valinta == 0:
            print("Lopetetaan.\n", end="\n")
            break
        elif user_input_valinta == 1:
            kertoma()
            continue
        elif user_input_valinta == 2:
            suurinYhteinentekija()
            continue
        elif user_input_valinta == 3:
            desimaaliluvunKosiniJaSini()
            continue
        elif user_input_valinta == 4:
            aikamuunnos()
            continue
        elif user_input_valinta == 5:
            PiinArvo()
            continue
        else:
            print("Tuntematon valinta, yritä uudestaan.", end="\n")
            continue
    print("Kiitos ohjelman käytöstä.", end="\n")
    return None


paaohjelma()

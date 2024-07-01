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
# Tehtävä L08T4.py

# eof
import random

def pelilogiikka(pelaajienMaara):

    pelitilanne = [0] * pelaajienMaara    
    
    for i in range(pelaajienMaara):

        while True:
            syote = input(f"Pelaaja {i+1}, heitä noppaa? (k/e): ")
            if syote.lower() == 'k':
                noppa = random.randint(1,6)
                pelitilanne[i] += noppa
                print(f"Heitetty noppa: {noppa}, silmäluvut yhteensä: {pelitilanne[i]}",end="\n")
                if pelitilanne[i] > 9:
                    print(f"Silmälukujen summa ylitti 9. Pelaaja {i+1}, hävisit pelin.\n", end="\n")
                    pelitilanne[i] = 0
                    break
            elif syote.lower() == 'e':
                print("",end="\n")
                break

    return pelitilanne


def loyda_voittaja(pelitilanne_lista):

    pelaaja_jolla_on_suurin_pistemaara = pelitilanne_lista.index(max(pelitilanne_lista))
    if pelitilanne_lista[pelaaja_jolla_on_suurin_pistemaara] >= 13 or pelitilanne_lista[pelaaja_jolla_on_suurin_pistemaara] == 0 :
        print("Kukaan pelaajista ei voittanut peliä.", end="\n")
    else:
        print(f"Pelaaja {pelaaja_jolla_on_suurin_pistemaara+1}, voitit pelin!", end="\n")
    


    return None

def paaohjelma():
    pelin_Tilanne = []
    siemenluku = int(input("Anna siemenluku satunnaislukugeneraattoria varten: "))
    random.seed(siemenluku)
    pelaajienLukumaara = int(input("Anna pelaajien lukumäärä: "))
    print("",end="\n")

    pelin_Tilanne = pelilogiikka(pelaajienLukumaara)
    
    loyda_voittaja(pelin_Tilanne)

    print("Kiitos ohjelman käytöstä.")
    pelin_Tilanne.clear()
    return None

paaohjelma()






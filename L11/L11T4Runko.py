# (c) LUT 2023 L11T4 Variaatio B - Rami Saarivuori
# Tämä esimerkki on tarkoitettu omatoimisen oppimisen tueksi ohjelmoinnin 
# opiskeluun. Muu käyttö kielletty.
##########################################################################################
# Ohjelma, joka etsii sopivia numeroita

######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 25.7.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L11T4.py

# eof

import time
import sys
import math

def hakufunktio(Nimi, Luvut):
    #####################################################
    # Lisää tarvittava koodi tämän kommentin alapuolelle.
    try:
        TiedostoAvattu = open(Nimi, "r", encoding="UTF-8")
        
        for Numero in TiedostoAvattu:
            Numero = Numero.strip()
            NumeroKorotettuna = str(int(sum(math.pow(int(Luku),5) for Luku in Numero)))
            if Numero == NumeroKorotettuna:
                Luvut.append(Numero)

        TiedostoAvattu.close()
    except OSError:
        print(f"{Nimi} käsittelyssä virhe, lopetetaan.", end="\n")
        sys.exit(0)




    # Lisää tarvittava koodi tämän kommentin yläpuolelle.
    #####################################################
    return Luvut

def paaohjelma():
    Nimi = input("Anna luettavan tiedoston nimi: ")
    Tulokset = []
    Kello1 = time.perf_counter()
    Tulokset = hakufunktio(Nimi, Tulokset)
    Kello2 = time.perf_counter()
    Aika = Kello2 - Kello1
    if not Tulokset:
        print("Hakualgoritmi ei löytänyt sopivia lukuja.")
    elif (Aika > 3):
        print("Hakualgoritmi ei ollut tarpeeksi nopea.")
    else:
        print("Hakualgoritmi oli riittävän nopea!")
        print("Se löysi {} lukua:".format(len(Tulokset)))
        for i in Tulokset:
            print(i, end=", ")
        print()
    print("Kiitos ohjelman käytöstä.")
    Tulokset.clear()
    return None

paaohjelma()
###########################################################################
# eof

######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 22.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L11T1.py

# eof
import math

def laske_neperin_luku(kierroksia):
    Eluku = 0.0
    for n in range(kierroksia):
        Eluku += 1 / math.factorial(n)
    return Eluku



print("Tämä ohjelma laskee Neperin luvulle desimaaleja.")
Kierroksia = int(input("Anna kierrosten määrä: "))

Tulos = laske_neperin_luku(Kierroksia)

# Tulostetaan tulos kahdenkymmenen desimaalin tarkkuudella
print(f"Neperin luvun likiarvo annetulla kierrosten määrällä:\n{Tulos:.20g}")
print("Kiitos ohjelman käytöstä.")


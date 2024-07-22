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
# Tehtävä L10T3.py

# eof

import numpy


Taulukko = numpy.zeros([4,4], int)

for Rivi in range(0, len(Taulukko)):
    for Sarake in range(0, len(Taulukko[Rivi])):
       # (RiviIndeksi) * (SarakeIndeksi+2)
       Taulukko[Rivi][Sarake] = Rivi * (Sarake+2)

# Lähtömatriisi. 
print("Tämä ohjelma testaa NumPy-matriisin käyttöä.", end="\n")
print("Lähtömatriisit tulostettuna NumPy-muotoilulla:", end="\n")
print("Matriisi:", end="\n")
print(Taulukko)
print("", end="\n")


# Transpoosi.
TaulukkoTranspoosi = numpy.transpose(Taulukko)
print("Matriisin transpoosi:",end="\n")
print(TaulukkoTranspoosi)
print("",end="\n")

# Tulosmatriisi.
print("Tulosmatriisi tulostettuna NumPy-muotoilulla:",end="\n")
TaulukkoTulosmatriisi = (Taulukko + TaulukkoTranspoosi)
print(TaulukkoTulosmatriisi)
print("", end="\n")


# Tulosmatriisi tulostettuna alkiot puolipisteillä eroteltuna:
print("Tulosmatriisi tulostettuna alkiot puolipisteillä eroteltuna:", end="\n")
for row in TaulukkoTulosmatriisi:
    print(";".join(map(str, row))+";")
print("", end="\n")

print("Kiitos ohjelman käytöstä.", end="\n")

numpy.delete(Taulukko, [4,4])
numpy.delete(TaulukkoTulosmatriisi, [4,4])
numpy.delete(TaulukkoTranspoosi, [4,4])
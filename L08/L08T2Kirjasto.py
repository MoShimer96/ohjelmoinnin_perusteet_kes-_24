######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 29.6.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T2.py

# eof

print("Käytetään kirjaston versiota 1.0", end="\n")

"""Rahayksiköiden muuntokertoimet 19.10.2023:
EUR→USD & 1.0558
EUR→SEK & 11.6155
USD→SEK & 11.0057"""


def EURtoUSD():
    rahaEuroina = float(input("Anna rahamäärä: "))
    rahaEURtoUSD = rahaEuroina * 1.0558
    rahaEURtoUSD_str = f"{rahaEURtoUSD:.2f}".rstrip('0').rstrip('.')
    print(f"{rahaEuroina} euroa on {rahaEURtoUSD_str} Yhdysvaltain dollaria.\n", end="\n")
    return None

def EURtoSEK():
    rahaEuroina = float(input("Anna rahamäärä: "))
    rahaEURtoSEK = rahaEuroina * 11.6155
    rahaEURtoSEK_str = f"{rahaEURtoSEK:.2f}".rstrip('0').rstrip('.')
    print(f"{rahaEuroina} euroa on {rahaEURtoSEK_str} Ruotsin kruunua.\n", end="\n")
    return None

def USDtoEUR():
    rahaUSD = float(input("Anna rahamäärä: "))
    rahaUSDtoEUR = rahaUSD / 1.0558
    rahaUSDtoEUR_str = f"{rahaUSDtoEUR:.2f}".rstrip('0').rstrip('.')
    print(f"{rahaUSD} Yhdysvaltain dollaria on {rahaUSDtoEUR_str} euroa.\n", end="\n")
    return None

def SEKtoEUR():
    rahaSEK = float(input("Anna rahamäärä: "))
    rahaSEKtoEUR = rahaSEK / 11.6155
    rahaSEKtoEUR_str = f"{rahaSEKtoEUR:.2f}".rstrip('0').rstrip('.')
    print(f"{rahaSEK} Ruotsin kruunua on {rahaSEKtoEUR_str} euroa.\n", end="\n")
    return None

def USDtoSEK():
    rahaUSD = float(input("Anna rahamäärä: "))
    rahaUSDtoSEK = rahaUSD * 11.0057
    rahaUSDtoSEK_str = f"{rahaUSDtoSEK:.2f}".rstrip('0').rstrip('.')
    print(f"{rahaUSD} Yhdysvaltain dollaria on {rahaUSDtoSEK_str} Ruotsin kruunua.\n", end="\n")
    return None

def SEKtoUSD():
    rahaSEK = float(input("Anna rahamäärä: "))
    rahaSEKtoUSD = rahaSEK / 11.0057
    rahaSEKtoUSD_str = f"{rahaSEKtoUSD:.2f}".rstrip('0').rstrip('.')
    print(f"{rahaSEK} Ruotsin kruunua on {rahaSEKtoUSD_str} Yhdysvaltain dollaria.\n", end="\n")
    return None

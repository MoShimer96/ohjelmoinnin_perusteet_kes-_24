######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 25.07.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L11T3.py


def fibonacciRecursive(Syote: int) -> int:
 
    # Base case
    if Syote == 1 or Syote == 2:
        return 1
    else:
        return fibonacciRecursive(Syote -1) + fibonacciRecursive(Syote -2)

def laskeLuku(Syote: int) -> int:
    
    Summa = 1

    for i in range(1, Syote):
        Summa += fibonacciRecursive(i)
        
    return Summa


def paaohjelma():
    print("Tämä ohjelma laskee Fibonaccin luvun rekursiivisesti.", end="\n")
    Luku = int(input("Anna luku, jolle Fibonaccin luku lasketaan: "))
    FibonacciLuku = laskeLuku(Luku)

    print(f"Fibonaccin luku luvulle {Luku} on {FibonacciLuku}.", end="\n")

    print("Kiitos ohjelman käytöstä.", end="\n")

    return None

paaohjelma()

# eof
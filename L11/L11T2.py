"""Tee Python-ohjelma, joka laskee Pell’n lukuja. Kysy käyttäjältä
laskettavien lukujen määrä. Tulosta luvut allekkain alla olevan esimerkkiajon mukaisesti.
Jos käyttäjä antaa kierrosten määräksi alle 1, tulosta käyttäjälle alla oleva virheilmoitus:
"Kierroksia on oltava vähintään 1 kpl."""

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
# Tehtävä L11T2.py





def pellLuvut(Syote: int) -> list:
    
    lst = []
    

    for i in range(0, Syote):
        if i == 0:
            lst.append(0)
        elif i == 1:
            lst.append(1)
        else:
            PellLuku = 2 * lst[i-1] + lst[i-2]
            lst.append(PellLuku)

    return lst

def tulosta(Lista: list):
    print(f"{len(Lista)}. ensimmäistä Pell'n lukua:", end="\n")
    for i in range(0, len(Lista)):
        print(f"{i+1}. Pell'n luku: {Lista[i]}", end="\n")

    return None

def paaohjelma():
    
    print("Tämä ohjelma laskee Pell'n lukusarjaa.", end="\n")
    Kierrokset = int(input("Anna laskettavien lukujen määrä: "))

    if Kierrokset < 1:
        print("Kierroksia on oltava vähintään 1 kpl.", end="\n")
    else:  
        PellLista = pellLuvut(Kierrokset)
        tulosta(PellLista)
    
    print("Kiitos ohjelman käytöstä.")
    return None


paaohjelma()


# eof
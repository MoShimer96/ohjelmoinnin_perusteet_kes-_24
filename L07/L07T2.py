######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 21.6.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T2.py

# eof

class ELOKUVA:

    def __init__(self):
        self.nimi =  None
        self.pituus =  None
        self.ohjaaja =  None


elokuva = ELOKUVA()
elokuva.nimi = input("Anna elokuvan nimi: ")
elokuva.pituus = int(input("Anna elokuvan pituus kokonaisina minuutteina: "))
elokuva.ohjaaja = input("Anna elokuvan ohjaaja: ")

print(f"Elokuvan '{elokuva.nimi}' on ohjannut {elokuva.ohjaaja} ja sen kesto on {elokuva.pituus} minuuttia.", end="\n")
print("Kiitos ohjelman käytöstä.")
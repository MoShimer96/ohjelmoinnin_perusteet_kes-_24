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
# Tehtävä L07T1.py

# eof

def paaohjelma():

    tiedostonNimi = input("Anna tiedoston nimi: ")
    tiedostoAvattu = open(tiedostonNimi, "r")
    #  Sessio;Hahmo;Noppien määrä;Noppa;Noppien silmäluvut
    next(tiedostoAvattu)
    print("Nopanheiton tulokset ovat seuraavat:",end="\n")
    
    for rivi in tiedostoAvattu:
        rivi_split = rivi.split(";")
        print(f"Pelaaja '{rivi_split[1].strip()}' heitti {rivi_split[2].strip()} kertaa noppaa {rivi_split[3].strip()} ja sai silmäluvut '{rivi_split[4].strip()}'.", end="\n")

    tiedostoAvattu.close()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

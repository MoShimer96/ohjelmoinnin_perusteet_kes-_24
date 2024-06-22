######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 22.6.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T1.py

# eof

class TUOTE:
    tuotteenNimi = None
    tuotteenHinta = None

""" Käyttäjän valitessa uusien tietojen antamisen, kutsu sopivaa aliohjelmaa ja välitä sille
 parametrina lista, luo aliohjelmassa uusi olio, sijoita käyttäjän antamat tiedot olioon, lisää olio
 listaan ja palauta lista paluuarvona kutsuvaan ohjelmaan. Näin saat lisättyä uuden tuotteen
 tiedot oliolistaan. """

def valintaYksi(lst):
    tuotteenNimiSyote = input("Anna tuotteen nimi: ")
    tuotteenHintaSyote = float(input("Anna tuotteen hinta (e): "))

    uusiTuote = TUOTE()
    uusiTuote.tuotteenNimi = tuotteenNimiSyote
    uusiTuote.tuotteenHinta = tuotteenHintaSyote
    lst.append(uusiTuote)

    return lst

"""  Käyttäjän valitessa tietojen lukemisen, välitä sopivalle aliohjelmalle tiedoston nimi ja lista. Lue
 tiedoston rivit, luo jokaista riviä varten olio ja sijoita kunkin sarakkeen arvo sopivaan olion
 jäsenmuuttujaan. Palauta lista paluuarvona kutsuvaan ohjelmaan. Näin saat lisättyä useita
 tuotteita oliolistaan. """

def valintaKaksi(syottoTiedosto, lst):

    # Esimerkkisyötetiedostosta
    # Tuotteennimi;Tuotteenhinta

    syottoTiedostoLuettu = open(syottoTiedosto, "r")
    next(syottoTiedostoLuettu)

    for rivi in syottoTiedostoLuettu:
        rivi_split = rivi.strip().split(";")
        uusiTuote =TUOTE()
        uusiTuote.tuotteenNimi = rivi_split[0]
        uusiTuote.tuotteenHinta = rivi_split[1]
        lst.append(uusiTuote)
    
    syottoTiedostoLuettu.close()
    print(f"Tiedosto {syottoTiedosto} luettu.")
    return lst

# Käyttäjän valitessa tietojen tulostuksen, välitä sopivalle aliohjelmalle lista ja tulosta tiedot siellä.
def valintaKolme(lst):
    print("Listalta löytyy seuraavat tuotteet ja hinnat:", end="\n")
    for item in lst:
        print(f"{item.tuotteenNimi} {item.tuotteenHinta}", end="\n")  
    return None

"""  Käyttäjän valitessa tietojen tallennuksen, välitä sopivalle aliohjelmalle tallennettavan tiedoston
 nimi sekä lista ja tallenna tiedot tiedostoon aliohjelmassa. """

def valintaNelja(uusiTiedostoNimi, lst):

    uusiTiedostoNimiAvattu = open(uusiTiedostoNimi, "w")
    uusiTiedostoNimiAvattu.write("Tuotteen nimi;Tuotteen hinta\n")
    # Käy läpi kaikki listassa olevat tuotteet
    for item in lst:
        uusiTiedostoNimiAvattu.write(f"{item.tuotteenNimi};{item.tuotteenHinta}\n")
    
    uusiTiedostoNimiAvattu.close()
    print(f"Tiedot kirjoitettu tiedostoon '{uusiTiedostoNimi}'.", end="\n")
    return None

# Ohjelman valikko palauttaa int
def valikko():
    print("Valitse haluamasi toiminto:", end="\n")
    print("1) Anna uuden tuotteen tiedot", end="\n")
    print("2) Lue tiedot tiedostosta", end="\n")
    print("3) Tulosta tiedot listalta", end="\n")
    print("4) Tallenna listan tiedot tiedostoon", end="\n")
    print("0) Lopeta", end="\n")
    valinta = int(input("Anna valintasi: "))
    return valinta

def paaohjelma():
    print("Tämä ohjelma hallitsee tuotteiden tietoja listalla.", end="\n")
    tuoteLista = []
    while True:
        valintaSyote = valikko()
        
        if valintaSyote == 0:

            """ Käyttäjän valitessa lopeta-toiminnon, ohjelma suorittaa lopetusrutiinit ja lopettaa ohjelman.
                Nämä sisältävät tässä vaiheessa oliolistan tyhjennyksen ja lopetustulosteiden näyttämisen.
                Muista tyhjentää tuotelista ohjelman lopussa. """
            print("Lopetetaan.", end="\n")
            print("",end="\n")
            print("Kiitos ohjelman käytöstä.")
            tuoteLista.clear()
            break

        elif valintaSyote == 1:
            tuoteLista = valintaYksi(tuoteLista)
            print("",end="\n")
            continue
        elif valintaSyote == 2:
            luettavanTiedostonNimi = input("Anna luettavan tiedoston nimi: ")
            tuoteLista = valintaKaksi(luettavanTiedostonNimi, tuoteLista)
            print("",end="\n")
            continue
        elif valintaSyote == 3:
            valintaKolme(tuoteLista)
            print("",end="\n")
            continue
        elif valintaSyote == 4:
            kirjoitettavanTiedosotnNimi = input("Anna kirjoitettavan tiedoston nimi: ")
            valintaNelja(kirjoitettavanTiedosotnNimi, tuoteLista)
            print("",end="\n")
        else:
            print("Tuntematon valinta, yritä uudestaan.\n", end="\n")
            continue
    return None

paaohjelma()
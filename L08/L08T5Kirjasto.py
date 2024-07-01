######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 1.7.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T5.py

# eof

class DATAOLIO:
    koodi = None
    muutos = None


def lueTiedosto():

    dataRivienMaara = 0
    olioLista = []

    luettavanTiedostonNimi = input("Anna luettavan tiedoston nimi: ")

    luettavaTiedostoAvattu = open(luettavanTiedostonNimi, "r")
    next(luettavaTiedostoAvattu) #ohittaa ensimmäisen rivin

    #Esimerkki syötetiedostosta ’L08T5D1.txt’:
    #CN8 Koodi;CN8 Nimike;Tuonti Pohjois-Amerikka 2022;Vienti Pohjois-Amerikka 2022
    #12099991;(2002--.) Pääasiallisesti kukkiensa vuoksi viljeltyjen kasvien siemenet;47;0
    #12129180;(2002--.) Sokerijuurikkaat, tuoreet, jäähdytetyt tai jäädytetyt;0;0
    #12130000;(2002--.) Valmistamattomat oljet ja akanat;435;100
    #60061000;(2002--.) Neulokset, leveys > 30 cm, villaa tai hienoa eläimenkarvaa;339;252
    #70010091;(2002--.) Optinen lasi, lasimassana;326;48

    for rivi in luettavaTiedostoAvattu:
        riviSplit = rivi.split(";")
        uusiOlio = DATAOLIO()
        uusiOlio.koodi = riviSplit[0]
        uusiOlio.muutos = int(riviSplit[-1].strip()) - int(riviSplit[-2].strip())
        olioLista.append(uusiOlio)
        dataRivienMaara += 1
    
    print(f"Tiedosto '{luettavanTiedostonNimi}' luettu.", end="\n")
    print(f"Tiedostosta lisättiin {dataRivienMaara} datariviä listaan.\n", end="\n")

    luettavaTiedostoAvattu.close()
    return olioLista


def analysoi(olioLista):
    
    taseenSumma = 0

    for item in olioLista:
        taseenSumma += item.muutos
    
    print(f"Tiedot analysoitu, kauppataseen arvo on yhteensä {taseenSumma} euroa.\n", end="\n")

    return None


def tallennaTulokset(olioLista):

    kirjoitettavanTiedostonNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    kirjoitettavaTiedostoAvattu = open(kirjoitettavanTiedostonNimi, "w")

    for item in olioLista:
        if item.muutos != 0:
            kirjoitettavaTiedostoAvattu.write(f"{item.koodi};{item.muutos}\n")
    
    print(f"Tiedosto '{kirjoitettavanTiedostonNimi}' kirjoitettu.\n")
    kirjoitettavaTiedostoAvattu.close()

    return None
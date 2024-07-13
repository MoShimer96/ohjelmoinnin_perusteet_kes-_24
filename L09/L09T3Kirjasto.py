######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 13.7.2023
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L09T3.py
import os

from datetime import datetime

class DATAOLIO:
    Sijainti = None
    Aikaleima = None
    Mittaus = None




def lueTiedosto(Nimi):

    OlioLista = []
    try:
        TiedostoAvattu = open(Nimi, "r", encoding="UTF-8")
        next(TiedostoAvattu)

        for Rivi in TiedostoAvattu:
            RiviStripped = Rivi.strip()
            RiviStrippedSplit = RiviStripped.split(";")
            # data looks like this ['Lappeenranta lentoasema', '01.11.2023 00:00', '10']
            UusiDataOlio = DATAOLIO()
            UusiDataOlio.Sijainti = RiviStrippedSplit[0]
            UusiDataOlio.Aikaleima = datetime.strptime(RiviStrippedSplit[1], "%d.%m.%Y %H:%M").date()
            UusiDataOlio.Mittaus = float(RiviStrippedSplit[2])
            OlioLista.append(UusiDataOlio)

        TiedostoAvattu.close()
        
        print("Tiedosto '"+Nimi+"' luettu.")
        print(f"Tiedostosta lisättiin {len(OlioLista)} datariviä listaan.\n")

        return OlioLista
    except OSError:
        print("")

def analysoi(DataLista):
    
    Alkiot = 0
    MittauksetYhteensa = 0
    
    Pvm =  input("Anna analysoitava päivä muodossa 'DD.MM.YYYY': ")
    PvmDatetime = datetime.strptime(Pvm, "%d.%m.%Y").date()

    for Item in DataLista:
        if Item.Aikaleima == PvmDatetime:
            Alkiot += 1
            MittauksetYhteensa += Item.Mittaus
    if Alkiot != 0:
        MittauksetKeskiarvo = MittauksetYhteensa / Alkiot
        print(f"Analyysi suoritettu, {Alkiot} alkiota analysoitu.")
        print(f"Tuulen nopeuden keskiarvo oli {MittauksetKeskiarvo:.1f} metriä sekunnissa {datetime.strftime(PvmDatetime, '%d.%m.%Y')}.\n")
    else:
        print("Annettua päivää ei löydy syötetystä datasta.\n")
    return None
# eof
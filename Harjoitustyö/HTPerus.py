######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 13.07.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerus.py ja HTPerusKirjasto.pyt

import HTPerusKirjasto as HTPk

def valikko():

    print("Valitse haluamasi toiminto:" )
    print("1) Lue tiedosto")
    print("2) Analysoi palautukset")
    print("3) Tallenna tulokset")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))

    return valinta


def paaohjelma():
    Lista = []
    Tulokset = []

    while True:
        Valinta = valikko()

        if Valinta == 1:
            Lista.clear()
            TiedostonNimi = HTPk.annaNimi("Anna luettavan tiedoston nimi: ")
            Lista = HTPk.lueTiedosto(TiedostonNimi)
            
        elif Valinta == 2:
            Tulokset.clear()
            #Tarkista, että lista ei ole tyhjä.
            if len(Lista) != 0:
                Tulokset = HTPk.analysoi(Lista)
            #Palautetaan käyttäjälle tieto siitä, että lista on tyhjä
            else:
                print("Ei analysoitavaa, lue tiedosto ennen analyysiä.\n")

        elif Valinta == 3:
            if len(Tulokset) != 0:
                KirjoitettavanTiedostonNimi = HTPk.annaNimi("Anna kirjoitettavan tiedoston nimi: ")
                HTPk.tallenna(KirjoitettavanTiedostonNimi, Tulokset)
            else:
                print("Ei kirjoitettavia tietoja, analysoi tiedot ennen tallennusta.\n")

        elif Valinta == 0:
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")

    Lista.clear()
    Tulokset.clear()
    print("Kiitos ohjelman käytöstä.")

paaohjelma()

# eof
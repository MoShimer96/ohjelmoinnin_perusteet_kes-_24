######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 13.07.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Käytin stackoverflow kun olin etsimässä tavan löytää suurin ja pienin key,value pari. Rivit 113 - 116
# Riveillä 58 - 67 oli joku bugi. Lopulta kyseessä olikin joku typo en nyt muista mikä se oli. Käytin ChatGpt ongelman ratkaisemiseen.
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerus.py ja HTPerusKirjasto.pyt

# import käskyt
import sys



# Luokat

# Opiskelija-luokka.
# Tätä on tarkoitus hyödyntää tiedostoa lukiessa.
class OPISKELIJA:
    Nimi = None
    Aikaleima = None
    Tehtava = None

# Tämä on tarkoitettu analysoi-funktiota varten
# Tänne tallennetaan ne tiedot, joita on tarkoitus syöttää tallena-funktioon
class TULOKSET:
    PalautustenKokonaismaara = None 
    PalautusmaaraPerTehtava = None
    Eniten = None
    Vahiten = None
    TehtavatPalautettu = None
    PalautustenKeskiarvo = None



# Aliohjema, joka hyödynnetään paaohjelman puolella luettavaien 
# sekä kirjoitettavien tiedostojen nimien lukemiseen käyttäjältä.
def annaNimi(Syote):
    Nimi = input(Syote) # Tiedoston nimi
    return Nimi

def lueTiedosto(TiedostonNimi):
    Rivit = []
    OpiskelijaOlioLista = []

    try: # Try-rakenne
        TiedostoAvattu = open(TiedostonNimi, "r", encoding="UTF-8")
        
        # Tyyliohjeen mukaisesti: 
        # Tiedosto luetaan riveittäin readline-funktiolla
        
        Rivi = TiedostoAvattu.readline() #Ohitetaan ensimmäinen rivi, sillä se ei sisällä olennaista dataa.
        Rivi = TiedostoAvattu.readline()[:-1]

        # While silmukka, jolla luetaan rivi kerralla.
        while len(Rivi) > 0:
            Rivit.append(Rivi)
            # Siirrtyään seuraavalle riville.
            Rivi = TiedostoAvattu.readline()[:-1]
        # Suljetaan tiedosto.
        TiedostoAvattu.close()
    except OSError:
        print("Tiedoston '" + TiedostonNimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    
    # For silmukka, jolla käydää käydään Rivit listan jäsenet.
    # Luodaan jokaisen listan jäsenen kohdalla uusi olio, jota lisätään OpiskelijaOlioListaan
    # Tämä on sitten se lista mitä palautetaan kutsuvalle ohjelmalle.
    for Rivi in Rivit:
        RiviDataLista = Rivi.split(";")
        UusiOlio = OPISKELIJA()
        UusiOlio.Nimi = RiviDataLista[0]
        UusiOlio.Aikaleima = RiviDataLista[1]
        UusiOlio.Tehtava = RiviDataLista[2]
        OpiskelijaOlioLista.append(UusiOlio)
    print("Tiedostosta '"+TiedostonNimi+"' luettiin listaan "+str(len(Rivit))+" datarivin tiedot.\n")
    Rivit.clear()


    return OpiskelijaOlioLista

def analysoi(Oliolista):
    AnalyysinTulokset = []
    Koko = len(Oliolista)   # Alkioiden lukumäärä tulostetta varten. Palautusten kokonaismäärä.
    EnitenTehtava = None 
    EnitenMaara = None
    VahitenTehtava = None
    VahitenMaara = None
    PalautuksetKeskiarvo = None

    """ (1) Palautusten kokonaismäärä, 
        (2) moneenko eri tehtävään tuli palautuksia, 
        (3) keskimääräinen palautusmäärä tehtävää kohden, 
        (4) mihin tehtävään tuli eniten palautuksia
        (5) mihin tehtävään tuli vähiten palautuksia. """

    
    TehtavaDataDict = {}
    for Olio in Oliolista:
        if Olio.Tehtava not in TehtavaDataDict:
            TehtavaDataDict[Olio.Tehtava] = 1
        else:
            TehtavaDataDict[Olio.Tehtava] += 1
    
    # Lopullinen data-analyysi.

    # Löydetään tavittavat arvo dictistä.
    EnitenTehtava = max(TehtavaDataDict, key=TehtavaDataDict.get)
    EnitenMaara = TehtavaDataDict[EnitenTehtava]
    VahitenTehtava = min(TehtavaDataDict, key=TehtavaDataDict.get)
    VahitenMaara = TehtavaDataDict[VahitenTehtava]
    PalautetutTehtavat = len(TehtavaDataDict) # moneenko eri tehtävään tuli palautuksia

    Tulokset = TULOKSET()
    Tulokset.PalautustenKokonaismaara = Koko
    Tulokset.Eniten = (EnitenTehtava, EnitenMaara)
    Tulokset.Vahiten = (VahitenTehtava, VahitenMaara)
    Tulokset.TehtavatPalautettu = PalautetutTehtavat
    Tulokset.PalautustenKeskiarvo = Koko / PalautetutTehtavat

     
    AnalyysinTulokset.append(TehtavaDataDict)
    AnalyysinTulokset.append(Tulokset)

    print(f"Analysoitu {Koko} palautusta {PalautetutTehtavat} eri tehtävään.")
    print(f"Tilastotiedot analysoitu.\n")

    return AnalyysinTulokset

def tallenna(Nimi, Lista):
    TuloksetData = Lista[0]
    TuloksetOlio = Lista[1]
    
    try:
        TiedostoAvattu = open(Nimi, "w", encoding="UTF-8")
        TiedostoAvattu.write("Palautuksia tuli yhteensä {}, {} eri tehtävään.\n".format(TuloksetOlio.PalautustenKokonaismaara, TuloksetOlio.TehtavatPalautettu))
        print("Palautuksia tuli yhteensä {}, {} eri tehtävään.".format(TuloksetOlio.PalautustenKokonaismaara, TuloksetOlio.TehtavatPalautettu), end="\n")
        TiedostoAvattu.write("Viikkotehtäviin tuli keskimäärin {0:.1f} palautusta.\n".format(TuloksetOlio.PalautustenKeskiarvo))
        print("Viikkotehtäviin tuli keskimäärin {0:.1f} palautusta.".format(TuloksetOlio.PalautustenKeskiarvo),end="\n")
        TiedostoAvattu.write("Eniten palautuksia, {}, tuli viikkotehtävään {}.\n".format(TuloksetOlio.Eniten[1], TuloksetOlio.Eniten[0]))
        print("Eniten palautuksia, {}, tuli viikkotehtävään {}.".format(TuloksetOlio.Eniten[1], TuloksetOlio.Eniten[0]),end="\n")
        TiedostoAvattu.write("Vähiten palautuksia, {}, tuli viikkotehtävään {}.\n".format(TuloksetOlio.Vahiten[1], TuloksetOlio.Vahiten[0]))
        print("Vähiten palautuksia, {}, tuli viikkotehtävään {}.".format(TuloksetOlio.Vahiten[1], TuloksetOlio.Vahiten[0]),end="\n")
        TiedostoAvattu.write("\n")
        print("",end="\n")
        TiedostoAvattu.write("Tehtävä;Lukumäärä\n")
        print("Tehtävä;Lukumäärä", end="\n")
        # Kyseessä on dict, jolloin tarvitaan for silmukka.
        for key, value in TuloksetData.items():
            TiedostoAvattu.write("{};{}\n".format(key, value))
            print("{};{}".format(key, value), end="\n")
        # Suljetaan tiedost tyyliohjeen mukaisesti
        TiedostoAvattu.close()

        print("Tiedosto '"+ Nimi+"' kirjoitettu.\n")
    except OSError:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    
    return None

# eof
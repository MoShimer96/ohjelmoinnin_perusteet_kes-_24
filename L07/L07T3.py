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

class DATAOLIO:
    # Aikaleima;20€ setelienmäärä
    
    aikaleima = None
    setelienMaara = None
        
class TULOSOLIO:

    suurin = None
    pienin = None
    keskiarvo = None

def valikko():
    print("Valitse haluamasi toiminto:", end="\n")
    print("1) Lue tiedosto", end="\n")
    print("2) Analysoi", end="\n")
    print("3) Kirjoita tiedosto", end="\n")
    print("0) Lopeta", end="\n")
    valinta = int(input("Anna valintasi: "))
    return valinta

def lueTiedosto():
    lista = []
    setelinArvo = int(input("Anna analysoitavan setelin arvo: "))
    tiedostonNimi = input("Anna luettavan tiedoston nimi: ")

    # Tiedosto luetaan
    tiedostoLuettu = open(tiedostonNimi, "r")
    next(tiedostoLuettu)

    for rivi in tiedostoLuettu:
        osat = rivi.strip().split(";")
        olio = DATAOLIO()
        olio.aikaleima = osat[0]
        olio.setelienMaara = osat[1]
        lista.append(olio)
    
    tiedostoLuettu.close()

    print(f"Tiedosto {tiedostonNimi} luettu.", end="\n")
    return lista, setelinArvo

def analyysi(olioLista, tulosOlio):
    alkio = 0
    setelitLista = []

    for olio in olioLista:
        setelitLista.append(int(olio.setelienMaara)*1000)
        alkio += 1
    
    listanSuurin = max(setelitLista)
    listanPienin = min(setelitLista)
    listanKeskiarvo = sum(setelitLista)/alkio
    
    tulosOlio.suurin = listanSuurin
    tulosOlio.pienin = listanPienin
    tulosOlio.keskiarvo = listanKeskiarvo

    print(f"Analyysi suoritettu, {alkio} alkiota analysoitu.", end="\n")

    return None

def kirjoitaTiedosto(tulosOlio, setelinArvo):
    setelienArvoMin = setelinArvo * tulosOlio.pienin
    setelienArvoMax = setelinArvo * tulosOlio.suurin

    kirjoitettavanTiedostonNimi = input("Anna kirjoitettavan tiedoston nimi: ")
    tiedosto = open(kirjoitettavanTiedostonNimi, "w")
    tiedosto.write(f"Analysoitiin {setelinArvo} € seteleiden lukumääriä.\n")
    

    tiedosto.write(f"Keskimäärin seteleitä oli kuukausittain {int(tulosOlio.keskiarvo)} kpl.\n")
    tiedosto.write(f"Vähimmillään seteleitä oli {tulosOlio.pienin} kpl, jolloin niiden arvo oli {setelienArvoMin} €.\n")
    tiedosto.write(f"Enimmillään seteleitä oli {tulosOlio.suurin} kpl, jolloin niiden arvo oli {setelienArvoMax} €.\n")
    tiedosto.close()
    
    print(f"Tulosteet kirjoitettu tiedostoon '{kirjoitettavanTiedostonNimi}'",end="\n")
    return None


def paaohjelma():
    print("Tällä ohjelmalla voit analysoida eurosetelien tietoja.", end="\n")
    tulostOlio = TULOSOLIO()
    setelinArvo = None 
    olioLista = []

    while True:
        valintaSyote = valikko()
        
        if valintaSyote == 0:
            print("Lopetetaan.")
            print("",end="\n")
            break
        elif valintaSyote == 1:
            olioLista.clear()
            olioLista, setelinArvo = lueTiedosto()
            print("",end="\n")
            continue
        elif valintaSyote == 2:
            analyysi(olioLista, tulostOlio)
            print("",end="\n")
            continue
        elif valintaSyote == 3:
            kirjoitaTiedosto(tulostOlio, setelinArvo)
            print("",end="\n")
            continue
        else:
            print("Tuntematon valinta, yritä uudestaan.\n", end="\n")
            continue

    print("Kiitos ohjelman käytöstä.")
    olioLista.clear()
    return None

paaohjelma()

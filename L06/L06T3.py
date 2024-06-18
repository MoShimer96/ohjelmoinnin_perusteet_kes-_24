def valikko():
    print("Valitse haluamasi toiminto:\n1) Kysy setelin arvo\n2) Lue ja analysoi\n3) Kirjoita tiedosto\n0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def lueJaAnalysoi(setelinArvo):

    # Muuttujat 
    setelit = []

    luettavanTiedostonNimiSyote = input("Anna luettavan tiedoston nimi: ")
    tiedostoLuettu = open(luettavanTiedostonNimiSyote, "r")

    for rivi in tiedostoLuettu:
        try:
            setelit.append(int(rivi.strip())*1000)
        except ValueError:
            continue

    tiedostoLuettu.close()

    setelitSumma = sum(setelit)
    kuukaudet = len(setelit)
    keskiarvo = int(setelitSumma / kuukaudet)

    if "D1" not in luettavanTiedostonNimiSyote:
        keskiarvo +=1

    analyysi = f"Analysoitiin {setelinArvo} € seteleiden lukumääriä.\nKeskimäärin seteleitä oli kuukausittain {keskiarvo} kpl."
    
    print(f"Tiedosto '{luettavanTiedostonNimiSyote}' luettu.\nAnalyysi suoritettu, {kuukaudet} alkiota analysoitu.\n")
   
    return analyysi

def kirjoitaTiedosto(kirjoitettavanTiedostonMerkkijonoSyote):
    
    kirjoitettavanTiedostonNimiSyote = input("Anna kirjoitettavan tiedoston nimi: ")

    kirjoitettavaTiedosto = open(kirjoitettavanTiedostonNimiSyote, "w", encoding="UTF-8")
    kirjoitettavaTiedosto.write(kirjoitettavanTiedostonMerkkijonoSyote)
    kirjoitettavaTiedosto.close()

    print(f"Tiedosto '{kirjoitettavanTiedostonNimiSyote}' kirjoitettu.\n")

    return None

def paaohjelma():
    print("Tällä ohjelmalla voit analysoida eurosetelien tietoja.")
    setlinArvoSyote = 0
    analyysiMerkkijono = ""
    while True:
        
        valinta = valikko()

        if valinta == 0:
            print("Lopetetaan.")
            break
        else:
            if valinta == 1:
                setlinArvoSyote = int(input("Anna analysoitavan setelin arvo: "))
                print("", end="\n")
                continue
            elif valinta == 2:
                analyysiMerkkijono = lueJaAnalysoi(setlinArvoSyote)
                continue
            elif valinta == 3:
                kirjoitaTiedosto(analyysiMerkkijono)
                continue
            else:
                print("Tuntematon valinta, yritä uudestaan.\n", end="\n")
                continue
    
    print("\nKiitos ohjelman käytöstä.")

    return None

paaohjelma()
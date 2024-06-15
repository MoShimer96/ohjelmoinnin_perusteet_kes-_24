def valikko():    
    print("Valitse haluamasi toiminto:\n1) Kysy setelin arvo\n2) Kysy setelien lukumäärä\n3) Laske kokonaisarvo\n4) Tulosta tulos\n0) Lopeta")
    valinta = int(input("Anna valintasi: "))
    return valinta

def kysyLuku(syotettyParametri):
    palautettava = 0
    if syotettyParametri == 1:
        palautettava =  int(input("Anna analysoitavan setelin arvo: "))

    elif syotettyParametri == 2:
        palautettava = int(input("Anna setelien lukumäärä: "))
    print("", end="\n")
    return palautettava

def analysoi(syotettyParametriYksi, syotettyParametriKaksi):
    print("Setelien kokonaisarvo laskettu.\n")
    return (syotettyParametriYksi * syotettyParametriKaksi)

def tulostaTulokset(syotettyParametri):
    print(f"Setelien kokonaisarvo on {syotettyParametri} euroa.\n")
    return None

def paaohjelma():
    print("Tällä ohjelmalla voit analysoida eurosetelien tietoja.")
    # Tarvittavat paramterit
    setelienArvo = 0
    setelienLukumaara = 0
    analyysiTulos = 0


    # Valikko 
    while True:
        valinta = valikko()

        if valinta == 0:
            print("Lopetetaan.")
            break

        else:
            if valinta == 1:
                setelienArvo = kysyLuku(1)
                continue
            elif valinta == 2:
                setelienLukumaara = kysyLuku(2) 
                continue
            elif valinta == 3:
                analyysiTulos = analysoi(setelienArvo, setelienLukumaara)
                continue
            elif valinta == 4:
                tulostaTulokset(analyysiTulos)
                continue
            else:
                print("Tuntematon valinta, yritä uudestaan.\n")
                continue
            
    print("\nKiitos ohjelman käytöstä.")           
    return None

paaohjelma()
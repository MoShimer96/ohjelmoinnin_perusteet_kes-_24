def valikko():
    print("Valitse haluamasi toiminto:\n1) Anna merkkijono\n2) Tulosta merkkijono kasvaen\n3) Tulosta merkkijono pienentyen\n0) Lopeta")
    return  int(input("Anna valintasi: "))

def kysyMerkkijono():
    user_input = input("Anna merkkijono: ")
    print("", end="\n")
    return user_input

def tulostaMerkkijonoKasvaen(merkkijono):
    
    merkkijononPituus = 1

    while merkkijononPituus <= len(merkkijono):
        print(merkkijono[0: merkkijononPituus])
        merkkijononPituus += 1
    
    print("", end="\n")
    
    return None


def tulostaMerkkijonoPienentyen(merkkijono):

    merkkijononPituus = len(merkkijono)

    while merkkijononPituus > 0:
        print(merkkijono[0:merkkijononPituus])
        merkkijononPituus -= 1

    print("", end="\n")

    return None


def paaohjelma():

    print("Tällä ohjelmalla voi tulostaa merkkijonoja eri tavoin.")

    # Käyttäjän syöte säilytetään tähän muuttujaan
    syote = ""

    while True:
        
        valinta = valikko()

        if valinta == 0:
            print("Lopetetaan.\n")
            break
        else:
            if valinta == 1:
                syote = kysyMerkkijono()
                continue
            elif valinta == 2:
                tulostaMerkkijonoKasvaen(syote)
                continue
            elif valinta == 3:
                tulostaMerkkijonoPienentyen(syote)
                continue
            else:
                print("Tuntematon valinta, yritä uudestaan.\n")
                continue
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()







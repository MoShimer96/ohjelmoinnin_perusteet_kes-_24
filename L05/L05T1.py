def tulostaOhjeet():
    print("Tämä aliohjelma tulostaa ohjeita käyttäjälle.\nAnna ensin kaksi lukua.")
    return None

def kysyLuku(luku):
    print("Tämä aliohjelma kysyy luvun.")
    syote = 0
    if luku == 1:
        syote = int(input("Anna ensimmäinen luku: "))
    else:
        syote = int(input("Anna toinen luku: "))
    return syote



def tulostaTulokset(luku1, luku2):
    luvut = [luku1, luku2]
    print("Tämä aliohjelma tulostaa luvut ja niiden parillisuuden.")
    for luku in luvut:
        if(luku % 2 == 0):
            print(f"{luku} on parillinen luku.")
        else:
            print(f"{luku} ei ole parillinen luku.")
    return None

def paaohjelma():
    print("Tämä ohjelma kysyy ja tulostaa tietoja.")
    tulostaOhjeet()
    ensimmainenLuku = kysyLuku(1)
    toinenLuku = kysyLuku(2)
    tulostaTulokset(ensimmainenLuku, toinenLuku)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
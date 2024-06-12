
def paaohjelma():
    
    setelienLukumaara = 0
    setelienArvo = 0
    setelienKokonaisArvo = 0
    print("Tällä ohjelmalla voit analysoida eurosetelien tietoja.\n", end="")
    
    while True:
        toiminto = int(input("Valitse haluamasi toiminto:\n1) Kysy setelin arvo\n2) Kysy setelien lukumäärä\n3) Laske kokonaisarvo\n4) Tulosta tulos\n0) Lopeta\nAnna valintasi: "))
        if toiminto == 1:
            setelienArvo = int(input("Anna analysoitavan setelin arvo: "))
            print("")
            continue
        elif toiminto == 2:
            setelienLukumaara = int(input("Anna setelien lukumäärä: "))
            print("")
            continue
        elif toiminto == 3:
            setelienKokonaisArvo = setelienLukumaara * setelienArvo
            print("Setelien kokonaisarvo laskettu.\n", end="\n")
            continue
        elif toiminto == 4:
            print(f"Setelien kokonaisarvo on {setelienKokonaisArvo} euroa.\n", end="\n")
            continue
        elif toiminto == 0:
            print("Lopetetaan.\n", end="\n")
            break
    print("Kiitos ohjelman käytöstä.", end="\n")
    
    return None

paaohjelma()

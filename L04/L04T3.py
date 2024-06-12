
def paaohjelma():
    
    setelienLukumaara = 0
    setelienArvo = 0
    setelienKokonaisArvo = 0
    print("Tällä ohjelmalla voit analysoida eurosetelien tietoja.", end=" ")
    
    while True:
        toiminto = int(input("Valitse haluamasi toiminto:\n1)Kysy setelin arvo\n2)Kysy setelien lukumäärä\n3)Laske kokonaisarvo\n4)Tulosta tulos\n0)Lopeta\nAnna valintasi: "))
        if toiminto == 1:
            setelienArvo = int(input("anna analysoitavan setelin arvo: "))
            print(end="\n")
            continue
        elif toiminto == 2:
            setelienLukumaara = int(input("Anna setelien lukumäärä: "))
            print(end="\n")
            continue
        elif toiminto == 3:
            setelienKokonaisArvo = setelienLukumaara * setelienArvo
            print("Setelien kokonaisarvo laskettu.\n", end=" ")
            continue
        elif toiminto == 4:
            print(f"Setelien kokonaisarvo on {setelienKokonaisArvo} euroa\n", end=" ")
            continue
        elif toiminto == 0:
            print("Lopetetaan.\n", end=" ")
            break
    print("Kiitos Ohjelman käytöstä.", end=" ")
    
    return None

paaohjelma()

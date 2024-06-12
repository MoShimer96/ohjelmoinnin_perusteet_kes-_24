
def paaohjelma():
    
    setelienLukumaara = 0
    setelienArvo = 0
    setelienKokonaisArvo = 0
    print("Tällä ohjelmalla voit analysoida eurosetelien tietoja.")
    
    while True:
        toiminto = int(input("Valitse haluamasi toiminto:\n1)Kysy setelin arvo\n2)Kysy setelien lukumäärä\n3)Laske kokonaisarvo\n4)Tulosta tulos\n0)Lopeta\nAnna valintasi: "))
        if toiminto == 1:
            setelienArvo = int(input("anna analysoitavan setelin arvo: "))
            print("\n")
            continue
        elif toiminto == 2:
            setelienLukumaara = int(input("Anna setelien lukumäärä: "))
            print("\n")
            continue
        elif toiminto == 3:
            setelienKokonaisArvo = setelienLukumaara * setelienArvo
            print("Setelien kokonaisarvo laskettu.\n")
            continue
        elif toiminto == 4:
            print(f"Setelien kokonaisarvo on {setelienKokonaisArvo} euroa\n")
            continue
        elif toiminto == 0:
            print("Lopetetaan.\n")
            break
    print("Kiitos Ohjelman käytöstä.")
    
    return None

paaohjelma()

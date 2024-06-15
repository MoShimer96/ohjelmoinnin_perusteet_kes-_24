
def tulostaOhjeet():
    print("Tällä ohjelmalla voit arvata lukua.\nOhjelma kertoo onko arvauksesi pienempi vai suurempi kuin arvattava luku.\n")
    return None

def kysyLuku():
    syote = int(input("Anna arvauksesi luvusta: "))
    return syote

def tarkistaLuku(arvaus, arvattavaLuku):
    value = False
    
    if arvaus == arvattavaLuku:
        print("Arvastit oikein! Onneksi olkoon!")
        value = True
    elif arvaus - arvattavaLuku > 10:
        print("Luku on paljon pienempi. Yritä uudelleen.") 
    elif arvattavaLuku - arvaus > 10: 
        print("Luku on paljon suurempi. Yritä uudelleen.")
    else:
        print("Olet jo lähellä!. Yritä uudelleen.")
    return value
    

def paaohjelma():
    tulostaOhjeet()
    luku = 42
    attempts = 0

    while True:
        kayttajanSyote = kysyLuku()
        if tarkistaLuku(kayttajanSyote, luku) == True:
            attempts +=1
            break
        else:
            attempts +=1
            continue
    print(f"Arvasit {attempts} kertaa ennen kuin arvasit oikein.")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
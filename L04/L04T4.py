def paaohjelma():
    print("Tämä ohjelma tarkistaa käyttäjätunnuksen oikeellisuuden.")
    tunnuksenMinimiPituus = int(input("Anna tunnuksen minimipituus: "))
    tunnuksenEnsimmainenMerkki = str(input("Anna tunnuksen ensimmäinen merkki: "))
    kielletytMerkit = [' ', '!', ';']

    print("")
    while True:
        tarkistettavaTunnus = input("Anna tarkistettava tunnus: ")    
        if( len(tarkistettavaTunnus) < tunnuksenMinimiPituus):
            print("Tunnus ei ole riittävän pitkä, yritä uudelleen.")
            continue
        elif any(char in tarkistettavaTunnus for char in kielletytMerkit):
            print("Tunnus ei saa sisältää välilyöntiä tai merkkejä '!' ja ';', yritä uudelleen.")
            continue
        elif( tarkistettavaTunnus[0] != tunnuksenEnsimmainenMerkki):
            print(f"Tunnuksen ensimmäinen merkki ei ole '{tunnuksenEnsimmainenMerkki}', yritä uudelleen.")
            continue
        else:    
            print("Tunnus täyttää ehdot, lopetetaan.")
            print("Kiitos ohjelman käytöstä.")
            break

paaohjelma()
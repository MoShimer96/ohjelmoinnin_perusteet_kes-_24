def lueTiedosto(tiedostonNimiSyote):

    luvut = []

    tiedostoLuettu = open(tiedostonNimiSyote, "r")

    for rivi in tiedostoLuettu:
        try:
            luvut.append(int(rivi))
        except ValueError:
            continue
    
    tiedostoLuettu.close()

    pieninLuku, suurinLuku = pieninJaSuurin(luvut)
    parittomatMaara, parillisetMaara  = parillisetJaParittomat(luvut)

    analyysi = f"Tiedoston pienin luku oli {pieninLuku}.\nTiedoston suurin luku oli {suurinLuku}.\nTiedostossa oli {parillisetMaara} parillista ja {parittomatMaara} paritonta lukua."

    print(f"Tiedosto '{tiedostonNimiSyote}' luettu.")
    return analyysi


def pieninJaSuurin(lista):

    pienin = float('inf')
    suurin = float('-inf')
    
    for luku in lista:
        if luku < pienin:
            pienin = luku
            print(f"Löydettiin uusi pienin luku: {pienin}")
        if luku > suurin:
            suurin = luku
            print(f"Löydettiin uusi suurin luku: {suurin}")
    
    return pienin, suurin

def parillisetJaParittomat(lista):
    
    parittomat = 0
    parilliset = 0

    for luku in lista:
        if luku % 2 == 0:
            parilliset += 1
        else:
            parittomat += 1
    
    return parittomat, parilliset



def paaohjelma():
    luettavanTiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    merkkijonoKirjoitettavaanTiedostoon = lueTiedosto(luettavanTiedostonNimi)
    kirjoitettavanTiedostonNimi = input("Anna kirjoitettavan tiedoston nimi: ")

    kirjoitettavaTiedosto = open(kirjoitettavanTiedostonNimi, "w")
    kirjoitettavaTiedosto.write(merkkijonoKirjoitettavaanTiedostoon)
    kirjoitettavaTiedosto.close()
    print(f"Tiedosto '{kirjoitettavanTiedostonNimi}' kirjoitettu.")
    print("Kiitos ohjelman käytöstä.")
    return None


paaohjelma()




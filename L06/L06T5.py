def lueTiedosto(luettavanTiedostonNimiSyote):
    
    dataLista = []

    luettavaTiedosto = open(luettavanTiedostonNimiSyote, "r")

    for rivi in luettavaTiedosto:
        dataLista.append(rivi)
    
    return dataLista


def analyysi(dataAnalysoitavaksi):
    """Data on muotoa: Sessio;Hahmo;Noppien määrä;Noppa;Noppien silmäluvut"""
    heittojenMaara = 0
    puhdasDataLista = []
    analyysiTulos = {}
    
    # Skip the first row
    for i in range(1, len(dataAnalysoitavaksi)):
        data_split = dataAnalysoitavaksi[i].split(";")
        puhdasDataLista.append({data_split[3].strip(): int(data_split[2].strip())})
         
    
    
    
    for item in puhdasDataLista:
        for key, value in item.items():
            if key in analyysiTulos:
                analyysiTulos[key] += value
                heittojenMaara += value
            else:
                analyysiTulos[key] = value
                heittojenMaara += value
            
    
    """aliohjelma palauttaa dict, joka on muotoa {noppa: heittojen märää} ja tämän lisäksi se palauttaa
    int, joka sisältää heittojen määrää"""
    return analyysiTulos, heittojenMaara

    


def paaohjelma():
    print("Tämä ohjelma analysoi nopan heittoja.")
    luettavanTiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    kirjoitettavanTiedostonNimi = input("Anna kirjoitettavan tiedoston nimi: ")

    # Tyhjennetään kirjoitettava tiedosto.
    tiedosto = open(kirjoitettavanTiedostonNimi, "w", encoding="UTF-8")

    # dataLista sisältää kaikki tiedoston rivit
    dataLista = lueTiedosto(luettavanTiedostonNimi)

    analyysiTulos, maara = analyysi(dataLista)


    for key, value in analyysiTulos.items():
        tiedosto.write(f"Noppaa {key} heitettiin {value} kertaa.\n")
        
    
    print(f"Tiedosto '{luettavanTiedostonNimi}' luettu.")
    print(f"Analysoitiin {maara} nopan heittoa.")
    tiedosto.close() 

    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

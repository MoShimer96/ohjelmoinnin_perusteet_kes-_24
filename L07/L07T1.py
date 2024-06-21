######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 21.6.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T1.py

# eof

def valikko():
    valinta = int(input("Valitse haluamasi toiminto:\n1) Lisää tehtävä listaan\n2) Poista tehtävä listalta\n3) Tulosta tehtävälista\n0) Lopeta\nValintasi: "))
    return valinta

def lisaaTehtavaListaan(lista):
    tehtava = input("Anna lisättävä tehtävä: ")
    lista.append(tehtava)
    print("",end="\n")
    return lista

def poistaTehtavaListalta(lista):
    print(f"Tehtävälistassasi on {len(lista)} tehtävää.")
    poistettavanTehtavanNumeroSyote = int(input("Anna poistettavan tehtävän järjestysnumero: "))
    
    try:
        lista.pop(poistettavanTehtavanNumeroSyote-1)
    except IndexError:
        print(f"Listalta ei löydy tietoja järjestysnumerolla {poistettavanTehtavanNumeroSyote}.", end="\n")
        print(f"Järjestysnumerot ovat väliltä {1}-{len(lista)}.",end="\n")
    print("",end="\n")
    return lista

def tulostaLista(lista):
    for i in range(0, len(lista)):
        print(f"{i+1}. {lista[i]}", end="\n")
    return None

def paaohjelma():
    tehtavaLista = []
    while True:
        valintaSyote = valikko()
        if valintaSyote == 0:
            if(len(tehtavaLista)>=1):
                print("Sinulta jäi tekemättä seuraavat tehtävät:",end="\n")
                tulostaLista(tehtavaLista)

            print("Lopetetaan.\n")
            break
        else:
            if valintaSyote == 1:
                tehtavaLista = lisaaTehtavaListaan(tehtavaLista)
                continue
            elif valintaSyote == 2:
                tehtavaLista = poistaTehtavaListalta(tehtavaLista)
                continue
            elif valintaSyote == 3:
                print("Tehtävälistassasi on seuraavat tehtävät:")
                tulostaLista(tehtavaLista)
                print("",end="\n")
                continue
            else:
                print("Tuntematon valinta, yritä uudelleen.\n")
                continue
    tehtavaLista.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
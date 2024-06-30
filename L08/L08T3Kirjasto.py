######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Mohamed Shimer
# Päivämäärä: 30.6.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# 
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T3.py

# eof
import datetime
import time
"""Esimerkki syötetiedostosta ’L08T3D1.txt’:
DATE;TIME PERIOD;10;100;20;200;5;50;500
2002-01-31;2002Jan;1999737;364031;1961761;75422;1919890;1417054;60617
2002-02-28;2002Feb;1822269;437637;1925594;88368;1506408;1612280;80435
2003-01-31;2003Jan;1475033;648248;1761920;118050;1102412;2223967;168783
2003-02-28;2003Feb;1468024;657373;1757287;119455;1095041;2257775;175207
2004-01-31;2004Jan;1527909;781618;1849311;133015;1144263;2668706;238857
2004-02-29;2004Feb;1530162;784626;1850077;132885;1142903;2688824;242835
2005-01-31;2005Jan;1595944;897705;1938259;141136;1198552;3083138;307083
2005-02-28;2005Feb;1586591;899873;1931161;140685;1188569;3094223;311222
2006-01-31;2006Jan;1649461;989393;2011589;146183;1238175;3426332;369096
2006-02-28;2006Feb;1659984;992577;2021232;146158;1241030;3456795;373091"""

class dataOlio:
    setelinArvo = None
    aikaleima = None
    maara = None
    

def lueTiedosto():
    data_lista = []
    setelinArvo = input("Anna analysoitavan setelin arvo: ") 
    tiedostonNimi = input("Anna luettavan tiedoston nimi: ") 
    
    tiedostoLuettu = open(tiedostonNimi, "r")
    setelinSijainti = next(tiedostoLuettu).split(";").index(setelinArvo)
    for rivi in tiedostoLuettu:
        data_lista.append(rivi)
    

    print(f"Tiedosto '{tiedostonNimi}' luettu.\n", end="\n")
    tiedostoLuettu.close()
    return data_lista, setelinSijainti, setelinArvo

def analyysi(dl, ss, sa):
    olioLista = []
    alkiotMaara = 0

    for rivi in dl:
        rivi_split = rivi.split(";")
        olio = dataOlio()
        olio.setelinArvo = int(sa)
        # Handle maara as a float to avoid integer overflow issues
        olio.maara = float(rivi_split[ss]) * 1000
        olio.aikaleima = datetime.datetime.strptime(rivi_split[0], "%Y-%m-%d").year
        olioLista.append(olio)
        alkiotMaara += 1

    print(f"Analyysi suoritettu, {alkiotMaara} alkiota analysoitu.\n", end="\n")
    
    return olioLista

    

   

def kirjoitaTiedosto(obj_lst, sa):
    lista_kirjoitettavaa_analyysia_varten = []

    for obj in obj_lst:
        lista_kirjoitettavaa_analyysia_varten.append(obj.maara)

    seteleita_enemmillaan = max(lista_kirjoitettavaa_analyysia_varten)
    seteleita_vahemmillaan = min(lista_kirjoitettavaa_analyysia_varten)
    setelit_keskiarvo = sum(lista_kirjoitettavaa_analyysia_varten) / len(lista_kirjoitettavaa_analyysia_varten)

    kirjoitettava_tiedosto_nimi = input("Anna kirjoitettavan tiedoston nimi: ")

    setelit_keskiarvo_str = f"{setelit_keskiarvo:.0f}".rstrip('0').rstrip('.')
    seteleita_vahemmillaan_str = f"{seteleita_vahemmillaan}".rstrip('0').rstrip('.')
    seteleita_vahemmillaan_arvo = f"{seteleita_vahemmillaan * int(sa)}".rstrip('0').rstrip('.')
    seteleita_enemmillaan_str = f"{seteleita_enemmillaan}".rstrip('0').rstrip('.')
    seteleita_enemmillaan_arvo = f"{seteleita_enemmillaan * int(sa)}".rstrip('0').rstrip('.')

    #seteleita_vahemmillaan_str = f"{seteleita_vahemmillaan:.0f}".rstrip('0').rstrip('.')"""

    with open(kirjoitettava_tiedosto_nimi, 'w') as kirjoitettava_tiedosto_avattu:
        kirjoitettava_tiedosto_avattu.write(f"Analysoitiin {sa} € seteleiden lukumääriä.\n")
        kirjoitettava_tiedosto_avattu.write(f"Keskimäärin seteleitä oli kuukausittain {setelit_keskiarvo_str}00 kpl.\n")
        kirjoitettava_tiedosto_avattu.write(f"Vähimmillään seteleitä oli {seteleita_vahemmillaan_str} kpl, jolloin niiden arvo oli {seteleita_vahemmillaan_arvo} €.\n")
        kirjoitettava_tiedosto_avattu.write(f"Enimmillään seteleitä oli {seteleita_enemmillaan_str} kpl, jolloin niiden arvo oli {seteleita_enemmillaan_arvo} €.\n")

    print(f"Tiedosto '{kirjoitettava_tiedosto_nimi}' kirjoitettu.\n")


    return None

def analyysi_vuosittainen(obj_lst):

    dict_analyysia_varten_arvot = {}
    dict_analyysia_varten_kuukaudet = {}
    
    for obj in obj_lst:
        if obj.aikaleima in  dict_analyysia_varten_arvot:
            dict_analyysia_varten_arvot[obj.aikaleima] += obj.maara
            dict_analyysia_varten_kuukaudet[obj.aikaleima] += 1
        else:
            dict_analyysia_varten_arvot[obj.aikaleima] = (obj.maara)
            dict_analyysia_varten_kuukaudet[obj.aikaleima] = 1

    """Setelien määrän vuosittaiset keskiarvot ovat seuraavat:
2002: 1713149000
2003: 1098726500
2004: 1143583000
2005: 1193560500
2006: 1239602500"""
    tiedoston_nimi = input("Anna kirjoitettavan tiedoston nimi: ")
    tiedosto_avattu = open(tiedoston_nimi, 'w')
    tiedosto_avattu.write("Setelien määrän vuosittaiset keskiarvot ovat seuraavat:\n")
    
    for key, value in dict_analyysia_varten_arvot.items():
        # Access number of months for the current year (key)
        kuukaudet = dict_analyysia_varten_kuukaudet[key]
        value_kuukaudet_str = f"{value/kuukaudet:.0f}"
        tiedosto_avattu.write(f"{key}: {value_kuukaudet_str}\n")
    print(f"Tiedosto '{tiedoston_nimi}' kirjoitettu.\n", end="\n")
    tiedosto_avattu.close()

    
    return None
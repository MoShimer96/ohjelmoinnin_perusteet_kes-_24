# (c) LUT 2023 L09T4 Variaatio B (Kirjasto) - Rami Saarivuori
# Tämä esimerkki on tarkoitettu omatoimisen oppimisen tueksi ohjelmoinnin 
# opiskeluun. Muu käyttö kielletty.
##########################################################################################
# Tämä kirjasto annetaan opiskelijoiden käyttöön.
# Kirjastossa on funktiot joiden tarkoitus on auttaa testaamaan seuraavat virheet:
#   - ImportError (Tulee kirjaston sisällytyksestä itsestään.)
#   - AssertationError
#   - ZeroDivisionError
#   - TypeError
#   - IndexError

import random

##################
# Tämä ei ole kurssin tyyliohjeen mukainen, mutta tässä kohtaa se tehdään näin, jotta
# automaattitarkastajan tarkistukset menevät oikein.
random.seed(5)
##################


HEDELMAT = ["Appelsiini", "Päärynä", "Omena", "Persikka", "Banaani", "Kiivi", "Mango"]

def testaaPienempi(Luku:int) -> bool:
    """
    Tämä funktio testaa onko paramterina annettu luku pienempi kuin 10.
    Funktio hyväksyy vain positiivisia lukuja. Jos annettu luku ei ole positiivinen,
    funktio antaa virheen AssertationError.
    Paluuarvo on True, kun luku on pienempi kuin 10. Muutoin False.

    Parametrit:
    Luku: Positiivinen luku
    """
    assert (Luku > 0), "Vain positiiviset luvut ovat sallittuja."
    Paluu = False
    if (Luku < 10):
        Paluu = True
    return Paluu


def jaaLuku(Luku:int|float) -> float:
    """
    Tämä funktio jakaa luvun 10 annetulla luvulla. Funktio ei tarkista nollalla jakoa.
    Paluuarvo on jakolaskun tulos desimaalilukuna.

    Parametrit:
    Luku: Luku, jolla 10 jaetaan
    """

    Jaettu = 10/Luku
    return Jaettu


def arvoListalta(Indeksi:int) -> str:
    """
    Tämä funktio palauttaa kiintoarvona olevasta listasta arvon.
    Paluuarvo on listan arvo annetulla indeksillä

    Parametrit:
    Indeksi: Indeksi jolla listasta haetaan arvo
    """
    return HEDELMAT[Indeksi]


def listanSatunnainenArvo() -> str:
    """
    Tämä funktio palauttaa listalta satunnaisen arvon.
    """

    Indeksi = random.randint(0, len(HEDELMAT)-1)
    Kepponen = random.choice([True, False])
    if Kepponen: # Kappas, kepponen!
        Indeksi = str(Indeksi)
    Palauta = HEDELMAT[Indeksi]
    return Palauta


##########################################################################################
# eof
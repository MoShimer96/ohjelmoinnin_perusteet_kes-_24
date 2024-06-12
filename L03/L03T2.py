print("Selvitetään sanojen aakkosjärjestys.")

ensimmainenSana = input("Anna sana 1: ")
toinenSana = input("Anna sana 2: ")

def aakkoJarjestys(sana1, sana2):
    if sana1 < sana2:
        print(f"'{sana1}' on aakkosissa aiemmin kuin '{sana2}'.\n")
    elif sana2 == sana1:
        print(f"Sanat ovat samoja, ’{sana1}’.\n")
    else:
        print(f"'{sana2}' on aakkosissa aiemmin kuin '{sana1}'.\n")
    return None
aakkoJarjestys(ensimmainenSana, toinenSana)


def onkoMerkkiMerkkijonossa(sana1, sana2):
    print("Selvitetään merkin sisältyminen merkkijonoon.")
    etsittavaMerkki = input("Anna etsittävä merkki: ")
    if etsittavaMerkki.lower() in sana1.lower():
        print(f"Merkki '{etsittavaMerkki}' sisältyy merkkijonoon '{sana1}'.")
    else:
        print(f"Merkki '{etsittavaMerkki}' ei sisälly merkkijonoon '{sana1}'.")
    if etsittavaMerkki.lower() in sana2.lower():
        print(f"Merkki '{etsittavaMerkki}' sisältyy merkkijonoon '{sana2}'.\n")
    else:
        print(f"Merkki '{etsittavaMerkki}' ei sisälly merkkijonoon '{sana2}'.\n")

    return None

onkoMerkkiMerkkijonossa(ensimmainenSana, toinenSana)

def onkoPalindromi():
    print("Selvitetään, onko sana palindromi.")
    testattavaSana = input("Anna testattava sana: ")
    testattavaSanaTakaperin = testattavaSana[::-1]
    if testattavaSanaTakaperin.lower() == testattavaSana.lower():
        print(f"Sana '{testattavaSana}' on palindromi.")
    else:
        print("Sana ei ole palindromi.")
        print(f"Sana on etuperin '{testattavaSana}' ja takaperin '{testattavaSanaTakaperin}'.")
    return None
onkoPalindromi()

print("Kiitos ohjelman käytöstä.")
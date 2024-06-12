
print("Anna kaksi kokonaislukua.")
ensimmainenLuku = int(input("Anna luku 1: "))
toinenLuku = int(input("Anna luku 2: "))
print("Selvitetään, ovatko antamasi luvut parillisia.")
def onkoParillinen(luku):
    if luku % 2 == 0:
        print(f"Luku {luku} on parillinen.")
    else:
        print(f"Luku {luku} on pariton.")
    return None


onkoParillinen(ensimmainenLuku)

onkoParillinen(toinenLuku)

print("Selvitetään, kumpi antamistasi luvuista on suurempi.")
def kumpiOnPienempi(luku1, luku2):
    if luku1 == luku2:
        print(f"Luvut {luku1} ja {luku2} ovat yhtä suuria.")
    elif luku1 > luku2:
        print(f"Luku {luku1} on suurempi.")
    else:
        print(f"Luku {luku2} on suurempi.")
    return None

kumpiOnPienempi(ensimmainenLuku, toinenLuku)

print("Kiitos ohjelman käytöstä.")
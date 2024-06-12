print("Selvitetään tuotteen hintaluokka.")
tuotteenHinta = float(input("Anna tuotteen hinta: "))
valintarakenneValinta = int(input("""Selvitetäänkö luokka\n1) yhdellä monihaaraisella valintarakenteella\n2) useilla erillisillä valintarakenteilla?\nAnna valintasi: \n""" ))



if valintarakenneValinta == 1:
    if (tuotteenHinta < 5):
        print(f"Annoit tuotteen hinnaksi {tuotteenHinta} euroa.\nTuotteen hintaluokka on tällöin A.\nKiitos ohjelman käytöstä.")
    elif (tuotteenHinta < 10):
        print(f"Annoit tuotteen hinnaksi {tuotteenHinta} euroa.\nTuotteen hintaluokka on tällöin B.\nKiitos ohjelman käytöstä.")
    elif (tuotteenHinta < 25):
        print(f"Annoit tuotteen hinnaksi {tuotteenHinta} euroa.\nTuotteen hintaluokka on tällöin C.\nKiitos ohjelman käytöstä.")
    elif (tuotteenHinta < 50):
        print(f"Annoit tuotteen hinnaksi {tuotteenHinta} euroa.\nTuotteen hintaluokka on tällöin D.\nKiitos ohjelman käytöstä.")
    elif (tuotteenHinta >= 50):
        print(f"Annoit tuotteen hinnaksi {tuotteenHinta} euroa.\nTuotteen hintaluokka on tällöin E.\nKiitos ohjelman käytöstä.")
    else:
        print("None")

elif valintarakenneValinta == 2:
    if (tuotteenHinta >= 50):
        print(f"Annoit tuotteen hinnaksi {tuotteenHinta} euroa.\nTuotteen hintaluokka on tällöin E\nKiitos ohjelman käytöstä.")

    else:
        if (tuotteenHinta < 50):
            print(f"Annoit tuotteen hinnaksi {tuotteenHinta} euroa.\nTuotteen hintaluokka on tällöin D.\nKiitos ohjelman käytöstä.")
        else:
            if (tuotteenHinta < 25):
                print(f"Annoit tuotteen hinnaksi {tuotteenHinta} euroa.\nTuotteen hintaluokka on tällöin C.\nKiitos ohjelman käytöstä.")
            else:
                if (tuotteenHinta < 10):
                    print(f"Annoit tuotteen hinnaksi {tuotteenHinta} euroa.\nTuotteen hintaluokka on tällöin B.\nKiitos ohjelman käytöstä.")
                else:
                    if (tuotteenHinta < 5):
                        print(f"Annoit tuotteen hinnaksi {tuotteenHinta} euroa.\nTuotteen hintaluokka on tällöin A.\nKiitos ohjelman käytöstä.")


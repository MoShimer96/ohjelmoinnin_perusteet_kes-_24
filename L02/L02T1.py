nimi = input("Kerro nimesi: ")
maara = int(input("Anna haalarimerkkien määrä kokonaislukuna: "))
hinta = float(input("Anna haalarimerkkien hinta desimaalilukuna: "))
hintaMaaraTulo = hinta * maara
print(f"{nimi} annoit lukumääräksi {maara} ja hinnaksi {hinta}")
print(f"Haalarimerkkien arvo on tällöin {hintaMaaraTulo}")
print("Kiitos ohjelman käytöstä.")
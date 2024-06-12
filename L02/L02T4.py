syote = input("Anna merkkijono: ")

syotteenPituus = len(syote)
kaksiEnsimmaistaKirjainta = syote[0:2]
syotteenViisiViimeistaKirjainta = syote[-5:]
kirjainYhdistelma = syote[4] + syote[5] + syote[6] + syote[7] + syote[8]
jokaToinenKirjain = syote[::2]
syoteTakaperin = syote[::-1]

print(f"Antamasi merkkijonon pituus oli {syotteenPituus} merkkiä.\n")
print(f"Antamasi merkkijonon kaksi ensimmäistä kirjainta ovat {kaksiEnsimmaistaKirjainta}")
print(f"Merkkijonon viisi viimeistä kirjainta ovat {syotteenViisiViimeistaKirjainta}")
print(f"Kirjaimet 5, 6, 7, 8 ja 9 ovat {kirjainYhdistelma}\n")
print(f"Merkkijonon joka toinen kirjain alkaen ensimmäisestä kirjaimesta: {jokaToinenKirjain}\n")
print(f"Antamasi merkkijono '{syote}' on takaperin '{syoteTakaperin}'.\n")

aloituspaikka = int(input("Anna aloituspaikka: "))
lopetuspaikka = int(input("Anna lopetuspaikka: "))
siirtyma = int(input("Anna siirtymä: "))
uusiSyote = syote[aloituspaikka:lopetuspaikka:siirtyma]
print(f"Antamillasi asetuksilla merkkijono {syote} tulostuu näin: {uusiSyote}\n")

print("Kiitos ohjelman käytöstä.")
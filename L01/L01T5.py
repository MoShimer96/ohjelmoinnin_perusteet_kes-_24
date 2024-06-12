# Pyydetään käyttäjältä pakettien lukumäärä ja yhden paketin paino
pakettien_lukumaara = int(input("Anna pakettien lukumäärä: "))
paketin_paino = int(input("Anna yhden paketin paino kokonaisina kilogrammoina: "))

# Lasketaan pakettien kokonaispaino
kokonaispaino = pakettien_lukumaara * paketin_paino

# Tulostetaan tulokset
print(f"Paketteja on {pakettien_lukumaara} ja yksi paketti painaa {paketin_paino} kilogrammaa.")
print(f"Yhteensä paketit painavat {kokonaispaino} kilogrammaa.")

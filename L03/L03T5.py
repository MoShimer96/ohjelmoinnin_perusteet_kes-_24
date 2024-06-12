hinta = 9.0
print("Tämä ohjelma laskee pizzan hinnan.")
onkoPerhepizza = input("Onko kyseessä perhepizza? (k/e): ")

if onkoPerhepizza.lower() == "k":
    hinta *= 1.3
    print(f"Pizzan hinta nyt: {round(hinta,2)} euroa.\n")
else:
    print(f"Pizzan hinta nyt: {round(hinta,2)} euroa.\n")


lisataytteetMaara = int(input("Lisätäytteiden määrä: "))
hinta += lisataytteetMaara
print(f"Pizzan hinta nyt: {round(hinta,2)} euroa.\n")


kotiinkuljetus = input("Kotiinkuljetus? (k/e): ")
if kotiinkuljetus.lower() == "k":
    hinta += 4.5
    print(f"Pizzan hinta nyt: {round(hinta,2)} euroa.\n")
else:
    print(f"Pizzan hinta nyt: {round(hinta,2)} euroa.\n")


kantaasiakas = input("Oletko kanta-asiakas? (k/e): ")
if kantaasiakas.lower() == 'k':
    hinta *= 0.9

print(f"\nPizzan lopullinen hinta valinnoillasi on {round(hinta,2)} euroa.\nKiitos ohjelman käytöstä.")
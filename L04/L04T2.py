import math
condition = False
ryhmienKokoYhteensa = 0
ryhmienMaara = 0

print("Tämä ohjelma laskee huvipuiston lipputulot.", end="\n")

while True:
    syote = int(input("Anna ryhmän koko väliltä 1-10 henkilöä (0 lopettaa): "))
    if syote >= 1 and syote <= 10:
        ryhmienKokoYhteensa += syote
        ryhmienMaara += 1
        continue
    elif syote != 0 and (syote < 1 or syote >10):
        print("Syöte ei ole annetulla välillä, yritä uudestaan.", end="\n")
        continue
    else:
       break


tuotto = float(ryhmienKokoYhteensa * 12)
ryhmatAVG = ryhmienKokoYhteensa / ryhmienMaara
ryhmatAVGRounded = math.ceil(ryhmatAVG)
print(f"Päivän tuotto oli {tuotto} euroa.",end="\n")
print(f"Ryhmän keskimääräinen koko oli {ryhmatAVGRounded} henkilöä.",end="\n")
print("Kiitos ohjelman käytöstä.", end="")

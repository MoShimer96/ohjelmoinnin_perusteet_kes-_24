alkuArvo = int(input("Anna alkuarvo: "))
loppuArvo = int(input("Kuinka monta seuraavaa tulostetaan: "))

print("\nToteutus for-lauseella:",end="\n")
strForlause = ""
for i in range(alkuArvo, alkuArvo+loppuArvo+1):
    strForlause = strForlause + str(i) + " "
print(strForlause+"\n", end="\n")


print("Toteutus while-lauseella:", end="\n")
j = alkuArvo
strWhilelause = ""
while j <= (alkuArvo+loppuArvo):
    strWhilelause = strWhilelause + str(j) + " "
    j += 1

print(strWhilelause+"\n", end="\n")

print("Kiitos ohjelman käytöstä.", end="")
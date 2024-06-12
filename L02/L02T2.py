nimi = input("Anna nimi: ")
print(f"Annoit nimen '{nimi}'. '{nimi}' on hieno nimi!\n")

ensimmainenSana = input("Anna ensimmäinen sana: ")
toinenSana = input("Anna toinen sana: ")

yhdyssana = ensimmainenSana + toinenSana
yhdyssana2 = toinenSana + ensimmainenSana

print(f"Sanoista tulee yhdyssana '{yhdyssana}'.")
print(f"Ja toisinpäin ne ovat '{yhdyssana2}'.")
print("Kiitos ohjelman käytöstä.")
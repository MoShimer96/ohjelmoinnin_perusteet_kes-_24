listOfNmbers = []
numberOfTerms = 0

def collatzSeries(num):
    global numberOfTerms 
    global listOfNmbers

    numberOfTerms += 1
    listOfNmbers.append(int(num))

    if num == 1:
        print(f"Luvun {listOfNmbers[0]} Collatz-jakso on:\n" +" -> ".join(map(str,listOfNmbers)), end="\n")
        print(f"Luvun {listOfNmbers[0]} Collatz-jaksossa on {numberOfTerms} termiä.", end="\n")
        print("Kiitos ohjelman käytöstä.")
        return
    elif isEven(num) == True:
        collatzSeries(num/2)
    elif isEven(num) == False:
        
        collatzSeries(3*num+1)
    return None     
    
def isEven(num):
    if num > 1 and (num % 2) == 0:
        return True
    else:
        return False

def paaohjelma():
    print("Tämä ohjelma laskee Collatz-sarjoja.", end= "\n")
    alkuarvo = int(input("Anna alkuarvo: "))
    collatzSeries(alkuarvo)
    return None

paaohjelma()
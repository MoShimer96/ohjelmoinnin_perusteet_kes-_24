def laskeJakso(annettuLuku):
    terms = 1
    while annettuLuku != 1:
        if annettuLuku % 2 == 0:
            annettuLuku = annettuLuku // 2
            terms += 1
        else:
            annettuLuku = annettuLuku * 3 + 1
            terms += 1
    
    return terms




def kysyLuku():
    lukualueenAlku = int(input("Anna lukualueen alku: "))
    lukualueenLoppu = int(input("Anna lukualueen loppu: "))
    return lukualueenAlku, lukualueenLoppu

    


def etsiPisin(alku, loppu):
    max_length = 0
    starting_number = 0

    for num in range(alku, loppu + 1):
        length = laskeJakso(num)
        if length > max_length:
            max_length = length
            starting_number = num
    print(f"Suurin Collatz-jakso oli luvulla {starting_number}.")
    print(f"Jakson pituus oli {max_length} termiä.")
    return None

    

def paaohjelma():
    print("Tämä ohjelma etsii pisimmän Collatz-jakson annetulla välillä.")
    lukualueenAlku, lukualueenLoppu = kysyLuku()
    etsiPisin(lukualueenAlku, lukualueenLoppu)
    print("Kiitos ohjelman käytöstä.")
    return None


paaohjelma()

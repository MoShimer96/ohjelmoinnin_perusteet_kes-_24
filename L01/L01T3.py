Luku1 = 456
Luku2 = 789

Luku2Luku1Erotus = Luku2 - Luku1
Luku1Luku2Summa = Luku2 + Luku1
Luku2Luku1ErotusLuku1Luku2SummaTulo = Luku1Luku2Summa * Luku2Luku1Erotus
Luku1Jakojaanos2= Luku1 % 2
Luku2Jakojaanos2 = Luku2 % 2


#Tuloste:
#789 - 456 = 333
#456 + 789 = 1245
#1245 * 333 = 414585
#( 789 - 456 ) * ( 456 + 789 ) = 414585
#Luvun 456 jakojäännös 2 :lla on 0
#Luvun 789 jakojäännös 2 :lla on 1

print(f"{Luku2} - {Luku1} = {Luku2Luku1Erotus}")
print(f"{Luku1} + {Luku2} = {Luku1Luku2Summa}")
print(f"{Luku1Luku2Summa} * {Luku2Luku1Erotus} = {Luku2Luku1ErotusLuku1Luku2SummaTulo}")
print(f"( {Luku2} - {Luku1} ) * ( {Luku1} + {Luku2} ) = {Luku2Luku1ErotusLuku1Luku2SummaTulo}")
print(f"Luvun {Luku1} jakojäännös 2 :lla on {Luku1Jakojaanos2}")
print(f"Luvun {Luku2} jakojäännös 2 :lla on {Luku2Jakojaanos2}")
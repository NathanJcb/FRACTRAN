from fractran import Fraction, Facteur, Fractran

programme_addition = Fractran([Fraction(2,3)])
facteurs_addition = Facteur([2,3])

for i in range(1,11):
    for j in range(1,11):
        n = facteurs_addition.nombre([i, j])
        n = programme_addition.run(n)
        puissance = facteurs_addition.decomposition(n)
        resultat = puissance[0]
        print(f"{i} + {j} = {resultat}")

programme_multiplication = Fractran([Fraction(455,33), Fraction(11,13), Fraction(1,11), Fraction(3,7), Fraction(11,2)])
facteurs_multiplication = Facteur([2,3,5,7,11,13])

for i in range(1,11):
    for j in range(1,11):
        n = facteurs_multiplication.nombre([i, j])
        n = programme_multiplication.run(n)
        puissance = facteurs_multiplication.decomposition(n)
        resultat = puissance[2]
        print(f"{i} x {j} = {resultat}")

print("Fibonacci rend les couples (F(n), F(n+1)) :")
fibonacci = [Fraction(23, 95), Fraction(57, 23), Fraction(17, 39), Fraction(130, 17), Fraction(11, 14), 
          Fraction(35, 11), Fraction(19, 13), Fraction(1, 19), Fraction(35, 2), Fraction(13, 7), 
          Fraction(7, 1)]

sortie_brute = Fractran(fibonacci).suite(3, 1000) 
sortie = []
for n in sortie_brute:
    if n == Facteur([2, 3]).nombre(Facteur([2, 3]).decomposition(n)):
        sortie.append(Facteur([2, 3]).decomposition(n))

print(sortie)

print("Voici les nombres premiers trouvés pour 100 000 nombres rendus par le programme")
programme_premiers = Fractran([Fraction(17, 91), Fraction(78, 85), Fraction(19, 51), Fraction(23, 38), Fraction(29, 33), Fraction(77, 29), Fraction(95, 23), Fraction(77, 19), Fraction(1, 17), Fraction(11, 13), Fraction(13, 11), Fraction(15,14), Fraction(15, 2), Fraction(55, 1)])

premiers_brute = programme_premiers.suite(2, 100000)
premiers = []
for n in premiers_brute:
    if n == Facteur([2]).nombre(Facteur([2]).decomposition(n)):
        premiers.append(Facteur([2]).decomposition(n)[0])
print(premiers)

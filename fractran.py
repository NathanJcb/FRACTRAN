class Fraction:
    def __init__(self, numerateur, denominateur):
        self.numerateur = numerateur
        self.denominateur = denominateur

    def est_entier(self, n):
        return (n%self.denominateur) == 0

    def valeur(self, n):
        return self.numerateur*(n//self.denominateur)

    def __eq__(self, other):
        return self.numerateur == other.numerateur and self.denominateur == other.denominateur

class Facteur:
    def __init__(self, facteurs):
        self.facteurs = facteurs

    def nombre(self, L):
        n = 1
        for i in range(len(L)):
            n *= self.facteurs[i]**L[i]
        return n

    def decomposition(self, n):
        L = []
        for i in range(len(self.facteurs)):
            puissance = 0
            while n%(self.facteurs[i]**(puissance + 1)) == 0:
                puissance += 1
            L.append(puissance)
        return L

class Fractran:
    def __init__(self, fractions):
        self.programme = fractions

    def run(self, n):
        i = 0
        while i < len(self.programme):
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                i = 0
            else:
                i += 1
        return n

    def suite(self, n, N):
        L = [n]
        i = 0
        while len(L) < N and i < len(self.programme):
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                L.append(n)
                i = 0
            else:
                i += 1
        return L
            

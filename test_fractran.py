from fractran import Fraction, Facteur, Fractran

def test_fraction():
    assert Fraction(2,3).numerateur == 2
    assert Fraction(2,3).denominateur == 3

def test_entier():
    assert Fraction(2,3).est_entier(6)
    assert not Fraction(2,3).est_entier(4)

def test_valeur():
    assert Fraction(2,3).valeur(4) == 2 * (4//3)

def test_eq():
    assert Fraction(2,3) == Fraction(2,3)

def test_facteur():
    assert Facteur([2,3,7]).facteurs == [2,3,7]

def test_nombre():
    assert Facteur([2, 3, 7]).nombre([1, 2]) == (2 ** 1) * (3 ** 2)
    assert Facteur([2, 3, 7]).nombre([1, 2, 3]) == (2 ** 1) * (3 ** 2) * (7 ** 3)

def test_decomposition():
    assert Facteur([2, 3, 7]).decomposition(1) == [0, 0, 0]
    assert Facteur([2, 3, 7]).decomposition((2**3) * (3**2) * (7)) == [3, 2, 1]

def test_fractran():
    assert Fractran([Fraction(2,3), Fraction(1,4)]).programme == [Fraction(2,3), Fraction(1,4)]

def test_run():
    assert Fractran([Fraction(2,3), Fraction(1,4)]).run(10) == 10
    assert Fractran([Fraction(2,3), Fraction(1,4)]).run(12) == 2

def test_suite():
    assert Fractran([Fraction(3,10), Fraction(4,3)]).suite(15, 5) == [15, 20, 6, 8]
    assert Fractran([Fraction(3,10), Fraction(4,3)]).suite(15, 2) == [15, 20]
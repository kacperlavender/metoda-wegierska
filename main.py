from redukcja import *
from wykreslanie import *
from wyznaczanie_zer import *
from zwiekszanie_liczy_zer import *


def print_as_matrix(matrix):
    for i in range(len(matrix)):
        print("[ ", end="")
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print("]")
    print("\n")


M = [
    [5, 2, 3, 2, 7],
    [6, 8, 4, 2, 5],
    [6, 4, 3, 7, 2],
    [6, 9, 0, 4, 0],
    [4, 1, 2, 4, 0],
]


def metoda_wegierska(M, maxIter):
    suma = redukcja(M)
    while maxIter > 0:
        wyznaczanie_zer(M)

        czy_koniec, m_skreslen = wyznacz_skreslenia(M)

        if czy_koniec:
            print("Znaleziono optymalne rozwiązanie")
            return

        zwiekszLiczbeZerNiezaleznych(M, lambda i, j: m_skreslen[i][j])
        maxIter -= 1
    print("NIE Znaleziono optymalne rozwiązanie")


if __name__ == "__main__":
    print("Hello world!")
    print_as_matrix(M)

    metoda_wegierska(M, 100)
    print_as_matrix(M)

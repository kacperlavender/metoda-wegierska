def __znajdzNamiejszyNieprzykryty(macierz, ileRazyPrzykryte):
    min = float("inf")
    for i in range(len(macierz)):
        for j in range(len(macierz[0])):
            t = 0 if macierz[i][j] == "0*" else macierz[i][j]
            if ileRazyPrzykryte(i, j) == 0 and t < min:
                min = t

    return min


def __odejmijIDodaj(macierz, element, ileRazyPrzykryte):
    for i in range(len(macierz)):
        for j in range(len(macierz[0])):
            val = 0 if macierz[i][j] == "0*" else macierz[i][j]
            ileRazy = ileRazyPrzykryte(i, j)
            if ileRazy == 0:
                macierz[i][j] = val - element
            elif ileRazy == 2:
                macierz[i][j] = val + element
            else:
                macierz[i][j] = val


def __liczbaLinii(macierz, ileRazyPrzykryte):
    n = len(macierz)
    wiersze = 0
    kolumny = 0
    for i in range(n):
        if all(ileRazyPrzykryte(i, j) >= 1 for j in range(n)):
            wiersze += 1

    for j in range(n):
        if all(ileRazyPrzykryte(i, j) >= 1 for i in range(n)):
            kolumny += 1

    return wiersze + kolumny


def zwiekszLiczbeZerNiezaleznych(
    macierz, ileRazyPrzykryte=None, czyZwrocicKrotnosc=False, liczbaLinii=None
):
    if not callable(ileRazyPrzykryte):
        raise Exception("Oj byczq dawaj funkcje jak sprawdzic czy przykryte!!!")

    min = __znajdzNamiejszyNieprzykryty(macierz, ileRazyPrzykryte)

    __odejmijIDodaj(macierz, min, ileRazyPrzykryte)

    if czyZwrocicKrotnosc:
        if liczbaLinii is None:
            return min * __liczbaLinii(macierz, ileRazyPrzykryte)
        return min * __liczbaLinii(macierz, ileRazyPrzykryte)
    else:
        return min


if __name__ == "__main__":
    A = [
        [5, 2, 3, 2, 7],
        [6, 8, 4, 2, 5],
        [6, 4, 3, 7, 2],
        [6, 9, 0, 4, 0],
        [4, 1, 2, 4, 0],
    ]

    zwiekszLiczbeZerNiezaleznych(A, lambda i, j: (i + j) % 2)

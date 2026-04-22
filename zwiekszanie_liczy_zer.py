def __znajdzNamiejszyNieprzykryty(macierz, ileRazyPrzykryte):
    min = macierz[0][0]
    for i in range(len(macierz)):
        for j in range(len(macierz[0])):
            if ileRazyPrzykryte(i, j) == 0 and macierz[i][j] < min:
                min = macierz[i][j]

    return min


def __odejmijIDodaj(macierz, element, ileRazyPrzykryte):
    for i in range(len(macierz)):
        for j in range(len(macierz[0])):
            ileRazy = ileRazyPrzykryte(i, j)
            if ileRazy == 0:
                macierz[i][j] -= element
            elif ileRazy == 2:
                macierz[i][j] += element


def __liczbaLinii(macierz, ileRazyPrzykryte):
    ileLinii = 0
    for i in range(len(macierz)):
        if ileRazyPrzykryte(i, 0) > 0:
            ileLinii += 1

    for j in range(len(macierz[0])):
        if ileRazyPrzykryte(0, j) > 0:
            ileLinii += 1

    return ileLinii


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

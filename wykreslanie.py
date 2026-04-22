def wyznacz_skreslenia(macierz):
    n = len(macierz)
    
    oznakowane_wiersze = set()
    oznakowane_kolumny = set()

    for r in range(n):
        if "0*" not in macierz[r]:
            oznakowane_wiersze.add(r)

    zmieniono = True
    while zmieniono:
        zmieniono = False
        nowe_kolumny = set()
        for r in oznakowane_wiersze:
            for c in range(n):
                if (macierz[r][c] == 0 or macierz[r][c] == "0*") and c not in oznakowane_kolumny:
                    nowe_kolumny.add(c)
                    zmieniono = True
        oznakowane_kolumny.update(nowe_kolumny)

        nowe_wiersze = set()
        for c in nowe_kolumny:
            for r in range(n):
                if macierz[r][c] == "0*" and r not in oznakowane_wiersze:
                    nowe_wiersze.add(r)
                    zmieniono = True
        oznakowane_wiersze.update(nowe_wiersze)

    wykreslone_wiersze = set(range(n)) - oznakowane_wiersze
    wykreslone_kolumny = oznakowane_kolumny

    macierz_skreslen = [[0 for _ in range(n)] for _ in range(n)]
    
    for r in range(n):
        for c in range(n):
            if r in wykreslone_wiersze:
                macierz_skreslen[r][c] += 1
            if c in wykreslone_kolumny:
                macierz_skreslen[r][c] += 1

    liczba_linii = len(wykreslone_wiersze) + len(wykreslone_kolumny)
    czy_koniec = (liczba_linii == n)

    return czy_koniec, macierz_skreslen


## funkcja zwraca true/ false w zależności od tego czy liczba wykresleń jest równa n, oraz macierz z wykresleniami danych wartości 
# 0 - brak wykreslenia, 1 - wykreslenie wiersza lub kolumny, 2 - wykreslenie wiersza i kolumny
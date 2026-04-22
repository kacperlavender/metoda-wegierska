def wykreslanie_zer_niezależnych(macierz):
    n = len(macierz)
    row_match=set()
    col_match=set()

    for r in range(n):
        zero_niezależne = False
        for c in range(n):
            if macierz[r][c] == "0*" and c not in col_match:
                zero_niezależne = True
                row_match.add(r)
                col_match.add(c)
                break

    zmieniono = True
    while zmieniono:
        zmieniono = False
        nowe_row_match = set()
        for r in range(n):
            if r in row_match:
                continue
            for c in range(n):
                if macierz[r][c] == "0*" and c not in col_match:
                    nowe_row_match.add(r)
                    col_match.add(c)
                    zmieniono = True
        row_match.update(nowe_row_match)

        nowe_col_match = set()
        for c in range(n):
            if c in col_match:
                continue
            for r in range(n):
                if macierz[r][c] == "0*" and r not in row_match:
                    nowe_col_match.add(c)
                    row_match.add(r)
                    zmieniono = True
        col_match.update(nowe_col_match)



    wykreslone_wier=[r for r in range(n) if r not in row_match]
    wykreslone_kol=list(col_match)
    liczba_linii = len(wykreslone_wier) + len(wykreslone_kol)

    if liczba_linii == n:
        return True,wykreslone_wier, wykreslone_kol
    else:
        return False,wykreslone_wier, wykreslone_kol




    
    


    



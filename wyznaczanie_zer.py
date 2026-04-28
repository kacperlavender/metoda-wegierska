def wyznaczanie_zer(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "0*":
                matrix[i][j] = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                if "0*" not in matrix[i] and not any(
                    matrix[k][j] == "0*" for k in range(n)
                ):
                    matrix[i][j] = "0*"

    match_row = [-1] * n
    match_col = [-1] * n

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "0*":
                match_row[i] = j
                match_col[j] = i

    def dfs(u, visited):
        for v in range(n):
            # Jeśli w danym miejscu jest zero i nie odwiedziliśmy tej kolumny
            if matrix[u][v] == 0 and not visited[v]:
                visited[v] = True
                # Jeśli kolumna v jest wolna lub możemy przesunąć jej obecne dopasowanie
                if match_col[v] < 0 or dfs(match_col[v], visited):
                    match_col[v] = u
                    match_row[u] = v
                    return True
        return False

    # Próbujemy znaleźć dodatkowe dopasowania dla wierszy, które nie mają 0*
    for i in range(n):
        if match_row[i] < 0:
            visited = [False] * n
            dfs(i, visited)

    # 4. AKTUALIZACJA MACIERZY: nanosimy ostateczne 0* na podstawie skojarzenia
    for i in range(n):
        # Czyścimy wiersz z ewentualnych starych śmieci
        for j in range(n):
            if matrix[i][j] == "0*":
                matrix[i][j] = 0
        # Wstawiamy poprawione 0*
        if match_row[i] >= 0:
            matrix[i][match_row[i]] = "0*"

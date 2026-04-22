import redukcja
import wyznaczanie_zer 

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
    [4, 1, 2, 4, 0]
]

if __name__ == "__main__":
    print("Hello world!")
    print_as_matrix(M)
    print(redukcja.redukcja(M), '\n')
    print_as_matrix(M)
    wyznaczanie_zer.wyznaczanie_zer(M)
    print_as_matrix(M)

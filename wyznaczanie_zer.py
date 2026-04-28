def wyznaczanie_zer(matrix):

    # for i in range(len(matrix)):
    #     for j in range(len(matrix)):
    #         if matrix[i][j] == "0*":
    #             matrix[i][j] = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                if "0*" in matrix[i] or "0*" in [
                    matrix[k][j] for k in range(len(matrix))
                ]:
                    continue
                else:
                    matrix[i][j] = "0*"

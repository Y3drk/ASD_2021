def arr_and_col(tab):
    n = len(tab)
    arr = [0 for i in range(len(tab))]
    col = [0 for i in range(len(tab))]
    for i in range(n):
        for j in range(n):
            arr[i] += tab[i][j]
            col[j] += tab[i][j]

    return arr,col
def kopia(tab):
    n = len(tab)
    kopia = [[0]*n for i in range(n)]
    for w in range(n):
        for k in range(n):
            kopia[w][k] = tab[w][k]

    return kopia
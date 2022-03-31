# zał. graf jest reprezentowany macierzowo, inicjalizacja nie jest potrzebna bo mamy założenie, że nie jest ważony (*)


def kopia(tab):
    n = len(tab)
    kopia = [[0]*n for i in range(n)]
    for w in range(n):
        for k in range(n):
            kopia[w][k] = tab[w][k]

    return kopia


def transitive_closure(G):
    n = len(G)
    T = kopia(G)  #jak zawsze, aby nie niszczyc "matrycy"
    # (*)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                T[i][j] = T[i][j] or (T[i][k] and T[k][j])

    return T


test = [[1,0,0,0],
        [0,1,1,1],
        [0,1,1,0],
        [1,0,1,1]]

res = transitive_closure(test)
for row in res:
    print(row)

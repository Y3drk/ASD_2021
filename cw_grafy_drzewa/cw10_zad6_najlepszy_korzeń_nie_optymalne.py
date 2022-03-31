'''Zadanie 6. (najlepszy korzeń) Dany jest acykliczny, spójny nieskierowany, ważony graf T (czyli T jest
tak naprawdę ważonym drzewem). Proszę wskazać algorytm, który znajduje taki wierzchołek T, z którego
odległość do najdalszego wierzchołka jest minimalna.'''

# jesli jest nieskierowany to krawedzie musza byc dodatnie, inaczej rip.

# odpalamy algorytm Floyda-Warshalla, a potem przechodzimy po wynikowej macierzy spisujac dla kazdego wierzchołka najdalasza odległosc
# z tych danych wybieramy najmniejsza z najwiekszych odległości

# działa na pewno, ale czy jest optymalne nwm, złożonośc narzucona przez alg. FW O(V^3)

def kopia(tab):
    n = len(tab)
    kopia = [[0] * n for _ in range(n)]
    for w in range(n):
        for k in range(n):
            kopia[w][k] = tab[w][k]

    return kopia


def best_root(G):
    n = len(G)
    S = kopia(G)  # niekoniecznie potrzebne, robimy kopie aby nie zniszczyc wyjsciowej reprezentacji grafu
    P = [[None] * n for _ in range(n)]


    for u in range(n):  # inicjalizacja tablicy parentów
        for v in range(n):
            if G[u][v] != float('inf') and u != v:
                P[u][v] = u

    # wlasciwy algorytm
    for t in range(n):
        for u in range(n):
            for v in range(n):
                if S[u][v] > S[u][t] + S[t][v]:
                    S[u][v] = S[u][t] + S[t][v]
                    P[u][v] = P[t][v]


    L = [-1 for _ in range(n)]
    for v in range(n):
        for u in range(n):
            L[v] = max(L[v], S[v][u])

    best = float('inf')
    ind = n
    for i in range(n):
        if best > L[i]:
            best = L[i]
            ind = i


    '''# weryfikacja - poszukiwanie cyklu ujemnego # u nas niepotrzebne bo ujemne krawedzie w grafie nieskierowanym to samobójstwo
    for x in range(n):
        for y in range(x + 1, n):
            if S[x][y] + S[y][x] < 0:
                return False, None, None'''

    return ind, L[ind]



test = [[0,3,7,float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf')],                 #0
        [3,0,float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf')],      #1
        [7,float('inf'),0,float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),1],                  #2
        [float('inf'),float('inf'),float('inf'),0,float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),8],      #3
        [float('inf'),float('inf'),float('inf'),float('inf'),0,float('inf'),float('inf'),float('inf'),float('inf'),10,float('inf')],#4
        [float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),0,float('inf'),float('inf'),float('inf'),16,float('inf')],#5
        [float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),0,float('inf'),float('inf'),11,float('inf')],#6
        [float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),0,float('inf'),2,float('inf')],#7
        [float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),0,float('inf'),4],#8
        [float('inf'),float('inf'),float('inf'),float('inf'),10,16,11,2,float('inf'),0,5],#9
        [float('inf'),float('inf'),1,8,float('inf'),float('inf'),float('inf'),float('inf'),4,5,0]] #10


res = best_root(test)
print("Najlepszy korzeń:",res[0],"z najwieksza odległoscia:",res[1])


# A i chuj mozna DFSem lub Dijkstra i chuj
# :)
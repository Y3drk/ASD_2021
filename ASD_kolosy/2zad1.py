from zad12testy import runtests

# wiemy ze miedzy dwoma wierzchołkami w drzewie istnieje dokładnie jedna scieżka --> odległosc miedzy wierzchołkami jest jednoznaczna
# oraz sciezka prowadzaca z u przez w do 3 roznych wierzchołków ma czesc wspolna u->w dla nich wszystkich

# skorzystamy z funkcji f(i,j) = odległosc wierzchołka i od wierzchołka j i bedziemy korzystac z rozwiazanych juz podproblemów
#f(i,j) = { d(i,k) + f(k,j)}

# BFS szukajacy najdłuzszej sciezki (raz BFS z losowego miejsca, potem ze znajlezionego najdalszego punktu drugi), potem doliczamy odnogi

# wynik odzyskujemy szukajac minimum sposród maksymalnych wartosci w kazdym wierszu tablicy F wypełnionej funkcja F

# złożoność --> czasowa O(n^2 + 2*(V + E)) 2*BFS + funkcje f(i,j) stad n^2 (dla kazdego elementu tablicy policzymy to dokładnie raz)


def best_root( L ):
    n = len(L)
    d1, _ = BFS(L,0)
    maxi = -1
    ind = n
    F = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        if maxi < d1[i]:
            maxi = d1[i]
            ind = i

    d2, p = BFS(L,ind)
    print(p)
    for i in range(n):
        if i != ind:
            F[i][p[i]] = d2[i] - d2[p[i]]
            F[p[i]][i] = d2[i] - d2[p[i]]

    for i in range(n):
        for j in range(i + 1, n):
            if F[i][j] == float('inf'):
                f(i,j,F,L,p)

    leaves = [-1 for _ in range(n)]
    best = float('inf')
    ind = n

    for i in range(n):
        maxi = -1
        for j in range(n):
            if j != i:
                maxi = max(maxi, F[i][j])

        leaves[i] = maxi

    for k in range(n):
        if leaves[k] < best:
            best = leaves[k]
            ind = k

    return ind


def f(i,j,F,L,p):
    n = len(L)
    if F[i][j] != float('inf'):
        return F[i][j]

    for v in L[i]:
        if p[v] != i:
            F[i][j] = min(F[i][j], 1 + f(v,j,F,L,p))
            F[j][i] = F[i][j]

    return float('inf')


def BFS(G,s):
    from queue import Queue
    n = len(G)  # n = |V|
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [-1 for _ in range(n)]
    Q = Queue()

    Q.put(s)
    visited[s] = True
    distance[s] = 0

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.put(v)

    return distance, parent

runtests( best_root ) 

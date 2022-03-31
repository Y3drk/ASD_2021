'''Definiujemy relację znajomości między osobami jako symetryczną.
Znajomość:
pierwszego stopnia to bezpośrednia znajomość osoby
drugiego stopnia to bycie “znajomym znajomego” osoby, ale nie bezpośrednim znajomym osoby
trzeciego, czwartego, piątego stopnia, itd.
nieskończonego stopnia zachodzi wtedy gdy nie ma ciągu znajomości, który łączyłby dwie osoby
Mając na wejściu listę osób i znajomości pierwszego stopnia między nimi, chcemy znaleźć największy stopień znajomości wśród każdej z możliwych par.
Znajdź optymalne rozwiązanie zarówno dla grafów rzadkich (|E| = O(|V|)), jak i gęstych (|E| = O(|V|^2)
'''

# idea - krawedzie maja wage jeden

# dla grafów rzadkich - BFS z każdego wierzchołka O(V(V + E)) ~= O(V^2) i wyciaganie wyników na biezaco

# dla grafów gęstych - Floyd - Warshall + przejscie po wyniku - O(V^3)

# zał. graf jest macierza sasiedztwa


def kopia(tab):
    n = len(tab)
    kopia = [[0] * n for _ in range(n)]
    for w in range(n):
        for k in range(n):
            kopia[w][k] = tab[w][k]

    return kopia


def BFS(G,s):
    from queue import Queue
    n = len(G)  # n = |V|
    visited = [False for _ in range(n)]  #inicjalizacja dodatkowych tablic z odp. informacjami
    parent = [None for _ in range(n)]
    distance = [-1 for _ in range(n)]
    Q = Queue()

    Q.put(s)           #krok startowy, "wrzucenie kamienia"
    visited[s] = True
    distance[s] = 0

    while not Q.empty():   #"rozchodzenie sie fali"
        u = Q.get()
        for v in range(n):  #sprawdzamy wszystkich dotychczas nieodwiedzonych sasiadów wierzchołka sciagnietego z kolejki
            if not visited[v] and G[u][v] == 1:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.put(v)

    return distance


def FW(G):
    n = len(G)
    S = kopia(G)
    P = [[None] * n for _ in range(n)]


    for u in range(n):
        for v in range(n):
            if G[u][v] != float('inf') and u != v:
                P[u][v] = u

    for t in range(n):
        for u in range(n):
            for v in range(n):
                if S[u][v] > S[u][t] + S[t][v]:
                    S[u][v] = S[u][t] + S[t][v]
                    P[u][v] = P[t][v]

    for x in range(n):
        for y in range(x + 1, n):
            if S[x][y] + S[y][x] < 0:
                return False, None, None

    return True, S, P


# GRAFY RZADKIE
def sparse_graf_friends(G):
    maxi = 0
    n = len(G)
    for v in range(n):
        tmp = BFS(G,v)
        for i in range(n):
            if i != v:
                if tmp[i] == -1:
                    maxi = float('inf')
                else:
                    maxi = max(maxi,tmp[i])

    return maxi


#GRAFY GESTE
def dense_graf_friends(G):
    res = FW(G)
    n = len(G)
    maxi = 0
    for u in range(n):
        for v in range(n):
            maxi = max(maxi,res[1][u][v])

    return maxi


G_4_sparse = [[0,1,0,1,0,0,1],
     [1,0,1,0,1,0,0],
     [0,1,0,0,1,0,0],
     [1,0,0,0,1,1,0],
     [0,1,1,0,0,1,1],
     [0,0,0,1,1,0,0],
     [1,0,0,0,1,0,0]]

G_4_dense = [[0,1,float('inf'),1,float('inf'),float('inf'),1],
             [1, 0, 1, float('inf'), 1, float('inf'), float('inf')],
             [float('inf'), 1, 0, float('inf'), 1, float('inf'), float('inf')],
             [1, float('inf'), float('inf'), 0, 1, 1, float('inf')],
             [float('inf'), 1, 1, float('inf'), 0, 1, 1],
             [float('inf'), float('inf'), float('inf'), 1, 1, 0, float('inf')],
             [1, float('inf'), float('inf'), float('inf'), 1, float('inf'), 0]]


print(sparse_graf_friends(G_4_sparse))
print(dense_graf_friends(G_4_dense))

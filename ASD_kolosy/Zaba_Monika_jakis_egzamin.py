'''tresc na alles'''

#tworzymy z tego graf i leicmy BFSem z podwójnym visited (czy gdzies weszlismy skokiem 2L czy 1L lub 1/2L)

# * -> jesli przyszlismy z 0 mozemy isc jak chcemy, jesli z 1 to tylko w 1/2


def preprocess_swamp(W,L):
    from math import sqrt
    n = len(W)
    Graph = [[0]*n for _ in range(n)]
    for w1 in range(n):
        for w2 in range(w1 + 1,n):
            if (sqrt((W[w2][0] - W[w1][0])**2 + (W[w2][1] - W[w1][1])**2)) <= 1/2*L:
                Graph[w1][w2], Graph[w2][w1] = 1/2,1/2

            elif 0.5 * L < (sqrt((W[w2][0] - W[w1][0])**2 + (W[w2][1] - W[w1][1])**2)) <= 1*L:
                Graph[w1][w2], Graph[w2][w1] = 1,1

            elif L < (sqrt((W[w2][0] - W[w1][0])**2 + (W[w2][1] - W[w1][1])**2)) <= 2*L:
                Graph[w1][w2], Graph[w2][w1] = 2,2

            else:
                Graph[w1][w2], Graph[w2][w1] = 0, 0

    return Graph


def BFS_for_frogs(G,s):
    from queue import Queue
    n = len(G)  # n = |V|
    visited = [[False for _ in range(2)] for _ in range(n)]
    distance = [[-1 for _ in range(2)] for _ in range(n)]
    Q = Queue()

    Q.put((s,0))    #do kolejki wrzucamy krotki: (wierzchołek, jaka sciezka przyszlismy - 0 -> 1/2L i L, 1 -> 2L)*
    visited[s][0] = True
    visited[s][1] = True
    distance[s][0] = 0
    distance[s][1] = 0

    while not Q.empty():
        u, type = Q.get()
        if type == 0:
            for v in range(n):
                if not visited[v][1] and G[u][v] == 2:
                    visited[v][1] = True
                    distance[v][1] = distance[u][0] + 1

                    Q.put((v,1))

                if not visited[v][0] and (G[u][v] == 1 or G[u][v] == 0.5):
                    visited[v][0] = True
                    distance[v][0] = distance[u][0] + 1

                    Q.put((v, 0))

        else:
            for v in range(n):
                if not visited[v][0] and G[u][v] == 0.5:
                    visited[v][0] = True
                    distance[v][0] = distance[u][1] + 1

                    Q.put((v, 0))

    '''for row in distance:
        print(row)'''

    best = float('inf')
    if distance[n-1][0] != -1:
        best = min(distance[n - 1][0], best)

    if distance[n - 1][1] != -1:
        best = min(best, distance[n-1][1])

    if best == float('inf'):
        return 'IMPOSSIBLE'
    else:
        return best


def monika_the_frog(S, L):
    G = preprocess_swamp(S, L)
    '''for row in G:
        print(row)'''

    res = BFS_for_frogs(G,0)
    print(res)


T0 = [(0,1),(0,3),(-1,2),(-1,4)]
L0 = 4
monika_the_frog(T0,L0)
print("-----")

T1 = [(2, 2), (3, 5), (5, 6), (6, 10), (11, 7)]
odp1 = 3
monika_the_frog(T1, 4.1)
print("-----")
T2 = [(2, 2), (3, 5), (5, 6), (6, 10), (11, 7)]
odp2 = 2
monika_the_frog(T2, 5)
print("-----")
T3 = [(2, 2), (3, 5), (5, 6), (6, 10), (11, 7)]
odp3 = 1
monika_the_frog(T3, 5.2)
print("-----")
T4 = [(2, 2), (3, 5), (5, 6), (6, 10), (11, 7)]
odp4 = False
monika_the_frog(T3, 2)


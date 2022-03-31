'''Dany jest graf ważony z dodatnimi wagami G.
Dana jest też lista E’ krawędzi, które nie należą do grafu, ale są krawędziami między wierzchołkami z G.
Dane są również dwa wierzchołki s i t. Podaj algorytm, który stwierdzi, którą jedną krawędź z E’ należy wszczepić do G,
aby jak najbardziej zmniejszyć dystans między s i t. Jeżeli żadna krawędź nie poprawi dystansu między s i t, to algorytm powinien to stwierdzić.'''


# idea -
# 1) puszczamy dijkstre z s do t zachowujemy distances
# (*) jesli graf jest skierowany to odwracamy krawedzie
# 2) puszczamy dijkstre od t do s, zapamietujemy distances
# 3) dla kazdej krawedzi z E' wykonuujemy sprawdzenie czy : ds[t] - (ds[u] + w + dt[v]) > maxi , czyli czy zysk na wszepieniu krawedzi jest najlepszy,
# jesli zadna krawedz niepoprawi sciezki zwracamy False

# ja tu dla ułatwienia przyjmuje ze graf jest nieskierowany, ale nie jest to jakis chory problem

def Dijkstra_4_adjlist(G, s):
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    processed = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [float('inf') for _ in range(n)]

    Q.put((0, s))  # (waga, wierzchołek)
    distance[s] = 0

    def relax(u, v, edge):
        if distance[v] > distance[u] + edge:
            distance[v] = distance[u] + edge
            parent[v] = u
            return True  # przyda sie do wsadzania wierzchołków do kolejki

        return False

    while not Q.empty():
        _, t = Q.get()
        if processed[t] == True:
            continue
        else:
            processed[t] = True
            for u in G[t]:  # u = (drugi wierzcholek krawedzi, waga krawedzi)
                if not processed[u[0]]:
                    if relax(t, u[0], u[1]):
                        Q.put((distance[u[0]], u[0]))

    return distance


def shrinking_edge(G, E, s, t):
    ds = Dijkstra_4_adjlist(G, s)
    dt = Dijkstra_4_adjlist(G, t)
    print(ds)
    print(dt)
    maxi = 0
    best_edge = None
    for u, v, w in E:
        print(u,v,w,ds[t] - (ds[u] + w + dt[v]))
        if ds[t] - (ds[u] + w + dt[v]) > maxi:
            maxi = ds[t] - (ds[u] + w + dt[v])
            best_edge = (u, v, w)

    if best_edge != None:
        print("Wybrana krawedz:", best_edge, "zyskalismy:", maxi)

    return best_edge


test = [[(1, 3), (2, 10), (4, 13)], [(0, 3), (2, 5)], [(0, 10), (1, 5), (3, 7), (6, 10)], [(2, 7), (6, 8)],
        [(0, 13), (5, 11)], [(4, 11), (7, 10)], [(2, 10), (3, 8), (7, 2)], [(5, 10), (6, 2)]]
E = [(0, 6, 2), (2, 7, 8), (0, 7, 5)]
start = 0
stop = 7
shrinking_edge(test, E, start, stop)

# 11zad6 z bitu było offline'm w zeszłym tygodniu

'''Oprócz długości krawędzi, graf ma przypisane koszty wierzchołków.
Zdefiniujmy koszt ścieżki jako sumę kosztów jej krawędzi oraz sumę kosztów wierzchołków (wraz z końcami).

Jak znaleźć najtańsze ścieżki między wierzchołkiem startowym a wszystkimi pozostałymi?

Podaj rozwiązanie zarówno dla grafu skierowanego, jak i nieskierowanego.
'''

# w obu przypadkach nalezy dodac wage wierzchołka do którego idzie krawedz do wagi krawedzi, bo nie ma czegos takiego w repr. komputerowej,
# jak graf nieskierowany


def add_vert_to_edges(G,V):
    n = len(G)
    for v in range(n):
        for u in G[v]:
            u[1] += V[u[0]]


def print_path(p,ind):
    if p[ind] != None:
        print_path(p,p[ind])

    print(ind,end=' ')


def Dijkstra_4_adjlist(G, s):
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    processed = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [float('inf') for _ in range(n)]

    Q.put((0,s))  # (waga, wierzchołek)
    distance[s] = 0

    def relax(u, v, edge):
        if distance[v] > distance[u] + edge:
            distance[v] = distance[u] + edge
            parent[v] = u
            return True  #przyda sie do wsadzania wierzchołków do kolejki

        return False

    while not Q.empty():
        _,t = Q.get()
        if processed[t] == True:
            continue
        else:
            processed[t] = True
            for u in G[t]: # u = (drugi wierzcholek krawedzi, waga krawedzi)
                if not processed[u[0]]:
                    if relax(t,u[0],u[1]):
                        Q.put((distance[u[0]],u[0]))

    return parent,distance


def launcher():
    test = [[[1,3],[3,4]],[[0,3],[3,7],[5,8]],[[3,8],[4,3],[5,3]],[[0,4],[1,7],[2,8],[4,5]],[[2,3],[3,5]],[[1,8],[2,3],[6,5]],[[5,5]]]
    V = [2,10,3,1,2,8,0]
    start = 0
    stop = 6
    add_vert_to_edges(test,V)
    #print(test)
    res = Dijkstra_4_adjlist(test,start)
    print(res[1][stop])
    print_path(res[0],stop)
    return


launcher()


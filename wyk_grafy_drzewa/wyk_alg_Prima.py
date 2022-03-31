#zał. implementacja dla listy sąsiedztwa
# zaczniemy budowanie zbioru S z wierzchołka nr 0


def Prim_MST(G):
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    processed = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    weight = [float('inf') for _ in range(n)]

    Q.put((0,0))  # (waga, wierzchołek)

    while not Q.empty():
        _,t = Q.get()
        if processed[t] == True:
            continue
        else:
            processed[t] = True
            for u in G[t]: # u = (drugi wierzcholek krawedzi, waga krawedzi)
                if not processed[u[0]] and u[1] < weight[u[0]]:
                    Q.put((u[1],u[0]))
                    weight[u[0]] = u[1]
                    parent[u[0]] = t

    return parent

#            0                  1                   2                         3                    4                   5
test0 = [[(1,1),(2,12)],[(0,1),(2,7),(4,5)],[(0,12),(1,7),(4,6),(3,8)],[(2,8),(4,4),(5,9)], [(1,5),(3,4),(5,3000)],[(3,9),(4,3000)]]
print(Prim_MST(test0))




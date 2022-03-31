#FOR ADJACIENCY LIST

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


#FOR ADJACIENCY MATRIX

def Dijkstra_4_adjmatrix(G,s):
    n = len(G)
    Queue = [float('inf') for _ in range(n)]
    processed = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [float('inf') for _ in range(n)]  #niepotrzebne bo queue ~= distance de facto, ale zachowamy dla porzadku

    Queue[s] = 0
    distance[s] = 0

    def relax(u, v, edge):
        if distance[v] > distance[u] + edge:
            distance[v] = distance[u] + edge
            parent[v] = u
            return True  #przyda sie do wsadzania wierzchołków do kolejki

        return False

    def get_vert():
        n = len(Queue)
        key = n
        best = float('inf')
        for i in range(n):
            if not processed[i] and best > Queue[i]:
                best = Queue[i]
                key = i

        return key, best

    while True:
        v, flag = get_vert()
        if flag == float('inf'):   #warunek zakonczenia przetwarzania
            break

        else:
            processed[v] = True
            for u in range(n):
                if G[v][u] != - 1 and not processed[u] and relax(v,u,G[v][u]):
                    Queue[u] = distance[u]

    return parent, distance


#                    0               1                         2                3                  4
test0_adjlist = [[(1,1),(2,5)],[(0,1),(2,2),(4,7),(3,8)],[(0,5),(1,2),(3,3)],[(1,8),(2,3),(4,1)],[(1,7),(3,1)]]
res_adjlist = Dijkstra_4_adjlist(test0_adjlist, 0)
print("FOR ADJ_LIST:\nParents:", res_adjlist[0], "\ndistance:", res_adjlist[1])
print("------")
test0_adj_matrix = [[-1,1,5,-1,-1],
                    [1,-1,2,8,7],
                    [5,2,-1,3,-1],
                    [-1,8,3,-1,1],
                    [-1,7,-1,1,-1]]
res_adjmatrix = Dijkstra_4_adjmatrix(test0_adj_matrix, 0)
print("FOR ADJ_MATRIX:\nParents:", res_adjmatrix[0], "\ndistance:", res_adjmatrix[1])


G3 = [[-1, 4, -1, -1, -1, -1, -1, 8, -1],   #[5, 6, 8, 2]
         [4, -1, 8, -1, -1, -1, -1, 11, -1],
         [-1, 8, -1, 7, -1, 4, -1, -1, 2],
         [-1, -1, 7, -1, 9, 14, -1, -1, -1],
         [-1, -1, -1, 9, -1, 10, -1, -1, -1],
         [-1, -1, 4, 14, 10, -1, 2, -1, -1],
         [-1, -1, -1, -1, -1, 2, -1, 1, 6],
         [8, 11, -1, -1, -1, -1, 1, -1, 7],
         [-1, -1, 2, -1, -1, -1, 6, 7, -1]]

print("------")
res_adjmatrixG3 = Dijkstra_4_adjmatrix(G3,0)
print("FOR ADJ_MATRIX G3:\nParents:", res_adjmatrixG3[0], "\ndistance:", res_adjmatrixG3[1])


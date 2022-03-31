'''Dany jest graf ważony  G, oraz drzewo rozpinające T zawierające wierzchołek s.
Podaj algorytm, który sprawdzi, czy T jest drzewem najkrótszych ścieżek od wierzchołka s.'''

#idea - dfsik bo T zeby znależć wszystkie dlugości scieżek , potem sprawdzamy czy może gdzieś w G nastąpić relaksajca wzgledem wyników z T

#zał. oba grafy reprezentujemy jako listy sąsiedztwa

def DFS_weighted(T, s):
    n = len(T)
    visited = [False for _ in range(n)]
    distance = [0 for i in range(n)]

    def DFS_visit(G,s):

        visited[s] = True
        for u in G[s]:
            if not visited[u[0]]:
                distance[u[0]] = distance[s] + u[1]
                DFS_visit(G,u[0])


        return
    distance[s] = 0
    DFS_visit(T,s)

    return distance


def shortest_paths_tree(G,T,s):
    distances = DFS_weighted(T,s)
    n = len(G)
    for v in range(n):
        for u in G[v]:
            if distances[v] > distances[u[0]] + u[1]:
                return False

    return True


#TESTY OD PIOTRKA
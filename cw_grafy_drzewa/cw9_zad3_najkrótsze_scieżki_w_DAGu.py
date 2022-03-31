'''Zadanie 3. (najkrósze ścieżki w DAGu) Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich
innych w acyklicznym grafie skierowanym?
'''

#idea - sortowanie topologiczne a potem taki pseudo Dijkstra


def topologic_sort_DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    list_of_tasks = []

    def DFS_visit(G,s):
        nonlocal list_of_tasks
        visited[s] = True
        for u in G[s]:
            if not visited[u[0]]:
                parent[u[0]] = s
                DFS_visit(G,u[0])

        list_of_tasks += [s]  #[chr(97+s)]
        return

    for u in range(n):
        if not visited[u]:
            DFS_visit(G,u)

    return list_of_tasks[::-1]


def shorthest_DAG_paths(G):
    n = len(G)
    top = topologic_sort_DFS(G)
    distance = [float('inf') for _ in range(n)]

    def relax(u, v, edge):
        if distance[v] > distance[u] + edge:
            distance[v] = distance[u] + edge
            return True  #przyda sie do wsadzania wierzchołków do kolejki

        return False

    distance[top[0]] = 0
    for i in range(n):
        for v in G[top[i]]:
            relax(top[i],v[0],v[1])

    return top,distance

#         0           1    2      3    4
G = [[(1,2),(4,4)],[(2,8)],[],[],[(3,1)]]
res = shorthest_DAG_paths(G)
print("Scieżki dla wierzchołków:",res[0],"\n",res[1])


#dotyczy tylko DAG'ów --> Directed Acyclic Graph
#sortuje jego wierzchołki tak,ze krawedzie wskazuja tylko w jedna strone, np. tylko z lewej na prawa

# algorytm działania :
# 1) wykonac na zadanym grafie Algorytm DFS i po przetworzeniu danego wierzchołka dopisywac go na poczatek listy zadan do wykonania

def topologic_sort_DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    list_of_tasks = []

    def DFS_visit(G,s):
        nonlocal list_of_tasks
        visited[s] = True
        for u in G[s]:
            if not visited[u]:
                parent[u] = s
                DFS_visit(G,u)

        list_of_tasks += [s]  #[chr(97+s)]
        return

    for u in range(n):
        if not visited[u]:
            DFS_visit(G,u)

    return list_of_tasks[::-1]


test = [[1,2],[2,3],[],[4,5,6],[],[],[]]
print(topologic_sort_DFS(test))
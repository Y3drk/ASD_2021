'''Policzyć liczbę spójnych składowych w grafie (implementacja przeciwna do tej z poprzedniego zadania)
'''


def spojne_skladowe_DFS(G):
    def DFS_Visit(G, u):
        nonlocal Visited
        Visited[u] = True
        for v in G[u]:
            if Visited[v] == False:
                DFS_Visit(G, v)
    # DFS
    n = len(G)
    Visited = [False] * n
    result = 0
    for u in range(n):
        if Visited[u] == False:
            result += 1   #za kazdym razem gdy zaczynamy DFS to wiemy, ze poprzedni musiał nie przejsci wszystkich wierzchołków zatem dochodzi nam nowa ss
            DFS_Visit(G, u)
    return result



G = [[1, 2],  # 0
     [0, 2],  # 1
     [0, 1],  # 2
     [4],  # 3
     [3],  # 4
     []]  # 5
# 3 spojne skladowe
print(spojne_skladowe_DFS(G))
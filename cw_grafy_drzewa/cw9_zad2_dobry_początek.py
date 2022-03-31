'''Zadanie 2. (dobry początek) Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który
stwierdza czy dany graf zawiera dobry początek.
'''


#idea - odpalamy dfs i zapisujemy czasy przetworzenia, potem jeszcze właczamy DFS z wierzchołka o najwyzszym zapisanym czasie.
# jesli w grafie sa dobre początki to tam na pewno jest

def good_begining(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    times = [-1 for _ in range(n)]

    time = 0

    def DFS_visit(G,s):
        nonlocal time
        visited[s] = True
        for u in G[s]:
            if not visited[u]:
                parent[u] = s
                DFS_visit(G,u)

        time += 1
        times[s] = time
        return

    DFS_visit(G,0)

    best = -1
    ind = n
    for i in range(n):
        if times[i] > best:  #znalezienie wierzchołka z najwyższym czasem przetworzenia, reste tablic
            ind = i
            best = times[i]
            visited[i] = False
            parent[i] = None

    DFS_visit(G,ind)

    for j in range(n):
        if not visited[j]:
            return False

    print(ind)
    return True


G = [[2,3],[4,5],[4,5],[1],[3],[4]]
print(good_begining(G))
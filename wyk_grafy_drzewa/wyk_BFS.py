#wykładowa implementacja algorytmu BFS
# założenie : graf reprezentujemy jak listę sasiedztwa, a konkretnie jako liste list, parametry parent i visited sa realizowane jako osobne tablice, gdzie indeks
# jest identyfikatorem wierzchołka

# złożonosc dla tej versji O(V+E)

def BFS(G,s):
    from queue import Queue
    n = len(G)  # n = |V|
    visited = [False for _ in range(n)]  #inicjalizacja dodatkowych tablic z odp. informacjami
    parent = [None for _ in range(n)]
    distance = [-1 for _ in range(n)]
    Q = Queue()

    Q.put(s)           #krok startowy, "wrzucenie kamienia"
    visited[s] = True
    distance[s] = 0

    while not Q.empty():   #"rozchodzenie sie fali"
        u = Q.get()
        for v in G[u]:  #sprawdzamy wszystkich dotychczas nieodwiedzonych sasiadów wierzchołka sciagnietego z kolejki
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.put(v)

    return visited,distance,parent


G = [[1,2],[0,4],[0,3,5],[2,4],[1,3,5],[2,4,6],[5,7],[6]]
result = BFS(G,0)
print("Done")
print("Visited:",result[0])
print("Distances:",result[1])
print("Parents:",result[2])
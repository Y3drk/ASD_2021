''' Proszę zaimplementować algorytm BFS tak, żeby znajdował
najkrótsze ścieżki w grafie i następnie, żeby dało się wypisać najkrotszą ścieżkę z zadanego punktu startowego
do wskazanego wierzchołka.'''


def BFS(G, s):
    from queue import Queue
    n = len(G)  # n = |V|
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [-1 for _ in range(n)]
    Q = Queue()

    Q.put(s)
    visited[s] = True
    distance[s] = 0

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.put(v)

    return parent


def print_path(parent,start,curr):

    if curr != start:
        print_path(parent,start,parent[curr])

    print(curr, end=', ')

    return


test = [[1, 2], [0, 6], [0, 3, 5, 6], [2, 4], [3, 5], [2, 4, 6, 7], [1, 2, 5], [5, 8], [7, 9, 10], [8, 10], [8, 9, 11],[10]]
start = 0
finish = 11
res = BFS(test, start)
print_path(res, start, finish)
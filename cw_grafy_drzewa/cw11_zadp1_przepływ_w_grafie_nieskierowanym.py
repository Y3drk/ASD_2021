# pozbyc sie klasy i przerobic na swoje !!!!

# idea - dodajemy fejk wierzchołki i przez niego puszczamy krawedz w druga strone, podczas gdy te nieskierowana ustawilismy w pierwsza strone

class graph:

    def __init__(self, size):
        self.m = [[0] * size for i in range(size)]
        self.size = size
        self.edges = 0

    def add_edge(self, v, u, weight):
        self.m[v][u] = weight
        self.m[u][v] = weight
        self.edges += 1

    def printG(self):
        for i in g.m:
            print(i)


from collections import deque


def BFS(g, s, t, parents):
    q = deque()
    number = len(g)

    visited = [False] * number
    q.appendleft(s)
    visited[s] = True

    while len(q) != 0:
        u = q.pop()

        for i in range(number):
            if len(q) == 0: q = deque()
            if g[u][i] != 0 and visited[i] == False:
                parents[i] = u
                visited[i] = True
                q.appendleft(i)

    return visited[t]


# maksymalny przepływ z wierzchołka s do t
def Ford_Fulkerson(g, s, t):
    parents = [None] * len(g)
    flow = 0

    while BFS(g, s, t, parents):

        current = t
        cur_flow = float("inf")

        while current != s:
            if g[parents[current]][current] < cur_flow:
                cur_flow = g[parents[current]][current]
            current = parents[current]

        flow += cur_flow
        v = t

        while v != s:
            g[parents[v]][v] -= cur_flow
            g[v][parents[v]] += cur_flow
            v = parents[v]
    return flow


def flow(g, s, t):

    matrix = [[0] * (g.size + g.edges) for _ in range(g.size + g.edges)] #!

    current = g.size  #!
    for i in range(g.size):
        for j in range(g.size):
            if i < j and g.m[i][j] != 0:
                matrix[i][j] = g.m[i][j]
                matrix[j][current] = matrix[current][i] = g.m[i][j]
                current += 1

    return Ford_Fulkerson(matrix, s, t)

g = graph(6)
g.add_edge(0,1,4)
g.add_edge(0,3,8)
g.add_edge(1,2,5)
g.add_edge(1,3,7)
g.add_edge(2,3,6)
g.add_edge(2,5,7)
g.add_edge(3,4,10)
g.add_edge(4,5,6)

print(flow(g,0,5))
#zał. graf otrzymujemy jako listę krawędzi, a dodatkowym argumentem jest V będące ilośćią wierzchołków
# oraz zakładamy, że graf jest spójny

class Node:
    def __init__(self,val):
        self.val = val
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)

    return x.parent


def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def Kruskal_MST(G,V):
    A = [] #stworzenie docelowej listy krawdzi MST
    Graph = [] #struktura, której użyjemy w operacjach find-union

    for i in range(V):
        Graph += [Node(i)]

    G.sort(key=lambda x: x[2]) #posorotwanie krawedzi Grafu

    for edge in G:
        if find(Graph[edge[0]]) != find(Graph[edge[1]]):  #jesli wierzchołki juz nie sa połaczone jakas sciezka,
            A += [edge]    # czyli dodadnie krawedzi nie tworzy cyklu to mozemy ja dodac do odp
            union(Graph[edge[0]],Graph[edge[1]])

    return A


V0 = 6
list0 = [(0,1,7), (0,5,1), (5,4,12), (5,1,8), (1,2,2), (5,3,4), (1,4,3),(4,3,6), (2,3,5)]
print(Kruskal_MST(list0,V0))




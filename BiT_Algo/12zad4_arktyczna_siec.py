'''W Arktyce osady są oddalone od siebie na ogromne odległości. Otrzymujemy je jako pary współrzędnych (x, y).
Niektóre z nich posiadają odbiorniki satelitarne - z takiej osady można bezpośrednio komunikować się z każdą inną osadą, która ma odbiornik satelitarny.
Chcemy teraz w każdej osadzie umiejscowić radioodbiorniki o tym samym ograniczonym zasięgu D (liczba całkowita),
aby można było się komunikować (pośrednio lub bezpośrednio) między każdą parą osad. Jakie jest minimalne D, które pozwoli osiągnąć ten cel?
Uzasadnij poprawność rozwiązania.
'''

# idea - łaczymy stacje z odbiornikami satelitarnymi krawedziami o wartosci 0 i odpalamy algorytm kruskala, minimalnym D jest najwieksza wartosc z wybranych krawedzi
# rozwiazanie jest poprawne ze wzgledu na def alg kruskala


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

    G.sort(key=lambda x: x[0]) #posorotwanie krawedzi Grafu

    for edge in G:
        if find(Graph[edge[1]]) != find(Graph[edge[2]]):  #jesli wierzchołki juz nie sa połaczone jakas sciezka,
            A += [edge]    # czyli dodadnie krawedzi nie tworzy cyklu to mozemy ja dodac do odp
            union(Graph[edge[1]],Graph[edge[2]])

    return A


def make_edges(P,S):
    from math import sqrt
    n = len(P)
    E = []
    for i in range(n):
        for j in range(i+1,n):
            #print(i,j)
            if S[i] and S[j]:
                E.append((0,i,j))
                #print("chuj")
            else:
                E.append((sqrt((P[i][0]-P[j][0])**2 + (P[i][1]-P[j][1])**2),i,j))

    return E


def launcher(P,S):
    E = make_edges(P,S)
    #print(E)
    res = Kruskal_MST(E,len(E))
    D = 0
    #print(res)
    for i in range(len(res)):
        D = max(D,res[i][0])

    return D


P0 = [(0,0),(3,3),(-3,0),(6,8),(2,1),(4,1)]
S0 = [False,True, False, False,True,True]
print(launcher(P0,S0))




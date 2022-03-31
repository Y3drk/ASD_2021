'''W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć wszystkie miasta siecią autostrad, tak aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ kontynent, na
którym leży państwo jest płaski położenie każdego z miast opisują dwie liczby x, y, a odległość w linii
prostej pomiędzy miastami liczona w kilometrach wyraża się wzorem len =
√
(x1 − x2)
2 + (y1 − y2)
2.
Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii prostej.
Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie
i jako cel postanowiono zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady.
Czas budowy autostrady wyrażony w dniach wynosi ⌈len⌉ (sufit z długości autostrady wyrażonej
w km).
Proszę zaimplementować funkcję highway(A), która dla danych położeń miast wyznacza minimalną liczbę dni dzielącą otwarcie pierwszej i ostatniej autostrady.
Przykład Dla tablicy A =[(10,10),(15,25),(20,20),(30,40)] wynikiem jest 7 (Autostrady
pomiędzy miastami 0-1, 0-2, 1-3)'''

#mapa autostrad to graf pełny
#idea - tworzymy wszystkie mozliwe krawedzie i na nich wykonujemy algorytm kruskala tyle razy ile jest krawedzi za kazdym razem wyrzucajac kolejna najmniejsza krawedz
# po kazdym kruskalu badamy róznice miedzy najmniejsza krawedzia a najwieksza.
# trzeba przy tym uwazac zeby nie rozspójnic grafu wiec bedziemy badac tez stopnie wierzchołków, bo graf jest nieskierowany wiec wystarczy ze kazdy wierzchołek bedzie
# miał stopień conajmniej 1

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


def Kruskal_highways(G,V):
    Graph = []

    low, high = float('inf'), float('-inf')

    for i in range(V):
        Graph += [Node(i)]

    for edge in G:
        if find(Graph[edge[0]]) != find(Graph[edge[1]]) and edge[3]:
            if low > edge[2]:
                low = edge[2]

            if high < edge[2]:
                high = edge[2]

            union(Graph[edge[0]],Graph[edge[1]])

    return high - low


def length(P1,P2):
    import math
    l = math.ceil(math.sqrt((P1[0] - P2[0])*(P1[0] - P2[0]) + (P1[1] - P2[1])*(P1[1] - P2[1])))
    return l


def highways(A):
    n = len(A)
    G = []
    for i in range(n):
        for j in range(i + 1,n):
            G.append([i,j,length(A[i],A[j]),True])

    G.sort(key=lambda x: x[2])
    deg = [(n-1) for _ in range(n)]
    flag = True
    best = float('inf')
    ind = 0

    while flag:
        flag = False
        #print(G)
        best = min(best, Kruskal_highways(G,n))
        while ind < len(G):  #po kazdej krawedzi przejdziemy raz
            if deg[G[ind][0]] - 1 > 0 and deg[G[ind][1]] - 1 > 0:
                G[ind][3] = False
                deg[G[ind][0]] -= 1
                deg[G[ind][1]] -= 1
                flag = True
                ind += 1
                break

            else:
                ind += 1

    return best


t1 = [(10,10),(15,25),(20,20),(30,40)]
print(highways(t1))

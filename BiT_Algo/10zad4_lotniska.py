'''Dostajemy na wejściu listę trójek (miastoA, miastoB, koszt). Każda z nich oznacza, że możemy zbudować drogę między miastem A i B za podany koszt. Ponadto, w dowolnym mieście możemy zbudować lotnisko za koszt K, niezależny od miasta. Na początku w żadnym mieście nie ma lotniska, podobnie między żadnymi dwoma miastami nie ma wybudowanej drogi.
Naszym celem jest zbudować lotniska i drogi za minimalny łączny koszt, tak aby każde miasto miało dostęp do lotniska.
Miasto ma dostęp do lotniska, jeśli:
jest w nim lotnisko, lub
można z niego dojechać do innego miasta, w którym jest lotnisko
Jeżeli istnieje więcej niż jedno rozwiązanie o minimalnym koszcie, należy wybrać to z największą ilością lotnisk.
'''

#idea - za pomoca alg kruskala łaczymy wszystkie miasta których drogi kosztuja < k i oczywiscie nie tworza cyklu.
# Potem dla wszystkich spojnych składowych budujemy po 1 lotnisku

# złozonosc O(ElogE) narzucone przez sort krawedzi

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


def airports(G,V, k):
    Graph = []
    counter = V
    cost = 0
    for i in range(V):
        Graph += [Node(i)]

    G.sort(key=lambda x: x[2])

    for edge in G:
        if edge[2] >= k:
            break
        if find(Graph[edge[0]]) != find(Graph[edge[1]]):
            union(Graph[edge[0]],Graph[edge[1]])
            counter -= 1
            cost += edge[2]

    cost += counter*k
    print(counter)

    return cost



test = [(0,1,2),(1,3,8),(2,3,9),(1,2,4),(1,4,7),(3,4,5),(0,2,3)]
print(airports(test,5,6))
print("----")
E = [(0,1,2),(0,3,1),(0,2,4),(2,4,3),(2,5,2),(4,5,7),(1,3,1)]
print(airports(E,6,3))
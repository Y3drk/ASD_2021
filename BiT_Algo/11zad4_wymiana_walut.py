'''Na tablicach w kantorze wisi lista trójek (waluta1, waluta2, kurs). Każda z takich trójek oznacza, że kantor kupi n waluty2 za kurs*n waluty1.
1) Znajdź najkorzystniejszą sekwencję wymiany waluty A na walutę B
2) Czy istnieje taka sekwencja wymiany walut, która zaczyna się i kończy w tej samej walucie i kończymy z większą ilością pieniędzy niż zaczynaliśmy?
'''

# 1) Tworzymy graf skierowany, gdzie wierzchołki to waluty, a krawedzie to transakcje wg opisu,
# 2) na tym odpalamy bellamana forda i: 1) robi sie sama w mysl algorytmu, a 2) to potencjalny cykl o ujemnej sumie, czyli też algorytm to wychwyci

def cryptocurrency_stuff(C,w):
    from math import log10
    G = [[] for _ in range(w)]

    #print(G)

    for c1,c2,k in C:
        G[c1] += [(c2,log10(k))]

    #print(G)
    return G


def BF_4_adjlist(G,s):
    n = len(G)
    #inicjalizacja
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[s] = 0

    #relaksacje
    def relax(u, v, edge):
        if distance[v] > distance[u] + edge:
            distance[v] = distance[u] + edge
            parent[v] = u

    for i in range(n - 1):
        for u in range(n):
            for v,edge in G[u]:    #te dwie  petle to przejscie po wszystkich krawedziach
                relax(u,v,edge)

    # weryfikacja

    for u in range(n):
        for v,w in G[u]:
            if distance[v] > distance[u] + w:
                return False, None, None

    return True, distance, parent

# PLN = 0
# EUR = 1
# YNG = 2
# USD = 3
C = [(0,1,4.5),(0,3,4),(3,0, 0.25),(1,3,0.75),(2,3,100),(0,2,0.4)]
G = cryptocurrency_stuff(C,4)
A = 0
B = 3
res = BF_4_adjlist(G,A)
print(res[0])
print(res[1])
print(res[2])
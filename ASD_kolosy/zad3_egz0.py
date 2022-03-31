from zad3testy_egz0 import runtests

#zmodyfikowana dijkstra, która bierze pod uwage czy do danego wierzchołka doszlismy w dwumilowych butach (ozn. 1) czy normalnie (ozn. 0)
# co za tym idze podwójna tablica visited oraz distance.


def jumper(G, s, w):
    n = len(G)
    processed = [[False for _ in range(2)] for _ in range(n)]
    distance = [[float('inf') for _ in range(2)] for _ in range(n)]

    distance[s][0] = 0
    distance[s][1] = 0

    def relax(u, v, edge, tm, add, l):
        if tm:
            if distance[v][0] > distance[u][1] + edge:
                distance[v][0] = distance[u][1] + edge

        else:
            if l == -1:
                if distance[v][0] > distance[u][0] + edge:
                    distance[v][0] = distance[u][0] + edge
            else:
                if distance[l][1] > distance[u][0] + max(edge, add):
                    distance[l][1] = distance[u][0] + max(edge, add)

    def get_vert():
        n = len(distance)
        key = n
        best = float('inf')
        tm = None
        for i in range(n):
            if not processed[i][0] and best > distance[i][0]:
                best = distance[i][0]
                key = i
                tm = False

            if not processed[i][1] and best > distance[i][1]:
                best = distance[i][1]
                key = i
                tm = True

        return key, tm, best

    while True:
        v, tm, flag = get_vert()
        if flag == float('inf'):  # warunek zakonczenia przetwarzania
            break

        else:
            if tm:   #wczesniejszy krok był w dwumilowych butach, ten na pewno musi byc bez nich
                processed[v][1] = True
                for u in range(n):
                    if G[v][u] != 0 and not processed[u][0]:
                        relax(v, u, G[v][u],tm, 0, 0)


            else: #poprzedni krok był zwykły obie opcje dostepne
                processed[v][0] = True
                for u in range(n):
                    if G[v][u] != 0:
                        if not processed[u][0]:
                            relax(v, u, G[v][u], tm, -1, -1) #gdy znowu robimy zwykły krok

                        for l in range(n): #gdy robimy krok dwumilowy
                            if G[u][l] != 0 and not processed[l][1]:
                                relax(v, u, G[u][l], tm, G[v][u], l)

    best = min(distance[w])
    return best


runtests(jumper)


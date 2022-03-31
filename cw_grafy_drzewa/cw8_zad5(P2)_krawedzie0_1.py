'''Zadanie 5. (krawędzie 0/1) Dana jest mapa kraju w postaci grafu G = (V, E). Kierowca chce przejechać
z miasta (wierzchołka) s to miasta t. Niestety niektóre drogi (krawędzie) są płatne. Każda droga ma taką
samą jednostkową opłatę. Proszę podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby
opłat. W ogólności graf G jest skierowany, ale można najpierw wskazać algorytm dla grafu nieskierowanego.'''

# pomysł - BFS z tym ze jesli dana dana droga jest darmowa to wstawiamy wierzchołek na poczatek kolejki

def cheapest_highway(G,s,t):
    from collections import deque #kolejka umozliwiajaca dodawanie elementu na przód
    n = len(G)  # n = |V|
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    Q = deque()

    Q.append(s)
    visited[s] = True
    distance[s] = 0

    while len(Q) != 0:
        u = Q.popleft()
        visited[u] = True  #przesuwamy tutaj, zeby móc dojsc gdzies droga dłuzsza ale za darmo
        if u == t:
            return distance[t]
        for v in range(n):
            if G[u][v] > -1 and not visited[v]:
                #print("przechodzimy z:",u,", do:",v,", za:",G[u][v])
                if G[u][v] == 0:
                    distance[v] = distance[u]
                    Q.appendleft(v)
                else:
                    distance[v] = distance[u] + 1
                    Q.append(v)

    return distance[t]



test = [[-1,1,-1,-1,-1,-1,-1,-1,-1],
        [1,-1,0,0,-1,-1,-1,-1,-1],
        [-1,0,-1,-1,1,-1,0,-1,-1],
        [-1,0,-1,-1,0,-1,-1,-1,-1],
        [-1,1,1,0,-1,-1,-1,-1,1],
        [-1,-1,-1,-1,1,-1,1,-1,-1],
        [-1,-1,0,-1,-1,1,-1,-1,0],
        [-1,-1,-1,-1,-1,-1,-1,-1,1],
        [-1,-1,-1,-1,1,-1,0, 1,-1]]

test2 = [[-1,1,-1,-1,-1,-1,-1,-1,-1],
        [1,-1,1,0,-1,-1,-1,-1,-1],
        [-1,0,-1,-1,1,-1,0,-1,-1],
        [-1,0,-1,-1,0,-1,-1,-1,-1],
        [-1,1,1,0,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,1,-1,1,-1,-1],
        [-1,-1,0,-1,-1,1,-1,-1,0],
        [-1,-1,-1,-1,-1,-1,-1,-1,1],
        [-1,-1,-1,-1,-1,-1,0, 1,-1]]

print(cheapest_highway(test2,4,8))
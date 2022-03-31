'''Dostajemy na wejściu graf, w którym wierzchołkami są miasta, a krawędziami drogi między nimi.
Dla każdego miasta znamy cenę paliwa w złotych na litr, a dla każdej drogi jej długość w kilometrach.
Nasz samochód ma zbiornik pojemności 100 litrów i pali jeden litr na kilometr.
Startujemy z miasta A z pustym zbiornikiem. Ile minimalnie musimy zapłacić za paliwo, aby dotrzeć do miasta B?
'''

#wszystko sprowadza sie do odpowiedniego przemodelowania grafu, tak aby rozważyć wszystkie mozliwosci, na tzw. Space-State Graph, gdzie
# wierzchołki sa reprezenotwane przez krotki (ind miasta, ile paliwa zostało w baku), a krawedzie sa ważone i tworzone w nastepujacy sposób:
# 1) jesli ilosc paliwa w wierzchołku u - długosc drogi >= ilosc paliwa w v, to prowadzimy krawedz o wadze 0 do wierzchołka (v, ilosc paliwa w wierzchołku u - długosc drogi)
# 2) wpp koszt krawedzi jest równy (koszt drogi + ilosć pozostałego paliwa w v - paliwo w u) * koszt paliwa w u

# nowy graf bedzie przechowywał dla kazdego wierzchołka (wierzchołek, ile w nim paliwa),
# krotki (wierzchołek, ile paliwa w nim bedziemy mieli, ile wydamy na dojazd)

# na tak przemodelowanym grafie odpalamy dijkstre, a wynikiem jest minimalna wartosc ze wszystkich w wierzchołkach (koniec drogi, cokolwiek)
# załozymy, ze graf wejsciowy jest lista sasiedztwa, a koszty paliwa w kazdym miescie sa przechowywane w osobnej tablicy


def into_Space_State(G,C,capacity):
    n = len(G)
    SS_Graph = [[[]]*(capacity+1) for i in range(n)]

    for u in range(n):
        for fu in range(capacity + 1):
            tmp = []
            for v in G[u]:
                for fv in range(capacity + 1):
                    #print("-----")
                    #print("Rozwijamy wierzchołek:",u,"w wierzchołek stanu",(u,fu),"dodajemy krawedz do wierzchołka stanu",(v[0],fv))
                    if fu - v[1] - fv == 0:
                        tmp.append([v[0],fv,0])
                        #print("Dodajemy krawedz o wadze:",0)
                    elif fu - v[1] - fv < 0 and capacity - v[1] >= fv:
                        tmp.append([v[0],fv,(v[1] + fv - fu)*C[u]])
                        #print("Dodajemy krawedz o wadze:",(v[1] + fv - fu)*C[u])

            #print("Powstał wierzchołek stanu:",(u,fu),tmp)
            SS_Graph[u][fu] = tmp

    return SS_Graph


def Dijkstra_4_Space_State_fucking_Graph(G, a, cap,C):
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    processed = [[False]*(cap+1) for _ in range(n)]
    cost = [[float('inf')]*(cap+1) for _ in range(n)]

    for i in range(cap+1):
        Q.put((i*C[a], i, a))  # (koszt,ile paliwa, wierzchołek)
        cost[a][i] = i*C[a]

    def relax(u, fu, v, fv, edge):
        if cost[v][fv] > cost[u][fu] + edge:
            cost[v][fv] = cost[u][fu] + edge
            return True  #przyda sie do wsadzania wierzchołków do kolejki

        return False

    while not Q.empty():
        _,ft,t = Q.get()
        if processed[t][ft] == True:
            continue
        else:
            processed[t][ft] = True
            for u in G[t][ft]:         # u = (drugi wierzcholek krawedzi, ile paliwa zostanie, koszt krawedzi)
                if not processed[u[0]][u[1]]:
                    if relax(t,ft,u[0],u[1], u[2]):
                        Q.put((cost[u[0]][u[1]],u[1],u[0]))

    return cost

#           0=A           1=B              2=C               3=D             4=E
test = [[(1,1),(2,1)],[(0,1),(2,2)],[(0,1),(1,2),(3,3)],[(2,3),(4,95)],[(3,95)]]
cap = 100
C = [1,2,3,4,1]
start = 0
stop = 4
SS_Graph = into_Space_State(test,C,cap)
'''for row in SS_Graph:
    print(row)
print("----")'''
cost = Dijkstra_4_Space_State_fucking_Graph(SS_Graph,start,cap,C)

'''for r in cost:
    print(r)'''
best = float('inf')
for i in range(cap+1):
    best = min(best,cost[stop][i])

print(best)


test_dla_ulomow = [[(1,1)],[(0,1)]]
C_ulom = [2,2]
t_ulom = 3

SS_Graph_ulom = into_Space_State(test_dla_ulomow,C_ulom,t_ulom)
'''for row in SS_Graph_ulom:
    print(row)
'''
cost_ulom = Dijkstra_4_Space_State_fucking_Graph(SS_Graph_ulom,0,t_ulom,C_ulom)

'''for r in cost_ulom:
    print(r)
best = float('inf')'''
for i in range(t_ulom+1):
    best = min(best,cost_ulom[1][i])

print(best)


G = [
    [[1, 7], [6, 3]],  # 0
    [[0, 7], [2, 3], [7, 4]],  # 1
    [[1, 3], [3, 8], [7, 4]],  # 2
    [[2, 8], [4, 3], [5, 10]],  # 3
    [[3, 3], [5, 8]],  # 4
    [[3, 10], [4, 8], [6, 6], [7, 3]],  # 5
    [[0, 3], [5, 6], [7, 5]],  # 6
    [[1, 4], [2, 4], [5, 3], [6, 5]]  # 7
]


S = [8, 5, 9, 700, 3, 3, 2, 1]  # gas stations
D = 10
a = 0
b = 4
SS_Graph_witek = into_Space_State(G,S,D)
'''for row in SS_Graph_witek:
    print(row)'''

cost_witek = Dijkstra_4_Space_State_fucking_Graph(SS_Graph_witek,a,D,S)

'''for r in cost_ulom:
    print(r)'''
#print(cost_witek)
best = float('inf')
for i in range(D+1):
    best = min(best,cost_witek[b][i])

print(best)
#wynik to 47

#wydaje sie działać